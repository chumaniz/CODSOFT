from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry('300x250')
window.resizable(0,0)
window.title("Calculator")

# This function takes button presses and converts them to the screen respectively
def button_click(item):
    global expression
    expression = expression + str(item)
    inputText.set(expression)

# This function enables the clearing of the screen
def button_clear():
    global expression
    expression = ""
    inputText.set("")






window.mainloop()