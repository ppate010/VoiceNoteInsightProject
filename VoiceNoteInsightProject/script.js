
document.getElementById('uploadButton').addEventListener('click', function() {
    var fileInput = document.getElementById('voiceNoteInput');
    if (fileInput.files.length > 0) {
        var formData = new FormData();
        formData.append('file', fileInput.files[0]);
        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('transcription').textContent = data.transcription;
            return fetch('/summarize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({text: data.transcription}),
            });
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('summary').textContent = data.summary;
            return fetch('/analyze_sentiment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({text: document.getElementById('transcription').textContent}),
            });
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('sentiment').textContent = `Sentiment: ${data.sentiment.label}, Confidence: ${data.sentiment.score}`;
        })
        .catch(error => console.error('Error:', error));
    }
});
