from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 210)
        self.rscore = 0
        self.lscore = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.lscore}   {self.rscore}", align="center", font=("courier", 60, "normal"))

    def rpoint(self):
        self.rscore += 1
        self.print_score()

    def lpoint(self):
        self.lscore += 1
        self.print_score()
