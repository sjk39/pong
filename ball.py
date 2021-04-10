from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(135)

    def move(self, hit):

        if hit and 0 < self.heading() < 90 or hit and 180 < self.heading() < 270:
            self.setheading(self.heading() + 90)
        elif hit:
            self.setheading(self.heading() - 90)
        else:
            if 0 < self.heading() < 90 or 270 < self.heading() < 360:
                if self.ycor() > 200:
                   self.setheading(315)
                elif self.ycor() < -200:
                   self.setheading(45)
            else:
                if self.ycor() > 200:
                    self.setheading(225)
                elif self.ycor() < -200:
                    self.setheading(135)



        self.forward(20)
