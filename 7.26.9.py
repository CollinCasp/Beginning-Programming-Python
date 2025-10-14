#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cjcordsen
#
# Created:     09/10/2025
# Copyright:   (c) cjcordsen 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def  print_triangular_numbers(n):
    for i in range(1, n + 1):
        triangular = (i * (i + 1)) // 2     #Formula to get the second row of numbers to be correct
        print(i, "\t", triangular)
    print()

print_triangular_numbers(5)