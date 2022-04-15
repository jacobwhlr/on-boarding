from tkinter import *
from tkinter import ttk
import ipaddress

# Create the window
top_level_window = Tk()
top_level_window.geometry("600x1000")
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
Global Variables
"""
acy_interfaces = ["10.10.10.10", "internet", "11.11.11.11", "internet1",
                  "12.12.12.12", "internet5", "13.13.13.13", "internet6"]

oex_interfaces = ["20.20.20.20", "internet", "21.21.21.21", "internet1",
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
    author_name = "Jacob"
    version_number = "1.0"
    Label(new_window, text=f"Author: {author_name}").grid(row=0, column=0, sticky="W")
    Label(new_window, text=f"Version: {version_number}").grid(row=1, column=0, sticky="W")


def hide_all_frames():
    about_program_frame.grid_forget()


def validate_user_name():
    if not get_user_name_entry.get():
        get_user_name_entry.configure(bg="red")
    else:
        get_user_name_entry.configure(bg="white")


def validate_customer_name():
    if not get_customer_name_entry.get():
        get_customer_name_entry.configure(bg="red")
    else:
        get_customer_name_entry.configure(bg="white")


def validate_program_name():
    if not get_program_name_entry.get():
        get_program_name_entry.configure(bg="red")
    else:
        get_program_name_entry.configure(bg="white")


def validate_er_number():
    if len(get_er_number_entry.get()) != 6 or (not get_er_number_entry.get().isdigit()):
        get_er_number_entry.configure(bg="red")
        validate_er_number_function = False
        return validate_er_number_function
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


def validate_type_of_connection():
    type_of_connection = nesg_connection_type_entry.get().lower()
    if (type_of_connection == "internet") or (type_of_connection == "ed6") or \
       (type_of_connection == "dts") or (type_of_connection == "dte"):
        nesg_connection_type_entry.configure(bg="white")
    else:
        nesg_connection_type_entry.configure(bg="red")


def delete_text_connection(event):
    try:
        nesg_connection_type_entry.delete(0, END)
    except ValueError:
        pass


def validate_nesg_location():
    location_of_connection = nesg_connection_location_entry.get().lower()
    if (location_of_connection == "acy") or (location_of_connection == "oex") or \
       (location_of_connection == "slc") or (location_of_connection == "atl"):
        nesg_connection_type_entry.configure(bg="white")
    else:
        nesg_connection_type_entry.configure(bg="red")


def delete_text_location(event):
    try:
        nesg_connection_location_entry.delete(0, END)
    except ValueError:
        pass


def validate_fti_crypto_ip():
    global interface_name_index
    global interface_next_hop_index
    global interface_crypto_map_index
    global nesg_location_for_save

    nesg_location = nesg_connection_location_entry.get().lower()
    nesg_crypto_ip = fti_crypto_ip_entry.get()
    nesg_location_for_save = fti_crypto_ip_entry.get()

    if nesg_location == 'acy':
        if nesg_crypto_ip not in acy_interfaces:
            fti_crypto_ip_entry.configure(bg="red")
        else:
            fti_crypto_ip_entry.configure(bg="white")
            interface_name_index = (acy_interfaces.index(nesg_crypto_ip) + 1)
            interface_next_hop_index = (acy_interfaces.index(nesg_crypto_ip) + 2)
            interface_crypto_map_index = (acy_interfaces.index(nesg_crypto_ip) + 3)
    elif nesg_location == 'oex':
        if nesg_crypto_ip not in oex_interfaces:
            fti_crypto_ip_entry.configure(bg="red")
        else:
            fti_crypto_ip_entry.configure(bg="white")
            interface_name_index = (oex_interfaces.index(nesg_crypto_ip) + 1)
            interface_next_hop_index = (oex_interfaces.index(nesg_crypto_ip) + 2)
            interface_crypto_map_index = (oex_interfaces.index(nesg_crypto_ip) + 3)


def validate_end_user_crypto_ip():
    try:
        ipaddress.ip_address(end_user_crypto_ip_entry.get())
        end_user_crypto_ip_entry.configure(bg="white")
    except ValueError:
        end_user_crypto_ip_entry.configure(bg="red")


def client_ips():
    global customer_list_of_ips
    customer_list_of_ips = []
    list_of_ip = end_user_customer_ip_entry.get().split(",")
    number_of_ips = len(list_of_ip)

    for i in range(0, number_of_ips):
        try:
            current_ip_in_list = ipaddress.ip_address(list_of_ip[i])
            customer_list_of_ips.append(current_ip_in_list)
            end_user_customer_ip_entry.configure(bg="white")
        except ValueError:
            end_user_customer_ip_entry.configure(bg="red")
            end_user_customer_ip_entry.delete(0, END)
            end_user_customer_ip_entry.insert(0, "IP is incorrect: " + list_of_ip[i])


def destination_ips():
    global destination_list_of_ips
    destination_list_of_ips = []
    list_of_ip = end_user_dst_ip_entry.get().split(",")
    number_of_ips = len(list_of_ip)

    for i in range(0, number_of_ips):
        try:
            current_ip_in_list = ipaddress.ip_address(list_of_ip[i])
            destination_list_of_ips.append(current_ip_in_list)
            end_user_customer_ip_entry.configure(bg="white")
            print(destination_list_of_ips)
        except ValueError:
            end_user_customer_ip_entry.configure(bg="red")
            end_user_customer_ip_entry.delete(0, END)
            end_user_customer_ip_entry.insert(0, "IP is incorrect: " + list_of_ip[i])


def validate_crypto_acl_name():
    if not crypto_acl_entry.get():
        crypto_acl_entry.configure(bg="red")
    else:
        crypto_acl_entry.configure(bg="white")


def validate_sequence_number():
    if len(get_sg_service_entry.get()) != 3 or (not get_sg_service_entry.get().isdigit()):
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
    # TODO: finish function for validate all button


# Save file
def save_to_file():
    # TODO: write for loop for crypto acl and write route statements
    sg_service = "FTIH-SG-"
    er_number = "ER-"
    subnet_mask = "255.255.255.255"

    # Open a file
    on_boarding_file = open("test_output.txt", "w")
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
    on_boarding_file.write("access-list" + " " + crypto_acl_entry.get() + " " + "extended permit ip host " + end_user_customer_ip_entry.get() + " host " + end_user_dst_ip_entry.get() + "\n")
    on_boarding_file.write("\n")

    if nesg_location_for_save == 'acy':
        on_boarding_file.write("crypto map " + acy_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "match address " + crypto_acl_entry.get() + "\n")
        on_boarding_file.write("crypto map " + acy_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set pfs group21" + "\n")
        on_boarding_file.write("crypto map " + acy_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set peer " + end_user_crypto_ip_entry.get() + "\n")
        on_boarding_file.write("crypto map " + acy_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
        on_boarding_file.write("crypto map " + acy_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set security-association lifetime seconds 28800" + "\n")
        on_boarding_file.write("\n")
    elif nesg_location_for_save == 'oex':
        on_boarding_file.write("crypto map " + oex_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "match address " + crypto_acl_entry.get() + "\n")
        on_boarding_file.write("crypto map " + oex_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set pfs group21" + "\n")
        on_boarding_file.write("crypto map " + oex_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set peer " + end_user_crypto_ip_entry.get() + "\n")
        on_boarding_file.write("crypto map " + oex_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
        on_boarding_file.write("crypto map " + oex_interfaces[interface_crypto_map_index] + " " + crypto_sequence_number_entry.get() + " " + "set security-association lifetime seconds 28800" + "\n")
        on_boarding_file.write("\n")

    on_boarding_file.write("tunnel-group " + end_user_crypto_ip_entry.get() + " " + "type ipsec-l2l" + "\n")
    on_boarding_file.write("tunnel-group " + end_user_crypto_ip_entry.get() + " " + "ipsec-attributes" + "\n")
    on_boarding_file.write("   ikev2 remote-authentication pre-shared-key " + crypto_psk_entry.get() + "\n")
    on_boarding_file.write("   ikev2 local-authentication pre-shared-key " + crypto_psk_entry.get() + "\n")
    on_boarding_file.write("\n")
#    on_boarding_file.write("route " + asa_interface_entry.get() + " " + end_user_crypto_ip_entry.get() + " " + subnet_mask + " " + asa_interface_next_hop_entry.get() + "\n")
#    on_boarding_file.write("route " + asa_interface_entry.get() + " " + end_user_customer_ip_entry.get() + " " + subnet_mask + " " + asa_interface_next_hop_entry.get() + "\n")
    on_boarding_file.write("\n")
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
    nesg_connection_type_entry.delete(0, END)
    nesg_connection_location_entry.delete(0, END)
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
get_user_name_label = Label(second_frame, text="What is your name: ")
get_user_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_user_name_entry = Entry(second_frame)
get_user_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_user_name_button = Button(second_frame, text="Validate", command=validate_user_name)
get_user_name_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get Customer Name
get_customer_name_label = Label(second_frame, text="What is the customer name: ")
get_customer_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_customer_name_entry = Entry(second_frame)
get_customer_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_customer_name_button = Button(second_frame, text="Validate", command=validate_customer_name)
get_customer_name_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get Program Name
get_program_name_label = Label(second_frame, text="What is the program name: ")
get_program_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_program_name_entry = Entry(second_frame)
get_program_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_program_name_button = Button(second_frame, text="Validate", command=validate_program_name)
get_program_name_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Get \er number
get_er_number_label = Label(second_frame, text="What is the ER number: ")
get_er_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_er_number_entry = Entry(second_frame)
get_er_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_er_number_button = Button(second_frame, text="Validate", command=validate_er_number)
get_er_number_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Get sg number
get_sg_service_label = Label(second_frame, text="What is the SG Service: ")
get_sg_service_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_sg_service_entry = Entry(second_frame)
get_sg_service_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_sg_service_button = Button(second_frame, text="Validate", command=validate_sg_number)
get_sg_service_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get TSB Number
get_ticket_number_label = Label(second_frame, text="What is the TSB number: ")
get_ticket_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
get_ticket_number_entry = Entry(second_frame)
get_ticket_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
get_ticket_number_button = Button(second_frame, text="Validate", command=validate_tsb_number)
get_ticket_number_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Type of connection
nesg_connection_type_label = Label(second_frame, text="What is the type of connection:")
nesg_connection_type_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
nesg_connection_type_entry = Entry(second_frame)
nesg_connection_type_entry.insert(0, "Internet/ED6/DTS/DTE")
nesg_connection_type_entry.bind("<FocusIn>", delete_text_connection)
nesg_connection_type_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
nesg_connection_type_button = Button(second_frame, text="Validate", command=validate_type_of_connection)
nesg_connection_type_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Get NESG Location
nesg_connection_location_label = Label(second_frame, text="NESG Location: ")
nesg_connection_location_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
nesg_connection_location_entry = Entry(second_frame)
nesg_connection_location_entry.insert(0, "ACY/OEX/SLC/ATL")
nesg_connection_location_entry.bind("<FocusIn>", delete_text_location)
nesg_connection_location_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
nesg_connection_location_button = Button(second_frame, text="Validate", command=validate_nesg_location)
nesg_connection_location_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# FTI Crypto IP
fti_crypto_ip_label = Label(second_frame, text="What is the FTI Crypto IP: ")
fti_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
fti_crypto_ip_entry = Entry(second_frame)
fti_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
fti_crypto_ip_button = Button(second_frame, text="Validate", command=validate_fti_crypto_ip)
fti_crypto_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get end user crypto IP
end_user_crypto_ip_label = Label(second_frame, text="What is the customers crypto IP? ")
end_user_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_crypto_ip_entry = Entry(second_frame)
end_user_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
end_user_crypto_ip_button = Button(second_frame, text="Validate", command=validate_end_user_crypto_ip)
end_user_crypto_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get end user client IP
end_user_customer_ip_label = Label(second_frame, text="Enter client IP's: ")
end_user_customer_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_customer_ip_entry = Entry(second_frame)
end_user_customer_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
end_user_customer_ip_button = Button(second_frame, text="Enter client IP's", command=client_ips)
end_user_customer_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get end user dst IP
end_user_dst_ip_label = Label(second_frame, text="What is the customers dst IP? ")
end_user_dst_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_dst_ip_entry = Entry(second_frame)
end_user_dst_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
end_user_dst_ip_button = Button(second_frame, text="Enter destination IP's", command=destination_ips)
end_user_dst_ip_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# name of crypto acl
crypto_acl_label = Label(second_frame, text="What is the name of the crypto ACL? ")
crypto_acl_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_acl_entry = Entry(second_frame)
crypto_acl_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
crypto_acl_button = Button(second_frame, text="Validate", command=validate_crypto_acl_name)
crypto_acl_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# next sequence number
crypto_sequence_number_label = Label(second_frame, text="What is the next sequence number ")
crypto_sequence_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_sequence_number_entry = Entry(second_frame)
crypto_sequence_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
crypto_sequence_number_button = Button(second_frame, text="Validate", command=validate_sequence_number)
crypto_sequence_number_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# get pre shared key
crypto_psk_label = Label(second_frame, text="What is the PSK? ")
crypto_psk_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_psk_entry = Entry(second_frame)
crypto_psk_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
crypto_psk_button = Button(second_frame, text="Validate", command=validate_password)
crypto_psk_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)
row_level += 1

# Buttons to save to file or reset all fields
validate_button = Button(second_frame, text="Validate", command=validate_for_file)
validate_button.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
save_button = Button(second_frame, text="Save", command=save_to_file)
save_button.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
reset_button = Button(second_frame, text="Reset", command=reset_all_fields)
reset_button.grid(row=row_level, column=2, padx=5, pady=5, sticky=W)

top_level_window.config(menu=my_menu)
top_level_window.mainloop()
