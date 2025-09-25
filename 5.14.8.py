#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      cjcordsen
#
# Created:     23/09/2025
# Copyright:   (c) cjcordsen 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import turtle

xs = [48, 117, 200, 240, 160, 260, 220]

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)
if xs == 200:
    tess.color("yellow", "yellow")
else:
    tess.color("blue", "red")


for v in xs:
    draw_bar(tess, v)

wn.mainloop()
