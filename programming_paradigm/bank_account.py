class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with optional initial balance (default is 0)."""
        self.__account_balance = initial_balance  # encapsulated attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient. Return True if successful."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance}")
