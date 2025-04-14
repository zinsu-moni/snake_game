from turtle import Screen, Turtle
from snake import Snake
from food import Food
from function import Scoreboard
import time

# Global variable for the screen
screen = Screen()

def setup_screen():
    screen.clearscreen()           # Clear any previous objects
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)               # Turn off automatic updates

def create_start_text():
    start_text = Turtle()
    start_text.color("green")
    start_text.hideturtle()
    start_text.penup()
    return start_text

def show_start_screen():
    setup_screen()  # Clear screen and set up fresh
    start_text = create_start_text()
    start_text.goto(0, 0)
    start_text.write("CLICK TO START", align="center", font=("Courier", 24, "normal"))
    screen.update()
    # Bind the click event to start the game
    screen.onclick(lambda x, y: start_game())
    
def show_game_over():
    start_text = create_start_text()
    start_text.goto(0, -100)
    start_text.write("CLICK TO RESTART", align="center", font=("Courier", 24, "normal"))
    screen.update()
    # Bind the click event to restart the game
    screen.onclick(lambda x, y: start_game())

def start_game():
    # Disable further clicks during the game by removing any onclick binding
    screen.onclick(None)

    # Reset the screen for a new game
    setup_screen()

    # Initialize game objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Set up key bindings for the snake
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall
        if (
            snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280
        ):
            scoreboard.game_over()
            game_is_on = False
            show_game_over()

        # Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False
                show_game_over()

# Start with the welcome screen
show_start_screen()
screen.mainloop()
