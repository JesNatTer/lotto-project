import math
import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("Shape area calculator")
root.geometry("1200x300")
root.resizable(0, 0)


class Circle:
    def __init__(self, master):
        frame = Frame(master, width=400, height=300, bg="#ff5733")
        frame.place(x=0, y=0)
        self.label = Label(frame, text="Enter radius of circle", bg="#ff5733")
        self.label.place(x=2, y=2)

        self.radiusInput = Entry(frame, bg="#ab2306")
        self.radiusInput.place(x=150, y=2)

        self.resultLabel = Label(frame, text=" ", width=10, highlightcolor="#222", bg="#ab2306")
        self.resultLabel.place(x=2, y=100)

        self.btn = Button(frame, text="Calculate Area", bg="#ab2306", highlightbackground="#222",
                          highlightcolor="#5f1100", command=self.area_of_circle)
        self.btn.place(x=2, y=50)

    def area_of_circle(self):
        radius = float(self.radiusInput.get())
        result = round(math.pi * float(radius**2), 2)
        self.resultLabel.config(text=result)


class Rectangle:
    def __init__(self, master):
        frame2 = Frame(master, width=400, height=300, bg="#c70039")
        frame2.place(x=400, y=0)
        self.label = Label(frame2, text="Enter width of rectangle", bg="#c70039")
        self.label.place(x=2, y=2)

        self.label2 = Label(frame2, text="Enter height of rectangle", bg="#c70039")
        self.label2.place(x=2, y=30)

        self.widthInput = Entry(frame2, bg="#8d0028")
        self.widthInput.place(x=170, y=2)

        self.heightInput = Entry(frame2, bg="#8d0028")
        self.heightInput.place(x=170, y=30)

        self.resultLabel = Label(frame2, text=" ", width=10, highlightcolor="#222", bg="#8d0028")
        self.resultLabel.place(x=2, y=100)

        self.btn = Button(frame2, text="Calculate Area", bg="#8d0028", highlightbackground="#222",
                          highlightcolor="#5f1100", command=self.area_of_rectangle)
        self.btn.place(x=2, y=60)

    def area_of_rectangle(self):
        width = float(self.widthInput.get())
        height = float(self.heightInput.get())
        result = round(height * width, 2)
        self.resultLabel.config(text=result)


class Triangle:
    def __init__(self, master):
        frame2 = Frame(master, width=400, height=300, bg="#581845")
        frame2.place(x=800, y=0)
        self.label = Label(frame2, text="Enter base of triangle", bg="#581845")
        self.label.place(x=2, y=2)

        self.label2 = Label(frame2, text="Enter height of triangle", bg="#581845")
        self.label2.place(x=2, y=30)

        self.baseInput = Entry(frame2, bg="#8a1968")
        self.baseInput.place(x=170, y=2)

        self.heightInput = Entry(frame2, bg="#8a1968")
        self.heightInput.place(x=170, y=30)

        self.resultLabel = Label(frame2, text=" ", width=10, highlightcolor="#222", bg="#8a1968")
        self.resultLabel.place(x=2, y=100)

        self.btn = Button(frame2, text="Calculate Area", bg="#8a1968", highlightbackground="#222",
                          highlightcolor="#5f1100", command=self.area_of_triangle)
        self.btn.place(x=2, y=60)

    def area_of_triangle(self):
        base = float(self.baseInput.get())
        height = float(self.heightInput.get())
        result = round((height * base/2), 2)
        self.resultLabel.config(text=result)


c = Circle(root)
r = Rectangle(root)
t = Triangle(root)
root.mainloop()
