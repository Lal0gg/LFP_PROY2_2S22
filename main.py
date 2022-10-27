from argparse import ONE_OR_MORE
from ctypes import resize
from msilib.schema import Control
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import BOTTOM, Menu, Scrollbar, Tk, XView, font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from pynput.mouse import Controller
from pynput.mouse import Listener
from scanner import Scanner
from reporTokens import *
# Variables globales

wnd_menu = None  # ventana menu
packtext = None
file = ""  # contenedor del archivo a analizar
bandera = False
fielpath = ""
flyggg=True
ScannerGG = Scanner()

def openfile():
    global file
    global packtext
    global bandera
    global filpathh
    filpathh = filedialog.askopenfilename(title='Abrir Archivo', filetypes=(
        ("LFP files", "*.lfp*"), ("Text Files", "*.txt"),("GPW Files", "*.gpw"), ("all files", "*.*")))
    try:
        if filpathh != "":
            if(bandera == False):
                file = open(filpathh, 'r', encoding="utf-8")
                contenido = file.read()
                packtext.insert(tk.INSERT, contenido)
                print(contenido)
                file.close()
                bandera = True
                tkinter.messagebox.showinfo(
                    "ALERTA", "Se cargo el araachivo exitosamente")
            else:
                tkinter.messagebox.showinfo(
                    "ERROR", "Ya se cargó  este archivo")
        else:
            tkinter.messagebox.showinfo("ERROR", "No se cargó ningún archivo")
    except:
        pass

def savefile():
    global filpathh
    global packtext
    contenido1 = packtext.get(1.0, tkinter.END)
    try:
        file = open(filpathh, 'w', encoding="utf-8")
        file.write(contenido1)
        file.close()
        tkinter.messagebox.showinfo("GUARDAR", "Se sobrescribió el archivo :D")
    except Exception as e:
        pass


def saveas():
    global packtext
    contenido2 = packtext.get(1.0, tkinter.END)
    filegg = filedialog.asksaveasfilename(title='Guardar Archivo', filetypes=(
        ("LFP files", "*.lfp*"), ("Text Files", "*.txt"), ("all files", "*.*")))
    try:
        file = open(filegg, 'w', encoding="utf-8")
        file.write(contenido2)
        file.close()
        tkinter.messagebox.showinfo("GUARDAR", "Se guard un nuevo archivo :D")
    except Exception as e:
        print(e)

def scanner():
    global filepath
    global file
    global packtext
    global ScannerGG
    contenido1 = packtext.get(1.0, tkinter.END)
    if contenido1 != "":
        ScannerGG.analyze(contenido1)
        ScannerGG.printScannergg()
        
    else:
        tkinter.messagebox.showinfo("ERROR", "No se puede analizar")

# Configuración ventana menu principal ===================================================================
wndw_menu = tkinter.Tk()
wndw_menu.title("WebIDE-Editor")
wndw_menu.resizable(0, 0)
wndw_menu.geometry("1080x720")
wndw_menu.config(bg="black")
#wndw_menu.config(bg="SlateBlue1")
wndw_menu.config(bd=30)
SubMenu = Menu(wnd_menu, selectcolor="green")
wndw_menu.config(menu=SubMenu)

#Variables para la posición
posx= StringVar()
posy = StringVar()

# Items del menú1
file_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nuevo", command=None, font=(
    "Courier 10 bold"), background="#E4E3FF")
file_menu.add_separator()
file_menu.add_command(label="Abrir", command=openfile, font=(
    "Courier 10 bold"), background="#E4E3FF")
file_menu.add_separator()
file_menu.add_command(label="Guardar", command=None, font=(
    "Courier 10 bold"), background="#E4E3FF")
file_menu.add_separator()
file_menu.add_command(label="Guardar Como", command=None, font=(
    "Courier 10 bold"), background="#E4E3FF")
file_menu.add_separator()
file_menu.add_command(label="Salir", font=(
    "Courier 10 bold"), background="#E4E3FF", command=wndw_menu.quit)
# Items del menú2
help_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Analizar", menu=help_menu)
help_menu.add_command(label="Generar Pag Web", command=None, font=(
    "Courier 10 bold"), background="#E4E3FF")
# Items del menú3
toks_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Tokens", menu=toks_menu)
toks_menu.add_command(label="Ver", command=None, font=(
    "Courier 10 bold"), background="#E4E3FF")

# Items del menú4
err_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Area de Errores", menu=err_menu)
err_menu.add_command(label="Ver Area", command=None, font=(
    "Courier 10 bold"), background="#E4E3FF")

#Label1
niuLabelx = Label(wndw_menu,text="x:",fg="white",font=("Courier 15 bold"),bg='black')
niuLabelx.place(x=1,y=10)
#Label2
niuLabely = Label(wndw_menu,text="y:",fg="white",font=("Courier 15 bold"),bg='black')
niuLabely.place(x=1,y=40)

#Label3
niuLabeln1 = Label(wndw_menu,fg="white",font=("Courier 15 bold"),bg='black',textvariable=posx)
niuLabeln1.place(x=30,y=11)

#Label4
niuLabeln2 = Label(wndw_menu,fg="white",font=("Courier 15 bold"),bg='black',textvariable=posy)
niuLabeln2.place(x=30,y=41)

def getxy(event):
    global posx 
    global posy
    
    xy=packtext.index(INSERT)
    nueva=xy.split('.')
    posx.set(nueva[0])
    posy.set(nueva[1])
    #Label3
    print('Cordenada x: ' ,posx ,'Coordenada y: ',posy)


packtext = Text(wndw_menu, width=110,height=40,font=('Courier', 10))
packtext.place(x=80,y=10)
packtext.config(foreground='#00FFCB',background='black',insertbackground='#A000FF')
scrollb= Scrollbar(wndw_menu,command=packtext.yview,background='black')
packtext['yscroll'] = scrollb.set
scrollb.grid(pady=300,padx=965)
packtext.bind("<Button-1>",getxy)

wndw_menu.mainloop()
# Fin ventana menu principal ===================================================================





