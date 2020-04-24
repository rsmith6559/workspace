#!/bin/bash


TXTFILE="./testHere2.txt"
HOST=""
PKGS=""

if [ ! -f "$TXTFILE" ]
then
	exit 1
fi

while read LINE
do
	if [[ -n $( echo "$LINE" | egrep '^- .*' ) ]]
	then
		HOST=$( echo "$LINE" | sed -e 's/^- //' )
		continue
	elif [[ -n $( echo "$LINE" | egrep '^.*$' ) ]]
	then
		PKGS="$PKGS $LINE"
		continue
	elif [ -z "$LINE" ] && [ -n "$HOST" ] && [ -n "$PKGS" ]
	then
#		ssh "$HOST" <<-EOF
#		yum -qy update "$PKGS"
#		exit
#		EOF
		echo "ssh $HOST"
		echo "yum -qy update $PKGS"
		echo -e "exit\n"
	else
		echo "What the hell???? $HOST $PKGS"
	fi
	HOST=""
	PKGS=""
done <"$TXTFILE"
