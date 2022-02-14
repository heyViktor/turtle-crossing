from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.goto(-180, 265)
        self.write(arg=f"Level: {self.score}", align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over.", align="center", font=FONT)