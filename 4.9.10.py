#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cjcordsen
#
# Created:     16/09/2025
# Copyright:   (c) cjcordsen 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import turtle

def draw_star (t,d):
    t.color("deeppink")
    for i in range(5):
        t.forward(d)
        t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(3)
tess.speed(.5)


size = 100
for f in range(5):
    draw_star(tess, size)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()




wn.mainloop()
