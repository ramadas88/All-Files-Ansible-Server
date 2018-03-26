#!/bin/bash

thisstring="1 2 3 4 8 9  5"

searchstring="8 9"

if `echo ${thisstring} | grep "${searchstring}" 1> /dev/null 2>&1 `

then
	echo "true"
else
	echo "False "
fi
