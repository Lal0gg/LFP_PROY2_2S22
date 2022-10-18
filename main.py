from ctypes import resize
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import BOTTOM, Menu, Scrollbar, Tk, XView, font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from turtle import back


# Variables globales
wnd_menu = None  # ventana menu
scroll1 = None
file = ""  # contenedor del archivo a analizar
bandera = False
fielpath = ""


def window_mainMenu():
    global wndw_menu
    global scroll1
    # Configuración ventana menu principal
    wndw_menu = tkinter.Tk()
    wndw_menu.title("WebIDE-Editor")
    wndw_menu.resizable(0, 0)
    wndw_menu.geometry("1080x720")
    wndw_menu.config(bg="black")
    #wndw_menu.config(bg="SlateBlue1")
    wndw_menu.config(bd=30)
    SubMenu = Menu(wnd_menu, selectcolor="green")
    wndw_menu.config(menu=SubMenu)
    imagenn = PhotoImage(file="fot.png")
    fondog= Label(wndw_menu,image=imagenn,background='black')
    fondog.place(x=0,y=0)

    # Items del menú1
    file_menu = Menu(SubMenu, tearoff=0)
    SubMenu.add_cascade(label="Archivo", menu=file_menu)
    file_menu.add_command(label="Nuevo", command=None, font=(
        "Courier 10 bold"), background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Abrir", command=None, font=(
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

        
    scroll1 = scrolledtext.ScrolledText(
        wndw_menu, width=100, height=40, font=('Courier', 10),wrap=WORD)
    scroll1.place(x=80, y=10)
    scroll1.config(foreground='#00FFCB',background='black',insertbackground='#A000FF')
    scroll1.focus()
    wndw_menu.mainloop()

window_mainMenu()