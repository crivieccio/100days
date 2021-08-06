import time
from turtle import Screen, back

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(height=600, width=800)
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()
    scoreboard = ScoreBoard()

    right_paddle = Paddle(x_pos=350, y_pos=0)
    left_paddle = Paddle(x_pos=-350, y_pos=0)
    ball = Ball()

    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")

    screen.onkey(left_paddle.up, 'w')
    screen.onkey(left_paddle.down, 's')

    game_on = True

    while game_on:
        screen.update()
        time.sleep(ball.move_speed())
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.back_to_center()
            scoreboard.l_point()
            scoreboard.update_scoreboard()

        if ball.xcor() < -380:
            ball.back_to_center()
            scoreboard.r_point()
            scoreboard.update_scoreboard()

    screen.exitonclick()


if __name__ == "__main__":
    main()
