#!/usr/bin/env python3

from turtle import *

from math import sin, radians

color("red", "yellow")

begin_fill()

n = 300
for i in range(n):
    v = 360 / n
    forward(100 * sin(radians(v)))
    left(v)

end_fill()
done()

# 1. Make the turtle draw a square

# 2. Make the turtle draw an n-sided figure, with all sides of size 100.

# 3. Ensure that the figure has the same size no matter the n.

# 4. Set n=300 and draw a circle :D.


