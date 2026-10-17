ATM_balance = 500_000

while True:
    print("Welcome to NU")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit\n")

    option = int(input("Choose one option:"))
    match option:
        case 1:
            print(ATM_balance)
        case 2:
            amount = int(input("Enter the amount to withdraw:"))
            if amount > ATM_balance:
                print(f"Too much, you have ONLY {ATM_balance}")
            else:
                ATM_balance -= amount
                print(f"successful withdrawal, now your balance is {ATM_balance}")
        case 3:
            amount = int(input("Enter the amount to deposit:"))
            ATM_balance += amount
            print(f"succesful deposit, now your balance is {ATM_balance}")
        case 4:
            print("BYE")
            break
        case _:
            print("Wrong option, try again")
    print("")