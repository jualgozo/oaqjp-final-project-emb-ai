import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of a given text using the Watson NLP API.

    Args:
        text_to_analyse (str): The text to be analyzed.

    Returns:
        dict: A dictionary containing the scores for each emotion (anger, disgust, fear, joy, sadness)
              and the dominant emotion. Returns a dictionary with None values if the input is invalid
              or if there is an error in the API response.
    """
    # Return None values if the input text is blank or empty
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # URL and headers for the Watson NLP API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Payload for the API request
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Send a POST request to the API
    response = requests.post(url, json = myobj, headers=header)
    
    # Handle error response from the API (e.g., bad request)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the dictionary with emotion scores and the dominant emotion
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }