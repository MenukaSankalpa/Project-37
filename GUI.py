from tkinter import*
from PIL import Image,ImageTk
import speech_to_text
import action



root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

def ask():
    #print("Hello")
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->'+user_val+"\n")
    
    if bot_val != None:
        text.insert(END, "BOT<---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()     
    
    
def del_text():
    print("Delete Text")    

def send():
    print("Send")
    
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1,padx=55,pady=10)

text_label = Label(frame, text="AI Assistance",font=("comic Sans ms", 14,"bold"),bg="#356696")
text_label.grid(row=0,column=0,padx=20,pady=10)

image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label = Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

text = Text(root, font=('courier 10 bold'),bg="#356696")
text.grid(row=1, column=0)
text.place(x = 100, y = 375, width=375, height=100)

entry = Entry(root, justify = CENTER)
entry.place(x=100, y=500, width=350, height=30)

Button1 = Button(root,text = "ASK", bg = "#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

Button2 = Button(root,text = "DELETE", bg = "#356696", pady=16,padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button2.place(x=225, y=575)

Button3 = Button(root,text = "SEND", bg = "#356696", pady=16,padx=40, borderwidth=3, relief=SOLID, command=send)
Button3.place(x=400, y=575)

root.mainloop()