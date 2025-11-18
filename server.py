"""
This is the main server module for my Flask application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/")
def starting_page():
    """
    This function renders the landing page of my application.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def call_emotion_detector():
    """
    This function calls the emotion detector.
    """
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)

    if result["dominant emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant emotion"]

    return f"""For the given statement, the system response is
    \'anger\': {anger}, 
    \'disgust\': {disgust}, 
    \'fear\': {fear}, 
    \'joy\': {joy} and 
    \'sadness\': {sadness}. 
    The dominant emotion is {dominant_emotion}"""
