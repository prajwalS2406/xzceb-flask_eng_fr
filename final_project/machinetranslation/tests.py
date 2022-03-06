import unittest

from translator import english_to_french, french_to_english




class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(""), "API Exception") # test null
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test positive
        self.assertNotEqual(english_to_french("Hello"), "Hello")  # test negative


class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(""), "API Exception") # test null
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test positive
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour") # test negative

unittest.main()