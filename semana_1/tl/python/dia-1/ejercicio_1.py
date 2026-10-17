#name = input("give me please your name: ")
#print (name)
#lastname = input("give me please your lastname: ")
#print (lastname)
#mail = input("enter your mail: ")
#print (mail)
#print (f"Your name is: {name}, your lastname is: {lastname}, and your mail is: {mail}")
#print ("Your name is: " + name + "your lastname is: " + lastname + "your mail is: " + mail)
"""number1 = int((input("Enter the first number: ")))
print(number1)
number2 = int((input("Enter your second number: ")))
print(number2)"""
#result = int(number1) + int(number2)
#print(result)
selection = -1
while selection != 5:
    number1 = int((input("Enter the first number: ")))
    number2 = int((input("Enter your second number: ")))

    print("what you want to do?:")
    print("1. add")
    print("2. substract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    selection = int(input("Enter your selection: "))

    match selection:
        case 1:
            print(number1+number2)
        case 2:
            print(number1-number2)
        case 3:
            print(number1*number2)
        case 4:
            print(number1/number2)
        case 5:
            print("Se youu...")
        case _:
            print("Incorrect selection")

print("you'r out")
"""
bad way

if selection == 1:
    result = number1+number2
elif selection == 2:
    result = number1-number2
elif selection == 3:
    result = number1*number2
elif selection == 4:
    result = number1/number2
else:
    print ("Incorrect selection")

print(result)
"""




