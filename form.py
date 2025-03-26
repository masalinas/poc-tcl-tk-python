import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}")

# Create main window
root = tk.Tk()
root.title("Simple Form")

# Labels and Entry Fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Submit Button
tk.Button(root, text="Submit", command=submit_form).grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
