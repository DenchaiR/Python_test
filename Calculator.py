from tkinter import *
from tkinter import ttk, messagebox
import os
import sys
import webbrowser

GUI = Tk()
GUI.title('Calculator V.0.1')
GUI.geometry('800x800')

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
FONT3 = ('Angsana New', 30, 'bold')

#############Dropdown#######################
menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Exit',command=GUI.quit)
menubar.add_cascade(label='File',menu=filemenu)

mathmenu = Menu(menubar,tearoff=0)
mathmenu.add_command(label='คำนวณความหนาแน่นเหล็ก')
mathmenu.add_command(label='คำนวณพื้นที่สามเหลี่ยม')
mathmenu.add_command(label='ตารางเหล็ก')

menubar.add_cascade(label='Calculate',menu=mathmenu)

def Contact():
    url = 'https://www.facebook.com/denchai.tog/'
    webbrowser.open(url)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label='ติดต่อเรา',command=Contact)
menubar.add_cascade(label='Help',menu=helpmenu)
################TAB#################
# Tab
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

Tab.pack(fill=BOTH, expand=1)

img_T1 = PhotoImage(file='T1.png')
img_T2 = PhotoImage(file='T2.png')
img_T3 = PhotoImage(file='T3.png')

Tab.add(T1, text='คำนวณพื้นที่วงกลม',image=img_T1,compound='left')
Tab.add(T2, text='คำนวณพื้นที่ปริมาตร',image=img_T2,compound='left')
Tab.add(T3, text='Help',image=img_T3,compound='left')
# Tab1
L = ttk.Label(T1, text='กรุณากรอกรัศมีวงกลม (เมตร)', font=FONT2)
L.pack(pady=10)

v_radius = StringVar()

E1 = ttk.Entry(T1, textvariable=v_radius, font=FONT1)
E1.pack(pady=20)
E1.focus()

def Calculate(event=None):
    try:
        unit = 'ตร.ม.'
        radius = float(v_radius.get())
        pi = 3.146
        calc = pi * (radius**2)
        text = 'วงกลมรัศมี: {} (เมตร) มีพื้นที่ทั้งหมด {:,.2f} {}'.format(radius, calc, unit)
        print(text)
        v_result.set(text)
        v_radius.set('')
    except ValueError:
        messagebox.showwarning('กรอกตัวเลข', 'กรอกตัวเลขเท่านั้น')
        v_radius.set('')
        E1.focus()

B1 = ttk.Button(T1, text='Calculate', command=Calculate)
B1.pack(ipadx=20, ipady=10)

E1.bind('<Return>', Calculate)

v_result = StringVar()
v_result.set('-------ผลลัพธ์-------')
R1 = ttk.Label(T1, textvariable=v_result, font=FONT3, foreground='green')
R1.pack(pady=20)

# Tab2
img = PhotoImage(file=resource_path('cube.png'))  # Correctly load the image
cube_img = ttk.Label(T2, image=img)
cube_img.pack()

L = ttk.Label(T2, text='กรุณากรอกขนาดระยะของลูกบาตร (เมตร)', font=FONT2)
L.pack(pady=10)

FTB = Frame(T2)  # Frame of table
FTB.pack()

v_cube1 = StringVar()
v_cube2 = StringVar()
v_cube3 = StringVar()

L1 = ttk.Label(FTB, text='กว้าง', font=FONT1)
L1.grid(row=0, column=0, pady=10, padx=10)
ET21 = ttk.Entry(FTB, textvariable=v_cube1, font=FONT1,width=10)
ET21.grid(row=0, column=1, pady=10)

L2 = ttk.Label(FTB, text='ยาว', font=FONT1)
L2.grid(row=1, column=0, pady=10, padx=10)
ET22 = ttk.Entry(FTB, textvariable=v_cube2, font=FONT1,width=10)
ET22.grid(row=1, column=1, pady=10)

L3 = ttk.Label(FTB, text='สูง', font=FONT1)
L3.grid(row=2, column=0, pady=10, padx=10)
ET23 = ttk.Entry(FTB, textvariable=v_cube3, font=FONT1,width=10)
ET23.grid(row=2, column=1, pady=10)

def Calculatecube(event=None):
    try:
        v1 = float(v_cube1.get())
        v2 = float(v_cube2.get())
        v3 = float(v_cube3.get())
        calc = v1*v2*v3
        text = 'ปริมาตรทั้งหมด({}x{}x{}) ทั้งหมด : {:,.3f} ลบ.ม.'.format(v1,v2,v3,calc)
        v_result2.set(text)
    except ValueError:
        messagebox.showwarning('กรอกตัวเลข', 'กรอกตัวเลขเท่านั้น')
        v_cube1.set('')
        v_cube2.set('')
        v_cube3.set('')
        E1.focus()    

B2 = ttk.Button(T2, text='คำนวณ', command=Calculatecube)
B2.pack(ipadx=20, ipady=10) 

ET21.bind('<Return>',lambda x:ET22.focus())
ET22.bind('<Return>',lambda x:ET23.focus())
ET23.bind('<Return>',Calculatecube)

v_result2 = StringVar()
v_result2.set('-------ผลลัพธ์-------')
R2 = ttk.Label(T2, textvariable=v_result2, font=FONT3, foreground='green')
R2.pack(pady=20)

# Tab3
FL = Frame(T3)
FL.place(x=300,y=250)

L = ttk.Label(FL, text='สนในพัฒนาต่อ ติดต่อ', font=FONT2)
L.pack(pady=10)
L = ttk.Label(FL, text='FB:Denchai Rattanapaiboon', font=FONT2)
L.pack(pady=10)

GUI.mainloop()