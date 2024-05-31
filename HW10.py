from tkinter import * #import all function inside main package
from tkinter import ttk, messagebox #import sub package of tkinter that look beautify than tkinter
import csv
import os

path = os.getcwd()

noteicon = os.path.join(path ,'note_icon.ico')

"""Program"""
def writecsv(data):
    #data = ['john' ,14 ,500]
    csvfile = os.path.join(path ,'Test.csv')
    with open(csvfile ,'a' ,newline='' ,encoding='utf-8') as file:
        #mode w = writerows a = append
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมจดบันทึก By Denchai R.')
GUI.geometry('500x500')
GUI.iconbitmap(noteicon)

#grid,pack,place are command for create widget

#pack is command to create widget

#place is command to create widget but assign point in X,Y position
#E1.place(x=300,y=300)

#สร้าง flame
F1 = Frame(GUI)
F1.place(x=20 ,y=50)

#Build main lable
L1 = ttk.Label(F1, text='หัวข้อความรู้', font=('Angsana New',18))
L1.pack()

v_title = StringVar()

#Build main box
E1 = ttk.Entry(F1 ,textvariable=v_title ,font=('Angsana New',20) ,width=50)
E1.pack()

#Build sub lable
L2 = ttk.Label(F1, text='รายละเอียด', font=('Angsana New',18))
L2.pack()

#Build sub box
T1 =Text(F1, font=('Angsana New',18) ,height=8 ,width=56)
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
B1 = ttk.Button(F1 ,text='บันทึก' ,command = save)
B1.pack(pady=10 ,ipadx=20 ,ipady=10)

####################BUTTON FLASHCARD#############################
def readcsv():
    with open('Test.csv' ,newline='' ,encoding='utf-8') as file:
        fr = csv.reader(file) # fw = file read
        data = list(fr)
        return data

# list = readcsv()
try:
    list = readcsv()
except:
    messagebox.showinfo('ไม่มีข้อมูล','ไม่เจอไฟล์ CSV กรุณาบันทึกข้อมูล')

global countindex
countindex = 0

def Flashcard():
    list = readcsv()

    GUI2 = Toplevel()
    GUI2.title('ทบทวนความรู้')
    GUI2.geometry('500x400')

    vtext_title = StringVar()
    vtext_detail = StringVar()
    title = ttk.Label(GUI2 ,textvariable=vtext_title ,font = ('Angsana New' ,20 ,'bold'))
    title.pack()
    vtext_title.set(list[0][0])
    detail = ttk.Label(GUI2 ,textvariable=vtext_detail ,font = ('Angsana New' ,18))
    detail.pack()
    vtext_detail.set(list[0][1].replace('\r',''))

    def Prev():
        global countindex
        if countindex == 0 :
            countindex = countindex
        else:
            countindex = countindex - 1
        #set text
        vtext_title.set(list[countindex][0])
        vtext_detail.set(list[countindex][1].replace('\r',''))

    BPrev = ttk.Button(GUI2,text='<',command=Prev)
    BPrev.place(x=170,y=350)

    def Next():
        #[a,b,c,d] len()
        global countindex
        if countindex == (len(list)-1) :
            countindex = len(list)-1
        else:
            countindex = countindex + 1
        #set text
        vtext_title.set(list[countindex][0])
        vtext_detail.set(list[countindex][1].replace('\r',''))
    
    BNext = ttk.Button(GUI2,text='>',command=Next)
    BNext.place(x=250,y=350)

    GUI2.mainloop()

notebutton = os.path.join(path, 'note_png_48.png')
notebutton = PhotoImage(file=notebutton)
BFlashcard = ttk.Button(GUI ,image=notebutton,command=Flashcard)             
BFlashcard.place(x=440 ,y=20)

GUI.mainloop()