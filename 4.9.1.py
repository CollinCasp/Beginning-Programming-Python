#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cjcordsen
#
# Created:     11/09/2025
# Copyright:   (c) cjcordsen 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import turtle
__import__("turtle").__traceable__ = False

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in range(4):
        t.color("deeppink")
        t.forward(sz)
        t.right(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

line = 40
size = 20
for i in range(5):
    draw_multicolor_square(tess, size)
    tess.penup()
    tess.left(180)
    tess.forward(10)
    tess.right(90)
    tess.forward(10)
    tess.right(90)
    tess.pendown()
    size = size +20


wn.mainloop()
