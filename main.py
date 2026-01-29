import random, os
from bank_accounts import BankAccount


#Display welcome message
print("====================================")
print("\tWELCOME TO YGOT BANK")
print("====================================\n")
print("   Thank you for banking with us!")
input("   Press enter to continue >>> ")
os.system('cls' if os.name == 'nt' else 'clear')

#Display menu
def menu():
    while True:
        print("=====================")
        print("\tMENU")
        print("=====================")
        print("1. Log In \n2. Create Account \n3. Balance Inquiry \n4. Deposit \n5. Withdraw \n6. Close Account \n7. Log Out \n8. Quit")
        print("=====================")    

        try:
            choice = int(input("\nEnter the number of your transaction: "))
            if 1 <= choice <= 8:
                os.system('cls' if os.name == 'nt' else 'clear')
                return choice   # # return the choice instead of using global
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
        
        input("Press enter to continue >>> ")
        os.system('cls' if os.name == 'nt' else 'clear')
        
#create a dictionary to hold multiple bank accounts
accounts = {}
current_user = None

# Main loop
while True:
    menu_choice = menu() # get fresh choice each time

    if menu_choice == 1: # Log In
        # Verify by account name
        matched_account = None
        for acc in accounts.values():
            if acc.verify_account_name():
                matched_account = acc
                print("Account verified! Please log in to continue...")
                break

        if matched_account is not None:    
            if matched_account.verify_username() and matched_account.verify_pin():
                current_user = matched_account
                print(f"\nWelcome, {current_user.first_name}!")
            else:
                print("Incorrect PIN. Login failed.")
        else:
            print("Account not found! Please create an account first.")

    elif menu_choice == 2: # Create Account
        new_account = BankAccount("", "", "", 0, "", "", "", 0.0)
        new_account.create_account()
        accounts[new_account.username] = new_account # store by username
        print("\nAccount successfully created!")
        new_account.created_account_display()

    elif menu_choice == 3: # Balance Inquiry
        if current_user is not None:
            print(current_user.display_balance())
        else:
            print("No user is logged in. Please log in first.")

    elif menu_choice == 4:  # Deposit
        if current_user is not None:
            try:
                amount = float(input("Enter amount to deposit: "))
                current_user.deposit(amount)
                print(f"Transaction successful! \nDeposited amount: {amount:.2f}  \nNew balance: {current_user.balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")
        else:
            print("No user is logged in. Please log in first.")

    elif menu_choice == 5:  # Withdraw
        if current_user is not None:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > current_user.balance:
                    print("Insufficient funds.")
                else:
                    current_user.withdraw(amount)
                    print(f"Transaction successful! \nWithdrawn amount: {amount:.2f}  \nNew balance: {current_user.balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")
        else:
            print("No user is logged in. Please log in first.")

    elif menu_choice == 6:  # Close Account
        if current_user is not None:
            confirm = input("Are you sure you want to close your account? (yes/no): ")
            if confirm.lower() == 'yes':
                del accounts[current_user.username]
                print("Account successfully closed.")
                print("Thank you for banking with us!\n")
                current_user = None  # log out automatically
            else:
                print("Account closure cancelled.")
        else:
            print("No user is logged in. Please log in first.")

    elif menu_choice == 7:  # Log Out
        if current_user is not None:
            print(f"User {current_user.username} has been logged out.")
            current_user = None
        else:
            print("No user is currently logged in.")

    elif menu_choice == 8: # Quit the program
        print("Thank you for banking with us! Goodbye!\n")
        break
    
    input("Press enter to continue >>> ")
    os.system('cls' if os.name == 'nt' else 'clear')
