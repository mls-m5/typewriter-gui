#!/usr/bin/python3

import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter.font as tkfont

import os

import hashlib

import sync #my synching methods

import datetime #for filenames

root = tkinter.Tk(className="Typist editor")

windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()

customFont = tkfont.Font(family="Courier New", weight="normal", size=10)
textPad = ScrolledText(root, width=20, height=10, font=customFont)
textPad ["insertofftime"] = 0


root.geometry("%dx%d" % (windowWidth, windowHeight))


#Remove borders
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

def hashString(string):
	m = hashlib.md5()
	m.update(string.encode("utf-8"))
	return m.hexdigest()
	

def save_command():
	
	#with open(fullPath, "r") as file:
	#	oldData = file.read()
	
	#data = textPad.get("1.0", END+"-1c") #Apparently the text widget adds blank
	## line to text automaticaly, removes that
	
	#m1 = hashString(data)
	#m2 = hashString(oldData)
	
	#if m1 == m2:
	#	print("file is not changed skip write")
	#	return
	
	with open(fullPath, "w") as file:
		 
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
	sync.syncFiles()
	root.after(10000, synchInterval)
	
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

root.configure(background="white")

root.mainloop()
