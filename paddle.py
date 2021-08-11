# step 2: create paddle class
from turtle import Turtle


class Paddle(Turtle):   # paddle class is now effectively the same as a Turtle class
    def __init__(self, paddle_position):
        super().__init__()  # enable Turtle methods to be used in Ball class
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(paddle_position)  # initial position of the paddle center

    def move_left(self):
        # move paddle left
        new_x = self.xcor() - 20
        self.goto(x=new_x, y=self.ycor())

    def move_right(self):
        # move paddle right
        new_x = self.xcor() + 20
        self.goto(x=new_x, y=self.ycor())