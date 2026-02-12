"""
Streamlit App — Simulasi Deteksi Anti Money Laundering (AML)
Model: CatBoost | Dataset: IBM Synthetic AML (HI-Small)
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import os
import time
import io
from catboost import CatBoostClassifier, Pool
from datetime import datetime

# ============================================================
# Config
# ============================================================
MODEL_PATH = os.path.join(os.path.dirname(__file__), "saved_models", "catboost_aml_model.cbm")
FEATURE_PATH = os.path.join(os.path.dirname(__file__), "saved_models", "feature_cols.json")
DEFAULT_THRESHOLD = 0.67

# ============================================================
# Load model & feature list (cached)
# ============================================================
@st.cache_resource
def load_model():
    model = CatBoostClassifier()
    model.load_model(MODEL_PATH)
    return model

@st.cache_data
def load_feature_cols():
    with open(FEATURE_PATH) as f:
        return json.load(f)

# ============================================================
# Feature Engineering — sama persis dengan notebook
# ============================================================
def engineer_features(df):
    """Apply all 59 features from the notebook pipeline."""

    # --- 1. Graph-based (degree) ---
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

    # --- 2. Amount stats ---
    from_amt = df.groupby('from_id')['Amount Paid'].agg(
        ['mean', 'std', 'min', 'max', 'sum', 'median']).reset_index()
    from_amt.columns = ['from_id', 'from_amt_mean', 'from_amt_std',
                         'from_amt_min', 'from_amt_max', 'from_amt_sum', 'from_amt_median']
    from_amt['from_amt_std'] = from_amt['from_amt_std'].fillna(0)

    to_amt = df.groupby('to_id')['Amount Received'].agg(
        ['mean', 'std', 'min', 'max', 'sum', 'median']).reset_index()
    to_amt.columns = ['to_id', 'to_amt_mean', 'to_amt_std',
                       'to_amt_min', 'to_amt_max', 'to_amt_sum', 'to_amt_median']
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

    # --- 3. Port numbering ---
    df_sorted = df.sort_values('Timestamp')
    to_port_map, from_port_map = {}, {}
    in_ports, out_ports = [], []
    for _, row in df_sorted.iterrows():
        tn, fn = row['to_id'], row['from_id']
        if tn not in to_port_map:
            to_port_map[tn] = {}
        if fn not in to_port_map[tn]:
            to_port_map[tn][fn] = len(to_port_map[tn])
        in_ports.append(to_port_map[tn][fn])
        if fn not in from_port_map:
            from_port_map[fn] = {}
        if tn not in from_port_map[fn]:
            from_port_map[fn][tn] = len(from_port_map[fn])
        out_ports.append(from_port_map[fn][tn])
    df_sorted['in_port'] = in_ports
    df_sorted['out_port'] = out_ports
    df = df_sorted

    # --- 4. Time deltas ---
    df = df.sort_values('Timestamp').copy()
    df['in_time_delta'] = df.groupby('to_id')['Timestamp'].diff().fillna(0)
    df['out_time_delta'] = df.groupby('from_id')['Timestamp'].diff().fillna(0)

    # --- 5. Temporal & behavioral ---
    df['day'] = (df['Timestamp'] // (3600 * 24)).astype(int)
    df['hour'] = ((df['Timestamp'] % (3600 * 24)) // 3600).astype(int)
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    df['is_self_tx'] = (df['from_id'] == df['to_id']).astype(int)
    df['same_currency'] = (df['Payment Currency'] == df['Receiving Currency']).astype(int)

    from_daily = df.groupby(['from_id', 'day']).size().reset_index(name='cnt')
    from_daily_avg = from_daily.groupby('from_id')['cnt'].mean().reset_index(name='from_avg_daily_tx')
    df = df.merge(from_daily_avg, on='from_id', how='left')

    to_daily = df.groupby(['to_id', 'day']).size().reset_index(name='cnt')
    to_daily_avg = to_daily.groupby('to_id')['cnt'].mean().reset_index(name='to_avg_daily_tx')
    df = df.merge(to_daily_avg, on='to_id', how='left')

    pair_count = df.groupby(['from_id', 'to_id']).size().reset_index(name='pair_tx_count')
    df = df.merge(pair_count, on=['from_id', 'to_id'], how='left')
    pair_amt = df.groupby(['from_id', 'to_id'])['Amount Paid'].agg(['mean', 'sum']).reset_index()
    pair_amt.columns = ['from_id', 'to_id', 'pair_amt_mean', 'pair_amt_sum']
    df = df.merge(pair_amt, on=['from_id', 'to_id'], how='left')
    df['is_repeat_pair'] = (df['pair_tx_count'] > 1).astype(int)
    df['is_round_amount'] = ((df['Amount Paid'] % 100 == 0) | (df['Amount Paid'] % 1000 == 0)).astype(int)

    return df


# ============================================================
# Parse raw CSV → processed DataFrame (same as notebook)
# ============================================================
def parse_raw_csv(raw_df):
    """Convert raw CSV (with string columns) to processed DataFrame."""
    currency_map, payment_format_map, account_map = {}, {}, {}

    def get_dict_val(name, collection):
        if name in collection:
            return collection[name]
        val = len(collection)
        collection[name] = val
        return val

    records = []
    first_ts = None
    cols = raw_df.columns.tolist()

    for i in range(len(raw_df)):
        row = raw_df.iloc[i]
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

        is_laundering = int(row['Is Laundering']) if 'Is Laundering' in cols else -1

        records.append({
            'from_id': from_id,
            'to_id': to_id,
            'Timestamp': ts_relative,
            'Amount Paid': amount_paid,
            'Payment Currency': pay_currency,
            'Amount Received': amount_received,
            'Receiving Currency': recv_currency,
            'Payment Format': pay_format,
            'Is Laundering': is_laundering,
        })

    df = pd.DataFrame(records)
    df = df.sort_values('Timestamp').reset_index(drop=True)
    df['Timestamp'] = df['Timestamp'] - df['Timestamp'].min()
    df = df.sort_values('Timestamp').reset_index(drop=True)
    return df


# ============================================================
# Streamlit UI
# ============================================================
def main():
    st.set_page_config(page_title="AML Detection — CatBoost", page_icon="🔍", layout="wide")

    st.title("🔍 Deteksi Anti Money Laundering (AML)")
    st.caption("Model CatBoost — Skripsi AML Detection")

    # Load model
    try:
        model = load_model()
        feature_cols = load_feature_cols()
        st.sidebar.success(f"✅ Model loaded ({len(feature_cols)} fitur)")
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        st.stop()

    # Sidebar — Threshold slider
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Pengaturan")
    threshold = st.sidebar.slider(
        "Threshold Prediksi",
        min_value=0.05, max_value=0.95, value=DEFAULT_THRESHOLD, step=0.01,
        help="Nilai probabilitas minimum agar transaksi diklasifikasikan sebagai mencurigakan."
    )
    st.sidebar.info(
        f"**Threshold = {threshold:.2f}**\n\n"
        f"- Tinggi (>0.7): Lebih sedikit alarm, tapi lebih akurat\n"
        f"- Rendah (<0.4): Lebih banyak terdeteksi, tapi lebih banyak alarm palsu"
    )

    # ============================================================
    # Simulasi Realtime (dari data asli)
    # ============================================================
    st.markdown("### 🎬 Simulasi Screening Transaksi Realtime")
    st.markdown(
        "Simulasi deteksi AML menggunakan **data transaksi asli** dari dataset. "
        "Data diproses melalui pipeline lengkap (feature engineering → prediksi) "
        "lalu ditampilkan baris per baris seperti sistem screening sesungguhnya."
    )

    CSV_PATH = os.path.join(os.path.dirname(__file__), "HI-Small_Trans.csv")
    csv_exists = os.path.exists(CSV_PATH)

    if not csv_exists:
        st.error(f"File `HI-Small_Trans.csv` tidak ditemukan di `{os.path.dirname(__file__)}`")
        st.stop()

    # --- Settings ---
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        n_tx = st.number_input("Jumlah transaksi untuk simulasi", min_value=50, max_value=5000, value=200, step=50, key="sim_n")
    with sc2:
        pct_suspicious = st.slider("% transaksi mencurigakan (oversample)", 5, 50, 15, key="sim_pct",
                                    help="Persentase transaksi mencurigakan dalam sampel. Dataset asli hanya ~0.1%, jadi kita oversample agar simulasi lebih menarik.")
    with sc3:
        speed = st.selectbox("Kecepatan animasi", ["Cepat (50ms)", "Normal (150ms)", "Lambat (300ms)"], index=0, key="sim_speed")
        speed_ms = {"Cepat (50ms)": 0.05, "Normal (150ms)": 0.15, "Lambat (300ms)": 0.3}[speed]

    if st.button("▶️ Mulai Simulasi", key="run_sim", type="primary"):
        # --- Step 1: Load & sample from real CSV ---
        with st.spinner("📂 Membaca dataset asli (~5 juta baris)... Ini bisa memakan waktu 30-60 detik."):
            raw_full = pd.read_csv(CSV_PATH, dtype=str)

            # Separate normal and suspicious
            suspicious_rows = raw_full[raw_full['Is Laundering'] == '1']
            normal_rows = raw_full[raw_full['Is Laundering'] == '0']

            n_sus_sample = max(int(n_tx * pct_suspicious / 100), 1)
            n_nor_sample = n_tx - n_sus_sample

            # Sample (with replacement if needed)
            sus_sample = suspicious_rows.sample(n=min(n_sus_sample, len(suspicious_rows)),
                                                 replace=n_sus_sample > len(suspicious_rows),
                                                 random_state=42)
            nor_sample = normal_rows.sample(n=min(n_nor_sample, len(normal_rows)),
                                             random_state=42)

            raw_sample = pd.concat([sus_sample, nor_sample]).sample(frac=1, random_state=42).reset_index(drop=True)

            st.success(f"✅ Sampel: {len(nor_sample)} normal + {len(sus_sample)} mencurigakan = {len(raw_sample)} total")

        # --- Step 2: Feature Engineering ---
        with st.spinner("⚙️ Menjalankan feature engineering (59 fitur)..."):
            df = parse_raw_csv(raw_sample)
            labels = df['Is Laundering'].values.copy()
            df = engineer_features(df)

            # Prepare features
            cat_feats = ['Payment Currency', 'Receiving Currency', 'Payment Format']
            for col in cat_feats:
                df[col] = df[col].astype(int)

            X_all = df[feature_cols]

        # --- Step 3: Batch predict (fast) ---
        with st.spinner("🤖 Menjalankan model CatBoost..."):
            pool = Pool(X_all, cat_features=cat_feats)
            probas_all = model.predict_proba(pool)[:, 1]
            preds_all = (probas_all >= threshold).astype(int)

        # Prepare display data
        display_data = raw_sample.reset_index(drop=True)

        # --- Step 4: Animate results ---
        st.markdown("---")
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        metric_total = col_m1.empty()
        metric_sus = col_m2.empty()
        metric_normal = col_m3.empty()
        metric_acc = col_m4.empty()

        progress_bar = st.progress(0)
        status_text = st.empty()
        table_placeholder = st.empty()

        results = []
        n_detected = 0
        n_correct = 0
        total = len(display_data)

        for i in range(total):
            row = display_data.iloc[i]
            proba = probas_all[i]
            pred = preds_all[i]
            actual = labels[i]

            pred_label = '🚨 Mencurigakan' if pred == 1 else '✅ Normal'
            actual_label = '🚨 Mencurigakan' if actual == 1 else '✅ Normal'
            is_correct = (pred == actual)
            n_correct += int(is_correct)

            if pred == 1:
                n_detected += 1

            # Get raw info for display
            amt_paid = row.get('Amount Paid', '?')
            results.append({
                'No': i + 1,
                'Waktu': row.get('Timestamp', ''),
                'Dari': f"{row.get('From Bank', '')}",
                'Ke': f"{row.get('To Bank', '')}",
                'Jumlah': f"${float(amt_paid):,.2f}" if amt_paid != '?' else '?',
                'Mata Uang': f"{row.get('Payment Currency', '')} → {row.get('Receiving Currency', '')}",
                'Format': row.get('Payment Format', ''),
                'Probabilitas': f"{proba:.4f}",
                'Prediksi': pred_label,
                'Aktual': actual_label,
                '✓/✗': '✓' if is_correct else '✗',
            })

            # Update metrics
            pct = (i + 1) / total
            progress_bar.progress(pct)
            status_text.markdown(f"⏳ Memproses transaksi **{i+1}/{total}**...")
            metric_total.metric("Diproses", f"{i+1}/{total}")
            metric_sus.metric("🚨 Terdeteksi", n_detected)
            metric_normal.metric("✅ Normal", (i + 1) - n_detected)
            metric_acc.metric("Akurasi", f"{n_correct/(i+1)*100:.1f}%")

            # Live table (last 20)
            table_placeholder.dataframe(
                pd.DataFrame(results[-20:]), use_container_width=True, hide_index=True
            )

            time.sleep(speed_ms)

        # --- Done ---
        status_text.markdown("✅ **Simulasi selesai!**")
        progress_bar.progress(1.0)

        # Final summary
        st.markdown("---")
        st.markdown("### 📊 Ringkasan Simulasi")

        actual_sus = int((labels == 1).sum())
        detected_sus = int(preds_all.sum())
        true_pos = int(((preds_all == 1) & (labels == 1)).sum())
        false_pos = int(((preds_all == 1) & (labels == 0)).sum())
        false_neg = int(((preds_all == 0) & (labels == 1)).sum())
        true_neg = int(((preds_all == 0) & (labels == 0)).sum())

        s1, s2, s3, s4 = st.columns(4)
        s1.metric("Total Transaksi", total)
        s2.metric("Mencurigakan (Aktual)", actual_sus)
        s3.metric("Terdeteksi Model", detected_sus)
        s4.metric("Akurasi", f"{n_correct/total*100:.1f}%")

        d1, d2, d3, d4 = st.columns(4)
        d1.metric("True Positive", true_pos, help="Mencurigakan yang benar terdeteksi")
        d2.metric("False Positive", false_pos, help="Normal yang salah di-flag")
        d3.metric("False Negative", false_neg, help="Mencurigakan yang terlewat")
        d4.metric("True Negative", true_neg, help="Normal yang benar teridentifikasi")

        if actual_sus > 0:
            from sklearn.metrics import f1_score, precision_score, recall_score
            f1 = f1_score(labels, preds_all)
            prec = precision_score(labels, preds_all, zero_division=0)
            rec = recall_score(labels, preds_all, zero_division=0)

            e1, e2, e3 = st.columns(3)
            e1.metric("F1-Score", f"{f1:.4f}")
            e2.metric("Precision", f"{prec:.4f}")
            e3.metric("Recall", f"{rec:.4f}")

        # Full results table
        st.markdown("### 📋 Seluruh Hasil Prediksi")
        full_df = pd.DataFrame(results)
        st.dataframe(full_df, use_container_width=True, hide_index=True)

        # Download as Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            full_df.to_excel(writer, index=False, sheet_name='Hasil Simulasi')
            summary_data = {
                'Metrik': ['Total Transaksi', 'Mencurigakan (Aktual)', 'Terdeteksi Model',
                           'True Positive', 'False Positive', 'False Negative', 'True Negative',
                           'F1-Score', 'Precision', 'Recall', 'Akurasi', 'Threshold'],
                'Nilai': [total, actual_sus, detected_sus,
                          true_pos, false_pos, false_neg, true_neg,
                          f"{f1:.4f}" if actual_sus > 0 else 'N/A',
                          f"{prec:.4f}" if actual_sus > 0 else 'N/A',
                          f"{rec:.4f}" if actual_sus > 0 else 'N/A',
                          f"{n_correct/total*100:.1f}%", threshold]
            }
            pd.DataFrame(summary_data).to_excel(writer, index=False, sheet_name='Ringkasan')
        output.seek(0)

        st.download_button(
            label="📥 Download Hasil (Excel)",
            data=output,
            file_name="simulasi_aml_results.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


if __name__ == "__main__":
    main()
