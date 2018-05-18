#!/usr/bin/python3

import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter.font as tkfont

import os

import hashlib

sync_enabled = False
try:
    import sync  # my synching methods
    sync_enabled = True
except e:
    print ("synching disabled")

import datetime  # for filenames

root = tkinter.Tk(className="Typist editor")

windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()

customFont = tkfont.Font(family="Courier New", weight="normal", size=10)
textPad = ScrolledText(root, width=20, height=10, font=customFont)
textPad["insertofftime"] = 0

root.geometry("%dx%d" % (windowWidth, windowHeight))

# Remove borders
textPad["borderwidth"] = 0
textPad["highlightthickness"] = 0
textPad.vbar["borderwidth"] = 0
textPad.vbar["background"] = "black"
textPad.vbar["width"] = 3

# here the main thing is that the dimensions must be larger than the root windows dimensions
# The width and height is meassured in rows and columns
textPad["width"] = int(windowWidth)
textPad["height"] = int(windowHeight)
textPad["cursor"] = "none"
textPad["wrap"] = "word"
textPad["padx"] = 5
textPad["pady"] = 5

textPad.pack()

infoFrame = None
infoVisible = False


def showInfoText(info_text):
    global infoFrame
    infoFrame = Label(root, text=info_text, justify=LEFT)
    infoFrame.pack()
    infoFrame.place(x=0, y=0)

def getHostName():
    from sys import platform
    if platform == "linux" or platform == "linux2":    
        import subprocess
        hostname = subprocess.check_output("hostname -I", shell=True).decode('utf-8').split()[0]
    else:
        import socket
        hostname = socket.gethostbyname(socket.gethostname())
    return hostname

def showInfo():
    global infoVisible
    global textPad
    
    hostname = getHostName()
    info_text =  "Press F1 to toggle this message\n" + "ip: " + hostname
    textPadText = textPad.get("1.0", END + "-1c")
    info_text += "\nwords: " + str(len(textPadText.split()))
    info_text += "\nletters: " + str(len(textPadText))
    info_text += "\nletters (no space): " + str(len("".join(textPadText.split())))

    showInfoText(info_text)
    infoVisible = True


def hideInfo():
    global infoVisible
    infoFrame.place_forget()
    infoVisible = False


def toggle_info(event = None):
    if infoVisible:
        hideInfo()
    else:
        showInfo()


# some data of the file
filename = datetime.datetime.today().strftime('%Y-%m-%d')
folder = "text"
fullPath = os.path.join(folder, filename)
synchableChanges = True

# create folder if it does not exists
if not os.path.exists(folder):
    os.makedirs(folder)


def open_command():
    try:
        with open(fullPath) as file:
            textPad.insert("1.0", file.read())
            textPad.edit_modified(False)  # so the file does not get written directly
    except FileNotFoundError:
        print("no file with the name " + filename + " exists, creating blank dockument")


open_command()


def hashString(string):
    m = hashlib.md5()
    m.update(string.encode("utf-8"))
    return m.hexdigest()


def save_command():
    data = textPad.get("1.0", END + "-1c")  # Apparently the text widget adds blank
    try:
        with open(fullPath, "r") as file:
            oldData = file.read()

        # line to text automaticaly, removes that

        m1 = hashString(data.strip())
        m2 = hashString(oldData.strip())
        # print(m1 + "\n")
        # print(m2 + "\n")

        if m1 == m2:
            # print("file is not changed, skip write")
            return
    except:
        # If file could not be opened just write a new file
        print("could not open file for comparison when saving")
        pass

    with open(fullPath, "w") as file:
        file.write(data)
        synchableChanges = True
        # print("writes to file " + filename);


def testSave():
    if textPad.edit_modified():
        textPad.edit_modified(False)
        synchableChanges = True;
        save_command()


def saveInterval():
    testSave()
    root.after(1000, saveInterval)


saveInterval()


def synchInterval():
    global synchableChanges
    sync.syncFiles()
    root.after(5000, synchInterval)


root.after(5000, synchInterval)


def backspace_word(event):
    w = event.widget
    charBeforeInsert = w.get("insert-1c", INSERT)
    if charBeforeInsert == " " or charBeforeInsert == "	":
        # clear spaces before next word
        w.delete("insert-1c wordstart", INSERT)
    event.widget.delete("insert-1c wordstart", INSERT)
    # event.widget.delete("insert-1c", INSERT)
    # event.widget.insert("insert wordstart", "hej")
    return "break"  # prevent event from propagating


def hello(args):
    print("hello")
    return "break"  # prevent event from propagating


textPad.focus()
textPad.bind("<Control-BackSpace>", backspace_word)
textPad.bind("<F1>", toggle_info)

root.configure(background="white")


toggle_info()

root.mainloop()
