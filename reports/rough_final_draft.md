# Hybrid Scam Detection: A Comparative Computational Linguistics Approach Using Rule-Based, BERT, and Hybrid NLP Systems

## Abstract

This project investigates the effectiveness of different computational approaches for detecting scam and phishing language across SMS and email communication. A rule-based linguistic model, a BERT-based contextual model, and a hybrid approach are evaluated on a multi-source dataset of over 16,000 messages. The results highlight trade-offs between interpretability and performance, demonstrating that combining symbolic and contextual methods provides a more robust framework for detecting deceptive language.

---

## 1. Introduction

Deceptive communication, including spam messages and phishing emails, relies heavily on linguistic manipulation such as urgency, impersonation, and reward-based persuasion. Detecting these patterns is a key challenge in natural language processing.

This project compares three approaches:

- rule-based symbolic model  
- BERT-based contextual model  
- hybrid model  

The goal is to evaluate how each approach captures deceptive language across different communication contexts.

---

## 2. Dataset

The dataset consists of **16,283 labeled messages** compiled from multiple sources:

- SMS spam dataset (UCI)  
- phishing email dataset (Kaggle)  
- SMS phishing / smishing dataset (Mendeley)  
- manually curated examples  

The dataset includes:

- 9,066 legitimate messages  
- 7,217 scam messages  

This multi-source dataset enables analysis across SMS and email communication rather than restricting the study to a single domain.

---

## 3. Methodology

### Rule-Based Linguistic System

The rule-based model uses explicitly defined linguistic patterns associated with scam messages, including:

- urgency language  
- reward-based persuasion  
- credential or account requests  
- impersonation or authority cues  
- fear or loss framing  
- action-based instructions  

The model assigns a score based on detected patterns and provides interpretable outputs through triggered rule categories.

---

### BERT-Based Contextual Model

The BERT-based model uses a pretrained transformer model to evaluate contextual meaning. Rather than relying on exact keyword matches, it considers how meaning is shaped by surrounding language.

In this project, a pretrained sentiment-based BERT model is used as a proxy for contextual classification rather than a fine-tuned scam detection model.

---

### Hybrid Model

The hybrid model combines rule-based scores and BERT predictions into a single output. This approach aims to balance interpretability and contextual understanding by leveraging both symbolic and machine-learned representations.

---

### Threshold Selection

Threshold values were applied to convert model scores into binary classifications. These thresholds were selected empirically to balance precision and recall, particularly for the rule-based and hybrid models, where score distributions differ significantly.

Small adjustments to threshold values were observed to significantly impact model performance, highlighting the sensitivity of classification decisions to scoring strategies.

---

## 4. Results

| Model        | Accuracy | Precision | Recall | F1 Score |
|-------------|---------|----------|--------|---------|
| Rule-Based  | 0.64    | 1.00     | 0.19   | 0.32    |
| BERT Proxy  | 0.72    | 0.63     | 0.85   | 0.73    |
| Hybrid      | 0.72    | 0.64     | 0.84   | 0.72    |

---

## 5. Discussion

The rule-based model achieves perfect precision, meaning it only flags messages as scams when explicit indicators are present. However, its recall is extremely low, demonstrating that it misses a large number of scam messages that do not match predefined patterns.

The BERT-based model significantly improves recall, capturing more subtle and context-based scam language. However, it produces more false positives, likely due to being trained on general sentiment rather than scam-specific data.

The hybrid model balances these approaches, achieving strong recall while slightly improving precision compared to BERT alone. However, it does not significantly outperform the BERT model, suggesting that simple score combination is not sufficient to fully leverage both approaches.

Disagreement analysis shows that the models frequently classify messages differently. This highlights the fundamental difference between symbolic and neural language processing:

- rule-based systems detect explicit linguistic cues  
- contextual models infer meaning from broader patterns  

The sensitivity of model performance to threshold selection further highlights the importance of calibration when combining symbolic and neural approaches.

---

## 6. Limitations

Several limitations affect the results:

- the BERT model is not fine-tuned for scam detection  
- dataset sources use different labeling standards  
- rule-based patterns cannot capture evolving scam language  
- hybrid model relies on simple weighted combination  

These limitations contribute to false positives, missed detections, and inconsistencies across models.

---

## 7. Conclusion

This project demonstrates that combining symbolic linguistic rules with contextual machine learning provides a more effective approach to detecting scam and phishing language than either method alone.

However, it also shows that each approach has inherent limitations. Rule-based systems are precise but narrow, while contextual models are flexible but less interpretable.

Future work should focus on fine-tuning models for domain-specific detection and developing more advanced hybrid methods that better integrate symbolic and neural representations.

---

## References

Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O’Reilly Media.

Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of deep bidirectional transformers for language understanding*.

Jurafsky, D., & Martin, J. H. (n.d.). *Speech and language processing*.

Nizzoli, L., Tardelli, S., Avvenuti, M., Cresci, S., & Tesconi, M. (2021). *Charting the landscape of online scams*. IEEE Access.

Bar-Hillel, Y. (1960). *A demonstration of the nonfeasibility of fully automatic high quality translation*.