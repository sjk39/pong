from turtle import Turtle
import random

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_one = 0
        self.score_two = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score: {self.score_one} - {self.score_two}", align=ALIGNMENT, font=FONT)

    def increase_score_one(self):
        self.score_one += 1
        self.clear()
        self.write(f"Score: {self.score_one} - {self.score_two}", align=ALIGNMENT, font=FONT)

    def increase_score_two(self):
        self.score_two += 1
        self.clear()
        self.write(f"Score: {self.score_one} - {self.score_two}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.reset()
        self.hideturtle()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)