def emotion_detector(text_to_analyse):
    if text_to_analyse is None or text_to_analyse.strip() == "":
        return {
            "error": "Invalid text! Please try again!",
            "status": 400
        }

    emotions = {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.90,
        "sadness": 0.04
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
    emotions = {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.90,
        "sadness": 0.04
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
