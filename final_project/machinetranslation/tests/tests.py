import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("I'm happy"), "Je suis heureux")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("je suis heureux"), "I'm happy")

if __name__ == "__main__":
    unittest.main()