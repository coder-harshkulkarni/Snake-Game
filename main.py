from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

SNAKE_SIZE = 20

screen = Screen()
screen.setup(width=.75, height=.75)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard(((screen.window_height() / 2) - (SNAKE_SIZE+SNAKE_SIZE)))

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game_continue = True

while is_game_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_tail()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (snake.head.xcor() > (screen.window_width() / 2 - SNAKE_SIZE) or
            snake.head.xcor() < -(screen.window_width() / 2 - SNAKE_SIZE) or
            snake.head.ycor() > (screen.window_height() / 2 - SNAKE_SIZE) or
            snake.head.ycor() < -(screen.window_height() / 2 - SNAKE_SIZE)):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
