import math
from random import randint

#exercise 2.1
name= input("Enter your name: ")
print(f"Hello, {name}!")


#exercise at class 2
Num1 = int(input("Enter Number A: "))
Num2 = int(input("Enter Number B: "))

print(f"The Number A is: {Num1} and the Number B is: {Num2} ")
Num1  = Num2
Num2 =  Num1
print(f"The Number A is: {Num1} and the Numbe5r B is: {Num2} ")

#exercise 2.2 (Radius of Circle)
radius = int(input("Enter radius: "))
area= math.pi*(radius**2)
print(f"The area is: {area}")

#exercise 2.3
Length = float(input("Enter Length: "))
Width  = float(input("Enter Width: "))
area = float(Length*Width)
Perimeter = float(2*(Width+Length))
print(f"The Area is: {area} and the Perimeter is: {Perimeter}")


#exercise 2.4

num1= float(input("Enter your first number: "))
num2= float(input("Enter your second number: "))
num3= float(input("Enter your third number: "))

sum= num1+num2+num3
average= (sum/3)
print(f"The sum of these number is : {sum}")

print(f"The average of these number is : {average}")



#exercise 2.5
talents = float(input("Enter number of Talents: "))
pounds = float(input("Enter number of Pounds: "))
lots= float(input("Enter number of Lots: "))

#total grams
totaltalents = talents*20*32*13.3          
totalpounds = pounds*32*13.3
totallots = lots*13.3
totalgrams = totaltalents + totalpounds + totallots

Kg= int(totalgrams/1000)
grams = totalgrams%1000

print(f"The weight in modern units: {Kg} kilograms and {grams:.2f} grams")


#exercise 2.6

num1 = randint(0,9)
num2 = randint(0,9)
num3 = randint(0,9)
num5 = randint(1,6)
num6=  randint(1,6)
num7 = randint(1,6)
num8 = randint(1,6)

print(f"the first code is : {num1}{num2}{num3} and the second code is : {num5}{num6}{num7}{num8}")

