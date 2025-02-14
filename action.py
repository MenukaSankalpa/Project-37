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
        return "ok sir"
    
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com lis now ready for you")
        return "gaana.com is now ready for you" 
    
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"
    
    elif "open google" in user_data:
        webbrowser.open("https://google.com")
        text_to_speech.text_to_speech("google.com is now ready for you")
        
    else:
        text_to_speech.text_to_speech("I am not able to undestant")
        return "I am not able to undestant"
    
Action()    