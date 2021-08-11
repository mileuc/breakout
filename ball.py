# step 3: create and move the ball
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()  # enable Turtle methods to be used in Ball class
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.030

    def move(self):
        # move ball
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        # when bounce occurs off top wall, y_move is changed so the ball moves down
        self.y_move *= -1

    def bounce_x(self):
        # when bounce occurs off left or right wall, x_move is changed so the ball moves in opposite direction
        self.x_move *= -1

    def bounce_paddle(self):
        self.y_move = abs(self.y_move)  # bounce in upward direction

    def bounce_block(self):
        self.y_move = -abs(self.y_move)  # bounce in downward direction

    def paddle_miss(self):
        # when paddle misses, spawn above the paddle and move upwards
        self.goto(x=0, y=-190)
        self.bounce_paddle()
