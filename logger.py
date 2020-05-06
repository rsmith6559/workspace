#!/usr/bin/python3.6

import logging
import logging.handlers

syslog = logging.getLogger( __name__ )
syslog.setLevel( logging.DEBUG )
syslog.addHandler( logging.handlers.SysLogHandler( address="/dev/log" ) )

syslog.warning( "Hello SYSLOG:WARN World!" )

