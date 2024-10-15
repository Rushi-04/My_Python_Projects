from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()

turtle.color("Red")
turtle.shape("classic")
turtle.shapesize(2)

def move_forward():
    turtle.forward(20)
def move_backward():
    turtle.backward(20)
def turn1():
    turtle.right(90)
def turn2():
    turtle.left(90)
def clean():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


    

screen.listen()
screen.onkey(key="6",fun=move_forward)
screen.onkey(key="4",fun=move_backward)
screen.onkey(key="8",fun=turn1)
screen.onkey(key="2",fun=turn2)
screen.onkey(key="c",fun=clean)
screen.exitonclick()
