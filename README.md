# Bank Account Simulator

A simple menu-driven banking application built with Python.

This project simulates basic bank account operations such as:

- Balance inquiry
- Depositing money
- Withdrawing money
- Transaction history
- Input validation
- Account state management

## Project Objective

The goal of this project is to practice:

- Python functions
- Classes and objects
- Loops
- Conditional statements
- Input validation
- Lists
- State management
- Exception handling

## Features

### 1. Check Balance

Displays the current account balance.

Example:

```text
Current Balance: ₹5000.00

### 2. Deposit Money
Allows the user to add money to the account.

The application validates that the deposit amount is greater than zero.

Example:

Enter amount: ₹2000
₹2000.00 deposited successfully.
New Balance: ₹7000.00

### 3. Withdraw Money
Allows the user to withdraw money from the account.

The application prevents withdrawals when:

The amount is zero or negative

The withdrawal amount is greater than the available balance

Example:

Enter amount: ₹1000
₹1000.00 withdrawn successfully.
New Balance: ₹6000.00

If the balance is insufficient:

Withdrawal rejected: insufficient balance.

### 4. Transaction History
All deposits and withdrawals are stored in a list.

Example:

========== TRANSACTION HISTORY ==========

1. 2026-10-03 16:30:10 | Deposit | ₹5000.00 | Balance: ₹5000.00
2. 2026-10-03 16:31:20 | Deposit | ₹2000.00 | Balance: ₹7000.00
3. 2026-10-03 16:32:15 | Withdrawal | ₹1000.00 | Balance: ₹6000.00

==========================================

5. Input Validation
The application validates:

Empty account holder names

Invalid menu choices

Non-numeric amounts

Zero or negative amounts

Withdrawals greater than the available balance

Technologies Used
Python 3

Python Standard Library

datetime module

No external packages are required.

Project Structure
bank-account-simulator/
│
├── bank_simulator.py
└── README.md

How to Run
Step 1: Install Python
Make sure Python 3 is installed.

Check your Python version:

python --version

or:

python3 --version

Step 2: Run the program
python bank_simulator.py

On some systems:

python3 bank_simulator.py

Example Usage
Welcome to the Bank Account Simulator!

Enter account holder name: Ankita

Welcome, Ankita!

========== BANK ACCOUNT SIMULATOR ==========
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
=============================================

Enter your choice (1-5): 2
Enter amount: ₹5000

₹5000.00 deposited successfully.
New Balance: ₹5000.00

========== BANK ACCOUNT SIMULATOR ==========
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
=============================================

Enter your choice (1-5): 3
Enter amount: ₹1500

₹1500.00 withdrawn successfully.
New Balance: ₹3500.00

========== BANK ACCOUNT SIMULATOR ==========
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
=============================================

Enter your choice (1-5): 4

========== TRANSACTION HISTORY ==========

1. 2026-10-03 16:30:10 | Deposit | ₹5000.00 | Balance: ₹5000.00
2. 2026-10-03 16:31:25 | Withdrawal | ₹1500.00 | Balance: ₹3500.00

==========================================

Enter your choice (1-5): 5

Thank you for using the Bank Account Simulator!
Final Balance: ₹3500.00

# Important Concepts
## Application State
The BankAccount class maintains the application's state:

self.balance
self.transactions

The balance changes after every deposit or withdrawal, while every operation is stored in the transaction list.

## Preventing Invalid Withdrawals
Before withdrawing money, the program checks:

if amount > self.balance:
    print("Withdrawal rejected: insufficient balance.")
    return

This prevents the account from going into a negative balance.

## Storing Transactions
Transactions are stored as dictionaries inside a list:

self.transactions.append({
    "type": "Deposit",
    "amount": amount,
    "balance": self.balance,
    "date": self._current_time()
})

This makes it easy to display the transaction history later.

