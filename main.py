from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

score = Score()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.velocity)
    ball.move()

    # detect upper and below wall collisions
    if ball.ycor() > 275 or ball.ycor() < -270:
        ball.bounce_y()

    # detect paddle collision
    if (ball.distance(right_paddle) < 50 and (350 > ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and (-350 < ball.xcor() < -320))):
        ball.bounce_x()

    # detect missing the ball by the right player
    if ball.xcor() > 400:
        score.lpoint()  # add a point to the left player
        ball.reset_position()

    # detect missing the ball by the left player
    if ball.xcor() < -400:
        score.rpoint() # add a point to the right player
        ball.reset_position()

    # Optional : exit when a player reaches a score 10
    """ if score.winner():
            game_on = False """



screen.exitonclick()
