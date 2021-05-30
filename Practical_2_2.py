# If Else Statement
a = float (input("Enter any integer number:"))
if 0 <= a < 9 :
    print("The number is a Single digit number")
elif 9 < a < 99:
    print("The number is a 2 digit number")
elif 99 < a < 999:
    print("The number is a 3 digit number")
elif 999 < a < 9999:
    print("The number is a 4 digit number")
elif 9999 < a :
    print("The number has more than 4 digits")
else :
    print("The number is a negative number")
    
