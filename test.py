from tkinter import *
from tkinter import messagebox
import Ploot_cl


def show_message():
    print(message_entry.get())



root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

message_entry = Entry()

message_button = Button(text="Click Me", command=show_message)

message_button.pack()
message_entry.pack()
stert = Ploot_cl.PlotClass(root)
root.mainloop()
