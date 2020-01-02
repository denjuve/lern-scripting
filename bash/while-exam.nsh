#!/bin/bash

echo "Enter number:"
read ENTEREDNUM

i=1
while [ $i -le $ENTEREDNUM ]; do
echo "Message $i"
((i=i+1))
done

