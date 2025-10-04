#-------------------------------------------------------------------------------
# Name:        module1
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

def days_of_week(day):
    if day == 0:
        print ("Today is Sunday")
    elif day == 1:
        print ("Today is Monday")
    elif day == 2:
        print ("Today is Tuesday")
    elif day == 3:
        print ("Today is Wednesday")
    elif day == 4:
        print ("Today is Thursday")
    elif day == 5:
        print ("Today is Friday")
    elif day == 6:
        print ("Today is Saturday")
    else:
        print ("Invalid Number")

day = int(input("Input Number Between 0 - 6"))

print(days_of_week(day))
