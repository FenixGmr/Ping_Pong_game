from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")

scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))






screen.listen()
screen.onkey(r_paddle.pong_up, "Up")
screen.onkey(r_paddle.pong_down, "Down")
screen.onkey(l_paddle.pong_up, "w")
screen.onkey(l_paddle.pong_down, "s")
screen.tracer(0)



is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time.sleep(0.0001)

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score1()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score()




















screen.exitonclick()

