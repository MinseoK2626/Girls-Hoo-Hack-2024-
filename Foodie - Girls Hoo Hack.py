import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class User:
    def __init__(self, name, tickets, flex_dollars):
        self.name = name
        self.tickets = tickets
        self.flex_dollars = flex_dollars


def send_one_ticket():
    if user_a.tickets >= 1:
        user_a.tickets -= 1
        user_b.tickets += 1

        label_user_a.config(text=f"{user_a.name} meal ticket : {user_a.tickets}")
        label_user_b.config(text=f"{user_b.name} meal ticket: {user_b.tickets}")

        messagebox.showinfo("YAY", "You just sent a ticket! Enjoy your meal with friend!")
    else:
        messagebox.showwarning("Boo, You don't have enough tickets!")


def send_flex_dollar():
    amount = int(entry_flex_dollar.get())
    if user_a.flex_dollars >= amount:
        user_a.flex_dollars -= amount
        user_b.flex_dollars += amount
        label_user_a.config(text=f"{user_a.name} flex dollars: {user_a.flex_dollars}")
        messagebox.showinfo("YAY", f"You just sent {amount} flex dollars!")
    else:
        messagebox.showwarning("Boo, You don't have enough flex dollars!")


user_a = User("Your", 5, 10)  
user_b = User("User B", 2, 5)


def option_selected(event):
    selected_option = option_var.get()
    if selected_option == "Meal Ticket":
        send_one_ticket()
    elif selected_option == "Flex Dollar":
        label_flex_dollar.pack(pady=5)
        entry_flex_dollar.pack(pady=5)
        button_send_flex.pack(pady=5)


def check_computing_id():
    label_user_a.pack(pady=10)
    label_user_b.pack(pady=10)
    options_menu.pack(pady=20)
    entry_computing_id.config(state="disabled")
    button_check_id.config(state="disabled")


root = tk.Tk()
root.title("Ticket Transfer Program")
root.geometry("400x400")

label_computing_id = tk.Label(root, text="Enter Computing ID:", font=("Arial", 14))
label_computing_id.pack(pady=10)

entry_computing_id = tk.Entry(root, font=("Arial", 14))
entry_computing_id.pack(pady=10)

button_check_id = tk.Button(root, text="Check ID", command=check_computing_id, font=("Arial", 14))
button_check_id.pack(pady=10)

label_user_a = tk.Label(root, text=f"{user_a.name} meal ticket: {user_a.tickets}\nflex dollars: {user_a.flex_dollars}",
                        font=("Arial", 16))
label_user_b = tk.Label(root, text=f"{user_b.name} meal ticket: {user_b.tickets}\nflex dollars: {user_b.flex_dollars}",
                        font=("Arial", 16))

option_var = tk.StringVar(root)
option_var.set("Select Option")  # Default option

options_menu = tk.OptionMenu(root, option_var, "Meal Ticket", "Flex Dollar", command=option_selected)
options_menu.config(font=("Arial", 14))

# Flex dollar : input field and button
label_flex_dollar = tk.Label(root, text="Enter amount to send:", font=("Arial", 14))
entry_flex_dollar = tk.Entry(root, font=("Arial", 14))
button_send_flex = tk.Button(root, text="Send Flex Dollar", command=send_flex_dollar, font=("Arial", 14))

root.mainloop()

