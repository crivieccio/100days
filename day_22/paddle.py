from turtle import Turtle, up

WIDTH_STRECH = 5
HEIGHT_STRECH = 1

COLOR = "white"
SHAPE = "square"

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=WIDTH_STRECH, stretch_len=HEIGHT_STRECH)
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
