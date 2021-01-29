from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.update()
time.sleep(1)

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

    if snake.head.distance(food) < 10:
        food.new_location()
        scoreboard.increase_score()

screen.exitonclick()
