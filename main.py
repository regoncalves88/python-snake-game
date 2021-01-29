from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = []
initial_x = 0

for n in range(3):
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    new_segment.setposition(x=initial_x, y=0)
    snake.append(new_segment)
    initial_x -= 20

screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.3)

    for n in range(len(snake) - 1, 0, -1):
        snake[n].setposition(snake[n - 1].position())

    snake[0].forward(20)

screen.exitonclick()
