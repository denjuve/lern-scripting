#!/usr/bin/env python3.6

import argparse

#build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
# ^This parser
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='Limit of lines')
parser.add_argument('--version', '-v',  action='version', version='%(prog)s 1.0')


#parse the arguments
args = parser.parse_args()
# ^ this args
print(args)


#read file reverse the contents and print
# error catching is if
try:
    f = open(args.filename)
except FileNotFoundError as error1:
#      ^ catching specific error
    print(f"ERROR: {error1}")
#except:
## ^catching any error
else:
    with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse()
    
        if args.limit:
            lines = lines[:args.limit]
    
        for line in lines:
            print(line.strip()[::-1])
finally:
    print(f"Finally - Print message regardless sucssseed or failed")
