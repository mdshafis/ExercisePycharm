
#Exercise_5
age = int(input("Enter your age: "))

if age >= 65:
    print("you are Retired")
elif 18<= age:
    print("you are a Washing Age")
elif 7<= age:
    print("you are in Studying")
elif 0<= age:
    print("you are in Children")



#Exercise_4

wheels = int(input("Enter the number of wheels: "))

if wheels == 2:
    print("Do you have Battery?")
    is_battery = input("Is it battery-powered (yes/no)? ")
    if is_battery == "yes":
        print("It is a E-Bike.")
    elif is_battery == "no":
        print("It is a bicycle.")
    else:
        print("Wrong input for battery-powered question.")
elif wheels == 3:
    print("It is a tricycle.")
elif wheels == 4:
    print("It is a car.")
else:
    print("Wrong input.")





#Exercise_3


Number = float(input("Enter a number: "))

if Number > 90:
    print("Your grade is A1")
elif Number > 80:
    print("Your grade is A2")
elif Number > 70:
    print("Your grade is B1")
elif Number > 60:
    print("Your grade is B2")
elif Number > 50:
    print("Your grade is C1")
elif Number > 35:
    print("Your grade is C2")
else:
    print("Your grade is F (Fail)")



#Exercise_2


age = float(input("Your age: "))
weight = float(input("Your weight: "))

if 15 <= age <= 18 and weight >= 55:
    print("The medicine can be used")
else:
    if weight < 55 and age < 15:
        print("Reason: Both age and weight are incorrect.")
    elif weight < 55:
        print("Reason: Weight is less than 55 kg.")
    elif age < 15:
        print("Reason: Age is less than 15.")
    elif age > 18:
        print("Reason: Age is greater than 18.")




#Exercise_1
money = float(input("Enter your money: "))
if money>= 5:
    print(f"You can buy latte")
    
