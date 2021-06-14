import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Ithuba National Lottery of South Africa - Play')
root.geometry('400x550')
root.config(bg='yellow')
root.resizable(0, 0)
list1 = []
list2 = []
list3 = []


def tester2(num):
    if len(list1) < 6:
        list1.append(num)
        btnpress = Label(root, text=list1)
        btnpress.place(x=10, y=50)
    elif len(list1) == 6 and len(list2) < 6:
        list2.append(num)
        btnpress2 = Label(root, text=list2)
        btnpress2.place(x=10, y=100)
    elif len(list2) == 6 and len(list1) == 6 and len(list3) < 6:
        list3.append(num)
        btnpress3 = Label(root, text=list3)
        btnpress3.place(x=10, y=150)
    if len(list3) == 6:
        btn1.config(state=DISABLED)


btn1 = Button(root, text=1, command=lambda: tester2(1))
btn1.place(x=10, y=10)
btn2 = Button(root, text=2, command=lambda: tester2(2))
btn2.place(x=50, y=10)
btn3 = Button(root, text=3, command=lambda: tester2(3))
btn3.place(x=90, y=10)
btn4 = Button(root, text=4, command=lambda: tester2(4))
btn4.place(x=130, y=10)
btn5 = Button(root, text=5, command=lambda: tester2(5))
btn5.place(x=170, y=10)
btn6 = Button(root, text=6, command=lambda: tester2(6))
btn6.place(x=210, y=10)
btn7 = Button(root, text=7, command=lambda: tester2(7))
btn7.place(x=250, y=10)

root.mainloop()


# max sets is 5