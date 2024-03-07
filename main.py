"""
Authour : Soudabeh Tabarsaii
"""
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

# Load model and tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    return model.config.id2label[predicted_class_id]

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        text = data['text']
        sentiment = predict_sentiment(text)
        return jsonify(sentiment=sentiment)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
