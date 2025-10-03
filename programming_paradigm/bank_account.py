class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default = 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Returns True if successful, else False."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
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
        """Display the current balance with 2 decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
