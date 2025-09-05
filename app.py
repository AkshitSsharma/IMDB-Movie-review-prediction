from flask import Flask, render_template, request
import joblib

# Load your saved model and vectorizer
model = joblib.load("logistic_model.pkl")  # or your SVM model
vectorizer = joblib.load("vectorizer.pkl")  # TF-IDF or CountVectorizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    if request.method == "POST":
        review = request.form["review"]  # get text from form
        review_vector = vectorizer.transform([review])  # transform text
        pred = model.predict(review_vector)  # 0 or 1
        
        # Map numeric prediction to human-readable text
        label_map = {0: "Negative", 1: "Positive"}
        sentiment = label_map[pred[0]]

    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)

