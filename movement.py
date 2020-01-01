import turtle

# Square
import math
from random import random

sarosh_turtle = turtle.Turtle()
sarosh_turtle.speed(100)


def square(x, y):
  sarosh_turtle.forward(x)
  sarosh_turtle.right(y)
  sarosh_turtle.forward(100)
  sarosh_turtle.right(90)
  sarosh_turtle.forward(100)
  sarosh_turtle.right(x)
  sarosh_turtle.forward(y)

def rectangle():
  sarosh_turtle.forward(300)
  sarosh_turtle.right(100)
  sarosh_turtle.forward(300)
  sarosh_turtle.right(100)
  sarosh_turtle.forward(300)
  sarosh_turtle.right(100)
  sarosh_turtle.forward(300)

"""
square()
sarosh_turtle.forward(200)
square()
"""
elephant_weight = 3000
ant_weight = 0.1
"""
if elephant_weight > ant_weight:
    square()

sarosh = "happy"
while sarosh == "happy":  # "==" is when you check 2 things
  sarosh_turtle.forward(10)
"""

# for i in range(6):
#    print(i)

for count in range(200):
    square(random() * 10, random() * 2)
