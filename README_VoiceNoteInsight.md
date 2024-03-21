
# VoiceNote Insight

VoiceNote Insight is an AI-powered tool designed to enhance productivity and accessibility by automatically transcribing, summarizing, and analyzing the sentiment of voice recordings. This project utilizes Python for the backend and a simple HTML/CSS/JavaScript frontend for interaction.

## Features

- **Automatic Transcription**: Convert voice recordings into text.
- **Content Summarization**: Generate concise summaries of the transcriptions.
- **Sentiment Analysis**: Analyze the sentiment of the voice notes (positive, negative, neutral).
- **Categorization**: Automatically categorize voice notes based on keywords and topics (Future enhancement).

## Setup and Installation

### Backend

1. Ensure Python 3.8+ is installed on your system.
2. Install required Python libraries:
    ```bash
    pip install Flask google-cloud-speech transformers torch
    ```
3. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to your Google Cloud credentials JSON file.
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials-file.json"
    ```
4. Run the Flask app:
    ```bash
    python app.py
    ```

### Frontend

Open the `index.html` file in a web browser to use the application.

## Usage

1. Use the web interface to upload a voice note.
2. The application will automatically transcribe, summarize, and analyze the sentiment of the uploaded voice note.
3. View the results on the web interface.

## Technologies Used

- Python Flask for the backend API.
- Google Cloud Speech-to-Text API for transcription.
- Hugging Face's Transformers library for NLP tasks.
- HTML/CSS/JavaScript for the frontend.

## Future Enhancements

- Implement categorization based on keywords and topics using NLP.
- Enhance the frontend with React or another modern framework for a richer user experience.
- Integrate with other productivity tools for seamless workflow automation.

## License

This project is open-source and available under the MIT License.
