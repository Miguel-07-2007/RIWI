selection = -1
while selection != 5:
    print("what you want to do?:")
    print("1. add")
    print("2. substract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    selection = int(input("Enter your selection: "))

    match selection:
        case 1:
            number1 = int((input("Enter the first number: ")))
            number2 = int((input("Enter your second number: ")))
            print(number1+number2)
        case 2:
            number1 = int((input("Enter the first number: ")))
            number2 = int((input("Enter your second number: ")))
            print(number1-number2)
        case 3:
            number1 = int((input("Enter the first number: ")))
            number2 = int((input("Enter your second number: ")))
            print(number1*number2)
        case 4:
            number1 = int((input("Enter the first number: ")))
            number2 = int((input("Enter your second number: ")))
            if number2 == 0:
                print("you can't divide by zero")
                continue
            print(number1/number2)
        case 5:
            print("Se youu...")
        case _:
            print("Incorrect selection")

print("you'r out")

