
from flask import Flask, request, jsonify
from transformers import pipeline
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import os

app = Flask(__name__)

# Assuming GOOGLE_APPLICATION_CREDENTIALS environment variable is set
client = speech.SpeechClient()

summarizer = pipeline("summarization")
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/upload', methods=['POST'])
def upload_voice_note():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        content = file.read()
        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US'
        )
        response = client.recognize(config=config, audio=audio)
        transcription = ''
        for result in response.results:
            transcription += result.alternatives[0].transcript
        return jsonify(transcription=transcription)

@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.json.get('text', '')
    if not text:
        return jsonify({"error": "No text provided for summarization"}), 400
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return jsonify(summary=summary[0]['summary_text'])

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    text = request.json.get('text', '')
    if not text:
        return jsonify({"error": "No text provided for sentiment analysis"}), 400
    sentiment = sentiment_analyzer(text)
    return jsonify(sentiment=sentiment[0])

if __name__ == '__main__':
    app.run(debug=True)
