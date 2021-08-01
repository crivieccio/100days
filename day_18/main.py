from random import randrange
from turtle import Screen, Turtle, heading

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(50):
#     if i % 2 == 0:
#         timmy.pendown()
#     else:
#         timmy.penup()
#     timmy.forward(10)
screen = Screen()
screen.colormode(255)

# for i in range(3, 11):
#     angle = 360/i
#     timmy.color(randrange(0, 255), randrange(0, 255), randrange(0, 255))
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(angle)
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     turn = randrange(0, 4)
#     color = (randrange(0, 256), randrange(0, 256), randrange(0, 256))
#     timmy.color(color)
#     timmy.forward(50)
#     timmy.setheading(directions[turn])


def random_color():
    return (randrange(0, 255), randrange(0, 255), randrange(0, 255))


for _ in range(360 // 5):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)


screen.exitonclick()
