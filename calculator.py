from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry('312x324')
window.resizable(0,0)
window.title("Calculator")

# This function takes button presses and converts them to the screen respectively
def button_click(item):
    global expression
    expression = expression + str(item)
    typedText.set(expression)

# This function enables the clearing of the screen
def button_clear():
    global expression
    expression = ""
    typedText.set("")

# Function for the equal button
    
def equals_sign():
    global expression
    answer = str(eval(expression))
    # 'eval' shows the string expression directly and returns the value as an integer
    typedText.set(answer)
    expression=""

expression = ""
typedText = StringVar()

screen_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="cyan", highlightcolor="cyan", highlightthickness=2)
screen_frame.pack(side=TOP)

screen_fill = Entry(screen_frame, font=('Impact', 18, 'bold'),
textvariable=typedText, width=50, bg="#cec7ff", bd=0, justify=RIGHT)

screen_fill.grid(row=0, column=0)

screen_fill.pack(ipady=10)


buttonPad = Frame(window, width=312, height=272.5, bg="grey")

buttonPad.pack()

# row1
clear = Button(buttonPad, text = "Clr", fg="red", width=32, height=3, bd=0, bg="#c9c7c7", cursor="hand2", command=lambda: button_clear()).grid(row=0, column=1, columnspan=3, padx=1, pady=1)

divide = Button(buttonPad, text="÷", fg="blue", width=10, height=3, bd=0, bg="#c9c7c7", cursor="hand2", command=lambda: button_click("÷")).grid(row=0, column=3, padx=1, pady=1)

# row2
seven = Button(buttonPad, text = "7", fg="black", width=10, height=3, bd=0, bg="#d1d1d1", cursor="hand2", command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(buttonPad, text="8", fg="black", width=10, height=3, bd=0, bg="#d1d1d1", cursor="hand2", command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1) 

nine = Button(buttonPad, text="9", fg="black", width=10, height=3, bd=0, bg="#d1d1d1", cursor="hand2", command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1) 

multiply = Button(buttonPad, text = "X", fg = "blue", width = 10, height = 3, bd = 0, bg = "#c9c7c7", cursor = "hand2", command = lambda: button_click("X")).grid(row = 1, column = 3, padx = 1, pady = 1)

# row3
four = Button(buttonPad, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#d1d1d1", cursor = "hand2", command = lambda: button_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(buttonPad, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#d1d1d1", cursor = "hand2", command = lambda: button_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(buttonPad, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#d1d1d1", cursor = "hand2", command = lambda: button_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(buttonPad, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#c9c7c7", cursor = "hand2", command = lambda: button_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

window.mainloop()