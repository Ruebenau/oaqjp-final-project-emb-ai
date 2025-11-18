import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detecor(self):
        res1 = emotion_detector("I am glad this happened")["dominant emotion"]
        res2 = emotion_detector("I am really mad about this")["dominant emotion"]
        res3 = emotion_detector("I feel disgusted just hearing about this")["dominant emotion"]
        res4 = emotion_detector("I am so sad about this")["dominant emotion"]
        res5 = emotion_detector("I am really afraid that this will happen")["dominant emotion"]

        self.assertEqual(res1, 'joy')
        self.assertEqual(res2, 'anger')
        self.assertEqual(res3, 'disgust')
        self.assertEqual(res4, 'sadness')
        self.assertEqual(res5, 'fear')

unittest.main()