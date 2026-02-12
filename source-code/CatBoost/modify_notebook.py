import json
import os

input_path = 'catboost_aml.ipynb'
output_path = 'catboost_aml_improved.ipynb'

print(f"Reading {input_path}...")
with open(input_path, 'r') as f:
    nb = json.load(f)

scaling_modified = False
threshold_modified = False

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source_lines = cell['source']
        source_text = "".join(source_lines)
        
        # Modification 1: scale_pos_weight
        if "scale_pos = min(imbalance_ratio, 10.0)" in source_text:
            print("Found scale_pos cell. Modifying...")
            new_source = source_text.replace(
                "scale_pos = min(imbalance_ratio, 10.0)",
                "scale_pos = 100.0 # Aggressively boosted"
            )
            new_source = new_source.replace(
                "print(f'Using scale_pos_weight: {scale_pos:.1f} (capped, similar to Multi-GNN w_ce2)')",
                "print(f'Using scale_pos_weight: {scale_pos:.1f} (Aggressive for recall)')"
            )
            # Re-split into lines keeping newlines
            cell['source'] = [line for line in new_source.splitlines(keepends=True)]
            scaling_modified = True

        # Modification 2: find_best_threshold to optimize F2
        if "def find_best_threshold(y_true, y_proba, metric='f1'):" in source_text:
            print("Found find_best_threshold cell. Modifying...")
            new_source = """from sklearn.metrics import fbeta_score, f1_score, precision_score, recall_score, average_precision_score, confusion_matrix
import numpy as np

def find_best_threshold(y_true, y_proba, metric='f2'):
    \"\"\"Find the threshold that maximizes F2 score.\"\"\"
    best_score = 0
    best_thresh = 0.5
    for thresh in np.arange(0.01, 0.95, 0.01):
        y_pred_t = (y_proba >= thresh).astype(int)
        if y_pred_t.sum() == 0:
            continue
        
        if metric == 'f2':
            score = fbeta_score(y_true, y_pred_t, beta=2)
        else:
            score = f1_score(y_true, y_pred_t)
            
        if score > best_score:
            best_score = score
            best_thresh = thresh
    return best_thresh, best_score

def evaluate_model(model, X, y, dataset_name='Test', threshold=0.5):
    \"\"\"Evaluate model with custom threshold.\"\"\"
    y_proba = model.predict_proba(X)[:, 1]
    y_pred = (y_proba >= threshold).astype(int)
    
    f1 = f1_score(y, y_pred)
    f2 = fbeta_score(y, y_pred, beta=2)
    precision = precision_score(y, y_pred, zero_division=0)
    recall = recall_score(y, y_pred, zero_division=0)
    pr_auc = average_precision_score(y, y_proba)
    cm = confusion_matrix(y, y_pred)
    
    print(f'=== {dataset_name} Metrics (threshold={threshold:.2f}) ===')
    print(f'  F1:        {f1:.4f}')
    print(f'  F2:        {f2:.4f}')
    print(f'  Precision: {precision:.4f}')
    print(f'  Recall:    {recall:.4f}')
    print(f'  PR-AUC:    {pr_auc:.4f}')
    print(f'  Confusion Matrix:')
    print(f'    {cm}')
    print()
    
    return {'f1': f1, 'f2': f2, 'precision': precision, 'recall': recall, 
            'pr_auc': pr_auc, 'confusion_matrix': cm, 
            'y_pred': y_pred, 'y_proba': y_proba}

# --- Find optimal threshold on VALIDATION set ---
val_proba = model.predict_proba(X_val)[:, 1]
best_threshold, best_val_score = find_best_threshold(y_val, val_proba, metric='f2')
print(f'Optimal threshold (tuned on validation for F2): {best_threshold:.2f} -> Val F2: {best_val_score:.4f}')
print()

# Evaluate on all splits with optimal threshold
tr_metrics = evaluate_model(model, X_train, y_train, 'Train', threshold=best_threshold)
val_metrics = evaluate_model(model, X_val, y_val, 'Validation', threshold=best_threshold)
te_metrics = evaluate_model(model, X_test, y_test, 'Test', threshold=best_threshold)
"""
            cell['source'] = [line + '\n' for line in new_source.splitlines()]
            threshold_modified = True

if scaling_modified and threshold_modified:
    print(f"Modifications successful. Saving to {output_path}...")
    with open(output_path, 'w') as f:
        json.dump(nb, f, indent=1)
else:
    print("Error: Could not find all target cells to modify.")
    print(f"Scaling Modified: {scaling_modified}")
    print(f"Threshold Modified: {threshold_modified}")
    exit(1)
