from datetime import datetime
class BankAccount:
    """A simple bank account simulator."""
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        if initial_balance > 0:
            self.transactions.append({
                "type": "Deposit",
                "amount": initial_balance,
                "balance": self.balance,
                "date": self._current_time()
            })
    def _current_time(self):
        """Return the current date and time."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def check_balance(self):
        """Display the current account balance."""
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self.balance,
            "date": self._current_time()
        })
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New Balance: ₹{self.balance:.2f}")
    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Withdrawal rejected: insufficient balance.")
            return
        self.balance -= amount
        self.transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "balance": self.balance,
            "date": self._current_time()
        })
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"New Balance: ₹{self.balance:.2f}")
    def show_transactions(self):
        """Display all account transactions."""
        print("\n========== TRANSACTION HISTORY ==========")
        if not self.transactions:
            print("No transactions available.")
            return
        for index, transaction in enumerate(self.transactions, start=1):
            print(
                f"{index}. "
                f"{transaction['date']} | "
                f"{transaction['type']} | "
                f"₹{transaction['amount']:.2f} | "
                f"Balance: ₹{transaction['balance']:.2f}"
            )
        print("==========================================")
def get_amount():
    """Get and validate a monetary amount from the user."""
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def display_menu():
    """Display the main menu."""
    print("\n========== BANK ACCOUNT SIMULATOR ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("=============================================")
def main():
    """Run the bank account simulator."""
    print("Welcome to the Bank Account Simulator!")
    account_holder = input("Enter account holder name: ").strip()
    while not account_holder:
        print("Account holder name cannot be empty.")
        account_holder = input("Enter account holder name: ").strip()
    print(f"\nWelcome, {account_holder}!")
    account = BankAccount(account_holder)
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = get_amount()
            account.deposit(amount)
        elif choice == "3":
            amount = get_amount()
            account.withdraw(amount)
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            print("\nThank you for using the Bank Account Simulator!")
            print(f"Final Balance: ₹{account.balance:.2f}")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")
if __name__ == "__main__":
    main()
