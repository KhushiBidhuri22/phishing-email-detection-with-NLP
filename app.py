from flask import Flask, render_template, request
import joblib
import numpy as np
import re
from scipy.sparse import hstack

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


# ---------------- Metadata Feature Functions ---------------- #

suspicious_words = [
    "verify", "account", "urgent", "click", "bank",
    "password", "login", "winner", "free", "security"
]

urgency_words = [
    "urgent", "immediately", "now",
    "asap", "today", "hurry"
]


def extract_metadata(text):

    words = text.split()

    email_length = len(text)

    word_count = len(words)

    avg_word_length = (
        sum(len(word) for word in words) / word_count
        if word_count > 0 else 0
    )

    url_count = len(
        re.findall(r"http[s]?://|www\.", text.lower())
    )

    email_count = len(
        re.findall(r"\S+@\S+", text)
    )

    digit_count = sum(
        char.isdigit() for char in text
    )

    exclamation_count = text.count("!")

    question_count = text.count("?")

    uppercase_count = sum(
        char.isupper() for char in text
    )

    special_char_count = len(
        re.findall(r"[^A-Za-z0-9\s]", text)
    )

    currency_count = len(
        re.findall(r"[$₹€£]", text)
    )

    suspicious_count = sum(
        1 for word in words
        if word.lower() in suspicious_words
    )

    urgency_score = sum(
        1 for word in words
        if word.lower() in urgency_words
    )


    return np.array([[
        email_length,
        word_count,
        avg_word_length,
        url_count,
        email_count,
        digit_count,
        exclamation_count,
        question_count,
        uppercase_count,
        special_char_count,
        currency_count,
        suspicious_count,
        urgency_score
    ]])


# ---------------- Flask Routes ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    email = request.form["email"]

    # TF-IDF features (10000)
    text_features = vectorizer.transform([email])

    # Metadata features (13)
    metadata_features = extract_metadata(email)

    # Combine -> 10013 features
    final_features = hstack(
        [text_features, metadata_features]
    )

    prediction = model.predict(final_features)[0]


    if prediction == 1:
        result = " Phishing Email"
    else:
        result = " Legitimate Email"


    return render_template(
        "index.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)