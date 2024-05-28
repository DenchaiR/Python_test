from tkinter import * #import all function inside main package
from tkinter import ttk #import sub package of tkinter that look beautify than tkinter
import csv

"""Program"""
def writecsv(data):
    #data = ['john' ,14 ,500]
    with open('Test.csv' ,'a' ,newline='' ,encoding='utf-8') as file:
        #mode w = writerows a = append
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมจดบันทึก By Denchai R.')
GUI.geometry('500x500')

#grid,pack,place are command for create widget

#pack is command to create widget

#place is command to create widget but assign point in X,Y position
#E1.place(x=300,y=300)

#Build main lable
L1 = ttk.Label(GUI, text='หัวข้อความรู้', font=('Angsana New',18))
L1.pack()

v_title = StringVar()

#Build main box
E1 = ttk.Entry(GUI ,textvariable=v_title ,font=('Angsana New',20) ,width=50)
E1.pack()

#Build sub lable
L2 = ttk.Label(GUI, text='รายละเอียด', font=('Angsana New',18))
L2.pack()

#Build sub box
T1 =Text(GUI, font=('Angsana New',18) ,height=8 ,width=56)
T1.pack()

def save():
    title = v_title.get()
    textbox = T1.get(1.0 ,"end-1c")
    print('----------')
    print(title)
    print('----------')
    print(textbox)
    print('----------')
    data = [title, textbox]
    writecsv(data)
    v_title.set('') # clear data after save
    T1.delete('1.0' ,END) # claer text box

#build button
B1 = ttk.Button(GUI ,text='บันทึก' ,command = save)
B1.pack(pady=10 ,ipadx=20 ,ipady=10)

GUI.mainloop()
