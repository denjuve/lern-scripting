#!/bin/bash
#env | grep [USER|HOME|HISTCON|TERM]


#export STARTOFSCRIPT=$(date)
#export MYUSERNAME=myuser
#export MYPASSWORD=pswd
#sleep 1
#export ENDOFSCRIPT=$(date)
#
#env | grep -E 'OFSCRIPT|MY'

echo "enter name"
read firstname
echo "name is $firstname"

echo "enter age"
read age
echo "age is $age"
echo "age after 10 years is: $(( $age + 10 ))"
