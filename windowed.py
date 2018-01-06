#!/usr/bin/python3

import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter.font as tkfont

import os

import sync #my synching methods

import datetime #for filenames

root = tkinter.Tk(className="Typist editor")

windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()

customFont = tkfont.Font(family="Courier New", weight="normal", size=10)
textPad = ScrolledText(root, width=20, height=10, font=customFont)
textPad ["insertofftime"] = 0


root.geometry("%dx%d" % (windowWidth, windowHeight))

textPad["width"] = int(windowWidth / 8)
textPad["height"] = int(windowHeight / 16)


textPad.pack()

#some data of the file
filename = datetime.datetime.today().strftime('%Y-%m-%d')
folder = "text"
fullPath = os.path.join(folder, filename)
synchableChanges = True

#create folder if it does not exists
if not os.path.exists(folder):
	os.makedirs(folder)

def open_command():
	try:
		with open(fullPath) as file:
			textPad.insert("1.0", file.read())
			textPad.edit_modified(False) #so the file does not get written directly
	except FileNotFoundError:
		print("no file with the name " + filename + " exists, creating blank dockument")


open_command()

def save_command():
	with open(fullPath, "w") as file:
		data = textPad.get("1.0", END+"-1c") #Apparently the text widget adds blank line to text automaticaly, removes that
		file.write(data)
		synchableChanges = True
		#print("writes to file " + filename);

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
	if synchableChanges:
		print("syncs...");
		if sync.syncFiles(): #from synch.py
			synchableChanges = False
	root.after(5000, synchInterval)
	
root.after(5000, synchInterval)

def backspace_word(event):
	w = event.widget
	charBeforeInsert = w.get("insert-1c", INSERT)
	if charBeforeInsert == " " or charBeforeInsert == "	":
		#clear spaces before next word
		w.delete("insert-1c wordstart", INSERT)
	event.widget.delete("insert-1c wordstart", INSERT)
	#event.widget.delete("insert-1c", INSERT)
	#event.widget.insert("insert wordstart", "hej")
	return "break" #prevent event from propagating

def hello(args):
    print("hello")
    return "break" #prevent event from propagating
    


textPad.focus()
textPad.bind("<Control-BackSpace>", backspace_word)

root.mainloop()
