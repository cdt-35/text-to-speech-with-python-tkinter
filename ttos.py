import tkinter as tk
from tkinter import ttk
import pyttsx3 as pt
from tkinter import filedialog as fd
from tkinter import messagebox as mb

win=tk.Tk()
win.title('Text to Speech')
win.geometry('360x170')
win.resizable(False,False)

e=pt.init()

def opn():
    global fn
    fn=fd.askopenfilename(filetypes=[('Text files','*.txt')])
    if fn=='':
        mb.showerror('Not found','No file were selected')
    else:
        e2.insert(0,fn)
def tts():
    if len(e1.state())==0 or e1.state()[0]!='disabled':
        sp=e.say(e1.get())
    else:
        f=open(fn,'r')
        sp=e.say(f.read())
    e.setProperty('rate','30')
    e.runAndWait()

def swt():
    if e2.state()[0]=='disabled':
        e2.configure(state='active')
        bt1.configure(state='active')
        e1.configure(state='disabled')
    else:
        e1.configure(state='active')
        e2.configure(state='disabled')
        bt1.configure(state='disabled')

def abt():
    mb.showinfo('Introduction','Hello user, you are using a text to speech converter.\nCreated by Abdullah Al Rafi')

l=ttk.Label(win,text='Text to Speech converter').grid(row=0,column=1)
dl=ttk.Label(win,text='='*len('Text to Speech converter')).grid(row=1,column=1)
sw=ttk.Button(win,text='Switch method',command=swt).grid(row=2,column=2)

l1=ttk.Label(win,text='Enter text:').grid(row=2,column=0)
e1=ttk.Entry(win,width=30)
e1.grid(row=2,column=1)
e1.focus()


l2=ttk.Label(win,text='or').grid(row=3,column=1)

l3=ttk.Label(win,text='Open file:').grid(row=4,column=0)
e2=ttk.Entry(win,width=30,state='disabled')
e2.grid(row=4,column=1)
bt1=ttk.Button(win,text='Select',command=opn,state='disabled')
bt1.grid(row=4,column=2)

l2=ttk.Button(win,text='Text to Speech',command=tts).grid(row=5,column=1,pady=10)

ab=ttk.Button(win,text='About',command=abt).grid(row=5,column=2)

win.mainloop()