#!/bin/dash

echo This program is: $0

file_name=$2
number_of_lines=$5
P1=race
P2=car
P3=fv
palindrome=$P1$P2$P3

echo $palindrome
echo going to print the first $number_of_lines lines of $file_name