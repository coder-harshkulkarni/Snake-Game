from turtle import Turtle

MOVE_DISTANCE = 20
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def add_tail(self, position):
        new_timmy = Turtle()
        new_timmy.shape("circle")
        new_timmy.color("white")
        new_timmy.penup()
        new_timmy.goto(position)
        self.turtles.append(new_timmy)

    def create_snake(self):
        for position in POSITIONS:
            self.add_tail(position)

    def reset(self):
        for tur in self.turtles:
            tur.goto(2000, 2000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend_tail(self):
        self.add_tail(self.turtles[-1].pos())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].pos())

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
