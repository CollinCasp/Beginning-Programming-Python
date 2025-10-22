#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jrcol
#
# Created:     21/10/2025
# Copyright:   (c) jrcol 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

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

def count_e(text):
    count = 0
    for c in text:
        if c == "e":
            count += 1
    return(count)
    print(count)

def count_word(text):
    words = len(text.split())
    return words

text = """Oh first time we came in together Guess we the ones [Verse 1] Feeling cooler than the April breeze As we blow like the summer leaves Girl I'm just hanging around
        And I'll come back down When you choose to come visit me now The crazy thing about my treehouse It's always me bugging me out It's all of the beautiful sounds
        That keeps my mouth quiet 'Cause me, I be into some loud [Chorus] One glad morning I'll be waiting With my lighter, to blaze (to blaze) Till that evening You
        come over And let me take you away Yeah [Interlude] I come out to the four pops Singing songs to the trees So I'm up in the city Smoke that sweet Virginia
        breeze See rap shows near New York Get tickets as low as $186 You might also like Workaholic DRAM 100% DRAM Broccoli DRAM [Verse 2] Girl it's looking so
        nice out Thinking maybe we can step out And give all the city a stroll And we can talk about the places where we want to go 'Cause baby I got big dreams
        Hollywood and the movie screens Millions of fans all for me With cars passing by and me hearing them play my CD [Chorus] One glad (one glad) morning
        (morning) You'll be (you'll be) waiting (waiting) With your (with your) lighter (lighter) to blaze (to light up) Till that (till that) evening (evening)
        I'll come (I'll come) over (over) And let you take me away Yeah [Verse 3] Fuck girl let's get so high that it casts on to the moon (to the moon babe)
        When we get back to daylight we can just keep our mood All I wish is you'll still be here when I get off tour When I get back we'll get higher than ever
        before [Bridge] Real love, feel love, taste love, smoke love Real love (real love) Feel love (feel love) Taste love (taste love) Smoke love (smoke love)
        Real love, feel love, taste love, smoke love Real love (real love) Feel love (feel love) Taste love (taste love) Smoke love (smoke love) Taste love, taste
        love, smoke love, smoke love [Outro] Ohh, ohh, ohh, ohh"""

clean = remove_punctuation(text)

total = count_word(clean)

e_word = count_e(clean)

percentage = (e_word / total) * 100

test(remove_punctuation('"Well, I never did!", said Alice.') == "Well I never did said Alice")
test(remove_punctuation("Are you very, very, sure?") == "Are you very very sure")
print(count_word("bananna"))


print(f'Your text contains {total} words, of which {e_word} ({percentage:.1f}%) contain an "e".')
