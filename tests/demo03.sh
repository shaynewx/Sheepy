#!/bin/dash

pwd
ls
id
date

for n in one two three
do
    read line
    echo Line $n $line
done