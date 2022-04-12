#!/usr/bin/python3.9

# get pre shared key
getPreSharedKey = input("What is the pre shared key:  ")
while not (len(getPreSharedKey) < 15):
   print ("You have entered an not so secret key Please try again.")
   getPreSharedKey = input("What is the pre shared key:  ")