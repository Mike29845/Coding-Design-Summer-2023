#Project 6(Connect 4)
from turtle import *
turtle = Turtle()
screen = Screen()
screen.setup(width=400, height=400, startx=None, starty=None)
turtle.hideturtle()
screen.tracer(False)
turtle.speed(0)

turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}

def board():
    screen.bgcolor('light blue')
    for x in range(-150, 200, 50):
        turtle.penup()
        turtle.goto(x, -200)
        turtle.pendown()
        turtle.goto(x, 200)
    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            turtle.penup()
            turtle.goto(x, y)
            turtle.dot(40, 'white')
            screen.update()

def click(x, y):
    player = state['player']
    rows = state['rows']
    col = int((x + 200) // 50)
    row = rows[col]
    x = col * 50 - 200 + 25
    y = row * 50 - 200 + 25
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(40, player)
    screen.update()
    rows[col] = row + 1
    state['player'] = turns[player]


board()
screen.onscreenclick(click)