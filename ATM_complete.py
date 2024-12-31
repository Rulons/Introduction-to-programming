class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin  # Default PIN is set to "1234" for simplicity

    # Method to check balance
    def check_balance(self):
        print(f"Your current balance is: £{self.balance}")

    # Method to deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Error: You cannot deposit a non-positive amount.")
        else:
            self.balance += amount
            print(f"Successfully deposited £{amount}. Your new balance is £{self.balance}.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: You cannot withdraw a non-positive amount.")
        elif amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew £{amount}. Your new balance is £{self.balance}.")

    # Method to validate PIN
    def validate_pin(self, entered_pin):
        if entered_pin == self.pin:
            return True
        else:
            return False


def main():
    atm = ATM(1000)  # Starting balance of £1000

    # Prompt for PIN
    entered_pin = input("Please enter your PIN: ")
    if atm.validate_pin(entered_pin):
        print("PIN verified successfully!")
    else:
        print("Incorrect PIN. Access denied.")
        return  # Exit the program if PIN is incorrect

    while True:
        print("\ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Please choose an option (1/2/3/4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: £"))
                atm.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: £"))
                atm.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option (1/2/3/4).")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")