# if-elif-else

light = input("Enter Color: ")

if (light == "Red"):
    print("STOP")

elif(light == "Yellow"):
    print("WAIT")   

elif(light == "Green"):
    print("GO")

else:
    print("LIGHT IS BROKEN")


#NESTING 
age = int(input("Enter your age: "))

if(age >= 18):
    if(age >80):
        print("CANNOT DRIVE")
    else:
        print("CAN DRIVE")
else:
    print("CANNOT DRIVE")            


#WAP to check if a number is EVEN or ODD

num = int(input("ENTER A NUMBER: "))

if (num%2 == 0):
    print("NUMBER IS EVEN")
else:
    print("NUMBER IS ODD")    