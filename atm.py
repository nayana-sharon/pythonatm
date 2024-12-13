import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")

        # Initialize user data
        self.accounts = {
            "12345": {"pin": "1234", "balance": 5000},
            "67890": {"pin": "6789", "balance": 3000}
        }
        self.logged_in = False
        self.current_account = None

        # Create the GUI components
        self.create_login_screen()

    def create_login_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Login Screen UI elements
        self.card_label = tk.Label(self.root, text="Card Number:")
        self.card_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.card_entry = tk.Entry(self.root)
        self.card_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pin_label = tk.Label(self.root, text="PIN:")
        self.pin_label.grid(row=1, column=0, padx=10, pady=10)

        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        card_number = self.card_entry.get()
        pin = self.pin_entry.get()

        if card_number in self.accounts and self.accounts[card_number]["pin"] == pin:
            self.logged_in = True
            self.current_account = card_number
            self.create_atm_screen()
        else:
            messagebox.showerror("Error", "Invalid card number or PIN.")
        
    def create_atm_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # ATM Screen UI elements
        self.balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance)
        self.balance_button.grid(row=0, column=0, padx=10, pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw Money", command=self.withdraw_money)
        self.withdraw_button.grid(row=0, column=1, padx=10, pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit Money", command=self.deposit_money)
        self.deposit_button.grid(row=1, column=0, padx=10, pady=10)

        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=1, padx=10, pady=10)

    def check_balance(self):
        balance = self.accounts[self.current_account]["balance"]
        messagebox.showinfo("Balance", f"Your current balance is ${balance}")

    def withdraw_money(self):
        def withdraw():
            amount = float(amount_entry.get())
            if amount > 0 and amount <= self.accounts[self.current_account]["balance"]:
                self.accounts[self.current_account]["balance"] -= amount
                messagebox.showinfo("Success", f"${amount} has been withdrawn.")
                top.withdraw()
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid amount.")

        top = tk.Toplevel(self.root)
        top.title("Withdraw Money")

        amount_label = tk.Label(top, text="Enter amount to withdraw:")
        amount_label.grid(row=0, column=0, padx=10, pady=10)

        amount_entry = tk.Entry(top)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        withdraw_button = tk.Button(top, text="Withdraw", command=withdraw)
        withdraw_button.grid(row=1, column=0, columnspan=2, pady=10)

    def deposit_money(self):
        def deposit():
            amount = float(amount_entry.get())
            if amount > 0:
                self.accounts[self.current_account]["balance"] += amount
                messagebox.showinfo("Success", f"${amount} has been deposited.")
                top.withdraw()
            else:
                messagebox.showerror("Error", "Invalid deposit amount.")

        top = tk.Toplevel(self.root)
        top.title("Deposit Money")

        amount_label = tk.Label(top, text="Enter amount to deposit:")
        amount_label.grid(row=0, column=0, padx=10, pady=10)

        amount_entry = tk.Entry(top)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        deposit_button = tk.Button(top, text="Deposit", command=deposit)
        deposit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def logout(self):
        self.logged_in = False
        self.current_account = None
        self.create_login_screen()

# Create the main window
root = tk.Tk()
atm = ATM(root)
root.mainloop()
