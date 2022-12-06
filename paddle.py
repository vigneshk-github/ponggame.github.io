from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.penup()
        self.goto(pos)

    def move_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def move_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)


