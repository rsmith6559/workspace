#!/bin/bash


for HOST in centos6 test2 centos8
do
	FOO=$( ssh "$HOST" <<-EOF
	yum -q check-update
	exit
	EOF
	) | egrep -v Activate

	if [ -n "$FOO" ]
	then
		echo "- $HOST"
		echo "$FOO"
	else
		echo "Nothing for $HOST"
	fi
	echo ""
done
