from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    review = request.form["review"]

    review_vector = vectorizer.transform([review])

    prediction = model.predict(review_vector)[0]

    probability = model.predict_proba(review_vector)

    confidence = round(max(probability[0]) * 100, 2)

    return render_template(
    "index.html",
    prediction=prediction,
    confidence=confidence,
    review=review
)

if __name__ == "__main__":
    app.run(debug=True)