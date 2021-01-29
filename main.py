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

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Eat food and grow
    if snake.head.distance(food) < 10:
        food.new_location()
        scoreboard.increase_score()
        snake.extend()

    # Hit the Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        scoreboard.game_over()

    # Hit the Tail
    for segment in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
