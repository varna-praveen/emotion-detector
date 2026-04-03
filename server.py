from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("text")

    if text is None or text.strip() == "":
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
