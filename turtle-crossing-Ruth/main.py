import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off automatic screen updates

# Create instances of Player, CarManager, and Scoreboard classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up key listening for the "Up" arrow key to make the player go up
screen.listen()
screen.onkey(player.go_up, "Up")

# Initialize the game state
game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(0.1)  # Pause to control the speed of the game
    screen.update()  # Update the screen manually

    # Create a new car and move existing cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False  # End the game
            scoreboard.game_over()

    # Detect successful crossing of the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()  # Increase the speed of cars and create more
        scoreboard.increase_level()

# Close the game window when the player clicks on it
screen.exitonclick()



