from turtle import Turtle

POSITION = [(0, 300), (0, -300)]


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.walls = []
        self.create_walls()

    def create_walls(self):
        for wall_starting_position in POSITION:
            wall = Turtle("square")
            wall.penup()
            wall.setposition(wall_starting_position)
            wall.color("white")
            wall.turtlesize(stretch_wid=0.01, stretch_len=40)
            self.walls.append(wall)
