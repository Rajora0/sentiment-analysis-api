## Sentiment Analysis API with Quantized Model

This repository contains a simple Flask API that performs sentiment analysis on text input using a quantized DistilBERT model. Quantization helps reduce the model size and inference time, making it more efficient for deployment.

### Structure

- **`app.py`:** Main Flask application file. Defines the API endpoint and handles requests.
- **`models/sentiment_model.py`:** Handles model loading, quantization, and inference.

```
└── 📁 models
    └── 📄 sentiment_model.py
📄 app.py
📄 requirements.txt 
```

### Setup and Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   (Make sure you have a `requirements.txt` file with the necessary packages, or create one with: `pip freeze > requirements.txt`)

2. **Run the Flask API:**
   ```bash
   flask run 
   ```
   (Or `python app.py`, depending on your setup)

3. **Send requests to the API:**

   You can use tools like `curl` or `Postman` to send POST requests to the `/predict` endpoint.

   **Example using `curl`:**

   ```bash
   curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"text": "This is a great movie! I highly recommend it."}' \
     http://127.0.0.1:5000/predict
   ```

   **Example using Python's `requests` library:**

   ```python
   import requests

   api_url = 'http://127.0.0.1:5000/predict'
   text = "This is a great movie! I highly recommend it."
   data = {'text': text}

   response = requests.post(api_url, json=data)

   if response.status_code == 200:
     result = response.json()
     print(result)
   else:
     print(f"Request error: {response.status_code}")
   ```

   The API will respond with a JSON object containing:

   ```json
   {
     "text": "This is a great movie! I highly recommend it.",
     "sentiment": "POSITIVE",
     "score": 0.9998656630516052
   }
   ```

### Notes

- The API currently uses a pre-trained and quantized DistilBERT model. You can replace this with a different model by modifying the `model_name` and loading the appropriate model file in `models/sentiment_model.py`.
- This is a basic example, and you might need to adjust it based on your specific needs and deployment environment. Consider adding error handling, authentication, and other features for a more robust application.