print("Programe Pyramid")
number = int(input("Please input  count : "))
space = number
for x in range (number):
    space = space - 1
    print(" " * space+  "*"*((x *2)+1))