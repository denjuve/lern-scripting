#!/usr/bin/env python3.6

import argparse
parsevar = argparse.ArgumentParser(description='Search for words including partial word')
parsevar.add_argument('snippet', help='partial (or complete) string to search in words file')

arguments = parsevar.parse_args()
snippet = arguments.snippet.lower()

f = open('/usr/share/dict/words')
allwords = f.readlines()
#matches = []
#
#for myword in allwords:
#    if snippet in myword.lower():
#        matches.append(myword)

#matches = [myword for myword in allwords if snippet in myword.lower()]
print([myword for myword in allwords if snippet in myword.lower()])

#print(matches)
