# # #Exercise 06
#
# import random
# from random import randint
#
# N =int(input("Enter the number of random points to generate: "))
# #Initialize the number of random points in the circle
# pinsidec = 0
# index =0
# #Generate the random points and check if they are inside the circle
# for index in range(N):
#     x = random.uniform(-1,1)
#     y = random.uniform(-1,1)
#     #check if the points inside the circle
#     if x**2 + y**2 <= 1:
#         pinsidec += 1
# #Calculate the approximation of pi
# pi_approximation = 4 * pinsidec/N
# #Print the result
# print(f"Approximation of π using {N} points: {pi_approximation}")


# #Exercise 05
#
# correct_username = "python"
# correct_password = "rules"
# max_attempts = 5
# attempts = 0
#
# while attempts < max_attempts:
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         if username == correct_username and password == correct_password:
#             print("Welcome")
#             break
#         else:
#             attempts += 1
#             print(f"Incorrect username or password. Attempts left: {max_attempts - attempts}")
# print("Access denied.")



# #Exercise 04
# from random import randint
# number_to_guess = randint(1, 10)
#
#
# while True:
#         try:
#             user_guess = int(input("Enter your guess (1-10): "))
#
#             if user_guess < number_to_guess:
#                 print("Too low! Try again.")
#             elif user_guess > number_to_guess:
#                 print("Too high! Try again.")
#             else:
#                 print("Correct! You've guessed the number.")
#                 break
#         except ValueError:
#             print("Invalid input. Please enter an integer between 1 and 10.")



# #Exercise 03
# list=[]
#
# num = (input("Enter a number to add: "))
#
# while num !="":
#     list.append(num)
#     num = (input("Enter a number to add: "))
#
# if list:
#     nummin = min(list)
#     print(f"This is the minimum number : {nummin}")
#     nummax = max(list)
#     print(f"This is the maximum number : {nummax}")
#
# else:
#     print("Invalid input. Run the program again.")




# #Exercise 02
# from operator import truediv
#
# while True:
#     userin = int(input("Enter Inches to convert into cm: "))
#     if userin <0:
#         print("Sorry! it's a Negative Value.")
#         break
#     else:
#         if userin > 0:
#             cm = userin * 2.54
#             print(f"Final Reading is {cm}.")







# #Exercise 01
#
# num = 1
# while num <=1000:
#     if num%3==0:
#         print(num)
#     num = num + 1