#!/usr/bin/python

import string
import fileinput

def remove_punctuation(s):
    return s.translate(string.maketrans("",""), string.punctuation)


words = []
for line in fileinput.input():
    for word in remove_punctuation(line.strip().lower()).split():
        print "{0}\t1".format(word)
