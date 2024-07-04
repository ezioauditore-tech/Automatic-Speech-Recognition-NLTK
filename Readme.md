# Speech Recognition with NLTK and Streamlit

This project is a simple speech recognition application using Streamlit and the `speech_recognition` library. It allows you to record audio from your microphone, convert it to text, and display the recognized text in a web interface.

## Requirements

- `Python 3.x`
- `streamlit`
- `SpeechRecognition`
- `nltk`

## Installation

1. Clone the repository or download the source code.

2. Install the required packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. Download necessary NLTK data:
    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open the provided local URL in your web browser.

3. Click the "Start Recording" button to begin recording audio. Speak into your microphone, and the recognized text will be displayed on the page.

## Project Structure

- `speech.py`: Contains the function for recording and recognizing speech.
- `app.py`: Contains the Streamlit application code that uses the function from `speech.py`.
- `requirements.txt`: Lists the required Python packages.