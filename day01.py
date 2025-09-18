# Calculator

num1 = int(input("enter the first no:"))
num2 = int(input("enter the second no:"))
ope = input("Enter the one operation (+,-,*,/):")

if ope == "+":
    print(f'ans = {num1+num2} ')
elif ope == "-":
    print(f'ans = {num1-num2} ')
elif ope == "*":
    print(f'ans = {num1*num2} ')    
elif ope == "/":
    print(f'ans = {num1/num2} ')
else:
    print("something went wrong")


#name formating

firstname = input("enter your name:")
lastname = input("enter your last name:")

print(lastname,firstname)
print(firstname.capitalize(),lastname.capitalize())
print(firstname.lower(),lastname.upper())

#date
from datetime import date
bdate_str = input("Enter your birth date (YYYY-MM-DD): ")
bdate = date.fromisoformat(bdate_str)

print((date.today()-bdate)/365,'years')