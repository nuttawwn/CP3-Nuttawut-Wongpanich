def plus_number (num_1,num_2):
    print("โปรแกรมบวกเลข")
    print(num_1,"+", num_2,"=",(num_1 + num_2)  )


def minus_number (num_1,num_2):
    print("โปรแกรมลบเลข")
    print(num_1,"-", num_2,"=",(num_1 - num_2)  )


def multiply_number (num_1,num_2):
    print("โปรแกรมคูณเลข")
    print(num_1,"x", num_2,"=",(num_1 * num_2)  )

def divide_number (num_1,num_2):
    print("โปรแกรมหารเลข")
    print(num_1,"/", num_2,"=",(num_1 / num_2)  )


num_1 = int(input("โปรดระบุจำนวนที่ 1 : "))
num_2 = int(input("โปรดระบุจำนวนที่ 2 : "))

plus_number(num_1,num_2)
minus_number (num_1,num_2)
multiply_number (num_1,num_2)
divide_number (num_1,num_2)
