name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 18:
    print(f"\n{name} is under 18")
else:
    print(f"\n{name} is 18 or older")