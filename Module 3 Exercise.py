#Exercile 01

size = float(input("Enter the length of the Fish: "))

if 42 <= size:
    print("You can catch the fish.")
elif size <42:
    small = 42%size
    print(f"Please release the fish into water. Fish is {small} cm smaller. ")

#Exercise 02

cabin = input("Enter your cabin class type (LUX/A/B/C): ")


if cabin == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabin == "A":
    print("above the car deck, equipped with a window.")
elif cabin == "B":
    print("windowless cabin above the car deck.")
elif cabin == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid Cabin Class")


# Exercise 03

gender = input("Enter your gender (male/female): ")
hg = int(input("Enter your hemoglobin level: "))

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





#Exercise 04
year = ""
while year !="exit":
    year = int(input("Enter a year or Type 'exit' to Terminate: "))
    if (year%100==0 and year%400==0) or (year%4==0):
        print(f"Wow!! The year {year} is Leap year.")
    else:
        print(f"Ops!! The year {year} is not Leap year.")










