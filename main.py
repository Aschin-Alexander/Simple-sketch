from tkinter import *
from tkinter import colorchooser

window = Tk()
button = Button(text='pencil', command=lambda: colorchooser.askcolor())
button.pack(side=BOTTOM)
#button.bind('<ListboxSelect>')

#colorchooser.askcolor()
print("Hello world!")

window.title('Hello Python')
window.geometry("500x400+10+20")
window.mainloop()
# 12312123123