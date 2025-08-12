

# Email Phishing Detection

## Overview

This project detects phishing emails using NLP and Machine Learning. It uses **TF-IDF vectorization** and **Logistic Regression** to classify emails as either phishing or legitimate.

## Features

* Preprocess email text (cleaning, tokenization, lemmatization)
* Extract TF-IDF features
* Train and evaluate ML model
* Streamlit-based web UI for live predictions

## Tech Stack

Python, Pandas, scikit-learn, NLTK, Streamlit

## Dataset

[Phishing Email Dataset - Kaggle](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?utm_source=chatgpt.com)

## Project Structure

```
email-phishing-detection/
│── README.md
│── requirements.txt
│── data/
│   └── phishing_dataset.csv
│── models/
│   ├── phishing_model.pkl
│   └── vectorizer.pkl
│── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── utils.py
└── ui/
    └── app.py
```

## How to Run

```bash
pip install -r requirements.txt
python src/train.py
streamlit run ui/app.py
```

## Future Improvements

* Integrate BERT for better accuracy
* Add API for email client integration
* Multi-language phishing detection support

---

If you want, I can also give you a **requirements.txt** that exactly matches this setup so it’s plug-and-play. That way, anyone who clones your repo can run it without troubleshooting dependencies.




