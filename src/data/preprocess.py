import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Cleans and preprocesses email text.
    Steps:
    1. Lowercase
    2. Remove URLs, HTML tags, numbers, and special characters
    3. Tokenize
    4. Remove stopwords
    5. Lemmatize words
    """
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # remove URLs
    text = re.sub(r"<.*?>", "", text)  # remove HTML tags
    text = re.sub(r"\d+", "", text)  # remove numbers
    text = re.sub(r"[^a-zA-Z]", " ", text)  # keep only letters

    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and len(word) > 2]

    return " ".join(tokens)
