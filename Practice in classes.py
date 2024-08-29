year = ""

while year != "exit":
    year = input("Enter a year or type 'exit' to terminate: ")

    if year == "exit":
        print("Thank you for using my program.")
        break

    year = int(year)

    if (year % 400 == 0) or (year % 100 == 0 and year % 4 == 0):
        print(f"Wow!! The year {year} is a Leap year.")
    else:
        print(f"Oops!! The year {year} is not a Leap year.")



gender = input("Enter your gender (male/female): ")
hg = int(input("Enter your hemoglobin level (g/l): "))

if gender == "male" and 134 <= hg <= 167:
    print("Your Hemoglobin level is Normal")
else:
    if gender == "male" and 134 > hg:
        print("Your Hemoglobin level is low")
    elif gender == "male" and hg > 167:
        print("Your Hemoglobin level is high")
if gender == "female" and 117 <= hg <= 155:
    print("Your Hemoglobin level is normal")
else:
    if 117 > hg:
        print("Your Hemoglobin level is low")
    elif hg > 155:
        print("Your Hemoglobin level is high")

cabin = ""
while cabin !="exit":
    cabin = input("Enter a cabin or Type 'exit' to Terminate: ").upper()
    if cabin == "exit":
        print("Thank you for not using my program.")
        break
    cabin = str(cabin)
    if cabin == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin == "B":
        print("Windowless cabin above the car deck.")
    elif cabin == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid Cabin Class")



# year = ""
#
# while year !="exit":
#     year = input("Enter a year or Type 'exit' to Terminate: ")
#     if year == "exit":
#         print("Thank you for not using my program.")
#         break
#     year = int(year)
#     if (year%100==0 and year%400==0) and (year%4==0):
#         print(f"Wow!! The year {year} is Leap year.")
#     else:
#         print(f"Ops!! The year {year} is not Leap year.")

# #Exercise_5
# age = int(input("Enter your age: "))
#
# if age >= 65:
#     print("you are Retired")
# elif 18<= age:
#     print("you are a Washing Age")
# elif 7<= age:
#     print("you are in Studying")
# elif 0<= age:
#     print("you are in Children")
#
#
#
# #Exercise_4
#
# wheels = int(input("Enter the number of wheels: "))
#
# if wheels == 2:
#     print("Do you have Battery?")
#     is_battery = input("Is it battery-powered (yes/no)? ")
#     if is_battery == "yes":
#         print("It is a E-Bike.")
#     elif is_battery == "no":
#         print("It is a bicycle.")
#     else:
#         print("Wrong input for battery-powered question.")
# elif wheels == 3:
#     print("It is a tricycle.")
# elif wheels == 4:
#     print("It is a car.")
# else:
#     print("Wrong input.")
#
#
#
#
#
# #Exercise_3
#
#
# Number = float(input("Enter a number: "))
#
# if Number > 90:
#     print("Your grade is A1")
# elif Number > 80:
#     print("Your grade is A2")
# elif Number > 70:
#     print("Your grade is B1")
# elif Number > 60:
#     print("Your grade is B2")
# elif Number > 50:
#     print("Your grade is C1")
# elif Number > 35:
#     print("Your grade is C2")
# else:
#     print("Your grade is F (Fail)")
#
#
#
# #Exercise_2
#
#
# age = float(input("Your age: "))
# weight = float(input("Your weight: "))
#
# if 15 <= age <= 18 and weight >= 55:
#     print("The medicine can be used")
# else:
#     if weight < 55 and age < 15:
#         print("Reason: Both age and weight are incorrect.")
#     elif weight < 55:
#         print("Reason: Weight is less than 55 kg.")
#     elif age < 15:
#         print("Reason: Age is less than 15.")
#     elif age > 18:
#         print("Reason: Age is greater than 18.")
#
#
#
#
# #Exercise_1
# money = float(input("Enter your money: "))
# if money>= 5:
#     print(f"You can buy latte")
    
