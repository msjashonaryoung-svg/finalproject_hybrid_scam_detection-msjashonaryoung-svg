# Hybrid Scam Detection  
### A Comparative Computational Linguistics Approach  

This project explores how different computational approaches detect scam and phishing language across SMS and email communication.

The system compares three models:

- Rule-based symbolic linguistic system  
- BERT-based contextual model  
- Hybrid model combining both approaches  

The goal is to evaluate performance, interpretability, and linguistic coverage across these methods while highlighting trade-offs between symbolic and neural language processing.

---

## Dataset

The dataset consists of over 16,000 labeled messages compiled from multiple sources:

- SMS spam dataset (UCI)  
- Email phishing dataset (Kaggle)  
- SMS phishing / smishing dataset (Mendeley)  
- Manually curated examples  

This multi-source dataset enables evaluation across different communication contexts.

---

## Models

### Rule-Based Model
Uses predefined linguistic patterns such as urgency, credential requests, and impersonation.

Strength: High interpretability  
Limitation: Low recall for subtle scams  

---

### BERT-Based Model
Uses a pretrained transformer model to analyze contextual meaning.

Strength: Captures nuanced language  
Limitation: Higher false positives due to lack of task-specific fine-tuning  

---

### Hybrid Model
Combines rule-based and contextual scores to balance interpretability and performance.

---

## Results

| Model        | Accuracy | Precision | Recall | F1 Score |
|-------------|---------|----------|--------|---------|
| Rule-Based  | 0.64    | 1.00     | 0.19   | 0.32    |
| BERT Proxy  | 0.72    | 0.63     | 0.85   | 0.73    |
| Hybrid      | 0.72    | 0.64     | 0.84   | 0.72    |

Key Insight:

Rule-based models are precise but miss many scams.  
BERT captures more scams but over-classifies.  
The hybrid model balances both but inherits limitations from each.

---

## Limitations

- BERT model is not fine-tuned for scam detection  
- Dataset sources have varying labeling standards  
- Rule-based system depends on predefined patterns  

---

## Future Work

- Fine-tune BERT on scam-specific datasets  
- Expand dataset with real-world sources  
- Improve hybrid model using advanced ensemble techniques  

---

## Project Structure

hybrid-scam-detection/
│
├── data/
│   ├── raw/                         # Original downloaded datasets
│   │   ├── uci_sms_spam.csv
│   │   ├── phishing_legit_dataset_KD_10000.csv
│   │   └── mendeley_sms_phishing.csv
│   │
│   └── processed/                  # Cleaned and combined dataset
│       └── combined_scam_dataset.csv
│
├── notebooks/
│   └── final_project_demo.ipynb    # Main analysis and modeling notebook
│
├── src/
│   ├── data_collection.py          # Dataset download, cleaning, and merging
│   ├── preprocessing.py            # Text cleaning utilities
│   ├── rule_engine.py              # Rule-based scoring system
│   ├── bert_model.py               # BERT scoring logic
│   ├── hybrid_model.py             # Hybrid model combination logic
│   └── evaluation.py               # Metrics and evaluation helpers
│
├── reports/
│   └── rough_final_draft.md        # Final written report (draft)
│
├── README.md                      # Project overview and results
├── requirements.txt               # Python dependencies
└── .gitignore                     # Ignored files

---

## How to Run

Run dataset preparation:

```bash
    python src/data_collection.py
```

Then open the notebook:

```bash
    notebooks/final_project_demo.ipynb
```

and run all cells.

---

## Summary

This project demonstrates that combining symbolic linguistic rules with contextual machine learning provides a more robust approach to detecting deceptive language, while also highlighting the trade-offs between interpretability and performance.
