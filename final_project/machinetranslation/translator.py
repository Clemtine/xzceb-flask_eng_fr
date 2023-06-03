"""
This Module translate word
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This fonction transalate english to french
    """
    french_text = MyMemoryTranslator(source="en", target="fr").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This fonction translate french worl in English
    """
    english_text = MyMemoryTranslator(source="fr", target="en").translate(french_text)
    return english_text
