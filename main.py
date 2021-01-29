from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")

snake = []
initial_x = 0

for n in range(3):
    segment = Turtle()
    segment.shape("square")
    segment.color("green")
    segment.setposition(x=initial_x, y=0)
    snake.append(segment)
    initial_x -= 20


screen.exitonclick()
