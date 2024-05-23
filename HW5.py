product = {
    1: {'ชื่อกาแฟ': '1.Americano', 'ราคา': 60},
    2: {'ชื่อกาแฟ': '2.Espresso', 'ราคา': 60},
    3: {'ชื่อกาแฟ': '3.Latte', 'ราคา': 70},
    4: {'ชื่อกาแฟ': '4.Mocha', 'ราคา': 70},
    5: {'ชื่อกาแฟ': '5.Green Tea', 'ราคา': 55},
}

# แสดงเมนูทั้งหมดของร้าน Denchai Cafe 
for item_number, details in product.items():
    print(f"{details['ชื่อกาแฟ']}: {details['ราคา']} บาท")

total_amount = 0  # ตัวแปรสำหรับสะสมยอดรวมทั้งหมด

while True:
    print('------------กรุณาพิมพ์เลขเมนูกาแฟที่ต้องการ-----------')
    
    try:
        p = int(input('เลขเมนูที่ต้องการ: '))
        q = int(input('จำนวนกี่แก้ว: '))
    except ValueError:
        print('กรุณาป้อนตัวเลขที่ถูกต้อง')
        continue
    
    print('--------------------กำลังคำนวณ------------------')
    
    if p in product:
        print(f'เลขเมนู: {p} \nคือเมนู: {product[p]["ชื่อกาแฟ"]} \nราคา: {product[p]["ราคา"]}')
        item_total = product[p]['ราคา'] * q
        total_amount += item_total
        print(f'จำนวน: {q} แก้ว\nรวมทั้งหมด: {item_total} บาท')
    else:
        print('ไม่มีเมนูนี้ในระบบ')
    
    # ถามลูกค้าว่าต้องการสั่งเพิ่มหรือไม่
    more = input('คุณต้องการสั่งเพิ่มอีกหรือไม่? (รับ/ไม่รับ): ')
    if more.strip().lower() != 'รับ':
        break

print('ยอดรวมทั้งหมดที่ต้องชำระ:', total_amount, 'บาท')
print('ขอบคุณที่มาใช้บริการร้าน Denchai Cafe ครับ')