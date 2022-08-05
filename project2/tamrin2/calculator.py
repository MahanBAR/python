print("1- plus")
print("2- minus")
print("3- times")
print("4- division")
print("5- power")
print("6- square root")
X = input("chosse your option:")
F = input("enter your first number:")
S = input("enter your second number:")
if int(X) == 1:
    print(int(F)+ int(S))
if int(X) == 2:
    print(int(F)- int(S))
if int(X) == 3:
    print(int(F)* int(S))
if int(X) == 4:
    print(int(F)/ int(S))
if int(X) == 5:
    print(int(F)** int(S))
if int(X) == 6:
    import math
    print(int(math.sqrt(int(F))))
    print(int(math.sqrt(int(S))))
    


