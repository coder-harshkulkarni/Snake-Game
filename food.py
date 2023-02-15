import random
import time
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(0.8, 0.8)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
