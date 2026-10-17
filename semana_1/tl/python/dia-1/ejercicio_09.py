price = int(input("Give me the price: "))
if price >= 200_000:
    print(f"Pay: {price*0.8}")
elif price >= 100_000:
    print(f"Pay: {price*0.9}")
else:
    print("Pay: price")