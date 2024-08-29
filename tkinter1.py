import tkinter as tk
from tkinter import messagebox


# Function to clear all fields
def clear_fields():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)


# Function to validate inputs
def validate_entries():
    name = e1.get()
    email = e2.get()
    phone = e3.get()
    address = e4.get()
    password = e5.get()

    # Simple validation checks
    if not name or not email or not phone or not address or not password:
        messagebox.showerror("Input Error", "All fields are required!")
        return False

    if '@' not in email or '.' not in email:
        messagebox.showerror("Input Error", "Invalid email format!")
        return False

    if not phone.isdigit() or len(phone) < 10:
        messagebox.showerror("Input Error", "Invalid phone number!")
        return False

    return True


# Function to open a new window with user details
def open_new_window():
    if not validate_entries():
        return

    new_window = tk.Toplevel(p)
    new_window.geometry("400x300")
    new_window.title("User Details")

    tk.Label(new_window, text="User Details", font=("bold", 14)).pack(pady=10)

    details = f"Name: {e1.get()}\nEmail: {e2.get()}\nPhone: {e3.get()}\nAddress: {e4.get()}"
    tk.Label(new_window, text=details, font=("Arial", 12), justify="left").pack(pady=10)

    tk.Button(new_window, text="Close", command=new_window.destroy, bg="red", fg="white").pack(pady=20)


# Main window setup
p = tk.Tk()
p.geometry("600x400")
p.title("User Registration Form")

# Title label
tk.Label(p, text="User Registration Form", bg="green", fg="white", width=40, font=("bold", 18)).pack()

# Creating labels and entry fields
tk.Label(p, text="Name", bg="yellow", fg="black", width=15, font=(10)).place(x=20, y=50)
e1 = tk.Entry(p, bd=5, width=30)
e1.place(x=200, y=50)

tk.Label(p, text="Email", bg="yellow", fg="black", width=15, font=(10)).place(x=20, y=100)
e2 = tk.Entry(p, bd=5, width=30)
e2.place(x=200, y=100)

tk.Label(p, text="Phone No.", bg="yellow", fg="black", width=15, font=(10)).place(x=20, y=150)
e3 = tk.Entry(p, bd=5, width=30)
e3.place(x=200, y=150)

tk.Label(p, text="Address", bg="yellow", fg="black", width=15, font=(10)).place(x=20, y=200)
e4 = tk.Entry(p, bd=5, width=30)
e4.place(x=200, y=200)

tk.Label(p, text="Password", bg="yellow", fg="black", width=15, font=(10)).place(x=20, y=250)
e5 = tk.Entry(p, bd=5, show="*", width=30)
e5.place(x=200, y=250)

# Creating buttons
tk.Button(p, text="Submit", fg="white", bg="green", width=20, font=("bold", 11), command=open_new_window).place(x=100,
                                                                                                                y=300)
tk.Button(p, text="Clear", fg="white", bg="red", width=20, font=("bold", 11), command=clear_fields).place(x=300, y=300)

p.mainloop()
