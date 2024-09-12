# print("Exercise 01")
# #Exercise 01:
#
# import random
#
# def roll_dice():
#     return random.randint(1, 6)
# def main():
#     result = roll_dice()
#     while result != 6:
#         print(f"Rolled: {result}")
#         result = roll_dice()
#     print(f"Rolled: {result} (Stopped)")
# main()
#
#
#
#
# #Exercise 02:
# def diceRoll(sides):
#     getScore = random.randint(1, sides)
#     return getScore
#
# def main():
#     sides = int(input("Enter the number of sides on the dice: "))
#     maxNumber = sides
#     roll = 0
#     while roll != maxNumber:
#         roll = diceRoll(sides)
#         print(f"Rolled: {roll}")
# main()
#
# print("Exercise 03")
# #Exercise 03
# def gallonToLiters(gallons):
#     liters = gallons * 3.78541
#     return liters
# def main():
#     while True:
#         try:
#             gallons = float(input("Enter the volume in gallons or negative value to quit: "))
#             if gallons < 0:
#                 break
#             liters = gallonToLiters(gallons)
#             print(f"{gallons} gallons is equal to {liters:.2f} liters.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
# main()
#
#
# print("Exercise 04")
# #Exercise 04:
# def generateList():
#     list = []
#     while True:
#         userInput = input("Enter a number to add in list: ")
#         if userInput == "":
#             break
#         else:
#             userInput = int(userInput)
#             list.append(userInput)
#     return list
# def sumList(list):
#     totalSum = 0
#     for i in range(len(list)):
#         totalSum += list[i]
#     return totalSum
# def main():
#     list = generateList()
#     totalSumList = sumList(list)
#     print("This is the list")
#     print(list)
#     print(f"the sum of the list is :{totalSumList}")
# main()
#
#
# print("Exercise 05")
# #Exercise 05
# def generateList():
#     list = []
#     while True:
#         userInput = input("Enter a number: ")
#         if userInput == "":
#             break
#         else:
#             userInput = int(userInput)
#             list.append(userInput)
#     return list
# def removeOdd(list):
#     evenList = []
#     for i in range(len(list)):
#         if  list[i]% 2 == 0:
#             evenList.append(list[i])
#     return evenList
# def main():
#     firstList = generateList()
#     secondList = removeOdd(firstList)
#     print(f"generated List is: {firstList}")
#     print(f"list of odd number from the list {secondList}")
# main()
#
#
print("Exercise 06")
#Exercise 06:

def pizzaPurchase():
    pizza1 = float(input("Enter the pizza price 1: "))
    pd1 = float(input("Enter the pizza diameter 1 in cm: "))
    pizza2 = float(input("Enter the pizza price 2: "))
    pd2 = float(input("Enter the pizza diameter 2 in cm: "))

    area1 = (3.14 / 4) * (pd1/100) ** 2
    area2 = (3.14 / 4) * (pd2/100) ** 2

    price1 = pizza1 / area1
    price2 = pizza2 / area2

    if price1 > price2:
        print(f"You sould purchase pizza 2 bcz it is {price2:.2f} per sqr mtr.")
    elif price2 > price1:
        print(f"You sould purchase pizza 1 bcz it is {price1:.2f} per sqr mtr.")

pizzaPurchase()