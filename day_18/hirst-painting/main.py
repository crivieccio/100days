from random import choice
from turtle import Screen, Turtle

import colorgram

rgb_colors = []
colors = colorgram.extract("index.jpg", 100)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))


screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.penup()
tim.setx(-250)
tim.sety(-250)

for i in range(10):
    tim.setposition(-250, -250 + i * 50)
    tim.setheading(0)
    for _ in range(10):
        color = choice(rgb_colors)
        tim.color(color)
        tim.pendown()
        tim.dot(20)
        tim.penup()
        tim.forward(50)

screen.exitonclick()
