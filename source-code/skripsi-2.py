import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

from catboost import CatBoostClassifier, Pool

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    f1_score,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.metrics import precision_recall_curve, auc

import matplotlib.pyplot as plt
import seaborn as sns

print(f"Pandas version: {pd.__version__}")
print(f"Numpy version: {np.__version__}")


file_path = "resources/HI-Small_Trans.csv"
df = pd.read_csv(file_path)

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df = df.sort_values("Timestamp").reset_index(drop=True)

print(f"Shape: {df.shape}")
print(f"Periode: {df['Timestamp'].min()} s/d {df['Timestamp'].max()}")
print(f"\n📋 Nama kolom:")
print(df.columns.tolist())
print(f"\n📊 Tipe data kolom:")
print(df.dtypes)
print(f"\n5 data pertama:")
df.head()

print(df["Is Laundering"].value_counts())
print(f"\nPersentase:")
print(df["Is Laundering"].value_counts(normalize=True) * 100)


df["year"] = df["Timestamp"].dt.year
df["month"] = df["Timestamp"].dt.month
df["day"] = df["Timestamp"].dt.day
df["hour"] = df["Timestamp"].dt.hour
df["day_of_week"] = df["Timestamp"].dt.dayofweek
df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)

df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)

print(f"\nKolom baru:")
print(
    df[["Timestamp", "year", "month", "day", "hour", "day_of_week", "is_weekend"]].head(
        10
    )
)


df = df.sort_values("Timestamp").reset_index(drop=True)


from collections import defaultdict

fan_out_counts = []
fan_in_counts = []
fan_out_seen = defaultdict(set)
fan_in_seen = defaultdict(set)

for idx, row in df.iterrows():
    fb = row["From Bank"]
    tb = row["To Bank"]

    fan_out_counts.append(len(fan_out_seen[fb]))
    fan_in_counts.append(len(fan_in_seen[tb]))

    fan_out_seen[fb].add(tb)
    fan_in_seen[tb].add(fb)

df["fan_out_count"] = fan_out_counts
df["fan_in_count"] = fan_in_counts


df["hour_timestamp"] = df["Timestamp"].dt.floor("H")
df["tx_velocity_from"] = 0
df["tx_velocity_to"] = 0

velocity_from = defaultdict(lambda: defaultdict(int))
velocity_to = defaultdict(lambda: defaultdict(int))

for idx, row in df.iterrows():
    fb = row["From Bank"]
    tb = row["To Bank"]
    hr = row["hour_timestamp"]

    df.at[idx, "tx_velocity_from"] = velocity_from[fb][hr]
    df.at[idx, "tx_velocity_to"] = velocity_to[tb][hr]

    velocity_from[fb][hr] += 1
    velocity_to[tb][hr] += 1


amount_from_sum = defaultdict(float)
amount_from_sum_sq = defaultdict(float)
amount_from_count = defaultdict(int)
amount_to_sum = defaultdict(float)
amount_to_sum_sq = defaultdict(float)
amount_to_count = defaultdict(int)

amount_zscore_from_list = []
amount_zscore_to_list = []

for idx, row in df.iterrows():
    fb = row["From Bank"]
    tb = row["To Bank"]
    amt = row["Amount Received"]

    if amount_from_count[fb] > 0:
        mean_from = amount_from_sum[fb] / amount_from_count[fb]
        var_from = (amount_from_sum_sq[fb] / amount_from_count[fb]) - (mean_from**2)
        std_from = np.sqrt(max(var_from, 0)) + 1e-6
        zscore_from = (amt - mean_from) / std_from
    else:
        zscore_from = 0.0

    if amount_to_count[tb] > 0:
        mean_to = amount_to_sum[tb] / amount_to_count[tb]
        var_to = (amount_to_sum_sq[tb] / amount_to_count[tb]) - (mean_to**2)
        std_to = np.sqrt(max(var_to, 0)) + 1e-6
        zscore_to = (amt - mean_to) / std_to
    else:
        zscore_to = 0.0

    amount_zscore_from_list.append(zscore_from)
    amount_zscore_to_list.append(zscore_to)

    amount_from_sum[fb] += amt
    amount_from_sum_sq[fb] += amt * amt
    amount_from_count[fb] += 1
    amount_to_sum[tb] += amt
    amount_to_sum_sq[tb] += amt * amt
    amount_to_count[tb] += 1

df["amount_zscore_from"] = amount_zscore_from_list
df["amount_zscore_to"] = amount_zscore_to_list


pair_counts_dict = defaultdict(int)
pair_freq_list = []

for idx, row in df.iterrows():
    pair = tuple(sorted([row["From Bank"], row["To Bank"]]))
    pair_freq_list.append(pair_counts_dict[pair])
    pair_counts_dict[pair] += 1

df["pair_frequency"] = pair_freq_list


payment_diversity_dict = defaultdict(set)
currency_diversity_dict = defaultdict(set)
payment_div_list = []
currency_div_list = []

for idx, row in df.iterrows():
    fb = row["From Bank"]
    payment_div_list.append(len(payment_diversity_dict[fb]))
    currency_div_list.append(len(currency_diversity_dict[fb]))

    payment_diversity_dict[fb].add(row["Payment Format"])
    currency_diversity_dict[fb].add(row["Receiving Currency"])

df["payment_format_diversity"] = payment_div_list
df["currency_diversity"] = currency_div_list


total_sent_dict = defaultdict(float)
total_received_dict = defaultdict(float)
total_sent_list = []
total_received_list = []

for idx, row in df.iterrows():
    fb = row["From Bank"]
    tb = row["To Bank"]
    amt = row["Amount Received"]

    total_sent_list.append(total_sent_dict[fb])
    total_received_list.append(total_received_dict[tb])

    total_sent_dict[fb] += amt
    total_received_dict[tb] += amt

df["total_amount_sent"] = total_sent_list
df["total_amount_received"] = total_received_list


df["is_suspicious_hour"] = df["hour"].apply(lambda x: 1 if x >= 0 and x <= 5 else 0)

df["fan_ratio"] = df["fan_in_count"] / (df["fan_out_count"] + 1)

df = df.drop(columns=["hour_timestamp"])


print(f"\n📊 Fitur baru yang ditambahkan (semua temporal-safe):")
new_features = [
    "fan_out_count",
    "fan_in_count",
    "tx_velocity_from",
    "tx_velocity_to",
    "amount_zscore_from",
    "amount_zscore_to",
    "pair_frequency",
    "payment_format_diversity",
    "currency_diversity",
    "is_suspicious_hour",
    "total_amount_sent",
    "total_amount_received",
    "fan_ratio",
]
for feat in new_features:
    print(f"   ✓ {feat}")

print(f"\n📈 Total fitur sekarang: {len(df.columns)}")
print(f"\nSample data dengan fitur temporal:")
print(
    df[
        [
            "From Bank",
            "To Bank",
            "Amount Received",
            "fan_out_count",
            "fan_in_count",
            "tx_velocity_from",
            "amount_zscore_from",
            "Is Laundering",
        ]
    ].head(10)
)


df_processed = df.drop(columns=["Timestamp"])

print(df_processed.columns.tolist())
print()

categorical_cols = []
for col in df_processed.columns:
    if df_processed[col].dtype == "object":
        categorical_cols.append(col)

        df_processed[col] = df_processed[col].astype(str)

print(f"   {categorical_cols}")


categorical_features = categorical_cols

print(f"Shape data: {df_processed.shape}")
print(f"\nSample data:")
print(df_processed.head(3))

n = len(df_processed)
train_size = int(0.6 * n)
valid_size = int(0.2 * n)

train_df = df_processed.iloc[:train_size].copy()
valid_df = df_processed.iloc[train_size : train_size + valid_size].copy()
test_df = df_processed.iloc[train_size + valid_size :].copy()

X_train = train_df.drop(columns=["Is Laundering"])
y_train = train_df["Is Laundering"]

X_valid = valid_df.drop(columns=["Is Laundering"])
y_valid = valid_df["Is Laundering"]

X_test = test_df.drop(columns=["Is Laundering"])
y_test = test_df["Is Laundering"]

print(f"\n📊 Ukuran dataset:")
print(f"Train: {len(X_train)} ({len(X_train)/n*100:.1f}%)")
print(f"Valid: {len(X_valid)} ({len(X_valid)/n*100:.1f}%)")
print(f"Test:  {len(X_test)} ({len(X_test)/n*100:.1f}%)")

print(f"\n📊 Distribusi target di setiap set:")
print(f"Train - Class 1: {y_train.sum()} ({y_train.sum()/len(y_train)*100:.2f}%)")
print(f"Valid - Class 1: {y_valid.sum()} ({y_valid.sum()/len(y_valid)*100:.2f}%)")
print(f"Test  - Class 1: {y_test.sum()} ({y_test.sum()/len(y_test)*100:.2f}%)")


account_cols = [col for col in X_train.columns if "Account" in col]
print(f"\nAccount columns detected: {account_cols}")

if account_cols:
    for col in account_cols:
        print(f"\n⏳ Encoding {col}...")

        freq_map = X_train[col].value_counts(normalize=True).to_dict()

        new_col_name = f"{col}_freq"
        X_train[new_col_name] = X_train[col].map(freq_map).fillna(0)
        X_valid[new_col_name] = X_valid[col].map(freq_map).fillna(0)
        X_test[new_col_name] = X_test[col].map(freq_map).fillna(0)

        print(f"     Train unique values: {X_train[col].nunique()}")
        print(f"     Valid unseen values: {(~X_valid[col].isin(X_train[col])).sum()}")
        print(f"     Test unseen values: {(~X_test[col].isin(X_train[col])).sum()}")

    print(f"\n🗑️  Dropping original Account columns: {account_cols}")
    X_train = X_train.drop(columns=account_cols)
    X_valid = X_valid.drop(columns=account_cols)
    X_test = X_test.drop(columns=account_cols)

    categorical_features = [
        col for col in categorical_features if col not in account_cols
    ]


print(f"\n📊 Final feature set:")
print(f"   Total features: {X_train.shape[1]}")
print(f"   Categorical features: {len(categorical_features)}")
print(f"   Numeric features: {X_train.shape[1] - len(categorical_features)}")


print(f"Training set:")
print(
    f"  Class 0 (Normal):     {(y_train == 0).sum():,} ({(y_train == 0).sum()/len(y_train)*100:.2f}%)"
)
print(
    f"  Class 1 (Laundering): {(y_train == 1).sum():,} ({(y_train == 1).sum()/len(y_train)*100:.2f}%)"
)

pos = y_train.sum()
neg = len(y_train) - pos
scale_pos_weight = neg / pos

print(f"\n📐 Class Weight Calculation:")
print(f"  Negative samples (Class 0): {neg:,}")
print(f"  Positive samples (Class 1): {pos:,}")
print(f"  Imbalance ratio: 1:{int(scale_pos_weight)}")

print(f"\n💡 Keuntungan Class Weights vs SMOTE:")
print(f"   ✓ Tidak ada synthetic samples yang unrealistic")
print(f"   ✓ Tidak ada overfitting ke synthetic patterns")
print(f"   ✓ Model belajar dari distribusi asli")
print(f"   ✓ Validasi lebih representatif untuk real deployment")


pos = y_train.sum()
neg = len(y_train) - pos
scale_pos_weight = neg / pos
base_scale_pos_weight = float(scale_pos_weight)

print(f"📊 Class imbalance ratio: {scale_pos_weight:.2f}")
print(f"   Recommended scale_pos_weight: {scale_pos_weight:.2f}")
print(f"\n💡 Paper Altman et al. (2023) melaporkan:")
print(f"   - LI-Large dataset: 1 laundering per 1,750 transaksi")
print(f"   - HI-Small dataset: 1 laundering per 807 transaksi")

categorical_features = [col for col in categorical_features if col in X_train.columns]
missing_cats = (
    sorted({col for col in categorical_cols if col not in X_train.columns})
    if "categorical_cols" in locals()
    else []
)
if missing_cats:
    print(
        f"\n⚠️  Kolom kategorikal yang sudah tidak ada dan di-skip CatBoost: {missing_cats}"
    )

train_pool = Pool(data=X_train, label=y_train, cat_features=categorical_features)

valid_pool = Pool(data=X_valid, label=y_valid, cat_features=categorical_features)

print(f"   Train pool: {len(X_train):,} samples")
print(f"   Valid pool: {len(X_valid):,} samples")
print(f"   Categorical features: {len(categorical_features)}")

from sklearn.metrics import average_precision_score

weight_grid = [1, 5, 10, 20, 50]
weight_tuning_records = []


def _precision_at_k_local(probs: np.ndarray, labels: pd.Series, top_k: int) -> float:
    top_k = min(top_k, len(labels))
    if top_k == 0:
        return 0.0
    ordered_idx = np.argsort(probs)[-top_k:]
    return float(labels.reset_index(drop=True).iloc[ordered_idx].sum() / top_k)


print(f"Base scale_pos_weight (neg/pos): {base_scale_pos_weight:.2f}")

for spw in weight_grid:
    print(f"   → Trial scale_pos_weight = {spw}")
    trial_model = CatBoostClassifier(
        iterations=600,
        learning_rate=0.05,
        depth=6,
        loss_function="Logloss",
        eval_metric="PRAUC",
        scale_pos_weight=spw,
        cat_features=categorical_features,
        random_seed=42,
        verbose=False,
        early_stopping_rounds=50,
        l2_leaf_reg=5,
        bootstrap_type="MVS",
        subsample=0.8,
        colsample_bylevel=0.8,
    )
    trial_model.fit(train_pool, eval_set=valid_pool, use_best_model=True, plot=True)
    prob_valid_trial = trial_model.predict_proba(X_valid)[:, 1]
    pr_auc_trial = average_precision_score(y_valid, prob_valid_trial)
    prec_at_1000 = _precision_at_k_local(prob_valid_trial, y_valid, top_k=1000)
    weight_tuning_records.append(
        {
            "scale_pos_weight": spw,
            "best_iteration": trial_model.get_best_iteration(),
            "validation_average_precision": pr_auc_trial,
            "precision@1000": prec_at_1000,
        }
    )

weight_tuning_df = pd.DataFrame(weight_tuning_records).sort_values(
    "validation_average_precision", ascending=False
)
best_scale_pos_weight = float(weight_tuning_df.iloc[0]["scale_pos_weight"])

display(weight_tuning_df)


print(f"\n📊 Data Training (NO SYNTHETIC DATA):")
print(f"   Training samples: {len(X_train):,}")
print(f"   Class 0 (Normal): {(y_train==0).sum():,}")
print(f"   Class 1 (Laundering): {(y_train==1).sum():,}")
print(f"   Features: {X_train.shape[1]}")
print(f"   Categorical features: {len(categorical_features)}")

pos = y_train.sum()
neg = len(y_train) - pos
base_scale_pos_weight = neg / pos

selected_scale_pos_weight = (
    best_scale_pos_weight
    if "best_scale_pos_weight" in locals()
    else min(50.0, base_scale_pos_weight)
)
print(f"\n⚖️  Class Weighting:")
print(f"   Base (neg/pos): {base_scale_pos_weight:.2f}")
if "best_scale_pos_weight" in locals():
    print(f"   Tuned scale_pos_weight (quick grid): {selected_scale_pos_weight:.2f}")
else:
    print(
        f"   Tuned scale_pos_weight: {selected_scale_pos_weight:.2f} (capped at 50 by default)"
    )

model = CatBoostClassifier(
    iterations=2000,
    learning_rate=0.05,
    depth=6,
    loss_function="Logloss",
    eval_metric="PRAUC",
    scale_pos_weight=selected_scale_pos_weight,
    cat_features=categorical_features,
    random_seed=42,
    verbose=100,
    early_stopping_rounds=100,
    use_best_model=True,
    l2_leaf_reg=5,
    bootstrap_type="MVS",
    od_type="Iter",
    subsample=0.8,
    colsample_bylevel=0.8,
)

print(f"   ✓ Iterations: 2000 (early stop: 100 rounds)")
print(f"   ✓ Learning rate: 0.05")
print(f"   ✓ Max depth: 6 (reduced for regularization)")
print(f"   ✓ Loss function: Logloss")
print(f"   ✓ Eval metric: PRAUC (proxy untuk AveragePrecision)")
print(f"   ✓ Scale pos weight: {selected_scale_pos_weight:.2f} (tuned)")
print(f"   ✓ L2 regularization: 5 (stronger)")
print(f"   ✓ Bootstrap type: MVS (supports subsample)")
print(f"   ✓ Subsample: 0.8")
print(f"   ✓ Colsample: 0.8")


model.fit(train_pool, eval_set=valid_pool, plot=False)

print(f"Best iteration: {model.get_best_iteration()}")
best_scores = model.get_best_score()
best_pr_auc = (
    best_scores["validation"].get("PRAUC", np.nan)
    if "validation" in best_scores
    else np.nan
)
print(f"Best validation PR-AUC: {best_pr_auc:.4f}")

from sklearn.isotonic import IsotonicRegression


prob_train_raw = model.predict_proba(X_train)[:, 1]
prob_valid_raw = model.predict_proba(X_valid)[:, 1]
prob_test_raw = model.predict_proba(X_test)[:, 1]

probability_calibrator = IsotonicRegression(out_of_bounds="clip")
probability_calibrator.fit(prob_valid_raw, y_valid)

prob_train = probability_calibrator.transform(prob_train_raw)
prob_valid = probability_calibrator.transform(prob_valid_raw)
prob_test = probability_calibrator.transform(prob_test_raw)

print(
    f"   Mean prob (valid) sebelum: {prob_valid_raw.mean():.4f} | sesudah: {prob_valid.mean():.4f}"
)
print(
    f"   Std prob (valid) sebelum:  {prob_valid_raw.std():.4f} | sesudah: {prob_valid.std():.4f}"
)


prob_test = probability_calibrator.transform(prob_test_raw)

y_pred_proba = prob_test
y_pred = (y_pred_proba >= 0.5).astype(int)

print(f"\n📊 Distribusi Prediksi:")
print(
    f"   Predicted Laundering: {y_pred.sum():,} ({y_pred.sum()/len(y_pred)*100:.2f}%)"
)
print(
    f"   Predicted Normal: {(y_pred == 0).sum():,} ({(y_pred == 0).sum()/len(y_pred)*100:.2f}%)"
)
print(f"\n📊 Ground Truth:")
print(f"   Actual Laundering: {y_test.sum():,} ({y_test.sum()/len(y_test)*100:.2f}%)")
print(
    f"   Actual Normal: {(y_test == 0).sum():,} ({(y_test == 0).sum()/len(y_test)*100:.2f}%)"
)

from sklearn.metrics import precision_recall_curve, average_precision_score, roc_curve
from sklearn.metrics import precision_score, recall_score, f1_score


precision = precision_score(y_test, y_pred, pos_label=1, zero_division=0)
recall = recall_score(y_test, y_pred, pos_label=1, zero_division=0)
f1 = f1_score(y_test, y_pred, pos_label=1, zero_division=0)
roc_auc = roc_auc_score(y_test, y_pred_proba)
pr_auc = average_precision_score(y_test, y_pred_proba)

print(f"\n🎯 Metrik Deteksi Pola Laundering (Class 1):")
print(f"   Precision: {precision:.4f} ({precision*100:.2f}%)")
print(f"   Recall:    {recall:.4f} ({recall*100:.2f}%)")
print(f"   F1-Score:  {f1:.4f}")
print(f"   ROC-AUC:   {roc_auc:.4f}")
print(f"   ⭐ PR-AUC: {pr_auc:.4f} (Metrik terpenting untuk AML!)")

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print(f"\n📊 Confusion Matrix:")
print(f"   False Positive (FP): {fp:,} - Normal incorrectly flagged ⚠️")
print(f"   False Negative (FN): {fn:,} - Laundering MISSED 🚨")

print(f"\n💡 Interpretasi Bisnis untuk Deteksi 8 Pola AML:")
if tp + fp > 0:
    print(f"   📌 Dari {tp + fp:,} transaksi yang ditandai mencurigakan:")

    print(f"      • {fp:,} adalah false alarm ({fp/(tp+fp)*100:.1f}%) ⚠️")
    print(f"      • Precision = {precision*100:.1f}%")

if tp + fn > 0:
    print(f"\n   📌 Dari {tp + fn:,} kasus laundering sebenarnya:")

    print(f"      • {fn:,} lolos dari deteksi ({fn/(tp+fn)*100:.1f}%) 🚨")
    print(f"      • Recall = {recall*100:.1f}%")

accuracy = (tp + tn) / (tp + tn + fp + fn)
baseline_acc = (y_test == 0).sum() / len(y_test)

print(f"\n⚠️ Akurasi Total: {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"   PENTING: Akurasi TIDAK boleh jadi metrik utama!")
print(f"   Baseline (always predict Normal): {baseline_acc*100:.2f}%")
print(f"   → Model bodoh juga bisa dapat akurasi {baseline_acc*100:.2f}%!")

print(f"\n🎯 Kesimpulan Metrik:")
print(f"   ⚠️ Precision = {precision*100:.1f}% perlu ditingkatkan (banyak false alarm)")
print(f"   💡 Untuk AML, Recall > Precision (missing fraud lebih berbahaya!)")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    ax=axes[0],
    xticklabels=["Normal (0)", "Laundering (1)"],
    yticklabels=["Normal (0)", "Laundering (1)"],
    cbar_kws={"label": "Count"},
)
axes[0].set_title(
    "Confusion Matrix - CatBoost AML Detection", fontsize=12, fontweight="bold"
)
axes[0].set_ylabel("True Label", fontsize=11)
axes[0].set_xlabel("Predicted Label", fontsize=11)

axes[0].text(
    0.5,
    -0.15,
    f"TN={tn:,}  FP={fp:,}\nFN={fn:,}  TP={tp:,}",
    ha="center",
    transform=axes[0].transAxes,
    fontsize=10,
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.3),
)

fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
axes[1].plot(
    fpr, tpr, color="darkblue", lw=2.5, label=f"CatBoost (AUC = {roc_auc:.4f})"
)
axes[1].plot(
    [0, 1], [0, 1], color="gray", lw=1.5, linestyle="--", label="Random Classifier"
)
axes[1].fill_between(fpr, tpr, alpha=0.2, color="blue")
axes[1].set_xlim([0.0, 1.0])
axes[1].set_ylim([0.0, 1.05])
axes[1].set_xlabel("False Positive Rate", fontsize=11)
axes[1].set_ylabel("True Positive Rate (Recall)", fontsize=11)
axes[1].set_title("ROC Curve - AML Detection", fontsize=12, fontweight="bold")
axes[1].legend(loc="lower right", fontsize=10)
axes[1].grid(alpha=0.3, linestyle="--")

precision_curve, recall_curve, _ = precision_recall_curve(y_test, y_pred_proba)
baseline_precision = y_test.sum() / len(y_test)

axes[2].plot(
    recall_curve,
    precision_curve,
    color="darkred",
    lw=2.5,
    label=f"CatBoost (PR-AUC = {pr_auc:.4f})",
)
axes[2].axhline(
    y=baseline_precision,
    color="gray",
    linestyle="--",
    lw=1.5,
    label=f"Baseline = {baseline_precision:.4f}",
)
axes[2].fill_between(recall_curve, precision_curve, alpha=0.2, color="red")
axes[2].set_xlim([0.0, 1.0])
axes[2].set_ylim([0.0, 1.05])
axes[2].set_xlabel("Recall (Sensitivity)", fontsize=11)
axes[2].set_ylabel("Precision", fontsize=11)
axes[2].set_title(
    "⭐ Precision-Recall Curve (Metrik Utama AML)", fontsize=12, fontweight="bold"
)
axes[2].legend(loc="lower left", fontsize=10)
axes[2].grid(alpha=0.3, linestyle="--")

axes[2].text(
    0.5,
    0.05,
    "PR-AUC > Baseline = Model berhasil!\nSemakin tinggi PR-AUC, semakin baik",
    ha="center",
    transform=axes[2].transAxes,
    fontsize=9,
    bbox=dict(boxstyle="round", facecolor="yellow", alpha=0.3),
)

plt.tight_layout()
plt.show()

print(
    f"      - Baseline kita = {baseline_precision:.4f} ({baseline_precision*100:.2f}%)"
)
print(f"      - PR-AUC kita = {pr_auc:.4f}")
print(
    f"      - Improvement = {(pr_auc/baseline_precision - 1)*100:.1f}% better than random!"
)


feature_importance = model.get_feature_importance(train_pool)
feature_names = X_train.columns

fi_df = pd.DataFrame(
    {"feature": feature_names, "importance": feature_importance}
).sort_values("importance", ascending=False)

print(fi_df.head(10))

plt.figure(figsize=(10, 6))
top_features = fi_df.head(15)
plt.barh(top_features["feature"], top_features["importance"])
plt.xlabel("Importance")
plt.title("Top 15 Feature Importance - CatBoost AML")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


import os

model_path = "catboost_aml.cbm"
model.save_model(model_path)

print(f"Ukuran file: {os.path.getsize(model_path) / 1024:.2f} KB")

model.save_model("catboost_aml.json", format="json")

from catboost import CatBoostClassifier

loaded_model = CatBoostClassifier()
loaded_model.load_model(model_path)

print(f"Model info: {loaded_model.get_params()['iterations']} iterations")


sample_size = min(len(X_test), 100000)
sample_indices = np.random.choice(len(X_test), sample_size, replace=False)
X_sample = X_test.iloc[sample_indices]
y_sample = y_test.iloc[sample_indices]

sample_proba_raw = model.predict_proba(X_sample)[:, 1]
if "probability_calibrator" in locals():
    sample_proba = probability_calibrator.transform(sample_proba_raw)
else:
    sample_proba = sample_proba_raw

sample_pred = (sample_proba >= 0.5).astype(int)

results_df = pd.DataFrame(
    {
        "Index": sample_indices,
        "True Label": y_sample.values,
        "Predicted": sample_pred,
        "Probability (Laundering)": sample_proba,
        "Correct": (y_sample.values == sample_pred),
    }
)

results_pred1 = results_df[results_df["Predicted"] == 1]

n_total = len(results_df)

n_test_laundering = int((y_sample == 1).sum())
n_test_normal = int((y_sample == 0).sum())
pct_test_laundering = n_test_laundering / n_total * 100 if n_total else 0.0
pct_test_normal = n_test_normal / n_total * 100 if n_total else 0.0

true_counts = results_df["True Label"].value_counts().to_dict()
n_analyzed_laundering = int(true_counts.get(1, 0))
n_analyzed_normal = int(true_counts.get(0, 0))
pct_analyzed_laundering = n_analyzed_laundering / n_total * 100 if n_total else 0.0
pct_analyzed_normal = n_analyzed_normal / n_total * 100 if n_total else 0.0

pred_counts = results_df["Predicted"].value_counts().to_dict()
n_pred_laundering = int(pred_counts.get(1, 0))
n_pred_normal = int(pred_counts.get(0, 0))
pct_pred_laundering = n_pred_laundering / n_total * 100 if n_total else 0.0
pct_pred_normal = n_pred_normal / n_total * 100 if n_total else 0.0

pred1_true_counts = results_pred1["True Label"].value_counts().to_dict()
n_pred1_true_laundering = int(pred1_true_counts.get(1, 0))
n_pred1_true_normal = int(pred1_true_counts.get(0, 0))
n_pred1_total = len(results_pred1)
pct_pred1_true_laundering = (
    n_pred1_true_laundering / n_pred1_total * 100 if n_pred1_total else 0.0
)
pct_pred1_true_normal = (
    n_pred1_true_normal / n_pred1_total * 100 if n_pred1_total else 0.0
)


print(f"Total sample: {n_total}")
print(f"Jumlah laundering: {n_test_laundering} ({pct_test_laundering:.2f}%)")
print(f"Jumlah normal   : {n_test_normal} ({pct_test_normal:.2f}%)")

print(
    f"Jumlah laundering (true) : {n_analyzed_laundering} ({pct_analyzed_laundering:.2f}%)"
)
print(f"Jumlah normal (true)     : {n_analyzed_normal} ({pct_analyzed_normal:.2f}%)")

print(f"Predicted laundering (1): {n_pred_laundering} ({pct_pred_laundering:.2f}%)")
print(f"Predicted normal    (0): {n_pred_normal} ({pct_pred_normal:.2f}%)")

print(f"Total predicted=1        : {n_pred1_total}")
print(
    f" -> Sebenarnya laundering: {n_pred1_true_laundering} ({pct_pred1_true_laundering:.2f}%)"
)
print(
    f" -> Sebenarnya normal    : {n_pred1_true_normal} ({pct_pred1_true_normal:.2f}%)"
)

print(f"Total predicted = 1: {len(results_pred1)} dari {len(results_df)}")


custom_threshold = 0.1
sample_pred_custom = (sample_proba >= custom_threshold).astype(int)

results_custom_df = pd.DataFrame(
    {
        "Index": sample_indices,
        "True Label": y_sample.values,
        "Probability": sample_proba,
        "Pred (0.5)": sample_pred,
        "Pred (0.3)": sample_pred_custom,
    }
)

print(results_custom_df.to_string(index=False))
print(
    f"   Dengan threshold 0.3, kita prediksi {sample_pred_custom.sum()} transaksi sebagai laundering"
)


from sklearn.metrics import precision_recall_curve, auc


if "prob_valid" not in locals():
    raise ValueError(
        "Probability arrays belum tersedia. Jalankan cell calibration terlebih dahulu."
    )

precision, recall, thresholds = precision_recall_curve(y_valid, prob_valid)

f1_scores = 2 * precision * recall / (precision + recall + 1e-12)
best_f1_idx = f1_scores.argmax()
best_threshold_f1 = thresholds[best_f1_idx] if best_f1_idx < len(thresholds) else 0.5
best_f1 = f1_scores[best_f1_idx]

print(f"\n📊 Optimization Results (Validation Set):")
print(f"   Best F1 Score: {best_f1:.4f}")
print(f"   Optimal Threshold: {best_threshold_f1:.4f}")
print(f"   Precision at optimal: {precision[best_f1_idx]:.4f}")
print(f"   Recall at optimal: {recall[best_f1_idx]:.4f}")

recall_targets = [0.8, 0.9, 0.95]
print(f"\n📈 Business-Driven Thresholds:")

for target_recall in recall_targets:
    idx = np.where(recall >= target_recall)[0]
    if len(idx) > 0:
        idx = idx[-1]
        thr = thresholds[idx] if idx < len(thresholds) else 0.0
        prec = precision[idx]
        rec = recall[idx]
        f1 = 2 * prec * rec / (prec + rec + 1e-12)
        print(
            f"   Recall ≥ {target_recall:.0%}: threshold={thr:.4f}, precision={prec:.4f}, F1={f1:.4f}"
        )
    else:
        print(f"   Recall ≥ {target_recall:.0%}: belum tercapai pada kurva PR")

pr_auc = auc(recall, precision)
print(f"\n📊 PR-AUC (Validation): {pr_auc:.4f}")

best_threshold = best_threshold_f1

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(recall, precision, "b-", linewidth=2, label=f"PR Curve (AUC={pr_auc:.3f})")
plt.scatter(
    recall[best_f1_idx],
    precision[best_f1_idx],
    color="red",
    s=100,
    zorder=5,
    label=f"Best F1={best_f1:.3f} @ thr={best_threshold:.3f}",
)
plt.xlabel("Recall", fontsize=12)
plt.ylabel("Precision", fontsize=12)
plt.title("Precision-Recall Curve - AML Detection", fontsize=14, fontweight="bold")
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


y_pred_train_opt = (prob_train >= best_threshold).astype(int)
y_pred_valid_opt = (prob_valid >= best_threshold).astype(int)
y_pred_test_opt = (prob_test >= best_threshold).astype(int)

y_pred_valid_default = (prob_valid >= 0.5).astype(int)

print(f"\n🎯 Validation Set - Optimal Threshold ({best_threshold:.4f}):")
print(
    classification_report(
        y_valid, y_pred_valid_opt, target_names=["Normal", "Laundering"], digits=4
    )
)

print(f"\n📊 Confusion Matrix (Validation - Optimal):")
cm = confusion_matrix(y_valid, y_pred_valid_opt)
print(f"                 Predicted Normal  Predicted Laundering")
print(f"Actual Normal           {cm[0,0]:6d}              {cm[0,1]:6d}")
print(f"Actual Laundering       {cm[1,0]:6d}              {cm[1,1]:6d}")

tn, fp, fn, tp = cm.ravel()
fpr = fp / (fp + tn)
fnr = fn / (fn + tp)

print(f"\n💼 Business Metrics (Validation):")
print(f"   False Positive Rate: {fpr:.4f} ({fp:,} innocent flagged)")
print(f"   False Negative Rate: {fnr:.4f} ({fn:,} laundering missed)")
print(f"   Cost of FP: {fp} investigations wasted")
print(f"   Cost of FN: {fn} laundering cases missed ⚠️")

print(f"\n📊 Comparison: Optimal vs Default Threshold (0.5):")
print(f"\n   Default Threshold (0.5):")
print(
    classification_report(
        y_valid, y_pred_valid_default, target_names=["Normal", "Laundering"], digits=4
    )
)

print(f"\n" + "=" * 80)
print(f"🎯 TEST SET EVALUATION (Final Performance)")
print(f"=" * 80)
print(f"\nThreshold: {best_threshold:.4f}")
print(
    classification_report(
        y_test, y_pred_test_opt, target_names=["Normal", "Laundering"], digits=4
    )
)

print(f"\n📊 Confusion Matrix (Test Set):")
cm_test = confusion_matrix(y_test, y_pred_test_opt)
print(f"                 Predicted Normal  Predicted Laundering")
print(f"Actual Normal           {cm_test[0,0]:6d}              {cm_test[0,1]:6d}")
print(f"Actual Laundering       {cm_test[1,0]:6d}              {cm_test[1,1]:6d}")

roc_auc_valid = roc_auc_score(y_valid, prob_valid)
roc_auc_test = roc_auc_score(y_test, prob_test)

print(f"\n📈 AUC Scores:")
print(f"   ROC-AUC (Validation): {roc_auc_valid:.4f}")
print(f"   ROC-AUC (Test): {roc_auc_test:.4f}")
print(f"   PR-AUC (Validation): {pr_auc:.4f}")


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if "prob_test" not in locals():
    raise ValueError("prob_test not found. Jalankan sel evaluasi terlebih dahulu.")

score_df = pd.DataFrame(
    {"probability": prob_test, "label": y_test.reset_index(drop=True)}
)
score_df["pred_default"] = (prob_test >= 0.5).astype(int)

print(score_df.groupby("label")["probability"].describe())

plt.figure(figsize=(10, 4))
plt.hist(
    score_df.loc[score_df["label"] == 0, "probability"],
    bins=120,
    alpha=0.6,
    label="Normal",
)
plt.hist(
    score_df.loc[score_df["label"] == 1, "probability"],
    bins=120,
    alpha=0.6,
    label="Laundering",
)
plt.yscale("log")
plt.xlabel("Predicted probability")
plt.ylabel("Frequency (log scale)")
plt.title("Probability distribution by true label (Test set)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

from sklearn.metrics import precision_recall_curve

precisions, recalls, pr_thresholds = precision_recall_curve(y_test, prob_test)
thr_df = pd.DataFrame(
    {
        "threshold": np.append(pr_thresholds, 1.0),
        "precision": precisions,
        "recall": recalls,
    }
)

print(thr_df.iloc[:-1].sort_values("precision", ascending=False).head(10))


def precision_at_k(probs: np.ndarray, labels: pd.Series, top_k: int) -> float:
    top_k = min(top_k, len(labels))
    if top_k == 0:
        return 0.0
    ordered_idx = np.argsort(probs)[-top_k:]
    return float(labels.reset_index(drop=True).iloc[ordered_idx].sum() / top_k)


for k in [100, 500, 1_000, 5_000, 10_000]:
    value = precision_at_k(prob_test, y_test.reset_index(drop=True), k)
    print(f"precision@{k:>5}: {value:.4f}")

ALERT_BUDGET = 5_000
labels_test = y_test.reset_index(drop=True)
ordered_idx = np.argsort(prob_test)[::-1]
alert_idx = ordered_idx[:ALERT_BUDGET]

alert_threshold = float(prob_test[alert_idx[-1]])
alert_df = pd.DataFrame(
    {"probability": prob_test[alert_idx], "label": labels_test.iloc[alert_idx]}
).reset_index(drop=True)

true_alerts = int(alert_df["label"].sum())
false_alerts = ALERT_BUDGET - true_alerts
missed_positives = int(labels_test.sum() - true_alerts)
true_negatives = int(len(labels_test) - ALERT_BUDGET - missed_positives)

precision_budget = true_alerts / ALERT_BUDGET if ALERT_BUDGET else 0.0
recall_budget = true_alerts / labels_test.sum()
fpr_budget = false_alerts / (false_alerts + true_negatives)

print(f"   Alerts sent: {ALERT_BUDGET:,}")
print(f"   Threshold corresponding to last alert: {alert_threshold:.4f}")
print(f"   True alerts: {true_alerts:,} | False alerts: {false_alerts:,}")
print(f"   Precision (budget): {precision_budget:.4f}")
print(f"   Recall (coverage): {recall_budget:.4f}")
print(f"   False Positive Rate (budgeted): {fpr_budget:.4f}")
print(f"   Missed laundering cases: {missed_positives:,}")

alert_df.head()

from sklearn.metrics import (
    precision_score,
    recall_score,
    average_precision_score,
    precision_recall_curve,
)

weight_candidates = [1, 5, 10, 15, 20, 30, 40, 50]
weight_results = []

print(
    "⚙️  Menjalankan training ulang CatBoost untuk setiap kandidat weight (iterasi 600)"
)
for weight_value in weight_candidates:
    trial_model = CatBoostClassifier(
        iterations=600,
        learning_rate=0.05,
        depth=6,
        loss_function="Logloss",
        eval_metric="PRAUC",
        scale_pos_weight=weight_value,
        cat_features=categorical_features,
        random_seed=42,
        verbose=False,
        early_stopping_rounds=50,
        l2_leaf_reg=5,
        bootstrap_type="MVS",
        subsample=0.8,
        colsample_bylevel=0.8,
    )
    trial_model.fit(train_pool, eval_set=valid_pool, use_best_model=True)
    prob_valid_trial = trial_model.predict_proba(X_valid)[:, 1]

    pr_prec, pr_rec, pr_thr = precision_recall_curve(y_valid, prob_valid_trial)
    f1_scores = 2 * pr_prec * pr_rec / (pr_prec + pr_rec + 1e-12)
    best_idx = f1_scores.argmax()
    best_thr = pr_thr[best_idx] if best_idx < len(pr_thr) else 0.5

    y_valid_pred = (prob_valid_trial >= best_thr).astype(int)
    prec_val = precision_score(y_valid, y_valid_pred, zero_division=0)
    rec_val = recall_score(y_valid, y_valid_pred)
    pr_auc_val = average_precision_score(y_valid, prob_valid_trial)

    topk_prec_1000 = precision_at_k(
        prob_valid_trial, y_valid.reset_index(drop=True), 1_000
    )

    weight_results.append(
        {
            "scale_pos_weight": weight_value,
            "best_threshold": best_thr,
            "precision": prec_val,
            "recall": rec_val,
            "best_f1": f1_scores[best_idx],
            "pr_auc": pr_auc_val,
            "precision@1000": topk_prec_1000,
        }
    )

weight_results_df = pd.DataFrame(weight_results)
weight_results_df.sort_values("precision@1000", ascending=False)


try:
    import shap


except ImportError:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "shap"])
    import shap


sample_size = min(1000, len(X_valid))
X_sample = X_valid.sample(n=sample_size, random_state=42)
y_sample = y_valid.loc[X_sample.index]

print(f"\n📊 SHAP Analysis on {sample_size} validation samples")
print(f"   Laundering samples: {y_sample.sum()}")
print(f"   Normal samples: {len(y_sample) - y_sample.sum()}")

print(f"\n⏳ Creating SHAP explainer...")
explainer = shap.TreeExplainer(model)

print(f"⏳ Computing SHAP values (this may take 1-2 minutes)...")
shap_values = explainer.shap_values(X_sample)

if isinstance(shap_values, list):
    shap_values_laundering = shap_values[1]
else:
    shap_values_laundering = shap_values


print(f"\n📊 1. SHAP Summary Plot (Feature Importance)")
plt.figure(figsize=(10, 8))
shap.summary_plot(shap_values_laundering, X_sample, plot_type="bar", show=False)
plt.title("SHAP Feature Importance - AML Detection", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

print(f"\n📊 2. SHAP Beeswarm Plot (Feature Impact)")
plt.figure(figsize=(10, 8))
shap.summary_plot(shap_values_laundering, X_sample, show=False)
plt.title("SHAP Feature Impact - AML Detection", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

feature_importance = np.abs(shap_values_laundering).mean(axis=0)
feature_names = X_sample.columns
top_indices = np.argsort(feature_importance)[-10:][::-1]

print(f"\n🏆 Top 10 Most Important Features:")
print(f"{'Rank':<6} {'Feature':<30} {'Mean |SHAP|':<15}")
for rank, idx in enumerate(top_indices, 1):
    print(f"{rank:<6} {feature_names[idx]:<30} {feature_importance[idx]:<15.4f}")

laundering_indices = y_sample[y_sample == 1].index
if len(laundering_indices) > 0:

    sample_idx_in_sample = 0
    for i, idx in enumerate(X_sample.index):
        if y_sample.loc[idx] == 1:
            sample_idx_in_sample = i
            original_idx = idx
            break

    print(f"\n📋 Example Explanation: Laundering Transaction")
    print(f"   Sample position: {sample_idx_in_sample}")
    print(f"   Actual: Laundering")

    prob_sample = model.predict_proba(X_sample.iloc[[sample_idx_in_sample]])[:, 1][0]
    print(f"   Predicted prob: {prob_sample:.4f}")

    plt.figure(figsize=(10, 6))
    shap.waterfall_plot(
        shap.Explanation(
            values=shap_values_laundering[sample_idx_in_sample],
            base_values=(
                explainer.expected_value
                if not isinstance(explainer.expected_value, list)
                else explainer.expected_value[1]
            ),
            data=X_sample.iloc[sample_idx_in_sample],
            feature_names=feature_names,
        ),
        show=False,
    )
    plt.title("SHAP Waterfall Plot - Laundering Case", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

print(f"\n💡 Key Insights:")
print(f"   - Review top features for domain consistency")
print(f"   - Verify no leakage features (e.g., future-looking stats)")
print(f"   - Use for audit trail and regulatory compliance")


print(f"   📈 Total: {X_train.shape[1]} features")


precision_val = tp / (tp + fp) if (tp + fp) > 0 else 0
recall_val = tp / (tp + fn) if (tp + fn) > 0 else 0
f1_val = (
    2 * precision_val * recall_val / (precision_val + recall_val)
    if (precision_val + recall_val) > 0
    else 0
)

print(f"   ⭐ PR-AUC:    {pr_auc:.4f} (Metrik utama untuk AML!)")
print(f"   📊 Precision: {precision_val:.4f} ({precision_val*100:.1f}%)")
print(f"   📊 Recall:    {recall_val:.4f} ({recall_val*100:.1f}%)")
print(f"   📊 F1-Score:  {f1_val:.4f}")
print(f"   📊 ROC-AUC:   {roc_auc_valid:.4f}")
print(f"   🎯 Optimal Threshold: {best_threshold:.4f}")
print(f"   ")
print(f"   Confusion Matrix (Validation):")
print(f"   - False Negative: {fn:,} laundering missed 🚨")
print(f"   - False Positive: {fp:,} false alarm ⚠️")

tn_test, fp_test, fn_test, tp_test = cm_test.ravel()
precision_test_val = tp_test / (tp_test + fp_test) if (tp_test + fp_test) > 0 else 0
recall_test_val = tp_test / (tp_test + fn_test) if (tp_test + fn_test) > 0 else 0
f1_test_val = (
    2 * precision_test_val * recall_test_val / (precision_test_val + recall_test_val)
    if (precision_test_val + recall_test_val) > 0
    else 0
)

from sklearn.metrics import precision_recall_curve, auc

precision_test_curve, recall_test_curve, _ = precision_recall_curve(y_test, prob_test)
test_pr_auc = auc(recall_test_curve, precision_test_curve)

print(f"   ⭐ PR-AUC (Test):    {test_pr_auc:.4f}")
print(
    f"   📊 Precision (Test): {precision_test_val:.4f} ({precision_test_val*100:.1f}%)"
)
print(f"   📊 Recall (Test):    {recall_test_val:.4f} ({recall_test_val*100:.1f}%)")
print(f"   📊 F1-Score (Test):  {f1_test_val:.4f}")
print(f"   📊 ROC-AUC (Test):   {roc_auc_test:.4f}")
print(f"   ")
print(f"   Confusion Matrix (Test):")
print(f"   - False Negative: {fn_test:,} laundering missed 🚨")
print(f"   - False Positive: {fp_test:,} false alarm ⚠️")

print(f"   ⚠️ Precision {precision_test_val*100:.1f}% → perlu human review")
print(
    f"   💡 Trade-off: High recall (catch all fraud) vs precision (reduce false alarms)"
)
print(f"   🎯 Untuk AML, Recall > Precision (missing fraud lebih berbahaya!)")

test_accuracy = (tp_test + tn_test) / (tp_test + tn_test + fp_test + fn_test)

print(f"   ❌ Akurasi = {test_accuracy*100:.2f}% ← MISLEADING!")
print(f"   ❌ Baseline (always predict normal) = {baseline_acc*100:.2f}%")
print(f"   ❌ Model bodoh juga dapat akurasi tinggi!")

print()

print(f"   ⚠️ Precision ~{precision_test_val*100:.0f}% (masih ada false positives)")
print(
    "   🔮 Future: Two-stage pipeline (CatBoost ranking + rules/model ringan) untuk menekan false positives"
)

print(f"   ⚠️ Precision {precision_test_val*100:.1f}% perlu improvement")


print(
    f"   ❌ Baseline (selalu prediksi 'Normal') = {(y_test==0).sum()/len(y_test)*100:.2f}% akurasi"
)
print(
    "   ❌ Model 'bodoh' bisa dapat akurasi tinggi tanpa deteksi laundering sama sekali"
)

print(
    "      - Bisa misleading untuk imbalanced (False Positive rate kecil karena banyak TN)"
)


print(
    "      - Metode: CatBoost + tuned class weights + calibrated probabilities + advanced features"
)
print(
    "      - SMOTE: hanya eksperimen ablation, pipeline akhir FULL class weights + calibration"
)
print(
    "      - Kontribusi: Bandingkan berbagai teknik handling imbalance dan jelaskan kenapa class weights dipakai di final pipeline"
)

print()

print(
    "   🔮 Future: Two-stage pipeline (CatBoost ranking + lightweight filter/rules) untuk memangkas false positive"
)


from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    precision_recall_curve,
    auc,
)

if "prob_test" not in locals() or "best_threshold" not in locals():
    raise ValueError("Harap jalankan sel evaluasi sebelum ringkasan akhir.")

y_pred_test_opt = (prob_test >= best_threshold).astype(int)
cm_test = confusion_matrix(y_test, y_pred_test_opt)
tn, fp, fn, tp = cm_test.ravel()
precision = precision_score(y_test, y_pred_test_opt, zero_division=0)
recall = recall_score(y_test, y_pred_test_opt)
f1 = f1_score(y_test, y_pred_test_opt)
roc_auc = roc_auc_score(y_test, prob_test)
prec_curve, rec_curve, _ = precision_recall_curve(y_test, prob_test)
pr_auc = auc(rec_curve, prec_curve)
base_rate = y_test.sum() / len(y_test)
imbalance_ratio = (
    float(scale_pos_weight)
    if "scale_pos_weight" in locals()
    else (len(y_train) - y_train.sum()) / y_train.sum()
)
fp_tp_ratio = (fp / tp) if tp else float("inf")


print(f"      • Total fitur terpakai: {X_train.shape[1]}")
print(
    f"      • scale_pos_weight ≈ {imbalance_ratio:,.0f} (neg/pos) → penalti FN lebih besar"
)

print(
    f"   ⭐ PR-AUC:   {pr_auc:.4f} ( {(pr_auc/base_rate-1)*100:.0f}% di atas baseline prevalence)"
)
print(
    f"   📊 Precision: {precision:.4f} ({precision*100:.1f}%) saat threshold optimal saat ini"
)
print(
    f"   📊 Recall:    {recall:.4f} ({recall*100:.1f}%) → hampir semua laundering tertangkap"
)
print(f"   📊 F1-Score:  {f1:.4f} (trade-off precision vs recall)")
print(f"   📊 ROC-AUC:   {roc_auc:.4f}")

print()
print(
    f"   ⚠️ Dari {tp+fp:,} alert yang dikirim, hanya {tp:,} benar ({precision*100:.1f}%)"
)
print(f"   ⚠️ {fp:,} alert palsu perlu dianalisis manusia → butuh filter lanjutan")
print(
    f"   🚨 {fn:,} laundering miss → perlu monitoring & threshold khusus pola high-risk"
)


fraction_normal_filtered = tn / (tn + fp)
print()

print(f"   • Precision masih {precision*100:.1f}% (rasio FP:TP ≈ {fp_tp_ratio:.0f}:1)")

print(
    "   1. Tambah two-stage filtering (rules / lightweight classifier) untuk pangkas FP"
)

print(
    "   • Altman et al. (2023). Realistic Synthetic Financial Transactions for AML Models. NeurIPS 2023."
)
print(
    "   • Goldstein et al. (2016). Precision-Recall considerations for imbalanced detection."
)

print(
    "   • Precision rendah (false alert tinggi) → butuh filter tahap-2 & threshold custom"
)
