from tkinter import *
from PIL import Image, ImageTk
from deep_translator import GoogleTranslator



# Tạo tkinter window
root = Tk()
root.title('My Simple Google Translate')
root.geometry('1000x800')
root.iconbitmap(r'F:\.Self-studying\translate-app\img+font\logo.ico')


load = Image.open(r'F:\.Self-studying\translate-app\img+font\background.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image= render)
img.place(x=0, y=0)

name = Label(root, text = " Vietnamese Translator", fg = "#FFFFFF", bd = 0, bg ="#03152D" )
name.config(font=("Transformers Movie", 30))
name.pack(pady = 10) #padding y

box = Text(root, width=28, height=8, font=("Consolas",16))
box.pack(pady=20)

button_frame = Frame(root).pack(side = BOTTOM)

def clear():
    pass
def translate():
    pass

clear_button = Button(button_frame, text="Clear Text", font=("Consolas", 10, 'bold'), bg = '#303030', fg = "#FFFFFF")
clear_button.place(x=310, y=310)
trans_button = Button(button_frame, text="Translate", font=("Consolas", 10, 'bold'), bg = '#303030', fg = "#FFFFFF")
trans_button.place(x=620, y=310)



root.mainloop()