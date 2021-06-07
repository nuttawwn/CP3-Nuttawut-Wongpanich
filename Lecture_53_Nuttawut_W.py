def vat_calculate (total_price):
    result = total_price + (total_price * (7/100))
    return int(result) #ด้านหลัง Return คือข้อมูล
print("โปรแกรมคำนวณภาษี")
total_price = int(input("ใส่จำนวนจำนวนเงิน : "))
print(vat_calculate(total_price),"บาท")