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

text = Text(root, font=('courier 10 bold'),bg="#356696")
text.grid(row=1, column=0)
text.place(x = 100, y = 375, width=375, height=100)

entry = Entry(root, justify = CENTER)
entry.place(x=100, y=500, width=350, height=30)

root.mainloop()