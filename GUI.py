from tkinter import*
from PIL import Image,ImageTk
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1,padx=55,pady=10)

text_label = Label(frame, text="AI Assistance",font=("comic Sans ms", 14,"bold"),bg="#356696")
text_label.grid(row=0,column=0,padx=20,pady=10)

image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label = Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)


root.mainloop()