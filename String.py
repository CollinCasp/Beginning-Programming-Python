#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cjcordsen
#
# Created:     16/10/2025
# Copyright:   (c) cjcordsen 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import string
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def count_a(text):
    count = 0
    for c in text:
        if c == "a":
            count += 1
    return(count)
    print(count)

def count_word(text):
    words = len(text.split())
    return words

text = "Bannana"

test(remove_punctuation('"Well, I never did!", said Alice.') == "Well I never did said Alice")
test(remove_punctuation("Are you very, very, sure?") == "Are you very very sure")
test(count_a("banana") == 3)
print(count_word("bananna"))
print(count_a("bananna"))

print ("Your text contains",count_a(text) ,"words, of which 109 (44.8%) contain an ""e"".)
