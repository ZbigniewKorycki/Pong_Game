from turtle import Screen
from paddle import Paddle
from ball import Ball
from net import Net
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
net = Net()


screen.listen()
screen.onkey(paddle_r.move_up_player_r, "Up")
screen.onkey(paddle_r.move_down_player_r, "Down")
screen.onkey(paddle_l.move_up_player_l, "w")
screen.onkey(paddle_l.move_down_player_l, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with r_paddle
    if (
        (ball.xcor() > 320)
        and (ball.distance(paddle_r) < 50)
        or (ball.xcor() < -320)
        and (ball.distance(paddle_l) < 50)
    ):
        ball.bounce_paddle()

    # Detect when right paddle misses
    if (ball.xcor() > 400) and (ball.distance(paddle_r) > 50):
        scoreboard.increase_score_player_l()
        ball.reset()

    if (ball.xcor() < -400) and (ball.distance(paddle_l) > 50):
        ball.goto(0, 0)
        scoreboard.increase_score_player_r()
        ball.reset()

screen.exitonclick()
