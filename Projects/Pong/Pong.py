from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball_1 = Ball()
score = Scoreboard() 


screen = Screen()
#Setting up the Screen
screen.listen()
screen.setup(width= 800, height = 600)  
screen.bgcolor("black")
screen.title("Welcome To Pong")
screen.onkey(fun=r_paddle.move_up,key=8)
screen.onkey(fun=r_paddle.move_down,key=2)
screen.onkey(fun=l_paddle.move_up,key="w")
screen.onkey(fun=l_paddle.move_down,key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball_1.move_speed)
    screen.update()
    ball_1.move()
    
    #Collision with walls
    if ball_1.ycor()>280 or ball_1.ycor()<-280:
        ball_1.bounce_y()
    if ball_1.xcor()>380 or ball_1.xcor()<-380:
        ball_1.bounce_x()
    
    #detecting Collision
    if ball_1.xcor()> 370 or ball_1.distance(r_paddle)<50:
        ball_1.bounce_x()
    if ball_1.xcor()<-370 or ball_1.distance(l_paddle)<50:
        ball_1.bounce_x()
    
    #Detect a miss (right)
    if ball_1.xcor() > 360:
        ball_1.reset_position()
        ball_1.bounce_x()
        ball_1.move_speed = 0.1
        score.l_point()
        
    
    #Detect a miss (Left)
    if ball_1.xcor() < -360:
        ball_1.reset_position()
        ball_1.bounce_x()
        score.r_point()
    
    # if score.l_point() ==5 or score.r_point() ==5:
    #     game_is_on = False
    #     print("Game Over")
screen.exitonclick()