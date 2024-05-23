cafe_menu = {'1':60,'2':65,'3':75,'4':75,'5':60}
#1=americano,2=espresso,3=latte,4=mocha,5=greentea
print('********************โปรแกรมคำนวณค่ากาแฟ by Denchai********************')
print('กรุณาใส่เป็นตัวเลขเท่านั้น!!!')
try:
    menu = input('คุณต้องการดื่มเมนูไหนครับ 1=americano,2=espresso,3=latte,4=mocha,5=greentea: ')
    quatity = int(input('ต้องการกี่แก้วดีครับ: '))
    pay = int(input('รับเงินจากคุณมา: '))
except:
    print('กรุณาใส่เป็นตัวเลขเท่านั้น!!!')
    menu = input('คุณต้องการดื่มเมนูไหนครับ 1=americano,2=espresso,3=latte,4=mocha,5=greentea: ')
    quatity = int(input('ต้องการกี่แก้วดีครับ: '))
    pay = int(input('รับเงินจากคุณมา: '))
total_price = cafe_menu[menu]* quatity
remain_money = pay-total_price
print('***************************Calculating****************************')
print(f'คุณสั่ง: {menu}')
print('จำนวน: {} แก้ว'.format(quatity))
print('คุณต้องจ่ายเงินทั้งสิ้น: {} บาท'.format(total_price))
print('ได้รับเงินจากคุณมา: {} บาท และถอนเงินให้คุณเป็นจำนวน: {} บาท ครับ'.format(pay,remain_money))
print('ขอบคุณที่ใช้บริการครับ')
