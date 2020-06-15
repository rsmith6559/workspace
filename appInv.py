#!/usr/bin/python

# Copyright 2013, Roger Smith
#
# Script to report the hostname and software version numbers of
# Mac OS 10.15 machines. Sent to a master, it creates a flat file
# database of all the softwares and their versions on all the machines.
#

import sys, os, time, re, commands, string
#from ftplib import FTP

# Configurable variable
#ftpServer = 'im.ipservice.com'
#
# Non-configurable variables
#
os.putenv( 'PATH', '/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin' )
host = commands.getstatusoutput( 'hostname -s' )[1]
#
#
# Put the app info into a tmp file
os.system( "system_profiler SPInstallHistoryDataType | egrep '(.*\:$|Version|Install Date)' | egrep -v 'Installations' > %s" % host )

#  Open the file for processing
try:
	infile = open( host, 'r' )
except:
	sys.stderr.write( 'host failed to open\n' )
	sys.exit( 2 )

# Create a dictionary of dictionaries to format the installed time, name
# of the software, and the version number from the raw output in host.
#
apps = {}
version = ""
verPattern = re.compile( " \(?[0-9\.-]{2,}\)?" )
line = string.lstrip( infile.readline() )
while( line ):
	if( re.match( ".*:$", line ) ):
		#  we have a software name line
		#  is the version number in the name?
		if( re.search( verPattern, line ) ):
			version = re.search( verPattern, line ).group( 0 )
			swName = re.sub( verPattern, '', line )
		else:
			swName = line

	if( re.match( "Version", line ) ):
		#  we have a version line
		version = line.split( ": " )[ 1 ]
		version = version[ :-1 ]

	if( re.match( "Install Date", line ) ):
		#  we have an installed line
		instTime = line.split( ": " )[ 1 ]
		instTime = instTime[ :-1 ]
		installed = time.mktime( time.strptime( instTime, "%m/%d/%y, %H:%M" ) )
		#  create our dict of dicts
		swName = swName[ :-1 ]
		#  does the key exist already?
		if( apps.has_key( swName ) ):
			#  if this is newer, just update version & installed
			if( apps[ swName ][ "installed" ] < installed ):
				apps[ swName ][ "installed" ] = installed
				apps[ swName ][ "version" ] = version
		else:
			# create a new dict from scratch
			apps[ swName ] = {}
			apps[ swName ][ "installed" ] = installed
			apps[ swName ][ "swName" ] = swName
			apps[ swName ][ "version" ] = version
		#  clean up
		swName = ""
		version = ""
		installed = ""

	line = string.lstrip( infile.readline() )

infile.close()

#  write the software name, version, installation and a couple of special
#  lines to a file that can be trnsferred to a server to be used
try:
	outfile = open( host, 'w' )
except:
	sys.stdout.write( "Couldn't open file for writing!\n" )
	sys.exit( 3 )

#  start with hostname and IP
outfile.write( "Hostname: %s\n" % host )
outfile.write( "IP: %s\n\n" % ( commands.getstatusoutput( 'ipconfig getifaddr en0' )[1] ) )

#  then our softwares
for key in apps.keys():
	line = "%s %s, %s\n" % ( apps[ key ][ "swName" ], apps[ key ][ "version" ], apps[ key ][ "installed" ] )
	outfile.write( line )

#  output the raw output of the hardware & system software profiles
outfile.write( "%s\n" % commands.getstatusoutput( 'system_profiler SPHardwareDataType' )[1] )
outfile.write( "%s\n" % commands.getstatusoutput( 'system_profiler SPSoftwareDataType' )[1] )

outfile.flush()
outfile.close()

# FTP the processed list of apps
#infile = open( host, 'r' )
#ftp = FTP( ftpServer )
#ftp.connect( ftpServer )
#ftp.login( 'mac', 'MacUser' )
#ftpCommand = 'STOR appInv/%s' %( hostname )
#ftp.storlines( ftpCommand, infile )
#ftp.quit()
#infile.close()

# Clean up and exit
#os.remove( host )

sys.exit( 0 )

