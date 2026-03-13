#!/bin/bash

awk 'BEGIN {print "Студенты, набравшие больше 80: "} $2 > 80 {print $1}' students.txt
awk 'BEGIN {print "Студенты набравшие меньше 70"} $2 < 70 {print $1}' students.txt
awk '$NR == 1 {ptint $0}' students.txt
