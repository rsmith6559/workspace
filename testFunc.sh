#!/bin/bash


function test()
{
	for arg in "$@"
	do
		if [ -z $( echo $arg | egrep '=' ) ]
		then
			echo "$0:test.$arg"
		else
			kw=$( echo $arg | sed -E 's/^([[:alnum:]]+)\=[[:alnum:]]+$/\1/' )
			val=$( echo $arg | sed -E 's/^[[:alnum:]]+\=([[:alnum:]]+)$/\1/' )
			eval "$kw"="\"$val\""
		fi
	done
	PROG="$0"
}

#test cat dog ferret fish bird
test $@

echo $PROG
echo "roger == $roger"

exit 0

