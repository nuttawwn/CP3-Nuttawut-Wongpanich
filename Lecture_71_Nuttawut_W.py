list_menu =[]
list_menu_price =[]
def showBill():
    food = "My New Food Order"
    print(food.center(50,"-"))
    for l in range(len(list_menu)) :
        print((l+1),"รายการอาหารที่เพิ่่มคือ",(list_menu[l]),"จำนวนราคาของอาหาร",(list_menu_price[l]),"บาท")

    total_price = sum(list_menu_price[0:(l+1)])
    print("\nจำนวนสินค้าทั้งหมดเป็น",(l+1),"รายการ","รวมเป็ยจำนวนเงินทั้งหมด",total_price,"บาท")

print("โปรแกรมเพิ่มรายการอาหาร สามารถเพิ่มรายการอาหารลงไปได้เลย")
print("หากต้องการหยุดเพิ่มรายการให้พิมพ์คำว่า Exit หรือ ออก ")
while True :
    menu_name =  input("ใส่ชื่อรายการอาหารที่ต้องการ//หากต้องการหยุดให้พิมพ์คำว่า ออก  : ")
    if(menu_name.lower() == "exit") or (menu_name == "ออก") :
        break
    else :
        menu_price = int(input("Price : "))
        list_menu.append(menu_name)
        #list_menu.append(menu_price)
        list_menu_price.append(menu_price)
showBill()