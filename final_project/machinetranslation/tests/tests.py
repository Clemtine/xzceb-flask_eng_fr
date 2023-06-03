
import unittest
from translator import english_to_french, french_to_english

class eng_to_fr(unittest.TestCase):
	def test1(self):
            self.assertEqual(english_to_french("hello"), "bonjour")

class fr_to_en(unittest.TestCase):
	def test1(self):
            self.assertEqual(french_to_english("bonjour"), "hello")

unittest.main()