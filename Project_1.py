#Project 1(Happy Birthday)
#Start code here
import time
def intro(name):
  print( "Hey " + name + ", it's your birthday today! Here is a little song:")
def song(name):
  time.sleep(2)
  for i in range(2):
    print("Happy Birthday to you!")
    time.sleep(1)
  print("Happy Birthday dear " + name + ",")
  time.sleep(1)
  print("Happy Birthday to you!")
def main():
  name = input("What is your name?")
  intro(name)
  song(name)
main()
