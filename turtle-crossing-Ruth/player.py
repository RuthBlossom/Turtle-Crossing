from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.shape("turtle")  # Set the player's shape to a turtle
        self.penup()  # Lift the pen to avoid drawing lines
        self.go_to_start()  # Move the player to the starting position
        self.setheading(90)  # Set the player's orientation to face upward

    def go_up(self):
        # Move the player forward by the MOVE_DISTANCE
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Move the player to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the player has reached the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



