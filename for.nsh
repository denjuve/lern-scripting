#!/bin/bash


#for LFILE in $(ls *.nsh)
#  do
#   chmod 0400 $LFILE
#  done

#!/bin/bash

LIST=$(ls )
DIRS=0
FILES=0

for LFILE in $LIST
do
if [ -d "$LFILE" ]; then
((DIRS=DIRS+1))
else
((FILES=FILES+1))
chmod +x $LFILE
fi
done
echo "$DIRS Dirs"
echo "$FILES Files"
ls -l
