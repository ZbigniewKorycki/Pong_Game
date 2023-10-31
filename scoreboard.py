from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
FINAL_SCORE_FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player_r = 0
        self.score_player_l = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"{self.score_player_l}   {self.score_player_r}", align=ALIGNMENT, font=FONT
        )

    def increase_score_player_l(self):
        self.score_player_l += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_player_r(self):
        self.score_player_r += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME IS FINAL", align=ALIGNMENT, font=FINAL_SCORE_FONT)
