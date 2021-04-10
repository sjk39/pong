from turtle import Turtle

class Pitch(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        #self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_len=40, stretch_wid=23)