import tkinter as tk
from tkinter import messagebox


balance = 1000.0

# Update balance display
def update_balance():
    balance_label.config(text=f"Balance: ₹{balance:.2f}")


def deposit():
    global balance
    try:
        amount = float(amount_entry.get())
        if amount > 0:
            balance += amount
            update_balance()
        else:
            messagebox.showerror("Error", "Enter a valid amount!")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount!")

    amount_entry.delete(0, tk.END)


def withdraw():
    global balance
    try:
        amount = float(amount_entry.get())
        if amount > 0 and amount <= balance:
            balance -= amount
            update_balance()
        elif amount > balance:
            messagebox.showerror("Error", "Insufficient balance!")
        else:
            messagebox.showerror("Error", "Enter a valid amount!")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount!")

    amount_entry.delete(0, tk.END)


root = tk.Tk()
root.title("My Bank")
root.geometry("350x250")
root.resizable(False, False)
root.configure(bg="#f3f4f6")


frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")


title = tk.Label(frame, text="My Bank", font=("Arial", 18, "bold"),
                 bg="white", fg="#1f2937")
title.pack(pady=10)

# Balance Label
balance_label = tk.Label(frame, text=f"Balance: ₹{balance:.2f}",
                         font=("Arial", 16, "bold"),
                         bg="white", fg="#2563eb")
balance_label.pack(pady=10)


amount_entry = tk.Entry(frame, font=("Arial", 14), width=20)
amount_entry.pack(pady=10)


btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack(pady=10)


deposit_btn = tk.Button(
    btn_frame,
    text="Deposit",
    bg="#10b981",
    fg="white",
    font=("Arial", 12, "bold"),
    width=10,
    command=deposit
)
deposit_btn.grid(row=0, column=0, padx=5)


withdraw_btn = tk.Button(
    btn_frame,
    text="Withdraw",
    bg="#ef4444",
    fg="white",
    font=("Arial", 12, "bold"),
    width=10,
    command=withdraw
)
withdraw_btn.grid(row=0, column=1, padx=5)

root.mainloop()
