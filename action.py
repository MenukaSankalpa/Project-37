import text_to_speech
import speech_to_text
import datetime 
import webbrowser

def Action():
    user_data = speech_to_text.speech_to_text()
    
    if "your name" in user_data:
        text_to_speech.text_to_speech("my name is AI Desktop vertual assistant")
        return "my name is Ai Desktop vertual assistant"
    
Action()    