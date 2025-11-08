#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jrcol
#
# Created:     08/11/2025
# Copyright:   (c) jrcol 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def make():
    myfile = open("test.txt", "w")
    myfile.write("My first file written from Python\n")
    myfile.write("---------------------------------\n")
    myfile.write("Hello, world!\n")
    myfile.close()

make()

def read():
    mynewhandle = open("test.txt", "r")
    while True:                            # Keep reading forever
        theline = mynewhandle.readline()   # Try to read next line
        if len(theline) == 0:              # If there are no more lines
            break                          #     leave the loop


        #print(theline, end="")
    print ("File Read")
    mynewhandle.close()

read()

def readlines():
    mynewhandle = open("test.txt", "r")
    reverse = open ("reverse.txt", "w")
    while True:
        theline = mynewhandle.readline()
        if len(theline) == 0:
            break

        words = theline.split()
        words.reverse()
        theline = " ".join(words) + "\n"

        reverse.write(theline)
        #print(theline, end="")
    print ("reverse.txt File Created")

    mynewhandle.close()

readlines()