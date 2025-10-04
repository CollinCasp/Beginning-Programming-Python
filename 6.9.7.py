#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jrcol
#
# Created:     01/10/2025
# Copyright:   (c) jrcol 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import sys

def to_secs(h,m,s):   # Buggy version
#Have to caculate total seconds
    total = h * 3600 + m * 60 + s
    return total

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

test_suite()