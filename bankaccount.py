import random

class BankAccount(object):
    def __init__(self, name, accountType, balance=0):
        """
        Constructor to initialize the account, generate an ID, 
        and create a transaction history file.
        """
        self.name = name
        self.accountType = accountType
        self.balance = balance
        
        # Generate a random 6-digit account number
        self.accountNumber = random.randint(100000, 999999)
        
        # Define the filename based on the specific naming format requested
        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        
        # Create the file and record the initial account creation
        with open(self.filename, "w") as file:
            file.write(f"Transaction History for {self.name}\n")
            file.write(f"Account Number: {self.accountNumber}\n")
            file.write(f"Account Type: {self.accountType}\n")
            file.write(f"Initial Balance: ${self.balance}\n")
            file.write("-" * 30 + "\n")

    def deposit(self, amount):
        """Deposits money and logs the transaction to the file."""
        if amount > 0:
            self.balance += amount
            log_entry = f"Deposited: ${amount} | New Balance: ${self.balance}\n"
            
            # Append transaction to the file
            with open(self.filename, "a") as file:
                file.write(log_entry)
            print(f"Successfully deposited ${amount}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraws money (if balance allows) and logs the transaction to the file."""
        if amount > self.balance:
            print(f"Transaction Denied: Insufficient funds. Balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            log_entry = f"Withdrew: ${amount} | New Balance: ${self.balance}\n"
            
            # Append transaction to the file
            with open(self.filename, "a") as file:
                file.write(log_entry)
            print(f"Successfully withdrew ${amount}.")

    def get_balance(self):
        """Returns the current balance."""
        return self.balance

    def get_id(self):
        """Returns the account ID."""
        return self.accountNumber

    def get_username(self):
        """Returns the holder's name."""
        return self.name

    def get_account_type(self):
        """Returns the account type."""
        return self.accountType

    def get_transaction_history(self):
        """Reads and displays the content of the transaction file."""
        print(f"\n--- Reading Statement File: {self.filename} ---")
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return "Transaction file not found."

# --- Testing the Code ---

# Create Account 1
user1 = BankAccount("AliceSmith", "savings", 1000)
user1.deposit(500)
user1.withdraw(200)

# Create Account 2
user2 = BankAccount("BobJones", "chequing", 200)
user2.deposit(50)
user2.withdraw(300) # Should fail due to insufficient funds

# Displaying info for User 1
print(f"\nUser: {user1.get_username()}")
print(f"Account ID: {user1.get_id()}")
print(f"Current Balance: ${user1.get_balance()}")

# Show Transaction History for User 1 from the file
print(user1.get_transaction_history())

# Show Transaction History for User 2 from the file
print(user2.get_transaction_history())
