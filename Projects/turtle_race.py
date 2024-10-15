import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=500,height=600)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
colors = ["red","black","orange","yellow","green","blue"]
speed = [10,20,10,10,20,10,20]

all_turtles = []
def create_turtle(name:str,y_cord:int,no):
    name = Turtle(shape="turtle") 
    name.shapesize(1)
    name.penup()
    name.goto(-230,y_cord)
    name.color(colors[no])
    all_turtles.append(name)
    

name = ["t1","t2","t3","t4","t5","t6"]
loc = [-100,-60,-20,20,60,100]
for i in range(6):
    create_turtle(name[i],loc[i],i)
    
    
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 210:
          is_race_on = False
          winning_color = turtle.pencolor()
          if winning_color == user_bet:
              print(f"You won ! The {winning_color} Turtle is the winner")
          else:
              print(f"You loose ! The {winning_color} Turtle is the winner")
              
           
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    
screen.listen()
screen.exitonclick()