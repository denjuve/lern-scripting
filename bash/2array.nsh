#!/bin/bash
array=("aaa" "bbb" "ccc" "ddd")

count=0
for i in ${array[@]}; do
echo "Processing el $count: ${array[count]}"
count=$(( $count + 1 ))
done
