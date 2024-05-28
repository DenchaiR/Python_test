import ttkbootstrap as ttk  # ใช้ ttkbootstrap แทน ttk
from ttkbootstrap.constants import *
from tkinter import *
import csv

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

def calculate():
    try:
        price = float(E2.get())
        month = int(E3.get())
        result = cal_credit_interest(price, month)
        result_label.delete(1.0, END)  # ลบข้อมูลทั้งหมดที่อยู่ใน Text widget
        result_label.insert(END, result)  # เพิ่มข้อความใหม่เข้าไปใน Text widget
        
    except ValueError:
        result_label.delete(1.0, END)  # ลบข้อมูลทั้งหมดที่อยู่ใน Text widget
        result_label.insert(END, "กรุณากรอกข้อมูลให้ถูกต้อง")

def save():
    try:
        price = float(E2.get())
        month = int(E3.get())
        result = cal_credit_interest(price, month)
        
        # บันทึกข้อมูลลงในไฟล์ CSV
        with open('credit_payment.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([price, month, result])
        
        result_label.delete(1.0, END)
        result_label.insert(END, "ข้อมูลถูกบันทึกลงในไฟล์ credit_payment.csv เรียบร้อยแล้ว")

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
GUI.geometry('300x700')

# Build main label
L1 = ttk.Label(GUI, text='โปรแกรมคำนวณยอดผ่อนบัตรเครดิต', font=('Angsana New', 20))
L1.pack()
L1_1 = ttk.Label(GUI, text='By Denchai R.', font=('Angsana New', 20))
L1_1.pack()
L1_1.pack(pady=10)

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
B1 = ttk.Button(GUI, text='คำนวณ', style='TButton', command=calculate)
B1.pack(pady=10, ipadx=20, ipady=10)

# Add save button
B2 = ttk.Button(GUI, text='บันทึก', style='TButton', command=save)
B2.pack(pady=10, ipadx=20, ipady=10)

# Build result label
L4 = ttk.Label(GUI, text='ผลลัพธ์', font=('Angsana New', 18))
L4.pack(pady=2)

# Build result box 
result_label = Text(GUI, font=('Angsana New', 18), wrap=WORD, height=8, width=30)
result_label.pack(pady=2)

GUI.mainloop()
