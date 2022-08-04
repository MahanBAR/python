while True:
    print("1- plus")
    print("2- minus")
    print("3- times")
    print("4- division")
    print("5- power")
    print("6- square root")
    print("7- quiet")

    option = int(input("choose your option:"))

    firstnumber = int(input("enter the first number:"))
    secondnumber = int(input("enter the second number:"))

    if option == 1:
        print(firstnumber + secondnumber)
    elif option == 2:
        print(firstnumber - secondnumber)
    elif option == 3:
        print(firstnumber * secondnumber)
    elif option == 4:
        print(firstnumber / secondnumber)
    elif option == 5:
        print(firstnumber ** secondnumber)
    elif option == 6:
        import math
        print(int(math.sqrt(int(firstnumber))))
        print(int(math.sqrt(int(secondnumber))))
    elif option == 7:
        break
    else:
        print("the option is wrong")
