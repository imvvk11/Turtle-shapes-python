import turtle
from turtle import color

my_turtle = turtle.Turtle()
my_turtle = turtle.color("blue")
my_turtle =turtle.bgcolor("green")
my_turtle = turtle.speed(0)

def square(length, angle):
    for i in range(4):
        my_turtle = turtle.forward(length)
        my_turtle = turtle.right(angle)
square(100, 90)

for i in range(150):
    square(100, 90)
    my_turtle = turtle.right(11)
