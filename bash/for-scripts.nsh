#!/bin/bash

scriptlist=$(ls *.nsh)

for scripts in $scriptlist; do
echo "Begin $scripts"
echo ""
cat $scripts
echo "End $scripts"
done
