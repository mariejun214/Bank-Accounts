
import random, msvcrt

def masked_input(prompt="Enter your PIN: "):
    print(prompt, end="", flush=True)
    pin = ""
    while True:
        ch = msvcrt.getch()
        if ch in {b"\r", b"\n"}:  # Enter key
            print()
            break
        elif ch == b"\x08":  # Backspace
            if len(pin) > 0:
                pin = pin[:-1]
                print("\b \b", end="", flush=True)
        else:
            pin += ch.decode("utf-8")
            print("*", end="", flush=True)
    return pin


class BankAccount:
    def __init__(self, first_name, last_name, account_name, account_id, account_type, username, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_name = account_name
        self.account_id = account_id
        self.account_type = account_type
        self.username = username
        self.pin = pin
        self.balance = balance

    #create account function
    def create_account(self):
        print("===== CREATE ACCOUNT =====")
        self.first_name = input("Enter First Name: ")
        self.last_name = input("Enter Last Name: ")
        self.account_id = random.randint(10000, 99999)
        self.account_type = input("Enter Account Type (Checking/Savings): ")
        self.username = input("Enter username: ")
        self.pin = input("Enter PIN: ")
        # set a single account_name for easier verification (e.g. "First Last")
        self.account_name = f"{self.first_name} {self.last_name}".strip()
        print("==========================")

    def created_account_display(self):
        peso_sign = chr(0x20B1)
        print("\n===== ACCOUNT DETAILS =====")
        print(f"Account Name: {self.first_name} {self.last_name}",
            f"\nAccount ID: {self.account_id}",
            f"\nAccount Type: {self.account_type}",
            f"\nUsername: {self.username}",
            f"\nPIN: {'*' * len(str(self.pin))}",
            f"\nBalance: {peso_sign}{self.balance:.2f}")
        print("===========================\n")
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def display_balance(self):
        peso_sign = chr(0x20B1)
        print("\n===== BALANCE INQUIRY =====")
        return f"Account Name: {self.first_name} {self.last_name}" + \
            f"\nAccount ID: {self.account_id}" + \
            f"\nAccount Type: {self.account_type}" + \
            f"\nAccount Balance: {peso_sign}{self.balance:.2f}" 
    
    def verify_account_name(self):
        print("\n=========LOG IN==========")
        entered_account_name = input("Enter account name (Full Name): ")
        # normalize comparison (trim and case-insensitive)
        return entered_account_name.strip().lower() == str(self.account_name).strip().lower()

    def verify_username(self):
        print("\nPlease enter your details for verification.")
        entered_username = input("Enter username: ")
        return entered_username == f"{self.username}"
    
    def verify_pin(self):
            entered_pin = masked_input("Enter your PIN: ")# to hide pin while typing
            return entered_pin == self.pin
    


