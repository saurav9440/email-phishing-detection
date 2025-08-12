import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
from src.data.preprocess import clean_text

# Load dataset
df = pd.read_csv("data/processed/merged_dataset.csv")

# Clean text
print("🧹 Cleaning text data...")
df["text_clean"] = df["email_text"].apply(clean_text)

# Features & Labels
X = df["text_clean"]
y = df["source"]

# Vectorize text
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
print("🤖 Training Logistic Regression model...")
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n📊 Model Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model & vectorizer
save_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'model')
os.makedirs(save_dir, exist_ok=True)

joblib.dump(model, os.path.join(save_dir, "phishing_model.pkl"))
joblib.dump(vectorizer, os.path.join(save_dir, "tfidf_vectorizer.pkl"))
print(f"✅ Model and vectorizer saved in {os.path.abspath(save_dir)}")
