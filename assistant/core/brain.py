from assistant.core.config import Config
from assistant.utils.nlp_processor import NLPProcessor
import datetime
import random

class Brain:
    def __init__(self):
        self.user_name = Config.USER_NAME
        self.responses = {
            "greeting": [
                f"Hello {self.user_name}, how can I help you today?",
                f"Hi {self.user_name}! What can I do for you?",
                f"Good day {self.user_name}! How may I assist you?"
            ],
            "name_inquiry": [
                "My name is GURU, your personal AI assistant",
                "I'm GURU, your digital companion",
                "You can call me GURU, your AI helper"
            ],
            "time_inquiry": self.get_current_time,
            "exit": [
                f"Goodbye {self.user_name}! Have a wonderful day.",
                f"See you later {self.user_name}!",
                f"Farewell {self.user_name}! Come back anytime."
            ],
            "default": [
                "I'm still learning about that. Could you rephrase?",
                "I'm not sure I understand. Can you try asking differently?",
                "I need more training on that topic. Please ask something else."
            ]
        }
        
    def process(self, text):
        intent = NLPProcessor.get_intent(text)
        
        if intent == "time_inquiry":
            return self.responses[intent]()
        
        if intent in self.responses:
            if isinstance(self.responses[intent], list):
                return random.choice(self.responses[intent])
            return self.responses[intent]
        
        # GPT fallback if enabled and internet available
        if Config.USE_GPT_FALLBACK:
            gpt_response = self.gpt_fallback(text)
            if gpt_response:
                return gpt_response
        
        return random.choice(self.responses["default"])
    
    def get_current_time(self):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"
    
    def gpt_fallback(self, text):
        """Use GPT for complex queries (requires internet and API key)"""
        if not Config.OPENAI_API_KEY:
            return None
            
        try:
            import openai
            openai.api_key = Config.OPENAI_API_KEY
            
            response = openai.Completion.create(
                engine=Config.GPT_MODEL,
                prompt=f"User: {text}\nGURU:",
                max_tokens=100,
                temperature=0.7,
                stop=["\n"]
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"GPT Error: {e}")
            return None