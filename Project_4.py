#Project 4(Rock Paper Scissors)
#Start code here
from turtle import *
import random
screen = Screen()
screen.bgcolor("cyan")
turtle = Turtle()
turtle.color("black")
turtle.shape("turtle")
def make_rock(x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.color("grey")
  turtle.width(30)
  turtle.pendown()
  turtle.begin_fill() # your own code
  turtle.circle(50)
  turtle.end_fill() # your own code
  turtle.penup()
def make_paper(x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.color("white")
  turtle.begin_fill() # your own code
  turtle.pendown()
  turtle.forward(90)
  turtle.right(90)
  turtle.forward(120)
  turtle.right(90)
  turtle.forward(90)
  turtle.right(90)
  turtle.forward(120)
  turtle.right(90)
  turtle.end_fill() # your own code
  turtle.penup()
def make_scissors(x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.color("red")
  turtle.width(10)
  turtle.pendown()
  turtle.circle(10)
  turtle.color("black")
  turtle.right(10)
  turtle.forward(90)
  turtle.penup()
  turtle.goto(x, y-30)
  turtle.color("red")
  turtle.pendown()
  turtle.circle(10)
  turtle.left(10)
  turtle.left(10)
  turtle.penup()
  turtle.goto(x, y-10)
  turtle.color("black")
  turtle.pendown()
  turtle.forward(90)
  turtle.right(10)
  turtle.penup()
def handle_player_move(move):
  if move=="rock":
    make_rock(-125, -50)
  elif move=="paper":
    make_paper(-175, 65)
  elif move=="scissors":
    make_scissors(-175, 0)
def handle_comp_move(move):
  if move=="rock":
    make_rock(125, -50)
  elif move=="paper":
    make_paper(100, 65)
  elif move=="scissors":
    make_scissors(100, 0)
wins = 0
losses = 0
ties = 0
while True:
  player_move = input("Please enter rock, paper, or scissors")
  comp_move = random.randint(1, 3)
  if comp_move==1:
    comp_move = "rock"
  elif comp_move==2:
    comp_move = "paper"
  elif comp_move==3:
    comp_move = "scissors"
  turtle.clear() # your own code
  handle_player_move(player_move)
  handle_comp_move(comp_move)
  if player_move=="rock" and comp_move=="scissors" or player_move=="scissors" and comp_move=="paper" or player_move=="paper" and comp_move=="rock":
    wins += 1
  elif comp_move=="rock" and player_move=="scissors" or comp_move=="scissors" and player_move=="paper" or comp_move=="paper" and player_move=="rock":
    losses += 1
  elif player_move==comp_move:
    ties += 1
  turtle.goto(-100, 100)
  turtle.color("black")
  turtle.write(("Wins: " + str(wins) + "   Losses: " + str(losses) + "   Ties: " + str(ties)), font=("Ariel", 12, "normal")) # your own code
