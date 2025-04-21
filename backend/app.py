from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

classifier = pipeline("text-classification")

@app.route("/predict", methods=["POST"])
def predict():
    input_text = request.json.get("input")
    result = classifier(input_text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)