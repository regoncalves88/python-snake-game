from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.speed(0)
        self.new_location()

    def new_location(self):
        self.setposition(randrange(-280, +280, 20), randrange(-280, +280, 20))