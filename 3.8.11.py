#-------------------------------------------------------------------------------
# Name:        3.8.11
# Purpose:
#
# Author:      cjcordsen
#
# Created:     09/09/2025
# Copyright:   (c) cjcordsen 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import turtle

wn = turtle.Screen()
wn.title("Fading Spiral")
turtle.colormode(1.0)
# turtle.color (0,0,0)

tess = turtle.Turtle()
tess.pensize(3)


size = 200
for i in range(5):
   tess.forward(size)
   tess.right(144)






wn.mainloop()