# Author: Brantley Richbourg <brichbourg AT gmail.com>
#Used Python Pure Ping -  http://www.g-loaded.eu/2009/10/30/python-ping/
#Python Ping imported at 'pure ping'

import os
import sys
import pureping

args = sys.argv

if len(args) == 2:


	if os.path.exists(args[1]):
		switch_ips = open(args[1]).read().splitlines()
		print '\nIP addresses are ', switch_ips
		print "=" * 25
		print "START PING TEST"
		print "=" * 25

		for each in switch_ips:
			testip = pureping.do_one(each,1)
			if testip == None:
				print each, "is dead."
			else:
				print '*', each, "IS ALIVE!!!"
						
		print "=" * 25
		print "END PING TEST"
		print "=" * 25

	else:
		print 'File, ', os.path.realpath(args[1]), 'does not exist.  Please try again.'

else:
	print 'ERROR: Invalid syntax\n'\
	'Example: \"sudo python pinglist.py file.txt\"'
	sys.exit(1)

