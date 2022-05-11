from tkinter import *
from tkinter import ttk
import ipaddress
import configparser

# Create the window
top_level_window = Tk()
top_level_window.geometry("600x1000")
top_level_window.title("Welcome to the on-boarding program")
# Variable to dynamically assign rows
row_level = 0

# Read from the config file
config_file = configparser.RawConfigParser()
config_file.read('config.txt')
details_dict = dict(config_file.items('MY_VARIABLES'))
author_name = details_dict['author']
version_number = details_dict['version']

"""
Global Variables
"""
ACY_INTERFACES = ["10.10.10.10", "internet", "11.11.11.11", "internet1",
                  "12.12.12.12", "internet5", "13.13.13.13", "internet6"]

OEX_INTERFACES = ["20.20.20.20", "internet", "21.21.21.21", "internet1",
                  "22.22.22.22", "internet5", "23.23.23.23", "internet6"]

"""
Functions
"""


def about_new_window():
    # Toplevel object which will be treated as a new window
    new_window = Toplevel(top_level_window)

    # sets the title of theToplevel widget
    new_window.title("About")

    # sets the geometry of toplevel
    new_window.geometry("200x200")

    # A Label widget to show in toplevel
    Label(new_window, text=f"Author: {author_name}").grid(row=0, column=0, sticky="W")
    Label(new_window, text=f"Version: {version_number}").grid(row=1, column=0, sticky="W")


def hide_all_frames():
    about_program_frame.grid_forget()


def validate_user_name():
    if get_user_name_entry.get():
        get_user_name_entry.configure(bg="white")
    else:
        get_user_name_entry.configure(bg="red")


def validate_customer_name():
    if get_customer_name_entry.get():
        get_customer_name_entry.configure(bg="white")
    else:
        get_customer_name_entry.configure(bg="red")


def validate_program_name():
    if get_program_name_entry.get():
        get_program_name_entry.configure(bg="white")
    else:
        get_program_name_entry.configure(bg="red")


def validate_er_number():
    if len(get_er_number_entry.get()) != 6 or (not get_er_number_entry.get().isdigit()):
        get_er_number_entry.configure(bg="red")
    else:
        get_er_number_entry.configure(bg="white")


def validate_sg_number():
    if len(get_sg_service_entry.get()) != 6 or (not get_sg_service_entry.get().isdigit()):
        get_sg_service_entry.configure(bg="red")
    else:
        get_sg_service_entry.configure(bg="white")


def validate_tsb_number():
    if len(get_ticket_number_entry.get()) != 13 or (not get_ticket_number_entry.get().isdigit()):
        get_ticket_number_entry.configure(bg="red")
    else:
        get_ticket_number_entry.configure(bg="white")


def is_nems_flow():
    global get_nems_flow_answer
    get_nems_flow_answer = show_nems_flow_answer.current()


def validate_type_of_connection():
    global get_type_of_connection
    get_type_of_connection = show_nesg_connection_type.current()


def validate_nesg_location():
    global nesg_location_for_save
    nesg_location_for_save = show_nesg_connection_location.current()


def validate_fti_crypto_ip():
    global interface_name_index
    global interface_next_hop_index
    global interface_crypto_map_index

    nesg_location = show_nesg_connection_location.current()
    nesg_crypto_ip = fti_crypto_ip_entry.get()

    if nesg_location == 'ACY':
        if nesg_crypto_ip not in ACY_INTERFACES:
            fti_crypto_ip_entry.configure(bg="red")
        else:
            fti_crypto_ip_entry.configure(bg="white")
            interface_name_index = (ACY_INTERFACES.index(nesg_crypto_ip) + 1)
            interface_next_hop_index = (ACY_INTERFACES.index(nesg_crypto_ip) + 2)
            interface_crypto_map_index = (ACY_INTERFACES.index(nesg_crypto_ip) + 3)
    elif nesg_location == 'OEX':
        if nesg_crypto_ip not in OEX_INTERFACES:
            fti_crypto_ip_entry.configure(bg="red")
        else:
            fti_crypto_ip_entry.configure(bg="white")
            interface_name_index = (OEX_INTERFACES.index(nesg_crypto_ip) + 1)
            interface_next_hop_index = (OEX_INTERFACES.index(nesg_crypto_ip) + 2)
            interface_crypto_map_index = (OEX_INTERFACES.index(nesg_crypto_ip) + 3)


def validate_end_user_crypto_ip():
    try:
        ipaddress.ip_address(end_user_crypto_ip_entry.get())
        end_user_crypto_ip_entry.configure(bg="white")
    except ValueError:
        end_user_crypto_ip_entry.configure(bg="red")


def client_ips():
    global customer_list_of_ips
    global client_number_of_ips
    customer_list_of_ips = []
    list_of_ips = end_user_customer_ip_entry.get().split(",")
    client_number_of_ips = len(list_of_ips)

    for i in range(0, client_number_of_ips):
        try:
            ipaddress.ip_address(list_of_ips[i])
            current_ip_in_list = list_of_ips[i]
            customer_list_of_ips.append(current_ip_in_list)
            end_user_customer_ip_entry.configure(bg="white")
        except ValueError:
            end_user_customer_ip_entry.configure(bg="red")
            end_user_customer_ip_entry.delete(0, END)
            end_user_customer_ip_entry.insert(0, "IP is incorrect: " + list_of_ips[i])


def destination_ips():
    global destination_list_of_ips
    global dst_number_of_ips
    destination_list_of_ips = []
    list_of_ips = end_user_dst_ip_entry.get().split(",")
    dst_number_of_ips = len(list_of_ips)

    for i in range(0, dst_number_of_ips):
        try:
            ipaddress.ip_address(list_of_ips[i])
            current_ip_in_list = list_of_ips[i]
            destination_list_of_ips.append(current_ip_in_list)
            end_user_customer_ip_entry.configure(bg="white")
        except ValueError:
            end_user_customer_ip_entry.configure(bg="red")
            end_user_customer_ip_entry.delete(0, END)
            end_user_customer_ip_entry.insert(0, "IP is incorrect: " + list_of_ips[i])


def validate_crypto_acl_name():
    if not crypto_acl_entry.get():
        crypto_acl_entry.configure(bg="red")
    else:
        crypto_acl_entry.configure(bg="white")


def validate_sequence_number():
    if len(get_sg_service_entry.get()) > 3 and not (get_sg_service_entry.get().isdigit()):
        crypto_sequence_number_entry.configure(bg="red")
    else:
        crypto_sequence_number_entry.configure(bg="white")


def validate_password():
    password = crypto_psk_entry.get()
    lower_case_count = 0
    upper_case_count = 0
    digit_case_count = 0
    special_case_count = 0
    password_length = len(password)

    for i in password:
        if i.islower():
            lower_case_count += 1
        elif i.isupper():
            upper_case_count += 1
        elif i.isdigit():
            digit_case_count += 1
        else:
            special_case_count += 1

    if (password_length <= 14) or (lower_case_count <= 1) or \
       (upper_case_count <= 1) or (digit_case_count <= 1) or \
       (special_case_count <= 1):
        crypto_psk_entry.configure(bg="red")
    else:
        crypto_psk_entry.configure(bg="white")


def validate_for_file():
    pass


# Save file
def save_to_file():
    sg_service = "FTIH-SG-"
    er_number = "ER-"
    subnet_mask = "255.255.255.255"

    # Open a file
    on_boarding_file = open("palo_output.txt", "w")
    on_boarding_file.write(get_user_name_entry.get() + " created this config" + "\n")
    on_boarding_file.write("Customer name is: " + get_customer_name_entry.get() + "\n")
    on_boarding_file.write("Program name is: " + get_program_name_entry.get() + "\n")
    on_boarding_file.write("ER number is: " + er_number + get_er_number_entry.get() + "\n")
    on_boarding_file.write("SG service is: " + sg_service + get_sg_service_entry.get() + "\n")
    on_boarding_file.write("The TSB number is: " + get_ticket_number_entry.get() + "\n")
    on_boarding_file.write("\n")
    on_boarding_file.write("\n")
    on_boarding_file.write("End user Crypto IP is: " + end_user_crypto_ip_entry.get() + "\n")
    on_boarding_file.write("FTI Crypto IP is " + fti_crypto_ip_entry.get() + "\n")
    on_boarding_file.write("End User Client IP is " + end_user_customer_ip_entry.get() + "\n")
    on_boarding_file.write("End DST Client IP is " + end_user_dst_ip_entry.get() + "\n")

    on_boarding_file.write("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + "\n")
    on_boarding_file.write("Below is the commands that you can copy and paste into the ASA" + "\n")
    on_boarding_file.write("\n")

    for i in range(0, client_number_of_ips):
        for j in range(0, dst_number_of_ips):
            on_boarding_file.write("access-list" + " " + crypto_acl_entry.get() + " " + "extended permit ip host " + customer_list_of_ips[i] + " host " + destination_list_of_ips[j] + "\n")
    on_boarding_file.write("\n")

    if nesg_location_for_save == 'ACY':
        on_boarding_file.write("crypto map " + ACY_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "match address " + crypto_acl_entry.get() + "\n")
        on_boarding_file.write("crypto map " + ACY_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set pfs group21" + "\n")
        on_boarding_file.write("crypto map " + ACY_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set peer " + end_user_crypto_ip_entry.get() + "\n")
        on_boarding_file.write("crypto map " + ACY_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
        on_boarding_file.write("crypto map " + ACY_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set security-association lifetime seconds 28800" + "\n")
        on_boarding_file.write("\n")
    elif nesg_location_for_save == 'OEX':
        on_boarding_file.write("crypto map " + OEX_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "match address " + crypto_acl_entry.get() + "\n")
        on_boarding_file.write("crypto map " + OEX_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set pfs group21" + "\n")
        on_boarding_file.write("crypto map " + OEX_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set peer " + end_user_crypto_ip_entry.get() + "\n")
        on_boarding_file.write("crypto map " + OEX_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
        on_boarding_file.write("crypto map " + OEX_INTERFACES[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set security-association lifetime seconds 28800" + "\n")
        on_boarding_file.write("\n")

    on_boarding_file.write("tunnel-group " + end_user_crypto_ip_entry.get() + " " + "type ipsec-l2l" + "\n")
    on_boarding_file.write("tunnel-group " + end_user_crypto_ip_entry.get() + " " + "ipsec-attributes" + "\n")
    on_boarding_file.write("   ikev2 remote-authentication pre-shared-key " + crypto_psk_entry.get() + "\n")
    on_boarding_file.write("   ikev2 local-authentication pre-shared-key " + crypto_psk_entry.get() + "\n")
    on_boarding_file.write("\n")
    if nesg_location_for_save == 'acy':
        on_boarding_file.write("route " + ACY_INTERFACES[interface_name_index] + " " + end_user_crypto_ip_entry.get() + " " + subnet_mask + " " + ACY_INTERFACES[interface_next_hop_index] + "\n")
        for i in range(0, client_number_of_ips):
            on_boarding_file.write("route " + ACY_INTERFACES[interface_name_index] + " " + customer_list_of_ips[i] + " " + subnet_mask + " " + ACY_INTERFACES[interface_next_hop_index] + "\n")
    on_boarding_file.write("\n")

    if get_nems_flow_answer == 1:
        on_boarding_file.write("object-group network NEMS-Client" + "\n")
        for i in range(0, client_number_of_ips):
            on_boarding_file.write("   network-object object " + customer_list_of_ips[i] + "\n")


    # Close opend file
    on_boarding_file.close()


# Clear all the fields button
def reset_all_fields():
    get_user_name_entry.delete(0, END)
    get_customer_name_entry.delete(0, END)
    get_program_name_entry.delete(0, END)
    get_er_number_entry.delete(0, END)
    get_sg_service_entry.delete(0, END)
    get_ticket_number_entry.delete(0, END)
    fti_crypto_ip_entry.delete(0, END)
    end_user_crypto_ip_entry.delete(0, END)
    end_user_customer_ip_entry.delete(0, END)
    end_user_dst_ip_entry.delete(0, END)
    crypto_acl_entry.delete(0, END)
    crypto_sequence_number_entry.delete(0, END)
    crypto_psk_entry.delete(0, END)


"""
Menu bar
"""
my_menu = Menu(top_level_window)

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=top_level_window.quit)

help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_new_window)

about_program_frame = Frame(top_level_window)
##########################################################################################################

# Get basic info
# get user who is building this flow out
get_user_name_label = Label(top_level_window, text="What is your name: ")
get_user_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_user_name_entry = Entry(top_level_window)
get_user_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_user_name_button = Button(top_level_window, text="Validate", command=validate_user_name)
get_user_name_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get Customer Name
get_customer_name_label = Label(top_level_window, text="What is the customer name: ")
get_customer_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_customer_name_entry = Entry(top_level_window)
get_customer_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_customer_name_button = Button(top_level_window, text="Validate", command=validate_customer_name)
get_customer_name_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get Program Name
get_program_name_label = Label(top_level_window, text="What is the program name: ")
get_program_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_program_name_entry = Entry(top_level_window)
get_program_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_program_name_button = Button(top_level_window, text="Validate", command=validate_program_name)
get_program_name_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Get ER number
get_er_number_label = Label(top_level_window, text="What is the ER number: ")
get_er_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_er_number_entry = Entry(top_level_window)
get_er_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_er_number_button = Button(top_level_window, text="Validate", command=validate_er_number)
get_er_number_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Get SG number
get_sg_service_label = Label(top_level_window, text="What is the SG Service: ")
get_sg_service_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_sg_service_entry = Entry(top_level_window)
get_sg_service_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_sg_service_button = Button(top_level_window, text="Validate", command=validate_sg_number)
get_sg_service_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get TSB Number
get_ticket_number_label = Label(top_level_window, text="What is the TSB number: ")
get_ticket_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_ticket_number_entry = Entry(top_level_window)
get_ticket_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_ticket_number_button = Button(top_level_window, text="Validate", command=validate_tsb_number)
get_ticket_number_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1


# is NEMS Flow
get_nems_flow_label = Label(top_level_window, text="Is this a NEMS flow? ")
get_nems_flow_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
show_nems_flow_answer = ttk.Combobox(top_level_window)
show_nems_flow_answer['values'] = ('yes', 'no')
show_nems_flow_answer.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
show_nems_flow_answer.current(1)
show_nems_flow_answer['state'] = 'readonly'
get_nems_flow_button = Button(top_level_window, text="Update", command=is_nems_flow)
get_nems_flow_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Type of connection
nesg_connection_type_label = Label(top_level_window, text="What is the type of connection:")
nesg_connection_type_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
show_nesg_connection_type = ttk.Combobox(top_level_window)
show_nesg_connection_type['values'] = ('Internet', 'ED6', 'DTS', 'DTE')
show_nesg_connection_type.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
show_nesg_connection_type.current(0)
show_nesg_connection_type['state'] = 'readonly'
nesg_connection_type_button = Button(top_level_window, text="Validate", command=validate_type_of_connection)
nesg_connection_type_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Get NESG Location
nesg_connection_location_label = Label(top_level_window, text="NESG Location: ")
nesg_connection_location_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
show_nesg_connection_location = ttk.Combobox(top_level_window)
show_nesg_connection_location['values'] = ('ACY', 'OEX', 'ATL', 'SLC')
show_nesg_connection_location.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
show_nesg_connection_location.current(0)
show_nesg_connection_location['state'] = 'readonly'
nesg_connection_location_button = Button(top_level_window, text="Validate", command=validate_nesg_location)
nesg_connection_location_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# FTI Crypto IP
fti_crypto_ip_label = Label(top_level_window, text="What is the FTI Crypto IP: ")
fti_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
fti_crypto_ip_entry = Entry(top_level_window)
fti_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
fti_crypto_ip_button = Button(top_level_window, text="Validate", command=validate_fti_crypto_ip)
fti_crypto_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get end user crypto IP
end_user_crypto_ip_label = Label(top_level_window, text="What is the customers crypto IP? ")
end_user_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_crypto_ip_entry = Entry(top_level_window)
end_user_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
end_user_crypto_ip_button = Button(top_level_window, text="Validate", command=validate_end_user_crypto_ip)
end_user_crypto_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get end user client IP
end_user_customer_ip_label = Label(top_level_window, text="Enter client IP's: ")
end_user_customer_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_customer_ip_entry = Entry(top_level_window)
end_user_customer_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
end_user_customer_ip_button = Button(top_level_window, text="Validate", command=client_ips)
end_user_customer_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get end user dst IP
end_user_dst_ip_label = Label(top_level_window, text="What is the customers dst IP? ")
end_user_dst_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_dst_ip_entry = Entry(top_level_window)
end_user_dst_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
end_user_dst_ip_button = Button(top_level_window, text="Validate", command=destination_ips)
end_user_dst_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# name of crypto acl
crypto_acl_label = Label(top_level_window, text="What is the name of the crypto ACL? ")
crypto_acl_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_acl_entry = Entry(top_level_window)
crypto_acl_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
crypto_acl_button = Button(top_level_window, text="Validate", command=validate_crypto_acl_name)
crypto_acl_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# next sequence number
crypto_sequence_number_label = Label(top_level_window, text="What is the next sequence number ")
crypto_sequence_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_sequence_number_entry = Entry(top_level_window)
crypto_sequence_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
crypto_sequence_number_button = Button(top_level_window, text="Validate", command=validate_sequence_number)
crypto_sequence_number_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get pre shared key
crypto_psk_label = Label(top_level_window, text="What is the PSK? ")
crypto_psk_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_psk_entry = Entry(top_level_window)
crypto_psk_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
crypto_psk_button = Button(top_level_window, text="Validate", command=validate_password)
crypto_psk_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Buttons to save to file or reset all fields
validate_button = Button(top_level_window, text="Validate", command=validate_for_file)
validate_button.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
save_button = Button(top_level_window, text="Save", command=save_to_file)
save_button.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
reset_button = Button(top_level_window, text="Reset", command=reset_all_fields)
reset_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)

top_level_window.config(menu=my_menu)
top_level_window.mainloop()
