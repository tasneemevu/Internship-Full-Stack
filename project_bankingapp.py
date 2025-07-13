class Bank:
    def __init__(self, initial_amount=0.00):
        self.balance= initial_amount

    def transaction_log(self, transaction_history):
        with open("transaction_log.txt", "a") as file:
            file.write(f"{transaction_history} with a new balance of {self.balance}\n")

    def withdraw(self, amount):
        try:
            amount= float(amount)
        except ValueError:
            amount = 0.00
        if amount:
            self.balance = self.balance - amount
            self.transaction_log(f"Withdrawn: {amount}, New Balance: {self.balance}")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0.00
        if amount:

            self.balance = self.balance + amount
            self.transaction_log(f"Deposited: {amount}, New Balance: {self.balance}")

account = Bank(100.00)

while True:
    try:
        action=input ("What kind of transactions would you like to do? (withdraw/deposit/exit): ").strip().lower()

    except KeyboardInterrupt:
        print("\nExiting the banking application.")
        break

    if action == "withdraw":
        amount = input("How much would you like to withdraw? ")
        account.withdraw(amount)
    elif action == "deposit":
        amount = input("How much would you like to deposit? ")
        account.deposit(amount)
    elif action == "exit":
        break
    else:
        print("Invalid action")
    print(f"Your current balance is: {account.balance}")
