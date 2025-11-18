#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jrcol
#
# Created:     17/11/2025
# Copyright:   (c) jrcol 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import string

#Alice’s_Adventures_in_Wonderland.txt

word_counts = {}

def remove_punctuation(s):                                          #Used in previous Homework
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def no_numbers(word,count_dict):                                                   #Function created to get rid of numbers
    if word.isalpha():
        count_dict[word] = count_dict.get(word, 0) + 1


def read():
    alice = open ("Alice’s_Adventures_in_Wonderland.txt", "r")      #Opens the file
    for line in alice:
        for word in line.split():
            word = word.translate(str.maketrans('', '', string.punctuation))
            word = word.lower()
            no_numbers(word,word_counts)

            if word:
                  word_counts[word] = word_counts.get(word, 0) + 1  #Counts the words
    alice.close()

def write():
    new_file = open ("alice_words.txt", "w")
    for word in sorted(word_counts.keys()):
        new_file.write(f"{word}: {word_counts[word]}\n")
    new_file.close()

read()
write()

print ("New file created alice_words with completed results")

