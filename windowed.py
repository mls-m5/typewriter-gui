#!/usr/bin/python3

import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter.font as tkfont

root = tkinter.Tk(className=" Just another Text Editor")



customFont = tkfont.Font(family="Courier 10 Pitch", size=10)
textPad = ScrolledText(root, width=20, height=10, font=customFont)


root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))

textPad["width"] = int(root.winfo_screenwidth() / 8)
textPad["height"] = int(root.winfo_screenheight() / 16)

print(root.winfo_screenwidth())
print(root.winfo_screenheight())

textPad.insert(INSERT, root.winfo_screenwidth())
textPad.insert(INSERT, root.winfo_screenheight())


# create a menu & define functions for each menu item

def open_command():
    pass
#         file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
#         if file != None:
#             contents = file.read()
#             textPad.insert('1.0',contents)
#             file.close()

def save_command(self):
    pass
#     file = tkFileDialog.asksaveasfile(mode='w')
#     if file != None:
#     # slice off the last character from get, as an extra return is added
#         data = self.textPad.get('1.0', END+'-1c')
#         file.write(data)
# #         file.close()
        
def exit_command():
    pass
#     if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
#         root.destroy()


def about_command():
    tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")
    

# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label="File", menu=filemenu)
# # filemenu.add_command(label="New", command=dummy)
# filemenu.add_command(label="Open...", command=open_command)
# filemenu.add_command(label="Save", command=save_command)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=exit_command)
# helpmenu = Menu(menu)
# menu.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="About...", command=about_command)

#
textPad.pack()

def hello(args):
    print("hello")
    return "break" #prevent event from propagating

textPad.bind("<Control-BackSpace>", hello)
root.mainloop()