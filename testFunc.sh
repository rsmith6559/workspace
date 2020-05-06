#!/bin/bash

function test()
{
	for word in "$@"
	do
		echo "test.$word"
	done
}

test cat dog ferret fish bird

exit 0

