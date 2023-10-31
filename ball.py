from turtle import Turtle
import random

STARTING_POSITION = (0, 0)
POSSIBLE_MOVE = [-10, 10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(STARTING_POSITION)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.speeder()

    def speeder(self):
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.y_move = random.choice(POSSIBLE_MOVE)
        self.bounce_paddle()
        self.ball_speed = 0.1
