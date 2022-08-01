print("1- power")
print("2- devide")
print("3- mines")
print("4- plus")

my_var = input("choose your option:")
if int(my_var) == 1:
    x_1 = input("enter first number:")
    x_2 = input("enter second number:")
if int(my_var) == 2:
    x_3 = input("enter your age:")   
if int(my_var) == 3:
    x_4 = input("enter your name:")
if int(my_var) == 4:
    x_5 = input("enter your lastname:")
    print(int(x_1) ** int(x_2) ** int(x_3) ** int(x_4) ** int(x_5))
