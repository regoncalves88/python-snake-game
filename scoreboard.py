from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(x=0, y=270)
        self.color("black")
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}\tHighest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.write_score()
