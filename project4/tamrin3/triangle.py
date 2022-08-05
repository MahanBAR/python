def function(firstnumber , secondnumber , thirdnumber):
        
    if firstnumber< secondnumber+thirdnumber:
        if secondnumber< firstnumber+thirdnumber:
            if thirdnumber< firstnumber+secondnumber:
                print("it is a triangle")
            else:
                print("it is not a triangle")

        else:
            print("it is not a triangle")
    
    else:
        print("it is not a triangle")

firstnumber = int(input("enter the first number:"))
secondnumber = int(input("enter the second number:"))
thirdnumber = int(input("enter the third number:"))

function(firstnumber , secondnumber , thirdnumber)
