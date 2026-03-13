#!/bin/bash

check_root () {
	if [ "$EUID" -ne "0" ]; then
		echo "ERROR. Вы не суперпользователь, идите отсуда!"
		exit
	else
		echo "О, да вы суперпользователь, проходите!"
		fi
}
check_root
