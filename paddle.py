from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddles()
        self.setposition(position)

    def create_paddles(self):
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color("white")

    def move_up_player_r(self):
        self.forward(20)

    def move_down_player_r(self):
        self.backward(20)

    def move_up_player_l(self):
        self.forward(20)

    def move_down_player_l(self):
        self.backward(20)
