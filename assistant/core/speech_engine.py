import speech_recognition as sr
import pyttsx3
import time
from assistant.core.config import Config
from assistant.utils.internet_checker import InternetChecker

class SpeechEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.engine = self._init_tts_engine()
        
        # Adjust for ambient noise
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
    
    def _init_tts_engine(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', Config.VOICE_RATE)
        engine.setProperty('volume', Config.VOICE_VOLUME)
        
        # Voice selection logic
        voices = engine.getProperty('voices')
        voice_found = False
        
        if Config.PREFERRED_VOICE == "indian_male":
            for voice in voices:
                if 'india' in voice.id.lower() and 'male' in voice.id.lower():
                    engine.setProperty('voice', voice.id)
                    voice_found = True
                    break
        
        if not voice_found:
            for voice in voices:
                if 'male' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
        
        return engine
    
    def listen(self):
        """Capture audio with offline fallback"""
        try:
            with self.mic as source:
                print("\nListening... (Speak now)")
                audio = self.recognizer.listen(
                    source, 
                    timeout=Config.LISTEN_TIMEOUT,
                    phrase_time_limit=Config.PHRASE_LIMIT
                )
            
            if Config.OFFLINE_MODE or not InternetChecker.is_connected():
                print("Using offline recognition...")
                return self.recognizer.recognize_sphinx(audio).lower()
            
            try:
                return self.recognizer.recognize_google(audio).lower()
            except sr.UnknownValueError:
                print("Online recognition failed, trying offline...")
                return self.recognizer.recognize_sphinx(audio).lower()
                
        except sr.WaitTimeoutError:
            print("Listening timed out")
            return ""
        except Exception as e:
            print(f"Recognition error: {e}")
            return ""
    
    def speak(self, text):
        print(f"GURU: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def test_voice(self):
        """Test different voice outputs"""
        self.speak("Hello! This is a voice test.")
        self.speak("My name is GURU, your AI assistant.")
        self.speak("I'm here to help you with your tasks.")