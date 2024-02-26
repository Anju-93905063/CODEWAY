import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    def generate():
        try:
            length = int(length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length must be a positive integer.")
                return
            password = generate_password(length)
            password_label.config(text=password)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the password length.")

    # Create GUI window
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("370x230")
    

    # Create widgets

    length_label = tk.Label(window, text="Enter the desired length of the password:",font=("Brush Script",11))
    length_label.pack()
    length_entry = tk.Entry(window,width=20,font=('Arial',13))
    length_entry.pack(ipadx=10)
    generate_button = tk.Button(window, text="Generate Password", command=generate,width=15,font=('Garamond',15),background="light pink")
    generate_button.pack(pady=15)
    password_label = tk.Label(window, text="_",font=('Arial',15))
    password_label.pack()

    # Run GUI
    window.mainloop()

generate_password_gui()
