import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Voice settings
    VOICE_RATE = 160
    VOICE_VOLUME = 0.9
    PREFERRED_VOICE = "indian_male"  # Options: 'indian_male', 'default_male', 'female'
    
    # Speech recognition
    LISTEN_TIMEOUT = 5
    PHRASE_LIMIT = 8
    
    # User information
    USER_NAME = os.getenv("USER_NAME", "Onkar")
    
    # AI Integration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    USE_GPT_FALLBACK = os.getenv("USE_GPT_FALLBACK", "false").lower() == "true"
    GPT_MODEL = "gpt-3.5-turbo-instruct"
    
    # Offline mode
    OFFLINE_MODE = os.getenv("OFFLINE_MODE", "false").lower() == "true"
    
    @staticmethod
    def configure_nltk():
        import nltk
        nltk.download('punkt', quiet=True)