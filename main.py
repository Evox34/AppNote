import pickle
import tkinter
from tkinter import *
import os
from tkinter import messagebox
import webbrowser

os.makedirs("AppNote", exist_ok=True)
os.makedirs("AppNote/Parametre" ,exist_ok=True)
os.makedirs("AppNote/sav",exist_ok=True)
# creation d'une fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("AppNote")
app.iconbitmap("png.ico")


def web():
	webbrowser.open_new("https://github.com/Evox34/AppNote")

# creation definition appuit and add a list to the listbox
def appuit(event) :
    
    list.insert("1", "Note:", var_entry.get())
    print("create note ")





	




def clear(event) :
	list.delete("1")
	print("remove note ")


# messagebox question

def Show() :
    result = messagebox.askquestion("Exit programe", "Are You Sure?", icon='warning')
    if result == 'yes' :
        print("Programe stop")
        app.quit()


# creation folder


Entrer = Label(text="Bienvenue sur AppNote  ")
bntgit = Button(text="github",command=web)
bntgit.pack()

Entrer.pack()

list = Listbox(bg="#818181")


list.insert("0", "Votre liste de note")

var_entry = tkinter.StringVar()

Entr = tkinter.Entry(app, textvariable=var_entry)
textSav = var_entry.get()
list.insert("1",)
 
Entr.bind("<Button-2>", appuit)
#  touch Button2 = function appuit
Entr.pack()

Entr.bind("<Up>",clear)
Text = tkinter.Label(app, textvariable=var_entry)

Text.pack()

# def button quit
Quit = Button(text="Quit", command=Show)
Quit.pack()

list.pack()

app.mainloop()
