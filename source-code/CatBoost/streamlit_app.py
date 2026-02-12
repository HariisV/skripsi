import streamlit as st
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from catboost import CatBoostClassifier, Pool

# ============================================================
# Page Config
# ============================================================
st.set_page_config(
    page_title="AML Detection — CatBoost",
    page_icon="🔍",
    layout="wide",
)

# ============================================================
# Helper Functions
# ============================================================

@st.cache_resource
def load_model():
    """Load saved CatBoost model."""
    model_path = os.path.join(os.path.dirname(__file__), "saved_models", "catboost_aml_model.cbm")
    model = CatBoostClassifier()
    model.load_model(model_path)
    return model

@st.cache_data
def load_feature_cols():
    """Load feature column names."""
    feat_path = os.path.join(os.path.dirname(__file__), "saved_models", "feature_cols.json")
    with open(feat_path) as f:
        return json.load(f)


def get_dict_val(name, collection):
    if name in collection:
        return collection[name]
    val = len(collection)
    collection[name] = val
    return val


def load_and_preprocess(raw):
    """Convert raw CSV (HI-Small format) into processed DataFrame."""
    currency_map, payment_format_map, account_map = {}, {}, {}
    records = []
    first_ts = None

    for i in range(len(raw)):
        row = raw.iloc[i]
        dt = datetime.strptime(str(row['Timestamp']), '%Y/%m/%d %H:%M')
        ts = dt.timestamp()

        if first_ts is None:
            start_time = datetime(dt.year, dt.month, dt.day)
            first_ts = start_time.timestamp() - 10

        ts_relative = ts - first_ts
        from_acc_str = str(row['From Bank']) + str(row.iloc[2])
        to_acc_str = str(row['To Bank']) + str(row.iloc[4])
        from_id = get_dict_val(from_acc_str, account_map)
        to_id = get_dict_val(to_acc_str, account_map)
        recv_currency = get_dict_val(str(row['Receiving Currency']), currency_map)
        pay_currency = get_dict_val(str(row['Payment Currency']), currency_map)
        pay_format = get_dict_val(str(row['Payment Format']), payment_format_map)
        amount_received = float(row['Amount Received'])
        amount_paid = float(row['Amount Paid'])
        is_laundering = int(row['Is Laundering'])

        records.append({
            'from_id': from_id, 'to_id': to_id,
            'Timestamp': ts_relative,
            'Amount Paid': amount_paid,
            'Payment Currency': pay_currency,
            'Amount Received': amount_received,
            'Receiving Currency': recv_currency,
            'Payment Format': pay_format,
            'Is Laundering': is_laundering,
        })

    df = pd.DataFrame(records).sort_values('Timestamp').reset_index(drop=True)
    return df


def engineer_features(df):
    """Full feature engineering pipeline (59 features)."""
    # Normalize timestamp
    df['Timestamp'] = df['Timestamp'] - df['Timestamp'].min()
    df = df.sort_values('Timestamp').reset_index(drop=True)

    # --- Graph-based features ---
    out_degree = df.groupby('from_id').size().reset_index(name='from_out_degree')
    in_degree = df.groupby('to_id').size().reset_index(name='to_in_degree')
    df = df.merge(out_degree, on='from_id', how='left')
    df = df.merge(in_degree, on='to_id', how='left')

    from_in_degree = df.groupby('to_id').size().reset_index(name='from_in_degree')
    from_in_degree.columns = ['from_id', 'from_in_degree']
    to_out_degree = df.groupby('from_id').size().reset_index(name='to_out_degree')
    to_out_degree.columns = ['to_id', 'to_out_degree']
    df = df.merge(from_in_degree, on='from_id', how='left')
    df = df.merge(to_out_degree, on='to_id', how='left')
    df['from_in_degree'] = df['from_in_degree'].fillna(0)
    df['to_out_degree'] = df['to_out_degree'].fillna(0)

    df['from_total_degree'] = df['from_out_degree'] + df['from_in_degree']
    df['to_total_degree'] = df['to_in_degree'] + df['to_out_degree']
    df['from_degree_ratio'] = df['from_out_degree'] / (df['from_in_degree'] + 1)
    df['to_degree_ratio'] = df['to_in_degree'] / (df['to_out_degree'] + 1)

    from_unique = df.groupby('from_id')['to_id'].nunique().reset_index(name='from_unique_neighbors')
    to_unique = df.groupby('to_id')['from_id'].nunique().reset_index(name='to_unique_neighbors')
    df = df.merge(from_unique, on='from_id', how='left')
    df = df.merge(to_unique, on='to_id', how='left')
    df['from_neighbor_diversity'] = df['from_unique_neighbors'] / (df['from_out_degree'] + 1)
    df['to_neighbor_diversity'] = df['to_unique_neighbors'] / (df['to_in_degree'] + 1)
    df['fanout_fanin_ratio'] = df['from_unique_neighbors'] / (df['to_unique_neighbors'] + 1)

    # --- Amount features ---
    from_amt = df.groupby('from_id')['Amount Paid'].agg(['mean','std','min','max','sum','median']).reset_index()
    from_amt.columns = ['from_id','from_amt_mean','from_amt_std','from_amt_min','from_amt_max','from_amt_sum','from_amt_median']
    from_amt['from_amt_std'] = from_amt['from_amt_std'].fillna(0)
    to_amt = df.groupby('to_id')['Amount Received'].agg(['mean','std','min','max','sum','median']).reset_index()
    to_amt.columns = ['to_id','to_amt_mean','to_amt_std','to_amt_min','to_amt_max','to_amt_sum','to_amt_median']
    to_amt['to_amt_std'] = to_amt['to_amt_std'].fillna(0)
    df = df.merge(from_amt, on='from_id', how='left')
    df = df.merge(to_amt, on='to_id', how='left')

    df['amount_diff'] = df['Amount Received'] - df['Amount Paid']
    df['amount_ratio'] = df['Amount Received'] / (df['Amount Paid'] + 1e-8)
    df['amount_diff_abs'] = df['amount_diff'].abs()
    df['amount_log_ratio'] = np.log1p(df['Amount Received']) - np.log1p(df['Amount Paid'])
    df['from_amt_zscore'] = (df['Amount Paid'] - df['from_amt_mean']) / (df['from_amt_std'] + 1e-8)
    df['to_amt_zscore'] = (df['Amount Received'] - df['to_amt_mean']) / (df['to_amt_std'] + 1e-8)
    df['from_amt_frac'] = df['Amount Paid'] / (df['from_amt_sum'] + 1e-8)
    df['to_amt_frac'] = df['Amount Received'] / (df['to_amt_sum'] + 1e-8)
    df['log_amount_paid'] = np.log1p(df['Amount Paid'])
    df['log_amount_received'] = np.log1p(df['Amount Received'])
    df['cross_amt_ratio'] = df['from_amt_mean'] / (df['to_amt_mean'] + 1e-8)

    # --- Port numbering ---
    df_sorted = df.sort_values('Timestamp')
    to_port_map, from_port_map = {}, {}
    in_ports, out_ports = [], []
    for _, row in df_sorted.iterrows():
        to_n, from_n = row['to_id'], row['from_id']
        if to_n not in to_port_map: to_port_map[to_n] = {}
        if from_n not in to_port_map[to_n]: to_port_map[to_n][from_n] = len(to_port_map[to_n])
        in_ports.append(to_port_map[to_n][from_n])
        if from_n not in from_port_map: from_port_map[from_n] = {}
        if to_n not in from_port_map[from_n]: from_port_map[from_n][to_n] = len(from_port_map[from_n])
        out_ports.append(from_port_map[from_n][to_n])
    df_sorted['in_port'] = in_ports
    df_sorted['out_port'] = out_ports
    df = df_sorted

    # --- Time deltas ---
    df = df.sort_values('Timestamp').copy()
    df['in_time_delta'] = df.groupby('to_id')['Timestamp'].diff().fillna(0)
    df['out_time_delta'] = df.groupby('from_id')['Timestamp'].diff().fillna(0)

    # --- Temporal & behavioral ---
    df['day'] = (df['Timestamp'] // (3600 * 24)).astype(int)
    df['hour'] = ((df['Timestamp'] % (3600 * 24)) // 3600).astype(int)
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    df['is_self_tx'] = (df['from_id'] == df['to_id']).astype(int)
    df['same_currency'] = (df['Payment Currency'] == df['Receiving Currency']).astype(int)

    from_daily = df.groupby(['from_id','day']).size().reset_index(name='cnt')
    from_daily_avg = from_daily.groupby('from_id')['cnt'].mean().reset_index(name='from_avg_daily_tx')
    df = df.merge(from_daily_avg, on='from_id', how='left')
    to_daily = df.groupby(['to_id','day']).size().reset_index(name='cnt')
    to_daily_avg = to_daily.groupby('to_id')['cnt'].mean().reset_index(name='to_avg_daily_tx')
    df = df.merge(to_daily_avg, on='to_id', how='left')

    pair_count = df.groupby(['from_id','to_id']).size().reset_index(name='pair_tx_count')
    df = df.merge(pair_count, on=['from_id','to_id'], how='left')
    pair_amt = df.groupby(['from_id','to_id'])['Amount Paid'].agg(['mean','sum']).reset_index()
    pair_amt.columns = ['from_id','to_id','pair_amt_mean','pair_amt_sum']
    df = df.merge(pair_amt, on=['from_id','to_id'], how='left')
    df['is_repeat_pair'] = (df['pair_tx_count'] > 1).astype(int)
    df['is_round_amount'] = ((df['Amount Paid'] % 100 == 0) | (df['Amount Paid'] % 1000 == 0)).astype(int)

    return df


# ============================================================
# UI
# ============================================================

st.title("🔍 Deteksi Pencucian Uang (AML)")
st.caption("Model CatBoost — 59 Fitur Berbasis Pola Transaksi")

st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Pengaturan")
    threshold = st.slider(
        "Threshold Prediksi",
        min_value=0.05, max_value=0.95, value=0.67, step=0.01,
        help="Threshold tinggi → lebih sedikit alarm palsu (Precision ↑). "
             "Threshold rendah → lebih banyak deteksi (Recall ↑)."
    )
    st.divider()
    st.markdown(
        "**Panduan Threshold:**\n"
        "- 🔴 **0.30–0.40** — Recall tinggi, banyak alarm palsu\n"
        "- 🟡 **0.50–0.60** — Seimbang\n"
        "- 🟢 **0.67** — Optimal (F1 terbaik)\n"
        "- 🔵 **0.80–0.90** — Precision tinggi, sedikit alarm"
    )

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Screening Batch (CSV)", "📈 Info Model", "ℹ️ Tentang"])

# ------ Tab 1: BATCH CSV ------
with tab1:
    st.subheader("Upload Data Transaksi")
    st.markdown(
        "Upload file CSV dengan format **HI-Small_Trans** "
        "(kolom: `Timestamp, From Bank, Account, To Bank, Account, Amount Received, "
        "Amount Paid, Receiving Currency, Payment Currency, Payment Format, Is Laundering`)."
    )

    uploaded = st.file_uploader("Pilih file CSV", type=["csv"])

    # Option to use sample data
    use_sample = st.checkbox("Atau gunakan sample data (1.000 baris pertama)", value=False)

    if uploaded or use_sample:
        with st.spinner("Memuat dan memproses data..."):
            if use_sample:
                csv_path = os.path.join(os.path.dirname(__file__), "HI-Small_Trans.csv")
                raw = pd.read_csv(csv_path, dtype=str, nrows=1000)
                st.info("Menggunakan 1.000 baris pertama dari dataset.")
            else:
                raw = pd.read_csv(uploaded, dtype=str)

            n_raw = len(raw)
            st.write(f"**Total transaksi dimuat:** {n_raw:,}")

        with st.spinner("Menjalankan feature engineering (59 fitur)..."):
            df = load_and_preprocess(raw)
            df = engineer_features(df)

        with st.spinner("Menjalankan prediksi model..."):
            model = load_model()
            feature_cols = load_feature_cols()

            X = df[feature_cols].copy()
            cat_features = ['Payment Currency', 'Receiving Currency', 'Payment Format']
            for col in cat_features:
                X[col] = X[col].astype(int)

            y_true = df['Is Laundering'].values
            y_proba = model.predict_proba(X)[:, 1]
            y_pred = (y_proba >= threshold).astype(int)

        # --- Results ---
        st.divider()
        st.subheader("Hasil Screening")

        n_flagged = y_pred.sum()
        n_total = len(y_pred)
        n_actual = y_true.sum()

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Transaksi", f"{n_total:,}")
        col2.metric("Terdeteksi Mencurigakan", f"{n_flagged:,}")
        col3.metric("Aktual Mencurigakan", f"{n_actual:,}")
        col4.metric("Threshold", f"{threshold:.2f}")

        # Metrics
        if n_actual > 0 and n_flagged > 0:
            from sklearn.metrics import f1_score, precision_score, recall_score
            f1 = f1_score(y_true, y_pred)
            prec = precision_score(y_true, y_pred)
            rec = recall_score(y_true, y_pred)

            col5, col6, col7 = st.columns(3)
            col5.metric("F1-Score", f"{f1:.4f}")
            col6.metric("Precision", f"{prec:.4f}")
            col7.metric("Recall", f"{rec:.4f}")

            # Confusion Matrix
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(y_true, y_pred)
            st.markdown("**Confusion Matrix:**")

            cm_df = pd.DataFrame(cm,
                index=["Aktual Normal", "Aktual Mencurigakan"],
                columns=["Prediksi Normal", "Prediksi Mencurigakan"])
            st.dataframe(cm_df, use_container_width=True)

        # Flagged transactions table
        st.subheader("Transaksi yang Di-flag")
        df_result = df.copy()
        df_result['Probabilitas'] = y_proba
        df_result['Prediksi'] = y_pred.astype(str).tolist()
        df_result['Prediksi'] = df_result['Prediksi'].replace({'1': '🚨 Mencurigakan', '0': '✅ Normal'})

        flagged = df_result[df_result['Probabilitas'] >= threshold].sort_values('Probabilitas', ascending=False)
        display_cols = ['from_id', 'to_id', 'Amount Paid', 'Amount Received',
                        'Payment Format', 'Probabilitas', 'Prediksi', 'Is Laundering']
        display_cols = [c for c in display_cols if c in flagged.columns]

        if len(flagged) > 0:
            st.dataframe(
                flagged[display_cols].head(100),
                use_container_width=True,
                hide_index=True,
            )
            if len(flagged) > 100:
                st.caption(f"Menampilkan 100 dari {len(flagged):,} transaksi yang di-flag.")
        else:
            st.info("Tidak ada transaksi yang terdeteksi mencurigakan pada threshold ini.")

        # Download results
        csv_out = df_result[['from_id','to_id','Amount Paid','Amount Received',
                             'Probabilitas','Prediksi','Is Laundering']].to_csv(index=False)
        st.download_button(
            "⬇️ Download Hasil Screening (CSV)",
            csv_out, "hasil_screening_aml.csv", "text/csv"
        )

# ------ Tab 2: Model Info ------
with tab2:
    st.subheader("Informasi Model")

    model = load_model()
    feature_cols = load_feature_cols()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Spesifikasi Model:**")
        st.markdown(f"""
        | Parameter | Nilai |
        |-----------|-------|
        | Algoritma | CatBoost |
        | Jumlah Fitur | {len(feature_cols)} |
        | Depth | 8 |
        | Learning Rate | 0.03 |
        | Scale Pos Weight | 10.0 |
        | Threshold Optimal | 0.67 |
        """)

    with col2:
        st.markdown("**Performa pada Test Set (threshold=0.67):**")
        st.markdown("""
        | Metrik | Nilai |
        |--------|-------|
        | F1-Score | 0.7140 |
        | Precision | 0.8770 |
        | Recall | 0.6021 |
        | PR-AUC | 0.7412 |
        | False Positives | 136 |
        """)

    st.divider()
    st.subheader("Feature Importance (Top 20)")

    fi = model.get_feature_importance()
    fi_df = pd.DataFrame({
        'Fitur': feature_cols,
        'Importance (%)': fi
    }).sort_values('Importance (%)', ascending=False).head(20)

    st.bar_chart(fi_df.set_index('Fitur')['Importance (%)'])
    st.dataframe(fi_df.reset_index(drop=True), use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("Daftar 59 Fitur")
    feat_df = pd.DataFrame({'No': range(1, len(feature_cols)+1), 'Fitur': feature_cols})
    st.dataframe(feat_df, use_container_width=True, hide_index=True)

# ------ Tab 3: About ------
with tab3:
    st.subheader("Tentang Aplikasi")
    st.markdown("""
    ### Deteksi Pencucian Uang dengan CatBoost

    Aplikasi ini merupakan simulasi sistem *screening* transaksi mencurigakan
    menggunakan model **CatBoost** yang dilatih pada dataset **IBM AML (HI-Small)**.

    **Alur Kerja:**
    1. Upload data transaksi (format CSV)
    2. Sistem melakukan *feature engineering* otomatis (59 fitur)
    3. Model CatBoost memprediksi probabilitas setiap transaksi
    4. Transaksi dengan probabilitas ≥ threshold di-*flag* sebagai mencurigakan

    **Dataset:**
    - 5.078.345 transaksi (18 hari)
    - Rasio ketidakseimbangan: 1:979

    **Hasil:**
    - F1-Score: 0.7140 (+140.8% vs Multi-GNN)
    - Precision: 0.8770 (hanya 136 alarm palsu dari 862K+ transaksi normal)

    ---
    *Dikembangkan sebagai bagian dari penelitian skripsi.*
    """)
