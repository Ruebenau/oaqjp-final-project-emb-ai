import requests
import json

def emotion_detector(text_to_analyse):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict';
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"};
    input = { "raw_document": { "text": text_to_analyse }};
    response = json.loads(requests.post(url, json=input, headers=header).text);

    emotion_scores = response["emotionPredictions"][0]["emotion"]

    anger = emotion_scores["anger"]
    disgust = emotion_scores["disgust"]
    fear = emotion_scores["fear"]
    joy = emotion_scores["joy"]
    sadness = emotion_scores["sadness"]
    dominant_emotion_score = max(anger, disgust, fear, joy, sadness)
    dominant_emotion = ""

    score_list = [anger, disgust, fear, joy, sadness]
    emotion_list = ['anger', 'disgust', 'fear', 'joy', 'sadness']

    for i, e in enumerate(score_list):
        if(e == dominant_emotion_score):
            dominant_emotion = emotion_list[i]

    response_dict = {   
                        "anger": anger, 
                        "disgust": disgust, 
                        "fear": fear, 
                        "joy": joy, 
                        "sadness": sadness, 
                        "dominant emotion": dominant_emotion
                    }

    return response_dict