from turtle import Turtle

POSITION_1 = (-350, 0)
POSITION_2 = (350, 0)
DIRECTIONS = {'UP': 90,
              'DOWN': 270}
DIMENSIONS = (20, 100)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.speed(0)

    def position(self, player):
        self.setheading(DIRECTIONS['UP'])
        if player == 1:
            self.goto(POSITION_1)
        else:
            self.goto(POSITION_2)

    def up(self):
        if self.ycor() < 200:
            self.setheading(DIRECTIONS['UP'])
            self.forward(20)

    def down(self):
        if self.ycor() > -200:
            self.setheading(DIRECTIONS['DOWN'])
            self.forward(20)

