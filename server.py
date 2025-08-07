"""
This module contains a Flask application for emotion detection.
"""
# Import necessary modules from Flask
from flask import Flask, render_template, request
# Import the emotion_detector function from the EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    """
    Analyzes the emotion of the text provided in the request and returns the result.
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Get the response from the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Handle the case where the input is invalid
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return the formatted response string
    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
