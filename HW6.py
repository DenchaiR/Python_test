def cal_credit_interest(price, month, interest=0.0069):
    """โปรแกรมสำหรับคำนวณยอดผ่อนบัตรเครดิตต่อเดือนโดยที่จ่ายเต็มจำนวนทุกเดือน"""
    if month <= 3:
        interest = 0  # ผ่อน 0% สำหรับการผ่อน 3 เดือนหรือน้อยกว่า
    monthly_payment = (price / month) + (price * interest)
    total_payment = monthly_payment * month
    print('หลังจากทำผ่อนแล้วคุณต้องชำระเป็นจำนวนเงินทั้งหมด: {:.2f} บาท'.format(total_payment))
    print('คุณต้องชำระค่าดอกเบี้ยทั้งหมด: {:.2f} บาท'.format(total_payment - price))
    print('คุณต้องชำระเงินต่อเดือนเป็นจำนวนทั้งหมด: {:.2f} บาทต่อเดือน'.format(monthly_payment))

print('------------ยินดีต้องรับสู่โปรแกรมทำผ่อนยอดบัตรเครดิต-------------')
print('------------ถ้าทำผ่อน 1-3 เดือน จะคิดดอกเบี้ย 0%---------------')
print('------------ถ้าทำผ่อน 4-10 เดือน จะคิดดอกเบี้ย 0.69%-----------')
while True:
    print('------------กรุณาพิมพ์รายการตามนี้-----------')
    
    try:
        price = int(input('ราคาสินค้าที่ต้องการผ่อน: '))
        month = int(input('จำนวนเดือนที่ต้องการผ่อน: '))
        print('--------------------กำลังคำนวณ------------------')
        cal_credit_interest(price, month)
        
        cont = input('คุณต้องการคำนวณอีกครั้งหรือไม่? (y/n): ')
        if cont.lower() != 'y':
            break
    except ValueError:
        print('กรุณาป้อนตัวเลขที่ถูกต้อง')
