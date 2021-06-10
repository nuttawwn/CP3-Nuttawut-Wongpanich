system_menu = {"ข้าวหมกไก่": 45 ,"ข้าวมันไก่": 35 ,"ข้าวมันไก่ทอด": 35 ,"ข้าวมันไก่(ผสม)": 45 ,
               "ข้าวขาหมู": 50 ,"ข้าวหมูแดง": 40 ,"ข้าวหมูกรอบ": 40 ,"ข้าวคลุกกะปิ": 50 ,"ข้าวหมูทอด่": 50 }
list_menu =[]
def showBill():
    food = "My New Food Order"
    print(food.center(50,"-"))
    total_price = 0
    for l in range(len(list_menu)) :
        print((l+1),"รายการอาหารที่เพิ่่มคือ",(list_menu[l][0]),"จำนวนราคาของอาหาร",(list_menu[l][1]),"บาท")
        total_price += (list_menu[l][1])

    print("\nจำนวนสินค้าทั้งหมดเป็น",(l+1),"รายการ","รวมเป็นจำนวนเงินทั้งหมด",total_price,"บาท")



print("รายการอาหารทีคุณ่ต้องการ")
order = (system_menu.keys())
print("รายการที่มี",order)
print("พิมพ์รายการที่ต้องการหากต้องการหยุดเพิ่มรายการให้พิมพ์คำว่า Exit หรือ ออก ")
while True :
    menu_name =  input("ใส่ชื่อรายการอาหารที่ต้องการ//หากต้องการหยุดให้พิมพ์คำว่า ออก  : ")
    if(menu_name.lower() == "exit") or (menu_name == "ออก") :
        break
    else :
        list_menu.append([menu_name,system_menu[menu_name]])

showBill()