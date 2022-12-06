from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(fun=paddle1.move_up, key="Up")
screen.onkey(fun=paddle1.move_down, key="Down")
screen.onkey(fun=paddle2.move_up, key="w")
screen.onkey(fun=paddle2.move_down, key="s")

is_game = True

while is_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 276 or ball.ycor() < -276:
        ball.bounce(1, -1)

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce(-1, 1)

    if ball.xcor() > 400:
        ball.reset_bounce()
        score.scorel()

    if ball.xcor() < -400:
        ball.reset_bounce()
        score.scorer()








screen.exitonclick()
