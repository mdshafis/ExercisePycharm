'''
#Task_1. Write a Car class that has the following properties: registration number, maximum speed,
# current speed and travelled distance. Add a class initializer that sets the first two of the
# properties based on parameter values. The current speed and travelled distance of a new car
# must be automatically set to zero. Write a main program where you create a new car
# (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties
# of the new car.

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f" Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/hr, Current Speed: {self.current_speed} km/hr, Travelled Distance: {self.travelled_distance} km"

car1 = Car("ABC-123", 142)
print (f"car1=> {car1}")
'''

'''
#Task_2. Extend the program by adding an accelerate method into the new class. The method should receive the change of
# speed (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the
# speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed
# and then print out the final speed. The travelled distance does not have to be updated yet.
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def __str__(self):
        return f" Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/hr, Current Speed: {self.current_speed} km/hr, Travelled Distance: {self.travelled_distance} km"

car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print (f"Current speed of car1 after acceleration: {car1.current_speed} km/hr")

car1.accelerate(-200)
print (f"Current speed of car1 after emergency brake: {car1.current_speed} km/hr")

print (f"car1=> {car1}")
'''
'''
#Task_3. Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5)
# increases the travelled distance to 2090 km.

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, number_of_hours):
                self.travelled_distance += self.current_speed * number_of_hours

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/hr, Current Speed: {self.current_speed} km/hr, Travelled Distance: {self.travelled_distance} km"

car1 = Car("ABC-123", 142)
car1.accelerate(30)
car1.accelerate(70)
car1.drive(5)
print (f"Distance travelled by car1: {car1.travelled_distance} km")

print (f"car1=> {car1}")
'''

#Task4. Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car
# objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed:
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accelerate method.
#Each car is made to drive for one hour. This is done with the drive method. The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.

import random
from tabulate import tabulate
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed}, Current Speed: {self.current_speed} km/hr, Travelled Distance: {self.travelled_distance} km"

cars = []
for c in range(10):
    registration_number = f"ABC-{c+1}"
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))

winner = None
while not winner:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            winner = car
            break

race_table = []
for car in cars:
    race_table.append([car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance])

headers = ["Registration Number", "Max Speed (km/h)", "Current Speed (km/h)", "Travelled Distance (km)"]
print(f"The winner is the car with Registration Number:{winner.registration_number}.")
print(f"The table with the properties of the 10 cars in the race is as follows: \n{(tabulate(race_table, headers=headers, tablefmt="fancy_grid"))}")
