from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry('300x250')
window.resizable(0,0)
window.title("Calculator")

def button_click(item):
    global expression
    expression = expression + str(item)
    inputText.set(expression)






window.mainloop()