import time
from turtle import Screen

from food import Food
from score_board import ScoreBoard
from snake import Snake


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score_board = ScoreBoard()

    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_board.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_on = False
            score_board.game_over()

        # Detect collision with tail
        # if head collides with any segment in the tail: game_over
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score_board.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
