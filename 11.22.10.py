#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cjcordsen
#
# Created:     23/10/2025
# Copyright:   (c) cjcordsen 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def replace (s, old, new):

    orgin = s
    split = orgin.split(old)
    combine = new
    split = combine.join(split)
    print(split)



test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")