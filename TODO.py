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
listboxTask=Listbox(frameTask, bg="green", fg="red", height=20, width=60, font="Modern")
listboxTask.pack(side=tk.RIGHT)







window.mainloop()
# mainloop() runs Tkinter event loop and displays everything

