from tkinter import *
from tkinter import ttk

# Create the window
top_level_window = Tk()
top_level_window.geometry("600x350")
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
    except ValueError:
        pass


nesg_connection_type_label = Label(second_frame, text="What is the type of connection:")
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
    except ValueError:
        pass


nesg_connection_location_label = Label(second_frame, text="NESG Location")
nesg_connection_location_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
nesg_connection_location_entry = Entry(second_frame)
nesg_connection_location_entry.insert(0, "ACY/OEX/SLC/ATL")
nesg_connection_location_entry.bind("<FocusIn>", delete_text_location)
nesg_connection_location_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# FTI Crypto IP
fti_crypto_ip_label = Label(second_frame, text="What is the FTI Crypto IP: ")
fti_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
fti_crypto_ip_entry = Entry(second_frame)
fti_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get end user crypto IP
end_user_crypto_ip_label = Label(second_frame, text="What is the customers crypto IP? ")
end_user_crypto_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_crypto_ip_entry = Entry(second_frame)
end_user_crypto_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get end user client IP
end_user_customer_ip_label = Label(second_frame, text="What is the customers client IP? ")
end_user_customer_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_customer_ip_entry = Entry(second_frame)
end_user_customer_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get end user dst IP
end_user_dst_ip_label = Label(second_frame, text="What is the customers dst IP? ")
end_user_dst_ip_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
end_user_dst_ip_entry = Entry(second_frame)
end_user_dst_ip_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# name of crypto acl
crypto_acl_label = Label(second_frame, text="What is the name of the crypto ACL? ")
crypto_acl_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_acl_entry = Entry(second_frame)
crypto_acl_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# name of crypto map on the interface
crypto_map_name_label = Label(second_frame, text="What is the crypto map name? ")
crypto_map_name_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_map_name_entry = Entry(second_frame)
crypto_map_name_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# name of asa interface
asa_interface_label = Label(second_frame, text="What is the ASA interface name? ")
asa_interface_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
asa_interface_entry = Entry(second_frame)
asa_interface_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# next sequence number
crypto_sequence_number_label = Label(second_frame, text="What is the next sequence number ")
crypto_sequence_number_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_sequence_number_entry = Entry(second_frame)
crypto_sequence_number_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# get pre shared key
crypto_psk_label = Label(second_frame, text="What is the PSK? ")
crypto_psk_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
crypto_psk_entry = Entry(second_frame)
crypto_psk_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1

# next hop interface IP
asa_interface_next_hop_label = Label(second_frame, text="What is the next hop interface IP ")
asa_interface_next_hop_label.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
asa_interface_next_hop_entry = Entry(second_frame)
asa_interface_next_hop_entry.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)
row_level += 1


# Buttons to save to file or reset all fields
def save_to_file():
    sg_service = "FTIH-SG-"
    er_number = "ER"
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
    on_boarding_file.write("access-list" + " " + crypto_acl_entry.get() + " " + "extended permit ip host " +
                           end_user_customer_ip_entry.get() + " host " + end_user_dst_ip_entry.get() + "\n")
    on_boarding_file.write("\n")
    on_boarding_file.write("crypto map " + crypto_map_name_entry.get() + " " + crypto_sequence_number_entry.get() +
                           " " + "match address " + crypto_acl_entry.get() + "\n")
    on_boarding_file.write("crypto map " + crypto_map_name_entry.get() + " " + crypto_sequence_number_entry.get() +
                           " " + "set pfs group21" + "\n")
    on_boarding_file.write("crypto map " + crypto_map_name_entry.get() + " " + crypto_sequence_number_entry.get() +
                           " " + "set peer " + end_user_crypto_ip_entry.get() + "\n")
    on_boarding_file.write("crypto map " + crypto_map_name_entry.get() + " " + crypto_sequence_number_entry.get() +
                           " " + "set ikev2 ipsec-proposal VPN-NEW VPN-NEW-BACKUP" + "\n")
    on_boarding_file.write("crypto map " + crypto_map_name_entry.get() + " " + crypto_sequence_number_entry.get() +
                           " " + "set security-association lifetime seconds 28800" + "\n")
    on_boarding_file.write("\n")

    on_boarding_file.write("tunnel-group " + end_user_crypto_ip_entry.get() + " " + "type ipsec-l2l" + "\n")
    on_boarding_file.write("tunnel-group " + end_user_crypto_ip_entry.get() + " " + "ipsec-attributes" + "\n")
    on_boarding_file.write("   ikev2 remote-authentication pre-shared-key " + crypto_psk_entry.get() + "\n")
    on_boarding_file.write("   ikev2 local-authentication pre-shared-key " + crypto_psk_entry.get() + "\n")
    on_boarding_file.write("\n")
    on_boarding_file.write("route " + asa_interface_entry.get() + " " + end_user_crypto_ip_entry.get() + " " +
                           subnet_mask + " " + asa_interface_next_hop_entry.get() + "\n")
    on_boarding_file.write("route " + asa_interface_entry.get() + " " + end_user_customer_ip_entry.get() + " " +
                           subnet_mask + " " + asa_interface_next_hop_entry.get() + "\n")
    on_boarding_file.write("\n")
    # Close opend file
    on_boarding_file.close()


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
    crypto_map_name_entry.delete(0, END)
    asa_interface_entry.delete(0, END)
    crypto_sequence_number_entry.delete(0, END)
    crypto_psk_entry.delete(0, END)
    asa_interface_next_hop_entry.delete(0, END)


save_button = Button(second_frame, text="Save", command=save_to_file)
save_button.grid(row=row_level, column=0, padx=5, pady=5, sticky=W)
reset_button = Button(second_frame, text="Reset", command=reset_all_fields)
reset_button.grid(row=row_level, column=1, padx=5, pady=5, sticky=W)

top_level_window.config(menu=my_menu)
top_level_window.mainloop()
