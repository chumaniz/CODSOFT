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
frameTask = tk.Frame(window)
frameTask.pack()

# Holding items in a list box
listboxTask=Listbox(frameTask, bg="green", fg="white", height=20, width=60, font="Modern")
listboxTask.pack(side=tk.LEFT)

# Scrolldown incase the list is too long for the window
# Using side to position the bar with its direction and side
scrollBar = tk.Scrollbar(frameTask)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
listboxTask.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=listboxTask.yview)


def entertask():
    # A new window will pop up to accept input
    inputText = ""
    def add():
        inputText=entryTask.get(1.0, "end-1c")
        if inputText =="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter Your Task.")
        else:
            listboxTask.insert(END, inputText)
            #closing root1 window
            root1.destroy 
    root1=Tk()
    entryTask=Text(root1,width=50,height=6)
    entryTask.pack()
    buttonTemp=tk.Button(root1, text="Add task", command=add)
    buttonTemp.pack()
    root1.mainloop()

# Making a Button widget
enterButton = tk.Button(window, text="Add Task", width=65, command=entertask)
enterButton.pack(pady=4)

# This function enables deletion of tasks
def delTask():
    # Using a selector system to delete tasks...like Gmail
    selected=listboxTask.curselection()
    listboxTask.delete(selected[0])

deleteButton = tk.Button(window, text="Delete Selected Task", width=65, command=delTask)
deleteButton.pack(pady=4)


# This function enables the app to mark the task as complete

def markcompleted():
    completed = listboxTask.curselection()
    if completed: # Check If item selected
        index = completed[0]
        item = listboxTask.get(index)

        item += " ✔"

        # Updating items in the listbox

        listboxTask.delete(index)
        listboxTask.insert(index, item)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to mark as completed.")

mark_button = tk.Button(window, text="Mark Task As Completed", width=65, command = markcompleted)
mark_button.pack(pady=4)


window.mainloop()
# mainloop() runs Tkinter event loop and displays everything

