#!/bin/bash
url=$1
offset=$2
interval=$3

function getLength() {

	url=$1
	ret=`curl -s -I -X HEAD $url | awk '/Content-Length:/ {print $2}'`
	echo $ret | sed 's/[^0-9]*//g'
}

function print() {

	url=$1
	offset=$2
	length=$3

	curl --header "Range: bytes=$offset-$length" -s $url
}

length=`getLength $url`
off=$((length - offset))


until [ "$off" -gt "$length" ]; do
	len=`getLength $url`

	if [ "$off" -eq "$len" ]; then
		sleep $interval
	else
		print $url $off $len
	fi

	off=$len
done
