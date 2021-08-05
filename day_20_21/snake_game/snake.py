from turtle import Turtle
from typing import List

COLOR = "white"
SHAPE = "square"
MOVE_DISTANCE = 20

DIRECTION_HEADINGS = {
    "up": 90,
    "down": 270,
    "right": 0,
    "left": 180
}

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        self.segments: List[Turtle] = []
        for position in STARTING_POSITIONS:
            self.add_segment(position=position)
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle(shape=SHAPE)
        segment.color(COLOR)
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION_HEADINGS["down"]:
            self.head.setheading(DIRECTION_HEADINGS["up"])

    def down(self):
        if self.head.heading() != DIRECTION_HEADINGS["up"]:
            self.head.setheading(DIRECTION_HEADINGS["down"])

    def left(self):
        if self.head.heading() != DIRECTION_HEADINGS["right"]:
            self.head.setheading(DIRECTION_HEADINGS["left"])

    def right(self):
        if self.head.heading() != DIRECTION_HEADINGS["left"]:
            self.head.setheading(DIRECTION_HEADINGS["right"])
