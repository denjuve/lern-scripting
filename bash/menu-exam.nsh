#!/bin/bash

clear
echo "Menu"
echo "---------------"
echo""
echo "1) Punkt Odin"
echo "2) Punkt Dwa"
echo "3) Punkt Tri"
echo "---------------"
echo "Make your choise"

read CHOISE

case $CHOISE in
1)
echo "You chose Punkt one";;
2)
echo "You chose Punkt two";;
3)
echo "You chose Punkt three";;
*)
echo "You chose wrong Punkt";;
esac
