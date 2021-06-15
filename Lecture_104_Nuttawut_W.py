class Customer:
    name = ""
    last = ""
    age = 0

    def add_cart (self):
        print("Add product ",self.name,self.last,"'s store")
#ลูกค้าคนที่ 1
customer_1 = Customer()
customer_1.name = "Nuttawut"
customer_1.last = "Wongpanich"
customer_1.add_cart()

#ลูกค้าคนที่ 2
customer_2 = Customer()
customer_2.name = "Arnon"
customer_2.last = "Sritong"
customer_2.add_cart()

#ลูกค้าคนที่ 3
customer_3 = Customer()
customer_3.name = "Gatechai"
customer_3.last = "Porntilagul"
customer_3.add_cart()

#ลูกค้าคนที่ 4
customer_4 = Customer()
customer_4.name = "Jirapongtorn"
customer_4.last = "Wongpanich"
customer_4.add_cart()
