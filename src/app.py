from flask import Flask, request, jsonify
from models.sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to receive text and return sentiment analysis.
    """
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text')

        if text is None:
            return jsonify({'error': 'Missing "text" field in request'}), 400

        sentiment = analyze_sentiment(text)

        return jsonify({
            'text': text,
            'sentiment': sentiment['label'],
            'score': sentiment['score']
        })

if __name__ == '__main__':
    app.run(debug=True)