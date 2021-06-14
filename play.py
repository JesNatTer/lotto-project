import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Ithuba National Lottery of South Africa - Play')
root.geometry('400x550')
root.config(bg='yellow')
root.resizable(0, 0)


def tester2():
    value = buttonlist
    btnpress = Label(root, text=value)
    btnpress.place(x=10, y=40)


btn1 = Button(root, text=1, command=tester2)
btn1.place(x=10, y=10)
btn2 = Button(root, text=2, command=tester2)
btn2.place(x=50, y=10)
btn3 = Button(root, text=3, command=tester2)
btn3.place(x=90, y=10)
btn4 = Button(root, text=4, command=tester2)
btn4.place(x=130, y=10)
btn5 = Button(root, text=5, command=tester2)
btn5.place(x=170, y=10)
btn6 = Button(root, text=6, command=tester2)
btn6.place(x=210, y=10)
btn7 = Button(root, text=7, command=tester2)
btn7.place(x=250, y=10)
buttonlist = {1: btn1, 2: btn2, 3: btn3, 4: btn4, 5: btn5, 6: btn6, 7: btn7}

root.mainloop()


# max sets is 5