# name=input("What is your name? ")
# age=26
# status="This patient already exist"
# if(name=="John Smith"):
#     print(status)
# else:
#     print("Welcome new patient")

#next exercise
# name=input("Enter Your name: ")
# color=input("Your Fav color? ")
# print(name+" likes " +color)

#next exercise
# pd=input("Enter weight in pounds: ")
# print(float(pd)*0.454)

#next exercise
# str="syed abdulla"
# name=str[:]
# print(name)

#formatted strings
# f="syed"
# l="abdulla"
# print(f'{f} [{l}] is a coder')
# print((f+" "+l).capitalize())

#math functions
import math

# c=10.9
# print(math.floor(c))

#exercise
amt=input("Do you have good credit? y or n s")
if amt=="y":
    pay=0.1*10**6
elif amt=="n":
    pay=0.2*10**6
else:
    exit(print("Wrong input"))
print(f"Down payment ${pay}")