name = input("Enter your name: ")
product = input("Enter the product: ")
price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

subtotal = price*quantity

if subtotal >= 500_000:
    total = subtotal*0.85
    discount = 15
elif subtotal >= 200_000:
    total = subtotal*0.9
    discount = 10
else:
    discount = 0
    total = subtotal
print(f"\n{name}'s check: \nSubtotal:{subtotal}\nDiscount:{discount}%\nTotal:{total:.0f}")