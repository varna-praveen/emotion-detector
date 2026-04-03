import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_sadness(self):
        result = emotion_detector("I am sad")
        self.assertIn('sadness', result)

    def test_anger(self):
        result = emotion_detector("I am angry")
        self.assertIn('anger', result)

if __name__ == "__main__":
    unittest.main()
