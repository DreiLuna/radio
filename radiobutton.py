from tkinter import *

root = Tk()

def op1():
    lable.configure(text="You have selected option 1!")

def op2():
    lable.configure(text="You have selected option 2!")

def op3():
    lable.configure(text="You have selected option 3!")

r1_v = IntVar()

option1 = Radiobutton(root, text="option 1", command = op1, value = 1, variable= r1_v)
option2 = Radiobutton(root, text="option 1", command = op2, value = 2, variable= r1_v)
option3 = Radiobutton(root, text="option 1", command = op3, value = 3, variable= r1_v)

lable = Label(root, text = "You have selected nothing.")

option1.grid(row= 0, column = 0)
option2.grid(row= 1, column = 0)
option3.grid(row= 2, column = 0)
lable.grid(row=3, column = 0)

root.mainloop()