import tkinter as tk
from tkinter import PhotoImage, Label, Button, Message, messagebox
from tkinter import *
import json
from difflib import get_close_matches
import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def search():

    data = json.load(open('data.json'))
    word = enterwordEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        textarea.delete(1.0, END)

        for item in meaning:
            textarea.insert(END, u'\u2922' + item + '\n')

    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('confirm ', f'Do you mean {close_match} instead')
        if res == True:

            enterwordEntry.delete(0, END)
            enterwordEntry.insert(END, close_match)
            meaning = data[close_match]
            textarea.delete(1.0, END)
            for item in meaning:
                textarea.insert(END, u'\u2922' + item + '\n')
        else:
            messagebox.showinfo('You enter the an incorrect word', 'check the word you entered')
            enterwordEntry.delete(0, END)
            textarea.delete(1.0, END)


def clear():
    enterwordEntry.delete(0,END)
    textarea.delete(1.0,END)


def exist():
    ask = messagebox.askyesno('Do you want to exist',)
    if ask:
        root.destroy()
    else:
        pass

def sound():
    engine.say(enterwordEntry.get())
    engine.runAndWait()



def text_area_sound():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()


# images are from pexels.com,flaticon.com
root = tk.Tk()
root.geometry('1000x600+100+30')
root.resizable(False, False)
root.title('kc talking dictionary')

# label for background immage
bgimg = PhotoImage(file='bg.png')
bglbl = Label(root, image=bgimg)
bglbl.place(x=0, y=0)

# label for the label enter word text

enterwordlab = Label(root, text='Enter Word', font=('castella', 40, 'bold'), fg='red3', bg='whitesmoke')
enterwordlab.place(x=530, y=20)

# entry label for writing
enterwordEntry = Entry(root, font=('arial', 23, 'bold'), justify='center')
enterwordEntry.place(x=510, y=80)

# search image
searchimg = PhotoImage(file='search.png')
searchlbl = Button(root, image=searchimg, bd=0, bg='whitesmoke', cursor='hand2', command=search,
                   activebackground='whitesmoke')
searchlbl.place(x=620, y=130)

# mic image
micimg = PhotoImage(file='mic.png')
miclbl = Button(root, image=micimg, bd=0, bg='whitesmoke',
                cursor='hand2', activebackground='whitesmoke',command=sound)
miclbl.place(x=710, y=130)

# enter meaning word
enterwordlab = Label(root, text='MEANING', font=('castella', 40, 'bold'), fg='red3', bg='whitesmoke')
enterwordlab.place(x=540, y=190)

# textarea LAbel
textarea = Text(root, width=34, height=8, font=('arial', 18, 'bold'), bd=8,
                relief=GROOVE)
textarea.place(x=460, y=260)

audioimage = PhotoImage(file='microphone.png')
audioButton = Button(root, image=audioimage, bd=0,
                     bg='whitesmoke', activebackground='whitesmoke', cursor='hand2', command=text_area_sound)
audioButton.place(x=520, y=515)

clearimage = PhotoImage(file='clear.png')
clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground=
            'whitesmoke', cursor='hand2',command=clear)
clearButton.place(x=630, y=515)

exitimage = PhotoImage(file='exit.png')
exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke',
                    activebackground='whitesmoke', cursor='hand2',command=exist)
exitButton.place(x=730, y=515)

root.mainloop()
