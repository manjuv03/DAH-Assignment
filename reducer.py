#!/usr/bin/python

import fileinput

count = 0
old_word = None

for line in fileinput.input():

    data = line.strip().split("\t")    

    if len(data) != 2:
        continue

    current_word, increment = data

    if old_word and old_word != current_word:
        print old_word, "\t", count
        old_word = current_word
        count = 0

    old_word = current_word
    count += int(increment)

if old_word != None:
    print old_word, "\t", count


