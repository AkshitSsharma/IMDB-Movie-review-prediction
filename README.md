# IMDB Movie Review Sentiment Prediction

A web application that predicts the sentiment of IMDB movie reviews as **positive** or **negative** using Natural Language Processing (NLP) and machine learning.  

The project implements **Naive Bayes** and **Logistic Regression** models, with Logistic Regression achieving **90% accuracy**. It is deployed as a **Flask web app** for real-time sentiment prediction.

---

## Features
- Clean and preprocess movie review text (tokenization, removing stopwords, vectorization)
- Compare performance of **Naive Bayes** and **Logistic Regression** models
- High-performing Logistic Regression model with **90% accuracy**
- Interactive **Flask web application** to predict sentiment in real-time

---

## Tech Stack
- **Python** – Core programming language
- **NLP Libraries** – NLTK, Scikit-learn
- **Machine Learning Models** – Naive Bayes, Logistic Regression
- **Web Framework** – Flask
- **Pickle/Joblib** – Model serialization for deployment

---

## Installation & Setup
1. Clone the repository:  
   ```bash
   Usage
   Install dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py


Open your browser and go to http://127.0.0.1:5000 to use the app.

Enter a movie review in the input box.

Click "Predict Sentiment".

The app will classify the review as Positive or Negative.

Model Performance
Model	Accuracy
Naive Bayes	85%
Logistic Regression	90%
   git clone https://github.com/yourusername/imdb-sentiment-analysis.git
   cd imdb-sentiment-analysis
