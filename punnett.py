from tkinter import *

root = Tk()
root.title("Punnett Square Calculator")
root.geometry("1000x750")

page1 = Frame(root, bg="red")
page2 = Frame(root, bg="pink")

e = Entry(root)

e.grid()
e.insert(0, "Name:")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.grid()

def showSingle():
    page1.tkraise()

def showDihybrid():
    page2.tkraise()

myButton = Button(root, text="Click Me!", command=myClick)

single = Button(root, text="Single Trait", command=showSingle)
singleLabel = Label(page1, text="How to Use Punnett Squares")
singleLabel.grid()
dihybrid = Button(root, text="Dihybrid Cross", command=showDihybrid)

single.grid(row=3, column=0)
dihybrid.grid(row=3, column=1)

page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")

root.mainloop()