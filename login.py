import tkinter as tk
from tkinter import *
from tkinter import messagebox
import datetime as dt
import re

root = tk.Tk()
root.title('Ithuba National Lottery of South Africa')
root.geometry('400x550')
root.config(bg='yellow')
root.resizable(0, 0)

date = dt.date.today()
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


class Login:
    def __init__(self, master):
        self.frame = Frame(master, bg='red', width=350, height=300)
        self.frame.place(x=25, y=200)

        self.details = Label(self.frame, text="Enter your details", bg='red')
        self.details.place(x=120, y=10)

        self.nameLabel = Label(self.frame, text="Name", bg='red')
        self.nameLabel.place(x=30, y=30)
        self.nameEntry = Entry(self.frame)
        self.nameEntry.place(x=100, y=30)

        self.emailLabel = Label(self.frame, text="Email", bg='red')
        self.emailLabel.place(x=30, y=60)
        self.emailEntry = Entry(self.frame)
        self.emailEntry.place(x=100, y=60)

        self.idLabel = Label(self.frame, text='ID', bg='red')
        self.idLabel.place(x=30, y=90)
        self.idEntry = Entry(self.frame)
        self.idEntry.place(x=100, y=90)

        def confirmingdetails():
            try:
                idcheck = int(self.idEntry.get())
                global ageval
                global emval
                ageval = 0
                emval = 0

                def idchecker():
                    idno = self.idEntry.get()
                    if 00 <= int(idno[0:2]) <= 21:
                        year = 2000 + int(idno[0:2])
                    else:
                        year = 1900 + int(idno[0:2])

                    yd = int(date.year) - year
                    md = int(date.month) - int(idno[2:4])
                    day = int(idno[4:6])

                    if len(idno) < 13 or len(idno) > 13:
                        messagebox.showerror('Invalid ID', 'ID must be 13 digits long')
                    elif int(self.idEntry.get()[2:4]) > 12:
                        messagebox.showerror("Invalid ID", "ID is invalid")
                    elif int(self.idEntry.get()[4:6]) > 31:
                        messagebox.showerror("Invalid ID", "ID is invalid")
                    elif self.idEntry.get()[2:4] == '02' and int(self.idEntry.get()[4:6]) > 29:
                        messagebox.showerror("Invalid ID", "ID is invalid")
                    else:
                        if yd > 18 or (yd == 18 and md == 0 and day < int(date.day)) or (yd == 18 and md > 0):
                            return 1
                        else:
                            messagebox.showerror("Do not meet age requirement", "You are too young to play the lotto.")
                            root.destroy()

                def emailchecker():
                    if re.search(regex, self.emailEntry.get()):
                        return 1
                    else:
                        messagebox.showerror("Invalid Email", "Please enter a valid email address")

                if idchecker() == 1 and emailchecker() == 1:
                    messagebox.showinfo("You Qualify", "Enter the game!")
                    root.destroy()
                    import play

            except ValueError:
                messagebox.showerror("Invalid Input", "ID must be a number")
                self.idEntry.delete(0, END)

        self.theButton = Button(self.frame, text="Enter", command=confirmingdetails)
        self.theButton.place(x=130, y=130)


page = Login(root)

root.mainloop()
