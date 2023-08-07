#Project 1(Grid Mesh)
#Start code here
import random
from turtle import *
screen = Screen()
screen.bgcolor(0, 0, 0)
t1 = Turtle()
t2 = Turtle()
turtles = [t1, t2]
turtle_width = 50
red = 255
green = 255
blue = 255
for turtle in turtles:
  turtle.pencolor(red, green, blue)
  turtle.width(turtle_width)
  turtle.speed(0)
for i in range(8):
  current_width = turtle_width
  for j in range(180):
    red = random.randint(10, 220)
    green = random.randint(10, 220)
    blue = random.randint(10, 220)
    t1.forward(3)
    t1.left(2)
    t1.pencolor(red, green, blue)
    t2.forward(3)
    t2.right(2)
    t2.pencolor(red, green, blue)
    if j < 90:
      current_width = current_width*.97
    elif j >= 90:
      current_width = current_width*1.03
    for turtle in turtles:
      turtle.width(current_width)
  for turtle in turtles:
    turtle.right(22.5)
