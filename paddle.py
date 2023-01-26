from turtle import Turtle


class Paddle(Turtle):
    """ Creates a paddle object
    accepts a tuple with x and y coordinates from user.
    Default: (0,0)"""
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.goto(position)
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()

    def up(self):
        if self.ycor() < 250:
            self.forward(20)

    def down(self):
        if self.ycor() > -250:
            self.backward(20)
