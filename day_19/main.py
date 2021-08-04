from turtle import Screen, Turtle


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_left():
    tim.left(5)


def rotate_right():
    tim.right(5)


def clear():
    screen.clear()


tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=rotate_left, key="a")
screen.onkey(fun=rotate_right, key="d")
screen.onkey(fun=clear, key="c")


screen.exitonclick()
