import re
from nltk.tokenize import word_tokenize

class NLPProcessor:
    @staticmethod
    def tokenize(text):
        return word_tokenize(text.lower())
    
    @staticmethod
    def contains_words(text, words):
        tokens = NLPProcessor.tokenize(text)
        return any(word in tokens for word in words)
    
    @staticmethod
    def get_intent(text):
        text = text.lower()
        
        # Greeting detection
        if any(word in text for word in ["hello", "hi", "hey", "greetings"]):
            return "greeting"
            
        # Name inquiry
        if any(phrase in text for phrase in ["your name", "who are you"]):
            return "name_inquiry"
            
        # Exit commands
        if any(word in text for word in ["exit", "quit", "goodbye"]):
            return "exit"
            
        # Time inquiry
        if "time" in text:
            return "time_inquiry"
            
        return "unknown"