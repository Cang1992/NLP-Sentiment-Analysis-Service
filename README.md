# NLP-Sentiment-Analysis-Service

## A Scalable Microservice for Real-time Sentiment Analysis

This repository presents a robust and scalable microservice for performing real-time sentiment analysis on text data. Built with Python and Flask, it leverages pre-trained transformer models (Hugging Face) to provide accurate sentiment scores, making it suitable for applications requiring immediate feedback on user-generated content, social media monitoring, or customer support analytics.

### Features

*   **RESTful API:** Easy-to-use API endpoints for submitting text and receiving sentiment predictions.
*   **Transformer Models:** Integration with state-of-the-art pre-trained models for high accuracy.
*   **Scalability:** Designed as a microservice, allowing for easy deployment and scaling in containerized environments.
*   **Docker Support:** Dockerfile included for simplified deployment.

### Getting Started

Follow these instructions to set up and run the sentiment analysis service locally.

#### Prerequisites

Ensure you have Python 3.8+ and Docker installed. Install Python dependencies:

```bash
pip install -r requirements.txt
```

#### Running Locally

1.  **Start the service:**
    ```bash
    python app.py
    ```
2.  **Access the API:** The service will be available at `http://127.0.0.1:5000`.

#### Running with Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t sentiment-service .
    ```
2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 sentiment-service
    ```

### API Endpoints

*   `POST /analyze`: Analyzes the sentiment of provided text.
    *   **Request Body:** `{"text": "Your input text here."}`
    *   **Response:** `{"sentiment": "positive", "score": 0.95}`

### Project Structure

```
. 
├── README.md
├── requirements.txt
├── app.py
└── Dockerfile
```

### Badges

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=for-the-badge&logo=flask)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=for-the-badge&logo=huggingface)
![Docker](https://img.shields.io/badge/Docker-20.x-blue?style=for-the-badge&logo=docker)

### License

This project is licensed under the MIT License - see the LICENSE file for details.
