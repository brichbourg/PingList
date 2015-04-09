# PingList.py
### Author
Brantley Richbourg <brichbourg@gmail.com>

#Installation and Usage

1.) Clone repo:
	git clone 

2.) Edit ips.txt to populate with your list of random IP addresses you want to test.

	10.10.1.10
	10.10.1.20
	10.20.30.40
	...
	10.254.254.1	

3.) Run script

	sudo python pinglist.py ips.txt

## Notes

This script uses a variation of the Python Ping script (http://www.g-loaded.eu/2009/10/30/python-ping/).  This code is included in this repo and is imported by PingList.py.  The use of this script requires running PingList.py as root, hence the reason to run with sudo.

This script was created on MAC OS 10.10.2.  No other operating systems were tested.# PingList
