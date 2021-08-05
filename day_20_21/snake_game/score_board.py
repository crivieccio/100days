from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
