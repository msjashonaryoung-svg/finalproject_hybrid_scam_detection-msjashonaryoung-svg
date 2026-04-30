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

```
finalproject_hybrid_scam_detection-msjashonaryoung-svg/
├── .devcontainer/
│   └── devcontainer.json
├── .gitignore
├── README.md
├── data/
│   ├── processed/
│   │   └── combined_scam_dataset.csv
│   └── raw/
│       ├── kaggle_email_phishing_normalized.csv
│       ├── manual_seed_examples.csv
│       ├── mendeley_sms_phishing.csv
│       ├── mendeley_sms_phishing_normalized.csv
│       ├── phishing_legit_dataset_KD_10000.csv
│       ├── sample_messages.csv
│       └── uci_sms_spam.csv
├── dockerfile
├── notebooks/
│   └── final_project_demo.ipynb
├── reports/
│   └── rough_final_draft.md
├── requirements.txt
└── src/
    ├── bert_model.py
    ├── data_collection.py
    ├── evaluation.py
    ├── hybrid_model.py
    ├── preprocessing.py
    └── rule_engine.py
```

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
