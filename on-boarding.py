#!/usr/bin/python3

"""
	File to automate the command generation of the on-boardings onBoardingFiler the ASA
	version 1 of the file
	created by Jacob Wheeler
"""

"""
things to do:
	figure out how get to subnet mask with verification
	make sure pre shared key is complex
"""

import ipaddress

SGService = "FTIH-SG-"
ERNumber = "ER"
subnetMask = "255.255.255.255"
VERSION = "1.0"

acyInterfaces = ["10.10.10.10", "internet", "11.11.11.11", "internet1",
                 "12.12.12.12", "internet5", "13.13.13.13", "internet6"]

oexInterfaces = ["20.20.20.20", "internet", "21.21.21.21", "internet1",
                 "22.22.22.22", "internet5", "23.23.23.23", "internet6"]

acyInternetInterfaces = ["10.10.10.10", "12.12.12.12"]

oexInternetInterfaces = ["20.20.20.20", "22.22.22.22"]

for i in range(1,2):
	print ()

print ("Welcome to the on-boarding creation script for ASA's")
print ("We are running version", VERSION, "of this script")

for i in range(1,2):
	print ()

# get user who is building this flow out
getUserName = input("What is your name: ")

# get Customer Name
getCustomerName = input("What is the customer name: ie Delta/Southwest ")

# get Program Name
getProgramName = input("What is the program name: ie NEMS/WMSCR  ")

# get ER Number
print ("Please enter the 6 digit number")
getERNumber = input("What is the ER number: ")
while len(getERNumber) != 6 or (not getERNumber.isdigit()):
    print ('Not a 6 digit number')
    getERNumber = input("What is the ER number: ")

# get the SG Service
print ("Please enter the 6 digit number")
getSGService = input("What is the SG Service: ")
while len(getSGService) != 6 or (not getSGService.isdigit()):
    print ('Not a 6 digit number')
    getSGService = input("What is the SG Service: ")

# get TSB Number
getTicketNumber = input("What is the TSB number: ")
while len(getTicketNumber) != 13 or (not getTicketNumber.isdigit()):
    print ('Not a 13 digit number')
    getTicketNumber = input("What is the TSB number: ")

NESGLocation = input("What is the NESG location: ").upper()
while not (NESGLocation == "ACY" or NESGLocation == "OEX"):
    print ('Not a valid location')
    NESGLocation = input("What is the NEGS location: ").upper()

for i in range(1,2):
	print ()
 
# get FTI crypto IP for ACY
if NESGLocation == "ACY":
   while True:
       try:
           acyFTICryptoIP = input(NESGLocation + " FTI Crypto IP: ")
           ipaddress.ip_address(acyFTICryptoIP)
           while not acyFTICryptoIP in acyInterfaces:
              print ("IP not in ACY Internet crypto list")
              acyFTICryptoIP = input(NESGLocation + " FTI Crypto IP: ")
              ipaddress.ip_address(acyFTICryptoIP)
       except ValueError:
           print ("FTI Crypto IP not valid. Please try again.")
           continue
       else:
           break
   acyInterfacesNameIndex = (acyInterfaces.index(acyFTICryptoIP) + 1)
   acyInterfacesNextHopIndex = (acyInterfaces.index(acyFTICryptoIP) + 2)
   acyInterfacesCryptoMapIndex = (acyInterfaces.index(acyFTICryptoIP) + 3)

# get FTI crypto IP for OEX
if NESGLocation == "OEX":
   while True:
       try:
           oexFTICryptoIP = input(NESGLocation + " FFTI Crypto IP: ")
           ipaddress.ip_address(oexFTICryptoIP)
           while not oexFTICryptoIP in oexInterfaces:
              print ("IP not in OEX Internet crypto list")
              oexFTICryptoIP = input(NESGLocation + " FFTI Crypto IP: ")
              ipaddress.ip_address(oexFTICryptoIP)
       except ValueError:
           print ("FTI Crypto IP not valid. Please try again.")
           continue
       else:
           break
   oexInterfacesNameIndex = (oexInterfaces.index(oexFTICryptoIP) + 1)
   oexInterfacesNextHopIndex = (oexInterfaces.index(oexFTICryptoIP) + 2)
   oexInterfacesCryptoMapIndex = (oexInterfaces.index(oexFTICryptoIP) + 3)


# get end user crypto IP
while True:
    try:
        EndUserCryptoIP = input("End User Crypto IP: ")
        ipaddress.ip_address(EndUserCryptoIP)
    except ValueError:
        print ("End User Crypto IP not valid. Please try again.")
        continue
    else:
        break

# get end user client IP(s)
getNumberOfClientIPs = input("How many client IP's do they have: ")
while not getNumberOfClientIPs.isdigit(): 
    print ('Not a number')
    getNumberOfClientIPs = input("How many client IP's do they have: ")

# change input from string to digit
getNumberOfClientIPsNumber = int(getNumberOfClientIPs)

EndUserClientIP = []

while True:
	try:
		for i in range(0, getNumberOfClientIPsNumber):
			ClientIP = input("End User Client IP: ")
			ipaddress.ip_address(ClientIP)
			EndUserClientIP.append(ClientIP)
	except ValueError:
		print ("End User Client IP not valid. Please try again.")
		continue
	else:
		break

# get dst IP(s)
getNumberOfDSTIPs = input("How many dst IP's do they have: ")
while not getNumberOfDSTIPs.isdigit(): 
    print ('Not a number')
    getNumberOfDSTIPs = input("How many dst IP's do they have: ")

# change input from string to digit
getNumberOfDSTIPsNumber = int(getNumberOfDSTIPs)

EndUserDSTIP = []

while True:
	try:
		for i in range(0, getNumberOfDSTIPsNumber):
			DSTIP = input("End User DST IP: ")
			ipaddress.ip_address(DSTIP)
			EndUserDSTIP.append(DSTIP)
	except ValueError:
		print ("End User DST IP not valid. Please try again.")
		continue
	else:
		break

# get crypto ACL Name
getCryptoACLName = input("What is the name of the crypto ACL:  ")

for i in range(1,2):
	print ()

print ("Now we will get the crypto sequence number for the crypto map.")
print ("issue the command show run crypto and find the next number avaiable on the interface that the crypto will go on.")
# get the crypto sequence number
print ("Please enter the 2 or 3 digit sequence number: ")
getSequenceNumber = input("What is the sequence number: ")
while len(getSequenceNumber) > 3 or (not getSequenceNumber.isdigit()):
    print ('Not a 2 or 3 digit sequence number')
    getSequenceNumber = input("Please enter the 3 digit sequence number: ")

for i in range(1,2):
	print ()

# get pre shared key
getPreSharedKey = input("What is the pre shared key:  ")
while not (len(getPreSharedKey) < 15):
   print ("You have entered an not so secret key Please try again.")
   getPreSharedKey = input("What is the pre shared key:  ")


isNemsFlow = input("Is this a NEMS flow at ACY or OEX? (yes or no) ").lower()
while not (isNemsFlow == "yes" or isNemsFlow == "no"):
   isNemsFlow = input("Is this a NEMS flow at ACY or OEX? (yes or no) ").lower()         


for i in range(1,3):
	print ()

# Open a file
onBoardingFile = open("foo.txt", "w")

onBoardingFile.write(getUserName + " created this config" + "\n")
onBoardingFile.write("Customer name is: "+ getCustomerName + "\n")
onBoardingFile.write("Program name is: "+ getProgramName + "\n")
onBoardingFile.write("ER number is: " + ERNumber + getERNumber + "\n")
onBoardingFile.write("SG service is: " + SGService + getSGService + "\n")
onBoardingFile.write("The TSB number is: " + getTicketNumber + "\n")
onBoardingFile.write("\n")
onBoardingFile.write("\n")


onBoardingFile.write("End User Crypto IP is " + EndUserCryptoIP + "\n")

if NESGLocation == "ACY":
   onBoardingFile.write("FTI Crypto IP is " + acyFTICryptoIP + "\n")
elif NESGLocation == "OEX":
   onBoardingFile.write("FTI Crypto IP is " + oexFTICryptoIP + "\n")

for i in range(0, getNumberOfClientIPsNumber):
	onBoardingFile.write ("End User Client IP is " + EndUserClientIP[i] + "\n")
for i in range(0, getNumberOfDSTIPsNumber):
	onBoardingFile.write ("End DST Client IP is " + EndUserDSTIP[i] + "\n")

onBoardingFile.write("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + "\n")
onBoardingFile.write("Below is the commands that you can copy and paste into the ASA" + "\n")
onBoardingFile.write("\n")

for i in range(0, getNumberOfClientIPsNumber):
	for j in range(0, getNumberOfDSTIPsNumber):
		onBoardingFile.write("access-list" + " " + getCryptoACLName + " " + "extended permit ip host " + EndUserClientIP[i] + " host " + EndUserDSTIP[j] + "\n")
onBoardingFile.write("\n")

if NESGLocation == "ACY":
   onBoardingFile.write ("crypto map " + acyInterfaces[acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "match address " + getCryptoACLName + "\n")
   onBoardingFile.write ("crypto map " + acyInterfaces[acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set pfs group21" + "\n")
   onBoardingFile.write ("crypto map " + acyInterfaces[acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set peer " + EndUserCryptoIP + "\n")
   onBoardingFile.write ("crypto map " + acyInterfaces[acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
   onBoardingFile.write ("crypto map " + acyInterfaces[acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set security-association lifetime seconds 28800" + "\n")
   onBoardingFile.write("\n")
elif NESGLocation == "OEX":
   onBoardingFile.write ("crypto map " + oexInterfaces[oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "match address " + getCryptoACLName + "\n")
   onBoardingFile.write ("crypto map " + oexInterfaces[oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set pfs group21" + "\n")
   onBoardingFile.write ("crypto map " + oexInterfaces[oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set peer " + EndUserCryptoIP + "\n")
   onBoardingFile.write ("crypto map " + oexInterfaces[oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
   onBoardingFile.write ("crypto map " + oexInterfaces[oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set security-association lifetime seconds 28800" + "\n")
   onBoardingFile.write("\n")

onBoardingFile.write ("tunnel-group " + EndUserCryptoIP + " " + "type ipsec-l2l" + "\n")
onBoardingFile.write ("tunnel-group " + EndUserCryptoIP + " " + "ipsec-attributes" + "\n")
onBoardingFile.write ("   ikev2 remote-authentication pre-shared-key " + getPreSharedKey + "\n")
onBoardingFile.write ("   ikev2 local-authentication pre-shared-key " + getPreSharedKey + "\n")
onBoardingFile.write("\n")


if NESGLocation == "ACY":
   onBoardingFile.write ("route " + acyInterfaces[acyInterfacesNameIndex] + " " + EndUserCryptoIP + " " + subnetMask + " " + acyInterfaces[acyInterfacesNextHopIndex] + "\n")
   for i in range(0, getNumberOfClientIPsNumber):
      onBoardingFile.write ("route "+ acyInterfaces[acyInterfacesNameIndex] + " " + EndUserClientIP[i] + " " + subnetMask + " " +  acyInterfaces[acyInterfacesNextHopIndex] + "\n")
onBoardingFile.write("\n")

if NESGLocation == "OEX":
   onBoardingFile.write ("route " + oexInterfaces[oexInterfacesNameIndex] + " " + EndUserCryptoIP + " " + subnetMask + " " + oexInterfaces[oexInterfacesNextHopIndex] + "\n")
   for i in range(0, getNumberOfClientIPsNumber):
      onBoardingFile.write ("route "+ oexInterfaces[oexInterfacesNameIndex] + " " + EndUserClientIP[i] + " " + subnetMask + " " +  oexInterfaces[oexInterfacesNextHopIndex] + "\n")
onBoardingFile.write("\n")

if isNemsFlow == "yes":
	onBoardingFile.write ("object-group network NEMS-Client" + "\n")
	for i in range(0, getNumberOfClientIPsNumber):
		onBoardingFile.write ("   network-object object " + EndUserClientIP[i] + "\n")

# Close opend file
onBoardingFile.close()