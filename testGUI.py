#!/usr/bin/python3

import tkinter as tk
from tkinter import colorchooser, messagebox

from matplotlib.backends.backend_tkagg import(
     FigureCanvasTkAgg, NavigationToolbar2Tk )
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


def newFile():
    print( colorchooser.askcolor( initialcolor="#ff0000" ) )
    
def openFile():
    messagebox.showinfo( message="Have a sparkling day!" )
    
def closeFile():
    if( messagebox.askyesno( message="Are you sure?", icon="question",
                                title="Are you kidding me??" ) ):
        mkMatPlotLibGrid()
           
def exitFile(): window.destroy()

def increase():
    val = int( lbl_value[ "text" ] )
    lbl_value[ "text" ] = f"{ val + 1 }"

def decrease():
    val = int( lbl_value[ "text" ] )
    lbl_value[ "text" ] = f"{ val - 1 }"

def mkMatPlotLibGrid():
    frame = tk.Frame( master=window )
    frame.grid( row=2, column=0, columnspan=3, sticky="nsew" )

    fig = Figure( figsize=( 5, 4 ), dpi=100 )
    t = np.arange( 0, 3, .01 )
    fig.add_subplot( 111 ).plot( t, 2 * np.sin( 2 * np.pi * t ) )

    canvas = FigureCanvasTkAgg( fig, master=frame )
    canvas.draw()

    toolbar = NavigationToolbar2Tk( canvas, frame )
    toolbar.update()

    canvas.get_tk_widget().pack( fill=tk.BOTH, expand=True )

window = tk.Tk()
window.option_add( '*tearOff', False )
window.title( "Increase / Decrease" )
window.rowconfigure( [ 0, 2 ], minsize=50, weight=1 )
window.columnconfigure( [ 0, 1, 2 ], minsize=50, weight=1 )

menubar = tk.Menu( window )
menu_file = tk.Menu( menubar )
menu_edit = tk.Menu( menubar )
menubar.add_cascade( menu=menu_file, label="File" )
menubar.add_cascade( menu=menu_edit, label="Edit" )

menu_file.add_command( label="Choose Color", command=newFile )
menu_file.add_separator()
menu_file.add_command( label="Message", command=openFile )
menu_file.add_separator()
menu_file.add_command( label="Grid", command=closeFile )
menu_file.add_separator()
menu_file.add_command( label="Exit", command=exitFile )

menu_edit.add_command( label="Grid", command=closeFile )

window[ "menu" ] = menubar

btn_decrease = tk.Button( window, text=" - ", command=decrease )
btn_decrease.grid( row=0, column=0, sticky="nsew" )

lbl_value = tk.Label( window, text="0" )
lbl_value.grid( row=0, column=1 )

btn_increase = tk.Button( window, text=" + ", command=increase )
btn_increase.grid( row=0, column=2, sticky="nsew" )

photo = tk.PhotoImage( file="./KEYBOARD.gif" )
lbl_picture = tk.Label( window, text="" )
lbl_picture[ "image" ] = photo
lbl_picture.grid( row=1, column=1 )

window.mainloop()

