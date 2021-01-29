from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        initial_x = 0

        for n in range(3):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.setposition(STARTING_POSITIONS[n])
            self.snake.append(new_segment)
            initial_x -= 20

    def move(self):
        for n in range(len(self.snake) - 1, 0, -1):
            self.snake[n].setposition(self.snake[n - 1].position())

        self.snake[0].forward(MOVE_DISTANCE)
