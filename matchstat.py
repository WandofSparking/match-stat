from tkinter import *

#-----------------------------------------setting screen bs up-----------------------------
root = Tk()
root.geometry("200x150")

root.configure()

frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

#------------------------------TOP LABEL--------------------------------------------------
top = StringVar()
top.set("Welcome to Echo's Match stats")

label = Label(frame, textvariable = top, )
label.pack()

#-------------------------------Match logger button and logic when clicked---------------------------------------
def logmatch():
    window = Toplevel()
    window.geometry('250x200')

    Label(window, text="Log Game").grid(row=0, column=0, columnspan=2)

    Label(window, text="Points:").grid(row=1, column=0, sticky="e")
    Entry(window).grid(row=1, column=1)

    Label(window, text="Assists:").grid(row=2, column=0, sticky="e")
    Entry(window).grid(row=2, column=1)

    Label(window, text="Saves:").grid(row=3, column=0, sticky="e")
    Entry(window).grid(row=3, column=1)

    Label(window, text="Stuns:").grid(row=4, column=0, sticky="e")
    Entry(window).grid(row=4, column=1)
    
lmbutton = Button(frame, text = "Log Match?", command= logmatch)
lmbutton.pack(pady= 300)


root.title("match stat")
root.mainloop()