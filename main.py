from tkinter import *
from tkinter import ttk


top_level_window = Tk()
top_level_window.geometry("400x250")
top_level_window.resizable(False, False)
top_level_window.title("Welcome to the database program")
row_level = 0


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
get_user_name_label = Label(top_level_window, text="What is your name: ")
get_user_name_label.grid(row=row_level, column=0)
get_user_name_entry = Entry(top_level_window)
get_user_name_entry.grid(row=row_level, column=1)
row_level += 1


# get Customer Name
#getCustomerName = input("What is the customer name: ie Delta/Southwest ")

# get Program Name
#getProgramName = input("What is the program name: ie NEMS/WMSCR  ")

"""
# Type of connection
def combo_clicked(event):
    global connection_type_selected
    connection_type_selected = connection_type_combo.get()
    print(connection_type_selected)
    return connection_type_selected


connection_type = [
    "Internet",
    "Matrix",
    "ED6",
    "DTS",
    "DTE"
]
connection_type_label = Label(top_level_window, text="Please select the type of connection:")
connection_type_label.grid(row=row_level, column=0, padx=10, pady=10)
connection_type_selected = StringVar()
connection_type_combo = ttk.Combobox(top_level_window, values=connection_type)
connection_type_combo.current(0)
connection_type_combo.bind("<<ComboboxSelected>>", combo_clicked)
connection_type_combo.grid(row=row_level, column=1, padx=10, pady=10)
row_level += 1


print(connection_type_selected)
"""


top_level_window.config(menu=my_menu)
top_level_window.mainloop()
