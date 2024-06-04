from tkinter import *
from tkinter import ttk, messagebox
import os
import sys

GUI = Tk()
GUI.title('Calculator V.0.1')
GUI.geometry('500x300')

# Function to get the path to the icon file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Set the icon using the resource_path function
icon_path = resource_path('calculator_icon.ico')
GUI.iconbitmap(icon_path)

# Font
FONT1 = ('Impact', 30)
FONT2 = ('Angsana New', 20)

L = ttk.Label(GUI, text='กรุณากรอกรัศมีวงกลม (เมตร)', font=FONT2)
L.pack(pady=10)

v_radius = StringVar()

E1 = ttk.Entry(GUI, textvariable=v_radius, font=FONT1)
E1.pack(pady=20)
E1.focus()

def Calculate(event=None):
    try:
        unit = 'ตร.ม.'
        radius = float(v_radius.get())
        pi = 3.146
        calc = pi * (radius**2)
        text = 'วงกลมนี้มีพื้นที่ {:,.2f} {}'.format(calc, unit)
        print(text)
        v_result.set(text)
        v_radius.set('')
    except ValueError:
        messagebox.showwarning('กรอกตัวเลข', 'กรอกตัวเลขเท่านั้น')
        v_radius.set('')
        E1.focus()

B1 = ttk.Button(GUI, text='Calculate', command=Calculate)
B1.pack(ipadx=20, ipady=10)

E1.bind('<Return>', Calculate)

v_result = StringVar()
v_result.set('-------ผลลัพธ์-------')
R1 = ttk.Label(GUI, textvariable=v_result, font=FONT2, foreground='green')
R1.pack(pady=20)

GUI.mainloop()
