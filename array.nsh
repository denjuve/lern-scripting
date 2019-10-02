#!/bin/bash
ARRAY=($(docker ps -aq))
#"first" "second" "third" "4th")
count=0
for I in ${ARRAY[@]}; do
echo "Processing element: ${ARRAY[count]}"
count=$(( $count + 1 ))
done
