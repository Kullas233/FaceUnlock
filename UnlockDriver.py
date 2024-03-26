import tkinter as tk
from tkinter import messagebox
from tkinter.constants import CENTER

root = tk.Tk()
root.attributes('-fullscreen',True)

label = tk.Label( root, text="Loading", font=("Arial", 50))
label.place(x=500, y=350)

def on_closing():
    pass

root.protocol("WM_DELETE_WINDOW", on_closing)

first = True
end = False
while True:
    root.update_idletasks()
    root.update()
    if first:
        from Unlock import *
        first = False
    
    if end:
        break
    else:
        end = lock()
