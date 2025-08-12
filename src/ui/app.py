import sys
import os

# Add the project root path (two levels up from this file) to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.model.predict import predict_email

import streamlit as st
from src.model.predict import predict_email

st.set_page_config(page_title="Email Phishing Detection", layout="centered")

st.title("📧 Email Phishing Detection")
st.write("Paste your email text below to check if it's **Phishing** or **Legitimate**.")

email_text = st.text_area("✉️ Email Content:", height=200)

if st.button("🔍 Check Email"):
    if email_text.strip() == "":
        st.warning("Please enter email content.")
    else:
        result = predict_email(email_text)
        if result == 1:
            st.error("🚨 This email is **PHISHING**!")
        else:
            st.success("✅ This email seems **Legitimate**.")
