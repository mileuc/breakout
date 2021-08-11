# step 4: create blocks
from turtle import Turtle
import random


# create block
class Block(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        # self.colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]
        self.shapesize(1, 5)
        self.goto(x, y)
        # self.color(random.choice(self.colors))
