a=float(input("Enter the First number:"))
b=float(input("Enter the Second number:"))
print("Mathematical Operations")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
ch=int(input("Enter your choice (1-4): "))

if ch == 1:
    print("The sum is: ", a+b)
elif ch == 2:
    print("The difference is: ", a-b)
elif ch == 3:
    print("The product is: ", a*b)
elif ch == 4:
    print("The result of division is: ", a/b)
else:
    print("Invalid Choice")

while True:
    cont = input("Would you like to continue? yes/no : ")
    if cont.lower()=="yes":
        a=float(input("Enter the First number:"))
        b=float(input("Enter the Second number:"))
        print("Mathematical Operations")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        ch=int(input("Enter your choice (1-4): "))

        if ch == 1:
            print("The sum is: ", a+b)
        elif ch == 2:
            print("The difference is: ", a-b)
        elif ch == 3:
            print("The product is: ", a*b)
        elif ch == 4:
            print("The result of division is: ", a/b)
        else:
            print("Invalid Choice")
    if cont == "no":
        break
