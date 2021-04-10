from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from pitch import Pitch
from paddle import Paddle
import time

sc = Screen()
sc.setup(width=1000, height=600)
p = Pitch()
sc.bgcolor("black")
sc.title("Pong")
sc.listen()
paddle_one = Paddle()
paddle_one.position(1)
paddle_two = Paddle()
paddle_two.position(2)
ball = Ball()
scoreboard = Scoreboard()
sc.onkey(paddle_one.up, "Up")
sc.onkey(paddle_one.down, "Down")

game_on = True
while game_on:
    sc.update()
    #time.sleep(0.001)

    if ball.distance(paddle_one.pos()) < 40 or ball.distance(paddle_two.pos()) < 40:
        ball.move(1)
        #prevents ball getting 'stuck' to paddle
        ball.move(0)
    else:
        ball.move(0)
    #if ball y cor different to comp y cor, move to coords
    if ball.ycor() > paddle_two.ycor() and ball.xcor() > 200:
        paddle_two.up()
    elif ball.ycor() < paddle_two.ycor() and ball.xcor() > 200:
        paddle_two.down()
    #if ball goes out left add one to comp score and replace ball and vice versa
    if ball.xcor() < -400:
        scoreboard.increase_score_two()
        ball.color("black")
        ball.__init__()
    elif ball.xcor() >400:
        scoreboard.increase_score_one()
        ball.color("black")
        ball.__init__()
    #if a player exceeds score limit end game
    if scoreboard.score_one > 9 or scoreboard.score_two >9:
        scoreboard.game_over()
        game_on = False

sc.exitonclick()

