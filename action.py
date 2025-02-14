import text_to_speech
import speech_to_text
import datetime 
import webbrowser

def Action():
    user_data = speech_to_text.speech_to_text()
    
    if "your name" in user_data:
        text_to_speech.text_to_speech("my name is AI Desktop virtual assistant")
        return "my name is Ai Desktop virtual assistant"
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("hey, sir how can i help you")
        return 'hey, sir how can i help you'
    elif "Good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
    elif "what is the time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour) + "Hour :",(str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
    
Action()    