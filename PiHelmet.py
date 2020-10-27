import tkinter as tk
from tkinter import *

from tkinter import ttk

root = tk.Tk()

style = ttk.Style()

style.layout('TNotebook.Tab', []) # turn off tabs


root.title("Goggle OS")

tabControl = ttk.Notebook(root)

#Main Tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')

#Settings Tabs
tabSettings = ttk.Notebook(tab2)

tabwifi = ttk.Frame(tabControl)


def key2(event):
    tabControl.select(tab2)

def key1(event):
    tabControl.select(tab1)

root.bind("1", key1)
root.bind("2", key2)

tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text='Map').grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab2, text='Settings').grid(column=0, row=0, padx=30, pady=30)



root.mainloop()

