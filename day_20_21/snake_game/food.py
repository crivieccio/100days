from random import randint
from turtle import Turtle


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
