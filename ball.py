from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce(self, x, y):
        self.x_move *= x
        self.y_move *= y
        self.move_speed *= 0.9

    def reset_bounce(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1