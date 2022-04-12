#!/usr/bin/python3
"""
import tkinter as tk

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()
"""
# password is less than 15 characters
#if (len(getPreSharedKey) < 15):

# password has less than 2 digits
#for i in getPreSharedKey:
#	if i.isdigit() < 2:

while True:
	try:
		upperCaseCharacters = 0
		
		print ("Password needs to be at least 15 characters")
		print ("Password needs to contain at least 2 digits")
		print ("Password needs to contain at least 2 uppercase characters")
		
		getPreSharedKey = input("What is the pre shared key:  ")
		print ("1")
		for i in getPreSharedKey:
			print ("2")
			if i.isupper():
				print ("3")
				upperCaseCharacters = upperCaseCharacters + 1
				if upperCaseCharacters <= 2:
					print ("4")
					print ("You have entered less than 2 numbers")
					getPreSharedKey = input("What is the pre shared key:  ")
	except Exception as e:
		print(e)
		continue
	else:
		break

print ("Pre shared key is: ", getPreSharedKey)


