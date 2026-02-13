m=int(input("enter the first number?"))
n=int(input("enter the second number?"))
print("welcome to simple calculator")
print(" press 2 for subtraction ")
print("press 3 for addition")
print ("press 4 for multiplication")
print(" press 5 for division")
calc=int(input("select a number: "))
if calc ==2:
    print(m-n)
elif calc ==3:
    print(m+n)
elif calc==4:
    print(m*n)
elif calc==5:
    print(m/n)
else:
    print("error")

