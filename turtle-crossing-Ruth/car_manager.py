from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        # Initialize the CarManager with an empty list to store cars and starting move distance
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Create a new car with a random chance
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a Turtle object with a square shape
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the car shape
            new_car.penup()  # Lift the pen to avoid drawing lines
            new_car.color(random.choice(COLORS))  # Set a random color for the car
            random_y = random.randint(-250, 250)  # Set a random Y-coordinate for the car
            new_car.goto(300, random_y)  # Position the car off-screen to the right
            self.all_cars.append(new_car)  # Add the new car to the list

    def move_cars(self):
        # Move all cars backward based on the current car_speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase the car speed when the player successfully crosses the finish line
        self.car_speed += MOVE_INCREMENT



