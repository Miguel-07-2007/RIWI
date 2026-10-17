age = int(input("Give me yur age: "))
def verify_age(age):
    if age < 0:
        print("age not valid")
    elif age < 18:
        print(f"is under 18")
    else:
        print(f"is 18 or older")
verify_age(age)