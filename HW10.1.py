import ttkbootstrap as ttk  # ใช้ ttkbootstrap แทน ttk
from ttkbootstrap.constants import *
from tkinter import *
import csv
import os

path = os.getcwd()

noteicon = os.path.join(path, 'note_icon.ico')

# โปรแกรมสำหรับคำนวณยอดผ่อนบัตรเครดิตต่อเดือนโดยที่จ่ายเต็มจำนวนทุกเดือน
def cal_credit_interest(price, month, interest=0.0069):
    if month <= 3:
        interest = 0  # ผ่อน 0% สำหรับการผ่อน 3 เดือนหรือน้อยกว่า
    monthly_payment = (price / month) + (price * interest)
    total_payment = monthly_payment * month
    result = (
        f'-หลังจากทำผ่อนแล้วคุณต้องชำระเป็นจำนวนเงินทั้งหมด: {total_payment:.2f} บาท\n'
        f'-คุณต้องชำระค่าดอกเบี้ยทั้งหมด: {total_payment - price:.2f} บาท\n'
        f'-คุณต้องชำระเงินต่อเดือนเป็นจำนวนทั้งหมด: {monthly_payment:.2f} บาทต่อเดือน'
    )
    return result

def calculate_and_save():
    try:
        price = float(E2.get())
        month = int(E3.get())
        result = cal_credit_interest(price, month)
        
        # บันทึกข้อมูลลงในไฟล์ CSV
        with open('credit_payment.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([price, month, result])
        
        result_label.delete(1.0, END)  # ลบข้อมูลทั้งหมดที่อยู่ใน Text widget
        result_label.insert(END, result)  # เพิ่มข้อความใหม่เข้าไปใน Text widget
        result_label.insert(END, "\n\nข้อมูลถูกบันทึกลงในไฟล์ credit_payment.csv เรียบร้อยแล้ว")
        
        # แสดงข้อมูลใน Terminal
        print(f'จำนวนเงินที่ต้องการผ่อน: {price} บาท')
        print(f'จำนวนเดือนที่ต้องการผ่อน: {month} เดือน')
        print('----------')
        print(result)
        print('----------')
        
    except ValueError:
        result_label.delete(1.0, END)
        result_label.insert(END, "กรุณากรอกข้อมูลให้ถูกต้อง")

# หน้าต่างของการใช้งาน GUI
GUI = ttk.Window(themename='darkly')  # สร้างหน้าต่าง GUI พร้อมกำหนดธีม
GUI.title('โปรแกรมคำนวณยอดผ่อนบัตรเครดิต By Denchai R.')
GUI.geometry('300x720')
GUI.iconbitmap(noteicon)  # ตั้งค่าไอคอนที่นี่

# Build main label
L1 = ttk.Label(GUI, text='โปรแกรมคำนวณยอดผ่อนบัตรเครดิต', font=('Angsana New', 20))
L1.pack()
L1_1 = ttk.Label(GUI, text='By Denchai R.', font=('Angsana New', 20))
L1_1.pack()
L1_1.pack(pady=10)

# Build sub label 4
L4 = ttk.Label(GUI, text='ดูประวัติ', font=('Angsana New', 18))
L4.pack(pady=2)

####################BUTTON FLASHCARD#############################
def readcsv():
    with open('credit_payment.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file)  # fw = file read
        data = list(fr)
        return data

flashcard_list = readcsv()

global countindex
countindex = 0

def Flashcard():
    flashcard_list = readcsv()

    GUI2 = Toplevel()
    GUI2.title('ประวัติ')
    GUI2.geometry('500x400')

    vtext_title = StringVar()
    vtext_subtitle = StringVar()
    vtext_detail = StringVar()
    title = ttk.Label(GUI2, textvariable=vtext_title, font=('Angsana New', 20, 'bold'))
    title.pack()
    vtext_title.set(flashcard_list[0][0])
    subtitle = ttk.Label(GUI2, textvariable=vtext_subtitle, font=('Angsana New', 20, 'bold'))
    subtitle.pack()
    vtext_subtitle.set(flashcard_list[0][1].replace('\r', ''))
    detail = ttk.Label(GUI2, textvariable=vtext_detail, font=('Angsana New', 18))
    detail.pack()
    vtext_detail.set(flashcard_list[0][2].replace('\r', ''))

    def Prev():
        global countindex
        if countindex == 0:
            countindex = countindex
        else:
            countindex = countindex - 1
        # set text
        vtext_title.set(flashcard_list[countindex][0])
        vtext_subtitle.set(flashcard_list[countindex][1].replace('\r', ''))
        vtext_detail.set(flashcard_list[countindex][2].replace('\r', ''))

    BPrev = ttk.Button(GUI2, text='<', command=Prev)
    BPrev.place(x=210, y=350)

    def Next():
        global countindex
        if countindex == (len(flashcard_list) - 1):
            countindex = len(flashcard_list) - 1
        else:
            countindex = countindex + 1
        # set text
        vtext_title.set(flashcard_list[countindex][0])
        vtext_subtitle.set(flashcard_list[countindex][1].replace('\r', ''))
        vtext_detail.set(flashcard_list[countindex][2].replace('\r', ''))
    
    BNext = ttk.Button(GUI2, text='>', command=Next)
    BNext.place(x=260, y=350)

    GUI2.mainloop()

notebutton = os.path.join(path, 'note_png_48.png')
notebutton = PhotoImage(file=notebutton)
BFlashcard = ttk.Button(GUI, image=notebutton, command=Flashcard)             
BFlashcard.pack()

# Build sub label 1
L2 = ttk.Label(GUI, text='จำนวนเงินที่ต้องการผ่อน', font=('Angsana New', 18))
L2.pack(pady=2)

# Build sub box 1
E2 = ttk.Entry(GUI, font=('Angsana New', 18), width=30)
E2.pack(pady=2)

# Build sub label 2
L3 = ttk.Label(GUI, text='จำนวนเดือนที่ต้องการผ่อน', font=('Angsana New', 18))
L3.pack(pady=2)

# Build sub box 2
E3 = ttk.Entry(GUI, font=('Angsana New', 18), width=30)
E3.pack(pady=2)

# Build button with custom style
B1 = ttk.Button(GUI, text='คำนวณ', style='TButton', command=calculate_and_save)
B1.pack(pady=10, ipadx=20, ipady=10)

# Build result label
L4 = ttk.Label(GUI, text='ผลลัพธ์', font=('Angsana New', 18))
L4.pack(pady=2)

# Build result box 
result_label = Text(GUI, font=('Angsana New', 18), wrap=WORD, height=6, width=30)
result_label.pack(pady=2)

GUI.mainloop()
