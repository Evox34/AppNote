import pickle
import tkinter
from tkinter import *
import os
from tkinter import messagebox


os.makedirs("AppNote", exist_ok=True)
os.makedirs("AppNote/Parametre" ,exist_ok=True)
os.makedirs("AppNote/sav",exist_ok=True)
# creation d'une fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("AppNote")
app.iconbitmap("png.ico")



# creation definition appuit and add a list to the listbox
def appuit(event) :
    NumNote = 0
    list.insert("1", "Note:", var_entry.get())





class Sav():
	#no-operational backup system
    def __init__(self,TextList,Numéro):
        self.textlist = TextList
        self.number = Numéro






with open("data.App","wb") as fil:
     Record = pickle.Pickler(fil)
     Record.dump(Sav)


def Supp(event) :
	list.Supp("1")


# messagebox question

def Show() :
    result = messagebox.askquestion("Exit programe", "Vous voulez quittez le programe?", icon='warning')
    if result == 'yes' :
        print("Programe stoper")
        app.quit()


# creation folder


Entrer = Label(text="Bienvenue sur AppNote Alpha 0.0.1 ")


Entrer.pack()

list = Listbox(bg="#818181")


list.insert("0", "Votre liste de note")

var_entry = tkinter.StringVar()
Sav = Sav(var_entry, 10)
Entr = tkinter.Entry(app, textvariable=var_entry)
textSav = var_entry.get()
list.insert("1",)
Entr.bind("<Up>", Supp)
#  touch UP = function appuit
Entr.bind("<Button-2>", appuit)
#  touch Button2 = function appuit
Entr.pack()

Text = tkinter.Label(app, textvariable=var_entry)

Text.pack()

# def button quit
Quit = Button(text="Quit", command=Show)
Quit.pack()

list.pack()

app.mainloop()
