from flask import Flask, render_template, request
import joblib

# Load your saved model and vectorizer
model = joblib.load("logistic_model.pkl")  # or your SVM model
vectorizer = joblib.load("vectorizer.pkl")  # TF-IDF or CountVectorizer

app = Flask(__name__)
