#!/bin/bash

filetoread=array.nsh

lines=1
while read -r script; do
echo "line #${lines}: $script"
((lines=lines+1))
done < "$filetoread"
