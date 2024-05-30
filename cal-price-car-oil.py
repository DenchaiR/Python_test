import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        distance = float(entry_distance.get())
        efficiency = float(entry_efficiency.get())
        price = float(entry_price.get())
        
        if distance < 0 or efficiency <= 0 or price < 0:
            raise ValueError("ค่าต้องเป็นบวกเท่านั้น")

        fuel_needed = distance / efficiency
        total_cost = fuel_needed * price

        label_result.config(text=f"จำนวนเงินที่ต้องเติมน้ำมัน: {total_cost:.2f} บาท")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนค่าที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณค่าน้ำมัน")

# สร้างและจัดวางเลเบลและเอนทรีสำหรับระยะทาง
label_distance = tk.Label(root, text="ระยะทาง (กิโลเมตร):")
label_distance.grid(row=0, column=0, padx=10, pady=10)

entry_distance = tk.Entry(root)
entry_distance.grid(row=0, column=1, padx=10, pady=10)

# สร้างและจัดวางเลเบลและเอนทรีสำหรับอัตราสิ้นเปลือง
label_efficiency = tk.Label(root, text="อัตราสิ้นเปลือง (กม./ลิตร):")
label_efficiency.grid(row=1, column=0, padx=10, pady=10)

entry_efficiency = tk.Entry(root)
entry_efficiency.grid(row=1, column=1, padx=10, pady=10)

# สร้างและจัดวางเลเบลและเอนทรีสำหรับราคาน้ำมัน
label_price = tk.Label(root, text="ราคาน้ำมัน (บาท/ลิตร):")
label_price.grid(row=2, column=0, padx=10, pady=10)

entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1, padx=10, pady=10)

# สร้างและจัดวางปุ่มคำนวณ
button_calculate = tk.Button(root, text="คำนวณ", command=calculate)
button_calculate.grid(row=3, columnspan=2, pady=20)

# สร้างและจัดวางเลเบลสำหรับแสดงผลลัพธ์
label_result = tk.Label(root, text="จำนวนเงินที่ต้องเติมน้ำมัน: ")
label_result.grid(row=4, columnspan=2, pady=10)

# เริ่มต้นโปรแกรม GUI
root.mainloop()
