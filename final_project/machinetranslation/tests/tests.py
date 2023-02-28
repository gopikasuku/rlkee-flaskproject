import unittest
from translator import french_to_english,english_to_french # pylint: disable=import-error

class TestFrenchTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french('Hi'),'Bonjour')
    
class TestEnglishTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""),"")
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),'Hi')
unittest.main()