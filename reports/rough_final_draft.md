# Hybrid Crypto Scam Detection: A Comparative Computational Linguistics Approach Using Rule-Based, BERT, and Hybrid NLP Systems

## Project Summary

This project examines how different computational approaches can be used to detect deceptive cryptocurrency scam language in text. Cryptocurrency scams continue to grow across social media, text messages, email, and online forums, which creates a real-world need for better language-based fraud detection systems. Rather than relying on only one method, this project compares three different frameworks for representing and analyzing language.

The first system is a rule-based model built from explicit linguistic cues such as urgency phrases, guaranteed return claims, impersonation language, wallet requests, suspicious commands, and other common scam indicators. The second system is a BERT-based contextual classifier that uses machine learning to evaluate meaning based on surrounding language rather than exact wording alone. The third system is a hybrid model that combines both approaches to test whether explicit rules and contextual modeling perform better together.

The overall goal is to determine which framework provides the best balance of detection performance, interpretability, and linguistic coverage. In other words, I do not just want to know which model gets the highest score. I also want to understand *how* each system represents language, what kinds of scam messages each one catches well, and where each one fails. Humans love inventing scams, so apparently we need models for that now.

---

## Introduction

Language is one of the primary tools used in online deception. Scam messages often rely on persuasion, urgency, false authority, fear, reward bait, and calls to immediate action. In cryptocurrency spaces, these tactics are especially common because transactions can be fast, anonymous, and difficult to reverse once funds are sent. A scam message does not always need advanced hacking. Sometimes it only needs the right wording at the right moment, which is rude but effective.

Because scam communication is language-driven, it is a strong use case for computational linguistics. The challenge is deciding how language should be modeled. Should deceptive language be captured through explicit human-authored rules? Should it be learned automatically from labeled examples using modern language models? Or is the strongest solution a combination of both?

This project uses cryptocurrency scam detection as a case study to compare those competing approaches.

---

## Research Question

Which computational linguistic framework best detects cryptocurrency scam language:

1. A rule-based symbolic linguistic system  
2. A BERT-based contextual classification system  
3. A hybrid system combining both methods

A secondary question is whether the strongest-performing system is also the most interpretable and practically useful.

---

## Why This Topic Matters

Online fraud continues to expand, and cryptocurrency scams have become one of the most visible examples of digital deception. Many scams are distributed through text-heavy channels such as social media posts, phishing emails, direct messages, fake support chats, and promotional spam. That means language itself becomes part of the attack surface.

A successful detection system could help flag suspicious communication earlier and reduce harm. Even in a classroom setting, this project demonstrates how computational linguistics can be applied to a modern real-world problem rather than only theoretical examples. Also, if the internet insists on being weird, we may as well study it properly.

---

## Proposed Methodology

## 1. Rule-Based Linguistic System

The first model will be a human-authored symbolic system using explicit scam indicators. These indicators will be organized into categories such as:

- urgency language  
- guaranteed profit claims  
- impersonation / fake authority  
- wallet or credential requests  
- fear of loss language  
- suspicious formatting or links

Example phrases may include:

- act now  
- limited time  
- guaranteed returns  
- official support  
- connect wallet  
- verify account

This system will assign scores based on detected linguistic features and return an explanation showing which rules were triggered.

### Purpose

This model represents explicit linguistic knowledge. It is transparent, interpretable, and closely aligned with symbolic computational linguistics.

---

## 2. BERT-Based Contextual System

The second model will use a pretrained BERT language model. BERT was originally trained on large general text corpora and learns contextual relationships between words. Instead of only checking exact phrases, it evaluates how meaning is shaped by surrounding language.

For this project, a labeled dataset of scam and legitimate crypto-related text will be collected. BERT will then be fine-tuned on that dataset so it can better distinguish deceptive and non-deceptive language in this specific domain.

### Purpose

This model represents machine-learned linguistic understanding. It may capture paraphrases, subtle persuasion tactics, and contextual scam intent that a rule system misses.

---

## 3. Hybrid System

The third model will combine the outputs of the rule-based system and the BERT classifier. For example, rule scores and BERT probabilities may be merged into a final risk score.

This system will test whether explicit linguistic knowledge and contextual machine learning perform better together than either method alone.

### Purpose

This model represents a hybrid view of language processing where handcrafted linguistic structure and learned semantic context support one another instead of competing like toddlers in a toy aisle.

---

## Data Sources

The dataset will include both scam and legitimate examples.

### Potential Scam Sources

- public spam or phishing datasets  
- cryptocurrency scam examples from research papers  
- scam-like social media posts  
- manually curated examples based on recurring scam tactics

### Potential Legitimate Sources

- CoinDesk news headlines  
- Cointelegraph articles  
- Binance or Coinbase announcements  
- Yahoo Finance headlines  
- educational or regulatory crypto content

Each example will be labeled as either:

- scam  
- legitimate

Optional future labels may include scam subtype categories such as phishing, impersonation, giveaway fraud, or investment scam.

---

## Tools and Libraries

The project will be implemented in Python using tools such as:

- pandas  
- numpy  
- nltk  
- scikit-learn  
- transformers  
- torch  
- matplotlib

Development will be organized through GitHub with notebook-based experimentation and reusable source modules.

---

## Evaluation Plan

All three systems will be tested on the same held-out evaluation data.

Metrics may include:

- Accuracy  
- Precision  
- Recall  
- F1-score

In addition to numeric metrics, the project will compare:

- interpretability  
- types of messages missed  
- false positives  
- practical usefulness

This matters because a model that scores well but cannot explain itself may be less useful than a slightly weaker model with clear reasoning.

---

## Connection to Course Themes

This project directly connects to symbolic computational linguistics by comparing different ways linguistic knowledge can be represented computationally.

### Rule-Based System
Uses explicit symbolic descriptions of language patterns.

### BERT-Based System
Uses learned contextual representations derived from labeled examples.

### Hybrid System
Combines symbolic rules with contextual inference.

The project also draws on lexical, semantic, pragmatic, and discourse features commonly studied in linguistics. In short, this is not just about catching scams. It is about comparing theories of language understanding through a real application.

---

## Limitations

Several limitations are expected:

- scam language changes quickly  
- datasets may be noisy or imbalanced  
- some legitimate marketing language may resemble scams  
- BERT requires more compute resources than rules  
- no model can perfectly detect all deception

Unfortunately, criminals do not pause innovation for academic timelines.

---

## Timeline / Next Steps

### Phase 1
Collect data and finalize preprocessing pipeline.

### Phase 2
Build and test rule-based system.

### Phase 3
Fine-tune and evaluate BERT system.

### Phase 4
Build hybrid scoring system.

### Phase 5
Compare results, finalize report, and prepare presentation.

---

## References

Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O’Reilly Media.

Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of deep bidirectional transformers for language understanding*.

Jurafsky, D., & Martin, J. H. (n.d.). *Speech and language processing*.

Nizzoli, L., Tardelli, S., Avvenuti, M., Cresci, S., & Tesconi, M. (2021). *Charting the landscape of online cryptocurrency scams*. IEEE Access.

Bar-Hillel, Y. (1960). *A demonstration of the nonfeasibility of fully automatic high quality translation*.