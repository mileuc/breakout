# step 5: create scoreboard
from turtle import Turtle
FONT = ("Courier", 20, "normal")


# create scoreboard that shows balls/lives remaining, high score, and current score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.balls_left = 5
        try:
            with open("high_score.txt", mode="r") as data:
                self.high_score = int(data.read())
        except FileNotFoundError or TypeError:
            with open("high_score.txt", mode="w") as data:
                self.high_score = 0
                data.write(f"{self.high_score}")
        self.status_text = f"Breakout | High Score: {self.high_score}"
        self.update_scoreboard()

    # clear and update the balls and score
    def update_scoreboard(self):
        self.clear()
        self.goto(x=-380, y=260)
        self.write(f"{self.balls_left} balls", align="left", font=FONT)
        self.goto(x=0, y=260)
        self.write(self.status_text, align="center", font=FONT)
        self.goto(x=375, y=260)
        self.write(self.score, align="right", font=FONT)

    # after a game is finished, check if the score is greater than the current high score and save it
    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        # self.score = 0  # reset score
        self.update_scoreboard()

    # add 5 points, times the number of walls cleared to score for every block destroyed
    def add_points(self, walls, row):
        if row == 130:
            self.score += (1 * walls)
        elif row == 155:
            self.score += (2 * walls)
        elif row == 180:
            self.score += (3 * walls)
        elif row == 205:
            self.score += (4 * walls)
        elif row == 230:
            self.score += (5 * walls)
        self.update_scoreboard()

    # deduct a ball every time a ball misses
    def deduct_balls(self):
        self.balls_left -= 1
        self.update_scoreboard()
