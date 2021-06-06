print("ยินดีต้องรับเข้าสู่ระบบ")
print("กรูณาป้อนข้อมูลรหัสผู้ใช้งาน")

un = input("Username : ")
pw = input("Password : ")
while un != "admin" and pw != "1234" :
    if un != "admin" and pw != "1234" :
        print("รหัสผู้ใช้และรหัสผ่านไม่ถูกต้อง")
        print("กรุณาป้อนรหัสอีกครั้ง")
        un = input("Username : ")
        pw = input("Password : ")
    elif   un == "admin" or pw != "1234" :
        print("รหัสผู้ใช้และไม่ถูกต้อง")
        print("กรุณาป้อนรหัสอีกครั้ง")
        un = input("Username : ")
        pw = input("Password : ")
    elif   un != "admin" or pw == "1234" :
        print("รหัสผู้ใช้ไม่ถูกต้อง")
        print("กรุณาป้อนรหัสอีกครั้ง")
        un = input("Username : ")
        pw = input("Password : ")

print("เข้าสู่ระบบเรียบร้อยแล้ว")
