#Project 1(Dynamic Shapes)
#Start code here
from turtle import *
screen = Screen()
screen.bgcolor(255, 255, 255)
shapes = 8
sides = int(input("Enter the number of sides for each shape"))
x = 0
y = 0
counter = 0
colors = ["red", "blue", "green", "pink", "yellow", "orange", "purple", "light blue"]
turtle = Turtle()
turtle.shape("turtle")
turtle.color(colors[1])
for shape in range(shapes):
  turtle.color(colors[counter%shapes])
  x += 5
  y += 5
  turtle.forward(x)
  turtle.left(y)
  for side in range(sides):
    turtle.begin_fill() # your own code
    turtle.pendown()
    turtle.forward(40)
    angle = 180 - 180 * (sides - 2) / sides
    turtle.left(angle)
    turtle.forward(40)
    turtle.penup()
    turtle.end_fill() # your own code
  counter += 1
