# ============================================
# Bank Account Management System using OOP
# ============================================

# Base Class
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        # Encapsulation: private attributes
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    # Display account details
    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__holder_name)
        print("Balance: ₹", self.__balance)


# Child Class (Inheritance)
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.04):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # Method Overriding
    def display_details(self):
        super().display_details()
        print("Account Type: Savings")
        print("Interest Rate:", self.interest_rate * 100, "%")

    # Extra method
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print("Interest added successfully.")


# Child Class (Inheritance)
class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    # Method Overriding
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")


# Main Program
if __name__ == "__main__":
    # Creating multiple objects
    acc1 = SavingsAccount(101, "Likitha", 10000)
    acc2 = CurrentAccount(102, "Ravi", 5000)

    # Simulating bank operations
    acc1.display_details()
    acc1.deposit(2000)
    acc1.add_interest()
    acc1.withdraw(1500)
    acc1.display_details()

    acc2.display_details()
    acc2.deposit(3000)
    acc2.withdraw(7000)
    acc2.display_details()
