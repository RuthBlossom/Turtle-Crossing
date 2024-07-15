from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.level = 1  # Initial level is set to 1
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(-280, 250)  # Set the initial position of the scoreboard
        self.update_scoreboard()  # Display the initial scoreboard

    def update_scoreboard(self):
        # Clear the existing content and write the current level on the scoreboard
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # Increase the level and update the scoreboard
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Display "GAME OVER" in the center of the screen
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

