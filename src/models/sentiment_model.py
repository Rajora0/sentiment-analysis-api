import torch
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification


# Load the model and tokenizer only once
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Quantize the model
quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

classifier = pipeline('sentiment-analysis', model=quantized_model, tokenizer=tokenizer)

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the text using the loaded model.
    """
    sentiment = classifier(text)[0]
    return {'label': sentiment['label'], 'score': sentiment['score']}