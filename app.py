from flask import Flask, request, jsonify
from transformers import pipeline
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load pre-trained sentiment analysis pipeline
# Using a smaller, faster model for demonstration purposes
try:
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    logging.info("Sentiment analysis pipeline loaded successfully.")
except Exception as e:
    logging.error(f"Error loading sentiment analysis pipeline: {e}")
    sentiment_pipeline = None

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    """API endpoint for sentiment analysis."""
    if sentiment_pipeline is None:
        return jsonify({"error": "Sentiment analysis model not loaded."}), 500

    data = request.get_json()
    if not data or "text" not in data:
        logging.warning("Invalid request: 'text' field missing.")
        return jsonify({"error": "Invalid request. Please provide 'text' in the JSON body."}), 400

    text_to_analyze = data["text"]
    logging.info(f"Received text for analysis: {text_to_analyze[:50]}...")

    try:
        result = sentiment_pipeline(text_to_analyze)[0]
        sentiment = result["label"].lower()
        score = round(result["score"], 4)
        logging.info(f"Analysis complete. Sentiment: {sentiment}, Score: {score}")
        return jsonify({"sentiment": sentiment, "score": score}), 200
    except Exception as e:
        logging.error(f"Error during sentiment analysis: {e}")
        return jsonify({"error": "An error occurred during sentiment analysis."}), 500

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    status = "ok" if sentiment_pipeline is not None else "degraded"
    logging.info(f"Health check requested. Status: {status}")
    return jsonify({"status": status}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
