import sys
import os
from pathlib import Path
import time

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from assistant.core import SpeechEngine, Brain, Config
from assistant.utils.nlp_processor import NLPProcessor  # Fixed import

def main():
    # Initialize components
    Config.configure_nltk()
    speech_engine = SpeechEngine()
    brain = Brain()
    
    # Startup message
    speech_engine.speak(f"Hello {Config.USER_NAME}! GURU is now active and ready to assist you.")
    
    # Main interaction loop
    try:
        while True:
            # Listen for user input
            user_input = speech_engine.listen()
            
            if not user_input:
                time.sleep(1)
                continue
                
            print(f"User: {user_input}")
            
            # Get response
            response = brain.process(user_input)
            
            # Handle exit commands
            if NLPProcessor.get_intent(user_input) == "exit":  # Now correctly imported
                speech_engine.speak(response)
                break
                
            # Send response
            if response:
                speech_engine.speak(response)
                
    except KeyboardInterrupt:
        speech_engine.speak("System shutting down. Goodbye!")
    except Exception as e:
        print(f"Critical error: {e}")
        import traceback
        traceback.print_exc()
        speech_engine.speak("I've encountered a serious problem. Restarting may be necessary.")

if __name__ == "__main__":
    main()