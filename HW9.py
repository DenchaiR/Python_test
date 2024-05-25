"""Cafe class สำหรับระบุเมนูในร้าน"""
class Cafe:
    #Attribute
    cafeName = 'Denchai Cafe'

    #Constructor
    def __init__(self, manu, price) :
        self.manu = manu
        self.price = price

    #Method
    def hello(self):
        print('===================สรุปการสั่งเครื่องดื่ม====================')

"""Customer class สำหรับเป็นลูกค้าของร้าน"""
class Customer(Cafe):
    def __init__(self, name, manu, price, orders, money):
        super().__init__(manu, price)
        self.name = name
        self.orders = orders
        self.money = money
    def buyCoffee(self):
        #คำนวณค่ากาแฟ
        self.total = self.price * self.orders
       
        #รับเงินมา
        self.money1 = self.money

        #เงินทอน
        self.money -= self.total

        print(f'ชื่อลูกค้า : {self.name}')
        print(f'สั่งเมนู : {self.manu}')
        print(f'ราคา : {self.price} บาท')
        print(f'จำนวน : {self.orders} แก้ว')
        print(f'รับเงินมาจำนวน : {self.money1} บาท')
        print(f'รวมเงินที่ต้องจ่ายทั้งสิ้น : {self.total} บาท')
        print(f'ทอนเงินให้ลูกค้าจำนวน : {self.money} บาท')

# """ทดสอบโปรแกรม"""
# customer01 = Customer('A' , 'Americano', 60, 2, 200)
# print(customer01.cafeName)
# customer01.hello()
# customer01.buyCoffee()
# print('==================================================')
# customer02 = Customer('B' , 'Espresso', 60, 1, 100)
# print(customer02.cafeName)
# customer02.hello()
# customer02.buyCoffee()
# print('==================================================')
# customer03 = Customer('C' , 'Latte', 70, 3, 300)
# print(customer03.cafeName)
# customer03.hello()
# customer03.buyCoffee()
# print('==================================================')
# customer04 = Customer('D' , 'Mocha', 70, 5, 400)
# print(customer04.cafeName)
# customer04.hello()
# customer04.buyCoffee()
# print('==================================================')
# customer05 = Customer('E' , 'Green_tea', 55, 4, 300)
# print(customer05.cafeName)
# customer05.hello()
# customer05.buyCoffee()

"""เมนูในร้าน"""
menu = {
    "Americano": 60,
    "Espresso": 60,
    "Latte": 70,
    "Mocha": 70,
    "Green tea": 55
}

"""แสดงเมนูและราคาของเมนูทั้งหมด"""
print('===============ยินดีต้อนรับสู่ Denchai Cafe================')
print("เมนูในร้าน:")
for item, price in menu.items():
    print(f"{item}: {price} บาท")

"""รับข้อมูลจากผู้ใช้"""
name = input("กรุณาใส่ชื่อลูกค้า: ")
menu_item = input("กรุณาใส่ชื่อเมนูที่ต้องการ (Americano, Espresso, Latte, Mocha, Green tea): ")
quantity = int(input("กรุณาใส่จำนวนที่ต้องการ: "))
money_input = int(input("กรุณาใส่จำนวนเงินที่ลูกค้าชำระ: "))

"""รับ input จาก User"""
customer01 = Customer(name, menu_item, menu[menu_item], quantity, money_input)
customer01.hello()
customer01.buyCoffee()
print('===============ขอบคุณที่มาอุดหนุนครับ/ค่ะ================')