#!/bin/sh /etc/rc.common
 
START=20
STOP=20
 
start() {        
        echo start
	echo $! > /var/run/program.pid
        while true;
	do
		SIGNALSTRENGTH = iwinfo wlan0-adhoc-2 info | grep "Signal: " | xargs | cut -d " " -f 2;
		echo "drawLights(mapTo5(" $SIGNALSTRENGTH "))" > /dev/ttyS0;
		sleep 1;
	done &
}                 
 
stop() {          
        echo stop
}