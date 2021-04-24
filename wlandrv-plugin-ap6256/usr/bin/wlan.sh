#!/bin/sh
PATH=/bin:/usr/bin:/sbin:/usr/sbin

start()
{
        ifconfig wlan0 up
        sleep 0.3
}

stop()
{
        ifconfig wlan0 down
        sleep 0.3
}

softap()
{
        ifconfig wlan0 up
        sleep 0.3
}

rftest()
{
:
}

case $1 in
"start")
start
;;
"stop")
stop
;;
"softap")
softap
;;
"rftest")
rftest
;;
*)
echo wlan.sh [start] [stop] [softap] [rftest]
exit 1
;;
esac

