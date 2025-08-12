import joblib
from src.data.preprocess import clean_text

# Load saved model & vectorizer
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

def predict_email(text):
    """
    Predict if an email is phishing or legitimate.
    """
    text_clean = clean_text(text)
    text_vec = vectorizer.transform([text_clean])
    prediction = model.predict(text_vec)[0]
    return prediction
