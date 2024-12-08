# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods
# go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method
# call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth
# floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by
# creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
'''
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"You are at floor {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"You are at floor {self.current_floor}")

    def go_to_floor(self, floor_number):
        if floor_number < self.bottom_floor or floor_number > self.top_floor:
            raise ValueError("Floor number out of range")
        print(f"Moving to floor number: {floor_number} ")
        while floor_number != self.current_floor:
            if floor_number < self.current_floor:
                self.floor_down()
            else:
                self.floor_up()


elevator = Elevator(0, 15)
elevator.go_to_floor(8)
elevator.go_to_floor(0)
'''

'''
# Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of
# the bottom and top floors and the number of elevators in the building. When a building is created, the building
# creates the required number of elevators. The list of elevators is stored as a property of the building. Write a
# method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"You are at floor {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"You are at floor {self.current_floor}")

    def go_to_floor(self, floor_number):
        if floor_number < self.bottom_floor or floor_number > self.top_floor:
            raise ValueError("Floor number out of range")
        print(f"Moving to floor number: {floor_number} ")
        while floor_number != self.current_floor:
            if floor_number < self.current_floor:
                self.floor_down()
            else:
                self.floor_up()


class Building:
    def __init__(self, top_floor, bottom_floor, no_of_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.no_of_elevators = no_of_elevators
        self.elevators = []

        for i in range(no_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevators(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > self.no_of_elevators:
            raise ValueError("Elevator number out of range")
        print(f"Running the elevator number {elevator_number} to floor {destination_floor}")

        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    #Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to
    # the bottom floor. Continue the main program by causing a fire alarm in your building.

    def fire_alarm(self):
        print("Fire in the building!")
        for i in range(self.no_of_elevators):
            self.run_elevators(i + 1, self.bottom_floor)
            print(f"Elevator {i + 1} has been evacuated and is now on the bottom floor.")

building = Building(15, 0, 3)

building.run_elevators(1, 3)
building.run_elevators(2, 5)
building.run_elevators(3, 6)

building.fire_alarm()
'''

# Question 4
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
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/hr, Current Speed: {self.current_speed} km/hr, Travelled Distance: {self.travelled_distance} km"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)  # drive for 1 hour

    def print_status(self):
        table = []
        for car in self.cars:
            table.append([car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance])
        headers = ["Registration Number", "Maximum Speed (km/h)", "Current Speed (km/h)", "Travelled Distance (km)"]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        print()

    def race_finished(self):

        return any(car.travelled_distance >= self.distance for car in self.cars)


cars = [Car(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(1, 11)]
race = Race("Grand Demolition Derby", 8000, cars)
hours_passed = 0
while not race.race_finished():
    race.hour_passes()
    hours_passed += 1
    if hours_passed % 10 == 0:
        print(f"\n Status at Hour {hours_passed}")
        race.print_status()

print(f"\n Final Status after {hours_passed} hours")
race.print_status()
