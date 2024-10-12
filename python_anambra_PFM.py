# Personal Finance Manager: 
# Build a program that allows users to input their income and expenses, 
# and then calculate their net savings. The program should use variables to 
#store different types of data (e.g., integers for amounts, strings for descriptions) 
# and perform arithmetic operations to calculate totals.

_________________________________________________________________________


class PersonalFinanceApp:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_income(self):
        amount = float(input("Enter the amount of income N"))
        self.balance += amount
        self.transactions.append(("Income", amount))
        print(f"Income added: ${amount: .2f}")

    def record_expense(self):
        amount = float(input("Enter the amount of expense: $"))
        if amount > self.balance:
            print("Insufficient balance. Please, try again.")
        else:
            category = input("Enter expense category (e.g., Rent, Food, Transport): ")
            self.balance -= amount
            self.transactions.append((category, amount))
            print(f"Expense recorded: ${amount: .2f} for {category}")

    def view_balance(self):
        print(f"Current balance: ${self.balance: .2f}")

    def transaction_summary(self):
        print("\nTransaction Summary: ")
        for t_type, amount in self.transactions:
            print(f"{t_type}: ${amount: .2f}")
        self.view_balance()

    def start(self):
        print("Personal Finance Manager!")

        while True:
            print("\nMenu:")
            print("1. Add Income")
            print("2. Record Expense")
            print("3. View Balance")
            print("4. View Transaction Summary")
            print("5. Exit")

            choice = input("Select an Option (1-5): ")
            if choice == "1":
                self.add_income()
            elif choice == "2":
                self.record_expense()
            elif choice == "3":
                self.view_balance()
            elif choice == "4":
                self.transaction_summary()
            elif choice == "5":
                print("Exiting... Thank you for using the app!")
                break
            else:
                print("Invalid option. Please try again")

app = PersonalFinanceApp()
app.start()
