def Title_menu (): #ส่วนไตเติ้ลเมนู
    print("ยินดีต้องรับเข้าสู่ระบบ")
    print("กรูณาป้อนข้อมูลรหัสผู้ใช้งาน")
    return login()

def login(): #ส่วน Login user
    un = input("Username : ")
    pw = input("Password : ")
    if un == "admin" and pw == "1234":
        return show_menu()
    else:
        return wrong()

def wrong (): #ส่วนใส่รหัสไม่ถูก
    print("ใส่รหัสผ่านไม่ถูกต้อง กรุณาใส่อีกครั้ง")
    return login()

def show_menu (): #ส่วนแสดงเมนู
    print("กรุณาเลือกระบบงานที่ต้องการทำงาน")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    return select_menu()

def select_menu (): #ส่วนเลือกเมนู
    job = input("กรุณาเลือกโปแกรมที่ต้องการ  : ")
    if job == "1" :
        print("You chose the '1.Vat Calculator' ")
        total_price = int(input("ใส่จำนวนเงิน :" ))
        return vatCalculate (total_price)
    elif job == "2" :
        print("You chose the '2.Price Calculator' ")
        return priceCalculate ()
    elif job == "exit" :
        exit()

    else:
        return wrong_menu ()

def vatCalculate (total_price): #เมนูที่ 1
    vat = 7
    result = total_price + (total_price * vat / 100)
    print("จำนวนเงินทั้งหมด",int(result),"บาท")
    return exit_programe()

def priceCalculate (): #เมนูที่ 2
    price_1 = int(input("ราคาสินค้าชิ้นที่ 1  : "))
    price_2 = int(input("ราคาสินค้าชิ้นที่ 2  : "))
    return vatCalculate( price_1 + price_2)

def wrong_menu (): #เลือกผิดเมนู
    print("คุณเลือกเมนูไม่ถูกต้อง")
    return select_menu ()

def exit_programe ():#ออกจากโปรแกรม
    print("คุณต้องการใช้งานต่อมั้ย")
    print("หากต้องการเล่นต่อพิมพ์ Y และหากไม่ต้องหารใช้งานต่อพิมพ์ N และหากต้องการเปลี่ยนรหัสผู้ใช้งานให้พิมพ์ C")
    print("แลหากต้องการเปลี่ยนรหัสผู้ใช้งานให้พิมพ์ C")
    ans = input("Y/N or C: ")
    if ans == "Y" or ans == "y" :
        return show_menu()
    elif ans == "N" or ans == "n" :
        exit()
    elif ans == "C" or ans == "c" :
        return Title_menu()
    else:
        print("คุณเลือกเมนูไม่ถูกต้อง")
        return exit_programe()


print(Title_menu())
