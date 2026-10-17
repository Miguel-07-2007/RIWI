while True:

    user = input("Enter your user: ")
    password = input("Enter your password: ")

    if user == "Admin123" and password == "1234":
        print("welcome")
        break
    else:
        print("user dont found, try again")