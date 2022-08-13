from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import os

def start():
    ipt2.delete(0,tkinter.END)
    ipt2.insert(0,eval(ipt1.get()))
w=tk.Tk()
w.geometry("200x100")
w.title("Calculator")
ipt1=Entry(w)
OK=Button(w,text="OK",command=start)
ipt2=Entry(w)
ipt1.pack()
OK.pack()
ipt2.pack()
w.mainloop()
