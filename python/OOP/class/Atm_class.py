class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0
        # self.run_atm()  # Starts the ATM interface
        print(id(self))  # Prints the memory address of the object
    def run_atm(self):
        # while True:
            self.menu()
            
    def menu(self):
        try:
            user_input = int(input('''
            Hello, welcome to the ATM
            How would you like to proceed?
            1. Enter 1 to create pin
            2. Enter 2 to check balance
            3. Enter 3 to deposit
            4. Enter 4 to withdraw
            5. Enter 5 to transfer
            6. Enter 6 to exit
                                                    
            Enter your choice:
            '''))

            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.check_balance()
            elif user_input == 3:
                self.deposit()
            elif user_input == 4:
                self.withdraw()
            elif user_input == 5:
                self.transfer()
            elif user_input == 6:
                self.exit()
                return  # Exits the loop by breaking out of the menu
            else:
                self.not_in_options()
                
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6.")

    def create_pin(self):
        pin = input("Enter a new 4-digit pin: ")
        if len(pin) == 4 and pin.isdigit():
            self.pin = pin
            print("Pin created successfully")
        else:
            print("Invalid pin format. Please enter a 4-digit pin.")

    def check_balance(self):
        if self.authenticate():
            print(f"Your balance is {self.balance}")

    def deposit(self):
        if self.authenticate():
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Your balance is now {self.balance}")
            else:
                print("Invalid amount")

    def withdraw(self):
        if self.authenticate():
            amount = int(input("Enter amount to withdraw: "))
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"Your balance is now {self.balance}")
            else:
                print("Invalid or insufficient amount")

    def transfer(self):
        if self.authenticate():
            amount = int(input("Enter amount to transfer: "))
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"Transfer successful. Your balance is now {self.balance}")
            else:
                print("Invalid or insufficient amount")

    def authenticate(self):
        temp_pin = input("Enter your pin: ")
        if temp_pin == self.pin:
            return True
        else:
            print("Invalid pin")
            return False

    def exit(self):
        print("Thank you for banking with us")

    def not_in_options(self):
        print("Invalid option")


