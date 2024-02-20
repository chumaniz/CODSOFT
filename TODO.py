# I am importing the Tkinter Library
# What I did was import a GUI Library with which I can design my application
# As well the messagebox widget which displays messages
from tkinter import *
import tkinter.messagebox 
import tkinter as tk

window = Tk()
# Now we proceed to give a title
window.title("Amahle's Todolist APP")

# Creating Frame widget to hold the listbox and scrollbar 
frameTask = Frame(window)
frameTask.pack()

# Holding items in a list box
listboxTask=Listbox(frameTask, bg="grey", fg="white", height=20, width=60, font="Modern")
listboxTask.pack(side=tk.LEFT)

# Scrolldown incase the list is too long for the window
# Using side to position the bar with its direction and side
scrollBar = Scrollbar(frameTask)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
listboxTask.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=listboxTask.yview)


window.mainloop()
# mainloop() runs Tkinter event loop and displays everything

