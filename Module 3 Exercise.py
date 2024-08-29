#Exercile 01
sizeLimit  = 42
size = float(input("Enter the length of the Fish in cm: "))

if sizeLimit <= size:
    print("You can catch the Zander.")
elif size <sizeLimit:
    small = sizeLimit%size
    print(f"Please release the Zander into water. Fish is {small} cm smaller. ")



#Exercise 02

cabin = ""
while cabin !="EXIT":
    cabin = input("Enter a cabin or Type 'exit' to Terminate: ").upper()
    if cabin == "EXIT":
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





# Exercise 03

gender = input("Enter your gender (male/female): ")
hg = int(input("Enter your hemoglobin level (g/l): "))

if gender == "MALE" and 134 <= hg <= 167:
    print("Your Hemoglobin level is Normal")
else:
    if 134 > hg:
        print("Your Hemoglobin level is low")
    elif hg > 167:
        print("Your Hemoglobin level is high")
if gender == "Female" and 117 <= hg <= 155:
    print("Your Hemoglobin level is normal")
else:
    if 117 > hg:
        print("Your Hemoglobin level is low")
    elif hg > 155:
        print("Your Hemoglobin level is high")







#Exercise 04


year = ""

while year != "exit":
    year = input("Enter a year or type 'exit' to terminate: ")

    if year == "exit":
        print("Thank you for using my program.")
        break

    year = int(year)

    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print(f"Wow!! The year {year} is a Leap year.")
    else:
        print(f"Oops!! The year {year} is not a Leap year.")
