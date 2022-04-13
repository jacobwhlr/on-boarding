from tkinter import *
from tkinter import ttk
import ipaddress

# Create the window
top_level_window = Tk()
top_level_window.geometry("600x350")
top_level_window.resizable(False, False)
top_level_window.title("Welcome to the on-boarding program")
row_level = 0

# Create the scroll bar
main_frame = Frame(top_level_window)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


"""
Menu bar
"""


def about_new_window():
    # Toplevel object which will be treated as a new window
    new_window = Toplevel(top_level_window)

    # sets the title of theToplevel widget
    new_window.title("About")

    # sets the geometry of toplevel
    new_window.geometry("200x200")

    # A Label widget to show in toplevel
    author_name = "Jacob"
    version_number = "1.0"
    Label(new_window, text=f"Author: {author_name}").grid(row=0, column=0, sticky="W")
    Label(new_window, text=f"Version: {version_number}").grid(row=1, column=0, sticky="W")


def hide_all_frames():
    about_program_frame.grid_forget()


my_menu = Menu(top_level_window)

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=top_level_window.quit)

help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_new_window)

about_program_frame = Frame(top_level_window)

# Get basic info
# get user who is building this flow out
get_user_name_label = Label(second_frame, text="What is your name: ")
get_user_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_user_name_entry = Entry(second_frame)
get_user_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get Customer Name
get_customer_name_label = Label(second_frame, text="What is the customer name: ")
get_customer_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_customer_name_entry = Entry(second_frame)
get_customer_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get Program Name
get_program_name_label = Label(second_frame, text="What is the program name: ")
get_program_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_program_name_entry = Entry(second_frame)
get_program_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# Get \er number
get_er_number_label = Label(second_frame, text="What is the ER number: ")
get_er_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_er_number_entry = Entry(second_frame)
get_er_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# Get sg number
get_sg_service_label = Label(second_frame, text="What is the SG Service: ")
get_sg_service_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_sg_service_entry = Entry(second_frame)
get_sg_service_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get TSB Number
get_ticket_number_label = Label(second_frame, text="What is the TSB number: ")
get_ticket_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_ticket_number_entry = Entry(second_frame)
get_ticket_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1


# Type of connection
def delete_text_connection(event):
    try:
        nesg_connection_type_entry.delete(0, END)
    except:
        pass


nesg_connection_type_label = Label(second_frame, text="Please select the type of connection:")
nesg_connection_type_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
nesg_connection_type_entry = Entry(second_frame)
nesg_connection_type_entry.insert(0, "Internet/ED6/DTS/DTE")
nesg_connection_type_entry.bind("<FocusIn>", delete_text_connection)
nesg_connection_type_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1


# Get NESG Location
def delete_text_location(event):
    try:
        nesg_connection_location_entry.delete(0, END)
    except:
        pass


nesg_connection_location_label = Label(second_frame, text="Please select the type of connection:")
nesg_connection_location_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
nesg_connection_location_entry = Entry(second_frame)
nesg_connection_location_entry.insert(0, "ACY/OEX/SLC/ATL")
nesg_connection_location_entry.bind("<FocusIn>", delete_text_location)
nesg_connection_location_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get end user crypto IP
end_user_crypto_ip_label = Label(second_frame, text="What is the customers crypto IP? ")
end_user_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_crypto_ip_entry = Entry(second_frame)
end_user_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get end user crypto IP
end_user_crypto_ip_label = Label(second_frame, text="What is the customers crypto IP? ")
end_user_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_crypto_ip_entry = Entry(second_frame)
end_user_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# Buttons to save to file or reset all fields
def save_to_file():
    sg_service = "FTIH-SG-"
    er_number = "ER"
    # Open a file
    on_boarding_file = open("foo.txt", "w")

    on_boarding_file.write(get_user_name_entry.get() + " created this config" + "\n")
    on_boarding_file.write("Customer name is: " + get_customer_name_entry.get() + "\n")
    on_boarding_file.write("Program name is: " + get_program_name_entry.get() + "\n")
    on_boarding_file.write("ER number is: " + er_number + get_er_number_entry.get() + "\n")
    on_boarding_file.write("SG service is: " + sg_service + get_sg_service_entry.get() + "\n")
    on_boarding_file.write("The TSB number is: " + get_ticket_number_entry.get() + "\n")
    on_boarding_file.write("\n")
    on_boarding_file.write("\n")
    #on_boarding_file.write("End User Crypto IP is " + end_user_crypto_ip_entry.get() + "\n")

    """
    for i in range(0, getNumberOfClientIPsNumber):
        onBoardingFile.write("End User Client IP is " + EndUserClientIP[i] + "\n")
    for i in range(0, getNumberOfDSTIPsNumber):
        onBoardingFile.write("End DST Client IP is " + EndUserDSTIP[i] + "\n")

    onBoardingFile.write("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + "\n")
    onBoardingFile.write("Below is the commands that you can copy and paste into the ASA" + "\n")
    onBoardingFile.write("\n")

    for i in range(0, getNumberOfClientIPsNumber):
        for j in range(0, getNumberOfDSTIPsNumber):
            onBoardingFile.write(
                "access-list" + " " + getCryptoACLName + " " + "extended permit ip host " + EndUserClientIP[
                    i] + " host " + EndUserDSTIP[j] + "\n")
    onBoardingFile.write("\n")

    if NESGLocation == "ACY":
        onBoardingFile.write("crypto map " + acyInterfaces[
            acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "match address " + getCryptoACLName + "\n")
        onBoardingFile.write("crypto map " + acyInterfaces[
            acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set pfs group21" + "\n")
        onBoardingFile.write("crypto map " + acyInterfaces[
            acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set peer " + EndUserCryptoIP + "\n")
        onBoardingFile.write("crypto map " + acyInterfaces[
            acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
        onBoardingFile.write("crypto map " + acyInterfaces[
            acyInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set security-association lifetime seconds 28800" + "\n")
        onBoardingFile.write("\n")
    elif NESGLocation == "OEX":
        onBoardingFile.write("crypto map " + oexInterfaces[
            oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "match address " + getCryptoACLName + "\n")
        onBoardingFile.write("crypto map " + oexInterfaces[
            oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set pfs group21" + "\n")
        onBoardingFile.write("crypto map " + oexInterfaces[
            oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set peer " + EndUserCryptoIP + "\n")
        onBoardingFile.write("crypto map " + oexInterfaces[
            oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
        onBoardingFile.write("crypto map " + oexInterfaces[
            oexInterfacesCryptoMapIndex] + " " + getSequenceNumber + " " + "set security-association lifetime seconds 28800" + "\n")
        onBoardingFile.write("\n")

    onBoardingFile.write("tunnel-group " + EndUserCryptoIP + " " + "type ipsec-l2l" + "\n")
    onBoardingFile.write("tunnel-group " + EndUserCryptoIP + " " + "ipsec-attributes" + "\n")
    onBoardingFile.write("   ikev2 remote-authentication pre-shared-key " + getPreSharedKey + "\n")
    onBoardingFile.write("   ikev2 local-authentication pre-shared-key " + getPreSharedKey + "\n")
    onBoardingFile.write("\n")

    if NESGLocation == "ACY":
        onBoardingFile.write(
            "route " + acyInterfaces[acyInterfacesNameIndex] + " " + EndUserCryptoIP + " " + subnetMask + " " +
            acyInterfaces[acyInterfacesNextHopIndex] + "\n")
        for i in range(0, getNumberOfClientIPsNumber):
            onBoardingFile.write(
                "route " + acyInterfaces[acyInterfacesNameIndex] + " " + EndUserClientIP[i] + " " + subnetMask + " " +
                acyInterfaces[acyInterfacesNextHopIndex] + "\n")
    onBoardingFile.write("\n")

    if NESGLocation == "OEX":
        onBoardingFile.write(
            "route " + oexInterfaces[oexInterfacesNameIndex] + " " + EndUserCryptoIP + " " + subnetMask + " " +
            oexInterfaces[oexInterfacesNextHopIndex] + "\n")
        for i in range(0, getNumberOfClientIPsNumber):
            onBoardingFile.write(
                "route " + oexInterfaces[oexInterfacesNameIndex] + " " + EndUserClientIP[i] + " " + subnetMask + " " +
                oexInterfaces[oexInterfacesNextHopIndex] + "\n")
    onBoardingFile.write("\n")

    if isNemsFlow == "yes":
        onBoardingFile.write("object-group network NEMS-Client" + "\n")
        for i in range(0, getNumberOfClientIPsNumber):
            onBoardingFile.write("   network-object object " + EndUserClientIP[i] + "\n")
    """
    # Close opend file
    on_boarding_file.close()


def reset_all_fields():
    get_user_name_entry.delete(0, END)
    get_customer_name_entry.delete(0, END)
    get_program_name_entry.delete(0, END)
    get_er_number_entry.delete(0, END)
    get_sg_service_entry.delete(0, END)
    get_ticket_number_entry.delete(0, END)


save_button = Button(second_frame, text="Save", command=save_to_file)
save_button.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
reset_button = Button(second_frame, text="Reset", command=reset_all_fields)
reset_button.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)

top_level_window.config(menu=my_menu)
top_level_window.mainloop()

"""

SGService = "FTIH-SG-"
ERNumber = "ER"
subnetMask = "255.255.255.255"
VERSION = "1.0"

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
"""
