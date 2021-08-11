from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time

# coordinates of blocks
BLOCK_X_COOR = [-340, -230, -120, -10, 100, 210, 320]
BLOCK_Y_COOR = [230, 205, 180, 155, 130]
block_list = []
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]


# step 4: function to load blocks on the screen
def load_blocks():
    for x in BLOCK_X_COOR:
        for y in BLOCK_Y_COOR:
            color = COLORS[BLOCK_Y_COOR.index(y)]
            block = Block(x, y)
            block.color(color)
            block_list.append(block)


# function to run game
def play_game(*args):
    game_on = True
    walls_number = 1
    # step 1: create screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("midnight blue")
    screen.title("Breakout")
    screen.tracer(0)  # turn turtle animation off

    paddle = Paddle((0, -250))
    ball = Ball()
    scoreboard = Scoreboard()

    load_blocks()

    valid_response = False
    play_text = "Do you want to play Breakout? (y/n)"
    while not valid_response:
        play = screen.textinput("Ready to play Breakout?", f"{play_text}").lower()
        if play == "y":
            valid_response = True
        elif play == "n":
            screen.bye()
        else:
            play_text = "Please enter a valid input (y/n). Try again."

    # step 2: bind paddle movements to key press events
    screen.listen()
    screen.onkeypress(paddle.move_left, "Left")
    screen.onkeypress(paddle.move_right, "Right")

    # turn turtle animation on for every nth screen update
    while game_on:
        time.sleep(ball.move_speed)     # specifying a sleep time of less than 1 will speed up game
        screen.update()     # update animations
        ball.move()

        # step 3: set conditions for ball movements
        if ball.ycor() >= 280:  # range: -300 to 300; ie. if ball is at the top wall
            ball.bounce_y()

        if ball.xcor() <= -380 or ball.xcor() >= 380:  # range: -400 to 400; ie. if ball is at the left or right wall
            ball.bounce_x()

        # if ball hits paddle
        if ball.distance(paddle) < 45 and ball.ycor() > -280:
            ball.bounce_paddle()
        for block in block_list:
            if ball.distance(block) < 50:
                screen.tracer(0)
                scoreboard.add_points(walls_number, block.ycor())
                block.goto(1000, 1000)  # remove block off screen if ball touches it
                ball.bounce_block()
                block_list.remove(block)
                if len(block_list) == 0:
                    if ball.move_speed > 0.015:
                        ball.move_speed -= 0.003    # ball increases a maximum of 5 times
                    ball.goto(x=0, y=-190)
                    ball.bounce_y()
                    load_blocks()
                    if walls_number <= 5:
                        walls_number += 1

        # detect when ball goes out of bounds
        if ball.ycor() < -280:
            ball.paddle_miss()
            scoreboard.deduct_balls()

        # detect when game is over
        if scoreboard.balls_left == 0:
            scoreboard.status_text = "Game Over!"
            scoreboard.reset_scoreboard()
            valid_response = False
            restart_text = "Do you want to restart? (y/n)"
            while not valid_response:
                restart = screen.textinput("Restart Game?", f"{restart_text}").lower()
                if restart == "y":
                    valid_response = True
                    screen.clearscreen()
                    play_game()
                elif restart == "n":
                    screen.bye()
                else:
                    restart_text = "Please enter a valid input (y/n). Try again."

    screen.mainloop()


play_game()