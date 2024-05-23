def drink(menu, money, menu_cafe):
    if menu in menu_cafe and money >= 60:
        print('คุณสามารถซื้อกาแฟ {} ได้ และจะทอนเงิน {} บาท'.format(menu, money - 60))
        print('ขอบคุณที่มาอุดหนุนครับ/ค่ะ')
    elif menu not in menu_cafe and money < 60:
        print('คุณไม่สามารถซื้อกาแฟ {} ได้ เนื่องจากขาดเงินอีก {} บาท'.format(menu, 60 - money))
        print('ขอบคุณที่มาอุดหนุนครับ/ค่ะ')
    elif menu not in menu_cafe:
        print('ไม่มีเมนูที่คุณเลือก กรุณาเลือกเมนูจากรายการที่มี')
        print('ขอบคุณที่มาอุดหนุนครับ/ค่ะ')
    else:
        print('คุณไม่สามารถซื้อกาแฟ {} ได้ เนื่องจากขาดเงินอีก {} บาท'.format(menu, 60 - money))
        print('ขอบคุณที่มาอุดหนุนครับ/ค่ะ')

print('------------ยินดีต้องรับสู่โปรแกรมขายกาแฟอัตโนมัติ-------------')
menu_cafe = ['americano', 'espresso', 'cappuccino']  # ประกาศตัวแปรเมนูที่นี่
while True:
    print('------------กรุณาพิมพ์เมนูที่ต้องการ-----------')
    print('เมนูทั้งหมดในร้านกาแฟ:')
    for item in menu_cafe:
        print(item)
    try:
        menu = input('เมนูที่ต้องการดื่ม: ')
        money = int(input('รับเงินจากคุณมาเป็นจำนวนเงิน: '))
    except ValueError:
        print('กรุณาป้อนตัวเลขที่ถูกต้อง')
        continue
    
    print('--------------------กำลังคำนวณ------------------')
    drink(menu, money, menu_cafe)
    break