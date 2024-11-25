import tkinter as tk
from tkinter import messagebox


def validate_email():
    email = email_entry.get()  

    length_of_email = len(email)
    number_of_at_characters = email.count("@")
    number_of_dot_characters = email.count(".")
    position_of_at = email.find("@")
    position_of_first_dot = email.find(".")
    position_of_last_dot = email.rfind(".")
    position_of_first_dot_after_the_at = email.find(".", position_of_at)

    error_message_no_at = "An email address has to contain a '@' character!"
    error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
    error_message_no_dot = "An email address has to contain at least one '.' character!"
    error_message_no_username = "The username before the '@' character cannot be empty!"
    error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
    error_message_no_server_name = "The domain cannot start with a '.' character!"
    error_message_no_tld = "The top-level domain cannot be empty!"
    error_message_short_tld = "The top-level domain has to be at least two characters long!"
    error_message_no_domain = "The domain after the '@' character cannot be empty!"
    error_message_invalid_username = "The username cannot start with a '.' character!"
    ok_message = "Valid email address :)"

    is_valid = True

    
    if number_of_at_characters == 0:
        messagebox.showerror("Error", error_message_no_at)
        is_valid = False
    elif number_of_at_characters > 1:
        messagebox.showerror("Error", error_message_too_many_at)
        is_valid = False
    elif email[:position_of_at] == "":
        messagebox.showerror("Error", error_message_no_username)
        is_valid = False
    elif email[position_of_at + 1:] == "":
        messagebox.showerror("Error", error_message_no_domain)
        is_valid = False
    elif number_of_dot_characters == 0:
        messagebox.showerror("Error", error_message_no_dot)
        is_valid = False
    elif position_of_first_dot_after_the_at == -1:
        messagebox.showerror("Error", error_message_no_dot_in_domain)
        is_valid = False
    elif email[position_of_at + 1] == ".":
        messagebox.showerror("Error", error_message_no_server_name)
        is_valid = False
    elif email[position_of_last_dot + 1:] == "":
        messagebox.showerror("Error", error_message_no_tld)
        is_valid = False
    elif len(email[position_of_last_dot + 1:]) < 2:
        messagebox.showerror("Error", error_message_short_tld)
        is_valid = False
    elif email[:position_of_at][0] == ".":
        messagebox.showerror("Error", error_message_invalid_username)
        is_valid = False

    if is_valid:
        messagebox.showinfo("Success", ok_message)


root = tk.Tk()
root.title("Email Validator")


label = tk.Label(root, text="Enter your email:")
label.pack(padx=10, pady=5)

email_entry = tk.Entry(root, width=30)
email_entry.pack(padx=10, pady=5)


validate_button = tk.Button(root, text="Validate Email", command=validate_email)
validate_button.pack(padx=10, pady=20)


root.mainloop()