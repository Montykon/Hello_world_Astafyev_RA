#!/bin/bash

for i in range {1..20}; do
	if [[ "$i" == "15" ]]; then 
        break
	elif [ $((i % 2)) -eq 1 ]; then
	echo "$i"
	fi
done
