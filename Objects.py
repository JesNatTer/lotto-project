import tkinter as tk
from tkinter import *
from tkinter import messagebox
import datetime as dt
from tkinter.font import Font
import re
import random

root = tk.Tk()
root.title('Ithuba National Lottery of South Africa')
root.geometry('400x550')
root.config(bg='yellow')
root.resizable(0, 0)

date = dt.date.today()
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
score = 0
winningtotal = 0
font1 = Font(family='Helvetica', size=40)

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
        self.score = 0

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
                    text = open("playerlog.txt", '+w')
                    text.write("Player: " + self.nameEntry.get() + "\nEmail: " + self.emailEntry.get()
                               + "\nID: " + self.idEntry.get())
                    text.close()
                    messagebox.showinfo("You Qualify", "Enter the game!")
                    root.withdraw()
                    self.playscreen()

            except ValueError:
                messagebox.showerror("Invalid Input", "ID must be a number")
                self.idEntry.delete(0, END)

        self.theButton = Button(self.frame, text="Enter", command=confirmingdetails)
        self.theButton.place(x=130, y=130)

    def playscreen(self):
        playsc = Toplevel()
        playsc.title('Ithuba National Lottery of South Africa - Play')
        playsc.geometry('400x550')
        playsc.config(bg='yellow')
        playsc.resizable(0, 0)
        list1 = []
        list2 = []
        list3 = []
        font1 = Font(family='Helvetica', size=35)

        def play(num):
            if len(list1) == 5:
                playbtn.config(state=NORMAL)
            elif len(list1) < 5:
                playbtn.config(state=DISABLED)
            if len(list1) < 6 and num not in list1:
                list1.append(num)
                set1.config(text=list1)
            elif len(list1) == 6 and len(list2) < 6 and num not in list2:
                list2.append(num)
                set2.config(text=list2)
            elif len(list2) == 6 and len(list1) == 6 and len(list3) < 6 and num not in list3:
                list3.append(num)
                set3.config(text=list3)
            if len(list3) == 6:
                btn1.config(state=DISABLED)
                btn2.config(state=DISABLED)
                btn3.config(state=DISABLED)
                btn4.config(state=DISABLED)
                btn5.config(state=DISABLED)
                btn6.config(state=DISABLED)
                btn7.config(state=DISABLED)
                btn8.config(state=DISABLED)
                btn9.config(state=DISABLED)
                btn10.config(state=DISABLED)
                btn11.config(state=DISABLED)
                btn12.config(state=DISABLED)
                btn13.config(state=DISABLED)
                btn14.config(state=DISABLED)
                btn15.config(state=DISABLED)
                btn16.config(state=DISABLED)
                btn17.config(state=DISABLED)
                btn18.config(state=DISABLED)
                btn19.config(state=DISABLED)
                btn20.config(state=DISABLED)
                btn21.config(state=DISABLED)
                btn22.config(state=DISABLED)
                btn23.config(state=DISABLED)
                btn24.config(state=DISABLED)
                btn25.config(state=DISABLED)
                btn26.config(state=DISABLED)
                btn27.config(state=DISABLED)
                btn28.config(state=DISABLED)
                btn29.config(state=DISABLED)
                btn30.config(state=DISABLED)
                btn31.config(state=DISABLED)
                btn32.config(state=DISABLED)
                btn33.config(state=DISABLED)
                btn34.config(state=DISABLED)
                btn35.config(state=DISABLED)
                btn36.config(state=DISABLED)
                btn37.config(state=DISABLED)
                btn38.config(state=DISABLED)
                btn39.config(state=DISABLED)
                btn40.config(state=DISABLED)
                btn41.config(state=DISABLED)
                btn42.config(state=DISABLED)
                btn44.config(state=DISABLED)
                btn43.config(state=DISABLED)
                btn45.config(state=DISABLED)
                btn46.config(state=DISABLED)
                btn47.config(state=DISABLED)
                btn48.config(state=DISABLED)
                btn49.config(state=DISABLED)

        btn1 = Button(playsc, text=1, command=lambda: play(1))
        btn1.place(x=20, y=10)
        btn2 = Button(playsc, text=2, command=lambda: play(2))
        btn2.place(x=60, y=10)
        btn3 = Button(playsc, text=3, command=lambda: play(3))
        btn3.place(x=100, y=10)
        btn4 = Button(playsc, text=4, command=lambda: play(4))
        btn4.place(x=140, y=10)
        btn5 = Button(playsc, text=5, command=lambda: play(5))
        btn5.place(x=180, y=10)
        btn6 = Button(playsc, text=6, command=lambda: play(6))
        btn6.place(x=220, y=10)
        btn7 = Button(playsc, text=7, command=lambda: play(7))
        btn7.place(x=260, y=10)
        btn8 = Button(playsc, text=8, command=lambda: play(8))
        btn8.place(x=300, y=10)
        btn9 = Button(playsc, text=9, command=lambda: play(9))
        btn9.place(x=340, y=10)
        btn10 = Button(playsc, text=10, width=1, command=lambda: play(10))
        btn10.place(x=20, y=50)
        btn11 = Button(playsc, text=11, width=1, command=lambda: play(11))
        btn11.place(x=60, y=50)
        btn12 = Button(playsc, text=12, width=1, command=lambda: play(12))
        btn12.place(x=100, y=50)
        btn13 = Button(playsc, text=13, width=1, command=lambda: play(13))
        btn13.place(x=140, y=50)
        btn14 = Button(playsc, text=14, width=1, command=lambda: play(14))
        btn14.place(x=180, y=50)
        btn15 = Button(playsc, text=15, width=1, command=lambda: play(15))
        btn15.place(x=220, y=50)
        btn16 = Button(playsc, text=16, width=1, command=lambda: play(16))
        btn16.place(x=260, y=50)
        btn17 = Button(playsc, text=17, width=1, command=lambda: play(17))
        btn17.place(x=300, y=50)
        btn18 = Button(playsc, text=18, width=1, command=lambda: play(18))
        btn18.place(x=340, y=50)
        btn19 = Button(playsc, text=19, width=1, command=lambda: play(19))
        btn19.place(x=20, y=90)
        btn20 = Button(playsc, text=20, width=1, command=lambda: play(20))
        btn20.place(x=60, y=90)
        btn21 = Button(playsc, text=21, width=1, command=lambda: play(21))
        btn21.place(x=100, y=90)
        btn22 = Button(playsc, text=22, width=1, command=lambda: play(22))
        btn22.place(x=140, y=90)
        btn23 = Button(playsc, text=23, width=1, command=lambda: play(23))
        btn23.place(x=180, y=90)
        btn24 = Button(playsc, text=24, width=1, command=lambda: play(24))
        btn24.place(x=220, y=90)
        btn25 = Button(playsc, text=25, width=1, command=lambda: play(25))
        btn25.place(x=260, y=90)
        btn26 = Button(playsc, text=26, width=1, command=lambda: play(26))
        btn26.place(x=300, y=90)
        btn27 = Button(playsc, text=27, width=1, command=lambda: play(27))
        btn27.place(x=340, y=90)
        btn28 = Button(playsc, text=28, width=1, command=lambda: play(28))
        btn28.place(x=20, y=130)
        btn29 = Button(playsc, text=29, width=1, command=lambda: play(29))
        btn29.place(x=60, y=130)
        btn30 = Button(playsc, text=30, width=1, command=lambda: play(30))
        btn30.place(x=100, y=130)
        btn31 = Button(playsc, text=31, width=1, command=lambda: play(31))
        btn31.place(x=140, y=130)
        btn32 = Button(playsc, text=32, width=1, command=lambda: play(32))
        btn32.place(x=180, y=130)
        btn33 = Button(playsc, text=33, width=1, command=lambda: play(33))
        btn33.place(x=220, y=130)
        btn34 = Button(playsc, text=34, width=1, command=lambda: play(34))
        btn34.place(x=260, y=130)
        btn35 = Button(playsc, text=35, width=1, command=lambda: play(35))
        btn35.place(x=300, y=130)
        btn36 = Button(playsc, text=36, width=1, command=lambda: play(36))
        btn36.place(x=340, y=130)
        btn37 = Button(playsc, text=37, width=1, command=lambda: play(37))
        btn37.place(x=20, y=170)
        btn38 = Button(playsc, text=38, width=1, command=lambda: play(38))
        btn38.place(x=60, y=170)
        btn39 = Button(playsc, text=39, width=1, command=lambda: play(39))
        btn39.place(x=100, y=170)
        btn40 = Button(playsc, text=40, width=1, command=lambda: play(40))
        btn40.place(x=140, y=170)
        btn41 = Button(playsc, text=41, width=1, command=lambda: play(41))
        btn41.place(x=180, y=170)
        btn42 = Button(playsc, text=42, width=1, command=lambda: play(42))
        btn42.place(x=220, y=170)
        btn43 = Button(playsc, text=43, width=1, command=lambda: play(43))
        btn43.place(x=260, y=170)
        btn44 = Button(playsc, text=44, width=1, command=lambda: play(44))
        btn44.place(x=300, y=170)
        btn45 = Button(playsc, text=45, width=1, command=lambda: play(45))
        btn45.place(x=340, y=170)
        btn46 = Button(playsc, text=46, width=1, command=lambda: play(46))
        btn46.place(x=20, y=210)
        btn47 = Button(playsc, text=47, width=1, command=lambda: play(47))
        btn47.place(x=60, y=210)
        btn48 = Button(playsc, text=48, width=1, command=lambda: play(48))
        btn48.place(x=100, y=210)
        btn49 = Button(playsc, text=49, width=1, command=lambda: play(49))
        btn49.place(x=140, y=210)
        total = Label(playsc, text="")
        total.place(x=10, y=530)

        set1 = Label(playsc, text='', font=font1, bg='yellow', width=15, justify='center')
        set1.place(x=0, y=260)
        set2 = Label(playsc, text='', font=font1, bg='yellow', width=15, justify='center')
        set2.place(x=0, y=310)
        set3 = Label(playsc, text='', font=font1, bg='yellow', width=15, justify='center')
        set3.place(x=0, y=360)

        def lotto():
            lottonums = random.sample(range(1, 49), 6)
            matches = [2.00, 100.00, 20.00, 100.50, 2384.00, 8584.00, 10000000.00]
            matches1 = 0
            matches2 = 0
            matches3 = 0
            played = 0
            played2 = 0
            played3 = 0
            global winningtotal
            global score
            matchset = []
            matchset2 = []
            matchset3 = []
            for x in range(0, 6):
                if len(list1) == 6:
                    played = 1
                    if list1[x] == lottonums[x]:
                        matches1 += 1
                        matchset.append(list1[x])
                if len(list2) == 6:
                    played2 = 1
                    if list2[x] == lottonums[x]:
                        matches2 += 1
                        matchset2.append(list2[x])
                if len(list3) == 6:
                    played3 = 1
                    if list3[x] == lottonums[x]:
                        matches3 += 1
                        matchset3.append(list3[x])
            if played == 1 and played2 == 0 and played3 == 0:
                winningtotal = matches[matches1]
                score = score + winningtotal
                if matches1 < 2:
                    messagebox.showinfo('Results', str(lottonums) + '\n' + 'Your matches are: ' + str(
                        matches1) + '\n'
                                        + 'You won: ' + str(winningtotal))
                else:
                    messagebox.showinfo('Congratulations',
                                        str(lottonums) + '\n' + 'Your matches are: ' + str(matches1)
                                        + '\n' + 'You won: ' + str(winningtotal))
                playbtn.config(state=DISABLED)
            elif played == 1 and played2 == 1 and played3 == 0:
                winningtotal = matches[matches1] + matches[matches2]
                score = score + winningtotal
                if winningtotal == 0:
                    messagebox.showinfo('Results',
                                        str(lottonums) + '\n' + "Your first set's matches are: " + str(
                                            matches1)
                                        + '\n' + "Your second set's matches are : " + str(
                                            matches2) + '\n' + 'You won: '
                                        + str(winningtotal))
                else:
                    messagebox.showinfo('Congratulations',
                                        str(lottonums) + '\n' + "Your first set's matches are: "
                                        + str(
                                            matches1) + '\n' + "Your second set's matches are : " + str(
                                            matches2) + '\n'
                                        + 'You won: ' + str(winningtotal))
            elif played == 1 and played2 == 1 and played3 == 1:
                winningtotal = matches[matches1] + matches[matches2] + matches[matches3]
                score = score + winningtotal
                if winningtotal == 0:
                    messagebox.showinfo('Results',
                                        str(lottonums) + '\n' + "Your first set's matches are: "
                                        + str(
                                            matches1) + '\n' + "Your second set's matches are : " + str(
                                            matches2) + '\n'
                                        + "Your third set's matches are: " + str(
                                            matches3) + '\n' + 'You won: '
                                        + str(winningtotal))
                else:
                    messagebox.showinfo('Congratulations',
                                        str(lottonums) + '\n' + "Your first set's matches are: "
                                        + str(
                                            matches1) + '\n' + "Your second set's matches are : " + str(
                                            matches2) + '\n'
                                        + "Your third set's matches are: " + str(
                                            matches3) + '\n' + 'You won: '
                                        + str(winningtotal))

            total.config(text="R" + str(score))
            playbtn.config(state=DISABLED)

            def retry():
                list1.clear()
                list2.clear()
                list3.clear()
                set1.config(text='')
                set2.config(text='')
                set3.config(text='')
                playbtn.config(state=NORMAL)
                btn1.config(state=NORMAL)
                btn2.config(state=NORMAL)
                btn3.config(state=NORMAL)
                btn4.config(state=NORMAL)
                btn5.config(state=NORMAL)
                btn6.config(state=NORMAL)
                btn7.config(state=NORMAL)
                btn8.config(state=NORMAL)
                btn9.config(state=NORMAL)
                btn10.config(state=NORMAL)
                btn11.config(state=NORMAL)
                btn12.config(state=NORMAL)
                btn13.config(state=NORMAL)
                btn14.config(state=NORMAL)
                btn15.config(state=NORMAL)
                btn16.config(state=NORMAL)
                btn17.config(state=NORMAL)
                btn18.config(state=NORMAL)
                btn19.config(state=NORMAL)
                btn20.config(state=NORMAL)
                btn21.config(state=NORMAL)
                btn22.config(state=NORMAL)
                btn23.config(state=NORMAL)
                btn24.config(state=NORMAL)
                btn25.config(state=NORMAL)
                btn26.config(state=NORMAL)
                btn27.config(state=NORMAL)
                btn28.config(state=NORMAL)
                btn29.config(state=NORMAL)
                btn30.config(state=NORMAL)
                btn31.config(state=NORMAL)
                btn32.config(state=NORMAL)
                btn33.config(state=NORMAL)
                btn34.config(state=NORMAL)
                btn35.config(state=NORMAL)
                btn36.config(state=NORMAL)
                btn37.config(state=NORMAL)
                btn38.config(state=NORMAL)
                btn39.config(state=NORMAL)
                btn40.config(state=NORMAL)
                btn41.config(state=NORMAL)
                btn42.config(state=NORMAL)
                btn44.config(state=NORMAL)
                btn43.config(state=NORMAL)
                btn45.config(state=NORMAL)
                btn46.config(state=NORMAL)
                btn47.config(state=NORMAL)
                btn48.config(state=NORMAL)
                btn49.config(state=NORMAL)

            playagainbtn = Button(playsc, text='Play again', command=retry)
            playagainbtn.place(x=170, y=500)

            def claimprize():
                playsc.withdraw()
                self.claimscreen()

            claimbtn = Button(playsc, text="Claim now", command=claimprize)
            claimbtn.place(x=50, y=500)

        playbtn = Button(playsc, text='Play', state=DISABLED, command=lotto)
        playbtn.place(x=170, y=450)

        playsc.mainloop()

    def claimscreen(self):
        claimsc = Toplevel()
        claimsc.geometry('450x450')
        font = Font(family='Helvetica', size=30)
        value_inside = StringVar(claimsc)

        value_inside.set("Select Bank")
        bankoptions = ['ABSA', 'Capitec', 'FNB', 'Nedbank']

        class InvalidAccountName:
            pass

        title = Label(claimsc, text='Claim your prize!', font=font)
        title.place(x=12, y=20)

        def bank(value_inside):
            if value_inside == 'Select Bank':
                pass
            else:
                accountNameEntry.config(state='normal')
                bankNrEntry.config(state='normal')

        bankselect = OptionMenu(claimsc, value_inside, *bankoptions, command=bank)
        bankselect.place(x=30, y=100)
        accountNameLabel = Label(claimsc, text="Account name")
        accountNameLabel.place(x=30, y=150)
        accountNameEntry = Entry(claimsc, state='readonly')
        accountNameEntry.place(x=150, y=150)
        bankNrLabel = Label(claimsc, text="Account Number")
        bankNrLabel.place(x=30, y=200)
        bankNrEntry = Entry(claimsc, state='readonly')
        bankNrEntry.place(x=150, y=200)

        def claim():
            if accountNameEntry.get() == '' or bankNrEntry.get() == '':
                messagebox.showerror("Fields unfilled", "Please enter both account name and bank account number")
            else:
                try:
                    banknr = int(bankNrEntry.get())
                    if str.isalpha(accountNameEntry.get()) is False:
                        raise InvalidAccountName
                    else:
                        messagebox.showinfo("test", score)
                except ValueError:
                    messagebox.showerror("Invalid Bank Number", "Please enter valid bank number (digits only)")
                except InvalidAccountName:
                    messagebox.showerror("Invalid Account Name", "Please enter valid account name (characters only")

        claimBtn = Button(claimsc, text="Claim", command=claim)
        claimBtn.place(x=200, y=270)

        claimsc.mainloop()


page = Login(root)

root.mainloop()