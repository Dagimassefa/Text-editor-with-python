from tkinter import *

from tkinter import filedialog

import tkinter
from tkinter import colorchooser
from turtle import color

window=Tk()


#function for opening the file
def OpenFile():
    filepath=filedialog.askopenfilename()
    pathh.insert(END,filepath)
    filepath=open(filepath)
    file_cont=filepath.read()
    text.insert(END,file_cont)
    filepath.close()


 #function for saving the file   
def SaveFile():
    file=filedialog.asksaveasfile(defaultextension='.txt',
    filetypes=[("Text File",".txt"),
    ("HTML File",".html"),
    ("All Files",".*")])
    filetext=str(text.get(1.0,END))
    file.write(filetext)
    file.close()
    if file is None:
        return


#function to cut a selected text in a file
def CutFile():
    global data
    if text.selection_get():
        data=text.selection_get()
        text.delete('sel.first','sel.last')


#function to copy a selected text in a file
def CopyFile():
    global data
    if text.selection_get():
        data=text.selection_get()


#function to paste a copied text in a file
def PasteFile():
    global data
    text.insert(tkinter.END,data)


#function to select all text in a file
def SelectAll():
    text.tag_add("sel","1.0","end")
    text.tag_config("sel")


#function to change the font of a text
def ChangeFont():
    color=colorchooser.askcolor()
    text.config(fg=color[1])


def quitfunction():
    window.destroy()


def NewFile():
    window.title("Untitled")
    text.delete(1.0,END)

menubar=Menu(window)
window.config(menu=menubar)


#File menu bar
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New File",command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Open",command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Save",command=SaveFile)


#Edit menu bar
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=CutFile)
editmenu.add_separator()
editmenu.add_command(label="Copy",command=CopyFile)
editmenu.add_separator()
editmenu.add_command(label="Paste",command=PasteFile)
editmenu.add_separator()
editmenu.add_command(label="Select All",command=SelectAll)


#Format menu bar
formatmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu)
formatmenu.add_command(label="Font Color",command=ChangeFont)



#Exit menu bar
exitmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Exit",menu=exitmenu)
exitmenu.add_command(label="Exit",command=quitfunction)


window.title("Text editor")
icon = PhotoImage(file='image.png')
window.iconphoto(True,icon)
text=Text(window)
pathh=Entry(window)
text.pack()
window.mainloop()