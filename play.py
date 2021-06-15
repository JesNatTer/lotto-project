import tkinter as tk
from tkinter import *
import tkinter.font as tfont
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Ithuba National Lottery of South Africa - Play')
root.geometry('400x550')
root.config(bg='yellow')
root.resizable(0, 0)
list1 = []
list2 = []
list3 = []
font1 = tfont.Font(family='Helvetica', size=35)
score = 0
winningtotal = 0


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


btn1 = Button(root, text=1, command=lambda: play(1))
btn1.place(x=20, y=10)
btn2 = Button(root, text=2, command=lambda: play(2))
btn2.place(x=60, y=10)
btn3 = Button(root, text=3, command=lambda: play(3))
btn3.place(x=100, y=10)
btn4 = Button(root, text=4, command=lambda: play(4))
btn4.place(x=140, y=10)
btn5 = Button(root, text=5, command=lambda: play(5))
btn5.place(x=180, y=10)
btn6 = Button(root, text=6, command=lambda: play(6))
btn6.place(x=220, y=10)
btn7 = Button(root, text=7, command=lambda: play(7))
btn7.place(x=260, y=10)
btn8 = Button(root, text=8, command=lambda: play(8))
btn8.place(x=300, y=10)
btn9 = Button(root, text=9, command=lambda: play(9))
btn9.place(x=340, y=10)
btn10 = Button(root, text=10, width=1, command=lambda: play(10))
btn10.place(x=20, y=50)
btn11 = Button(root, text=11, width=1, command=lambda: play(11))
btn11.place(x=60, y=50)
btn12 = Button(root, text=12, width=1, command=lambda: play(12))
btn12.place(x=100, y=50)
btn13 = Button(root, text=13, width=1, command=lambda: play(13))
btn13.place(x=140, y=50)
btn14 = Button(root, text=14, width=1, command=lambda: play(14))
btn14.place(x=180, y=50)
btn15 = Button(root, text=15, width=1, command=lambda: play(15))
btn15.place(x=220, y=50)
btn16 = Button(root, text=16, width=1, command=lambda: play(16))
btn16.place(x=260, y=50)
btn17 = Button(root, text=17, width=1, command=lambda: play(17))
btn17.place(x=300, y=50)
btn18 = Button(root, text=18, width=1, command=lambda: play(18))
btn18.place(x=340, y=50)
btn19 = Button(root, text=19, width=1, command=lambda: play(19))
btn19.place(x=20, y=90)
btn20 = Button(root, text=20, width=1, command=lambda: play(20))
btn20.place(x=60, y=90)
btn21 = Button(root, text=21, width=1, command=lambda: play(21))
btn21.place(x=100, y=90)
btn22 = Button(root, text=22, width=1, command=lambda: play(22))
btn22.place(x=140, y=90)
btn23 = Button(root, text=23, width=1, command=lambda: play(23))
btn23.place(x=180, y=90)
btn24 = Button(root, text=24, width=1, command=lambda: play(24))
btn24.place(x=220, y=90)
btn25 = Button(root, text=25, width=1, command=lambda: play(25))
btn25.place(x=260, y=90)
btn26 = Button(root, text=26, width=1, command=lambda: play(26))
btn26.place(x=300, y=90)
btn27 = Button(root, text=27, width=1, command=lambda: play(27))
btn27.place(x=340, y=90)
btn28 = Button(root, text=28, width=1, command=lambda: play(28))
btn28.place(x=20, y=130)
btn29 = Button(root, text=29, width=1, command=lambda: play(29))
btn29.place(x=60, y=130)
btn30 = Button(root, text=30, width=1, command=lambda: play(30))
btn30.place(x=100, y=130)
btn31 = Button(root, text=31, width=1, command=lambda: play(31))
btn31.place(x=140, y=130)
btn32 = Button(root, text=32, width=1, command=lambda: play(32))
btn32.place(x=180, y=130)
btn33 = Button(root, text=33, width=1, command=lambda: play(33))
btn33.place(x=220, y=130)
btn34 = Button(root, text=34, width=1, command=lambda: play(34))
btn34.place(x=260, y=130)
btn35 = Button(root, text=35, width=1, command=lambda: play(35))
btn35.place(x=300, y=130)
btn36 = Button(root, text=36, width=1, command=lambda: play(36))
btn36.place(x=340, y=130)
btn37 = Button(root, text=37, width=1, command=lambda: play(37))
btn37.place(x=20, y=170)
btn38 = Button(root, text=38, width=1, command=lambda: play(38))
btn38.place(x=60, y=170)
btn39 = Button(root, text=39, width=1, command=lambda: play(39))
btn39.place(x=100, y=170)
btn40 = Button(root, text=40, width=1, command=lambda: play(40))
btn40.place(x=140, y=170)
btn41 = Button(root, text=41, width=1, command=lambda: play(41))
btn41.place(x=180, y=170)
btn42 = Button(root, text=42, width=1, command=lambda: play(42))
btn42.place(x=220, y=170)
btn43 = Button(root, text=43, width=1, command=lambda: play(43))
btn43.place(x=260, y=170)
btn44 = Button(root, text=44, width=1, command=lambda: play(44))
btn44.place(x=300, y=170)
btn45 = Button(root, text=45, width=1, command=lambda: play(45))
btn45.place(x=340, y=170)
btn46 = Button(root, text=46, width=1, command=lambda: play(46))
btn46.place(x=20, y=210)
btn47 = Button(root, text=47, width=1, command=lambda: play(47))
btn47.place(x=60, y=210)
btn48 = Button(root, text=48, width=1, command=lambda: play(48))
btn48.place(x=100, y=210)
btn49 = Button(root, text=49, width=1, command=lambda: play(49))
btn49.place(x=140, y=210)
total = Label(root, text="")
total.place(x=10, y=530)

set1 = Label(root, text='', font=font1, bg='yellow', width=15, justify='center')
set1.place(x=0, y=260)
set2 = Label(root, text='', font=font1, bg='yellow', width=15, justify='center')
set2.place(x=0, y=310)
set3 = Label(root, text='', font=font1, bg='yellow', width=15, justify='center')
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
            messagebox.showinfo('Results', str(lottonums) + '\n' + 'Your matches are: ' + str(matches1) + '\n'
                                + 'You won: ' + str(winningtotal))
        else:
            messagebox.showinfo('Congratulations', str(lottonums) + '\n' + 'Your matches are: ' + str(matches1)
                                + '\n' + 'You won: ' + str(winningtotal))
        playbtn.config(state=DISABLED)
    elif played == 1 and played2 == 1 and played3 == 0:
        winningtotal = matches[matches1] + matches[matches2]
        score = score + winningtotal
        if winningtotal == 0:
            messagebox.showinfo('Results', str(lottonums) + '\n' + "Your first set's matches are: " + str(matches1)
                                + '\n'+ "Your second set's matches are : " + str(matches2) + '\n' + 'You won: '
                                + str(winningtotal))
        else:
            messagebox.showinfo('Congratulations', str(lottonums) + '\n' + "Your first set's matches are: "
                                + str(matches1) + '\n' + "Your second set's matches are : " + str(matches2) + '\n'
                                + 'You won: ' + str(winningtotal))
    elif played == 1 and played2 == 1 and played3 == 1:
        winningtotal = matches[matches1] + matches[matches2] + matches[matches3]
        score = score + winningtotal
        if winningtotal == 0:
            messagebox.showinfo('Results', str(lottonums) + '\n' + "Your first set's matches are: "
                                + str(matches1) + '\n' + "Your second set's matches are : " + str(matches2) + '\n'
                                + "Your third set's matches are: " + str(matches3) + '\n' + 'You won: '
                                + str(winningtotal))
        else:
            messagebox.showinfo('Congratulations', str(lottonums) + '\n' + "Your first set's matches are: "
                                + str(matches1) + '\n' + "Your second set's matches are : " + str(matches2) + '\n'
                                + "Your third set's matches are: " + str(matches3) + '\n' + 'You won: '
                                + str(winningtotal))

    total.config(text="R"+str(score))
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

    playagainbtn = Button(root, text='Play again', command=retry)
    playagainbtn.place(x=170, y=500)


playbtn = Button(root, text='Play', state=DISABLED, command=lotto)
playbtn.place(x=170, y=450)


root.mainloop()

#\n