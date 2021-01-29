from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.update()
time.sleep(1)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.3)

    snake.move()

screen.exitonclick()
