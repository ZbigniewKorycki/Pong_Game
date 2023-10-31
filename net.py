from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.create_net()

    def create_net(self):
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=300)
        self.pencolor("white")
        self.pendown()
        self.setheading(270)
        for line in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
