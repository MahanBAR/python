print("enrter 3 number getting the max number:")
number_one = int(input("first number:"))
number_two =int(input("second number:"))
number_three =int(input("third number:"))

max = 0

if number_one > number_two:
    if number_one > number_three:
        max = number_one
    else:
        max = number_three
if number_two > number_one:
    if number_two > number_three:
        max = number_two
    else:
        max = number_three
print(max)
