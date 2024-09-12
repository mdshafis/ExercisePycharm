# #Exercise 01
#
# import random
#
# num_dice = int(input("How many dice would you like to roll: "))
# total_sum = 0
# for _ in range(num_dice):
#     roll = random.randint(1, 6)
#     total_sum += roll
#
#     print(f"The sum of your dice rolls is: {total_sum}")


# #Exercise 02:
#
# numbers = []
#
# while True:
#     user_input = input("Enter a number (or press Enter to quit): ")
#     if user_input == "":
#         break
#     try:
#         number = float(user_input)
#         numbers.append(number)
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#
# numbers.sort(reverse=True)
# print("The five greatest numbers are: ")
# for number in numbers[:5]:
#     print(number)



# #Exercise 03:
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to the square root of the number
#         if num % i == 0:
#             return False
#     return True
#
# user_input = input("Enter an integer: ")
# try:
#     number = int(user_input)
#     if is_prime(number):
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")
# except ValueError:
#     print("Please enter a valid integer.")


# #Exercise 04
# cities = []
#
# # Use a for loop to get the names of five cities from the user
# for i in range(5):
#     city = input(f"Enter the name of city {i + 1}: ")
#     cities.append(city)
#
# print("The cities you entered are:")
# for city in cities:
#     print(city)
