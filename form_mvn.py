import tkinter as tk
from tkinter import messagebox

class FormModel:
    def __init__(self):
        self.name = ""
        self.email = ""

    def set_data(self, name, email):
        self.name = name
        self.email = email

class FormView:
    def __init__(self, root, controller):
        self.controller = controller
        root.title("Simple Form (MVC)")
        
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Submit", command=self.controller.submit_form).grid(row=2, column=0, columnspan=2, pady=10)
    
    def get_inputs(self):
        return self.name_entry.get(), self.email_entry.get()

class FormController:
    def __init__(self, root):
        self.model = FormModel()
        self.view = FormView(root, self)

    def submit_form(self):
        name, email = self.view.get_inputs()
        self.model.set_data(name, email)
        messagebox.showinfo("Form Submitted", f"Name: {self.model.name}\nEmail: {self.model.email}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormController(root)
    root.mainloop()
