from datetime import datetime

name = "Suresh Kumar"
pin = 2003
balance = 10000
attempts = 0
transactions = []
daily_limit = 20000
withdrawn_today = 0
max_transaction = 50000

def load_data():
    global pin, balance

    with open("atm_data.txt", "r") as file:
        data = file.readlines()

    pin = int(data[0].strip())
    balance = int(data[1].strip())

def load_transactions():
    global transactions

    with open("transactions.txt", "r") as file:
        transactions = file.readlines()

    transactions = [transaction.strip() for transaction in transactions]

def save_data():
    with open("atm_data.txt", "w") as file:
        file.write(str(pin) + "\n")
        file.write(str(balance))

# for Balance
def check_balance():
    print("Your current balance is:", balance)

#For Deposit
def deposit():
    global balance

    try:
        amount = int(input("Enter amount to deposit: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Invalid amount")

    elif amount > max_transaction:
        print("Maximum transaction limit is:", max_transaction)

    else:
        balance = balance + amount
        save_data()

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = time + " | Deposit: " + str(amount) + " | Balance: " + str(balance)
        transactions.append(transaction)

        with open("transactions.txt", "a") as file:
            file.write(transaction + "\n")

        print("Your new balance:", balance)
        print("Transaction successful")

# For Withdraw
def withdraw():
    global balance, withdrawn_today

    try:
        amount = int(input("Enter amount to withdraw: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Invalid amount")

    elif amount > max_transaction:
        print("Maximum transaction limit is:", max_transaction)

    elif amount > balance:
        print("Insufficient balance")

    else:
        if withdrawn_today + amount <= daily_limit:
            print("Withdraw successful")

            balance = balance - amount
            withdrawn_today = withdrawn_today + amount

            save_data()

            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = time + " | Withdraw: " + str(amount) + " | Balance: " + str(balance)
            transactions.append(transaction)

            with open("transactions.txt", "a") as file:
                file.write(transaction + "\n")

            print("Remaining balance:", balance)
            print("Transaction successful")
            print("Withdrawn today:", withdrawn_today)
            print("Remaining withdrawal limit:",
                  daily_limit - withdrawn_today)

        else:
            print("Daily withdrawal limit exceeded.")

# For Pin
def change_pin():
    global pin

    enter_pin = input("Enter your current PIN: ")

    if len(enter_pin) != 4 or not enter_pin.isdigit():
        print("PIN must be exactly 4 digits")
        return

    enter_pin = int(enter_pin)

    if enter_pin == pin:
        new_pin = input("Enter your new PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            pin = int(new_pin)
            save_data()
            print("PIN changed successfully")
        else:
            print("PIN must be exactly 4 digits")
    else:
        print("Invalid current PIN")

# For mini statement
def mini_statement():
    print("======= MINI STATEMENT =======")
    print("Current Balance:", balance)

    if len(transactions) == 0:
        print("No Transactions")
    else:
        for transaction in transactions[-5:]:
            print(transaction)

# For login
def login():
    global attempts

    while attempts < 3:
        enter_pin = input("Enter your PIN: ")

        if len(enter_pin) != 4 or not enter_pin.isdigit():
            print("PIN must be exactly 4 digits")
            continue

        enter_pin = int(enter_pin)

        if enter_pin == pin:
            print("Login successful")
            return True
        else:
            print("Incorrect PIN")
            attempts = attempts + 1

    print("Card Blocked")
    return False

load_data()
load_transactions()

if login():
    print("Welcome",name)
    while True:
        print("======== ATM ========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("5. Change PIN")
        print("6. MINI Statement")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue
        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using Python ATM.")
            print("Goodbye,", name)
            break

        elif choice == 5:
            change_pin()

        elif choice == 6:
            mini_statement()

        else:
            print("Invalid choice")