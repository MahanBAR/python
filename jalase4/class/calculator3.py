
while True:
    print("1- plus")
    print("2- minus")
    print("3- times")
    print("4- division")
    print("5- power")
    print("6- quit")

    option = input("chosse your option:")

    number_1 = int(input("enter first number:"))
    number_2 = int(input("enter second number:"))

    if option==("1"):
        print(number_1+number_2)
    elif option==("2"):
        print(number_1-number_2)
    elif option==("3"):
        print(number_1*number_2)
    elif option==("4"):
        print(number_1/number_2)
    elif option==("5"):
        print(number_1**number_2)
    elif option==("6"):
        break
    else: 
        print("wrong option ")
        