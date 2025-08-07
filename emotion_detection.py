import requests
import json

def emotion_detector(text_to_analyse):
    # URL and Header for the model
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    print(formatted_response)

    #
    #anger = formatted_response['emotionPredictions']['anger']
    #anger_score = formatted_response['emotionPredictions']['anger_score']

    #disgust = formatted_response['emotionPredictions']['disgust']
    #disgust_score = formatted_response['emotionPredictions']['disgust_score']

    #fear = formatted_response['emotionPredictions']['fear']
    #fear_score = formatted_response['emotionPredictions']['fear_score']

    #joy = formatted_response['emotionPredictions']['joy']
    #joy_score = formatted_response['emotionPredictions']['joy_score']

    #sadness = formatted_response['emotionPredictions']['sadness']
    #sadness_score = formatted_response['emotionPredictions']['sadness_score']

    # Returning the dictionary    
    #return { }