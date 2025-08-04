def atm(balance):
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print(f"Your balance is: ₦{balance}")
        
        elif choice == '2':
            amount = input("Enter deposit amount: ")
            if amount.replace('.', '', 1).isdigit():
                balance += float(amount)
                print(f"Deposited ₦{amount}. New balance: ₦{balance}")
            else:
                print("Invalid deposit amount.")
        
        elif choice == '3':
            amount = input("Enter withdrawal amount: ")
            if amount.replace('.', '', 1).isdigit():
                amount = float(amount)
                if amount <= balance:
                    balance -= amount
                    print(f"Withdrew ₦{amount}. New balance: ₦{balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid withdrawal amount.")
        
        elif choice == '4':
            print("Thank you for using the ATM.")
            return balance
        
        else:
            print("Invalid option. Please choose between 1 and 4.")

# === Get initial balance from user ===
initial_input = input("Enter initial balance: ")

if initial_input.replace('.', '', 1).isdigit():
    initial_balance = float(initial_input)
    final_balance = atm(initial_balance)
    print(f"\nFinal balance: ₦{final_balance}")
else:
    print("Invalid initial balance. Please enter a number.")
