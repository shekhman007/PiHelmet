import os
import time
import tkinter as tk
from PIL import ImageTk

from tkinter import ttk

root = tk.Tk()

style = ttk.Style()

style.layout('TNotebook.Tab', []) # turn off tabs

root.config(cursor="none")

root.wait_visibility(root)

root.attributes('-fullscreen', True)

root.title("Goggle OS")

tabControl = ttk.Notebook(root)

img = ImageTk.PhotoImage(file="loading.jpeg")

def getMap():
    os.system(
        'curl "https://api.mapbox.com/styles/v1/nudnik-shpilkas/ckgjw83u407941bmomr7t7fm1/static/-72.940188,41.881729,18/240x135?access_token=pk.eyJ1IjoibnVkbmlrLXNocGlsa2FzIiwiYSI6ImNrZ2p0YWs5eTA0ODYyc3BuZWdienV0NmoifQ.X9NhPLVGiF5Rc5mInC85hQ" --output /~/pihelmet/tile.jpeg'
        )
    img = ImageTk.PhotoImage(file="tile.jpeg")
    ttk.Label(tab1, image=img).grid(column=0, row=0, padx=30, pady=30)
    root.update()
    root.update_idletasks()
    time.sleep(1)
    root.update_idletasks()

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

ttk.Label(tab1, image=img).grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab2, text='Settings').grid(column=0, row=0, padx=30, pady=30)

while True:
    getMap()
