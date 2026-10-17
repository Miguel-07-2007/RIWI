side1 = int(input("Give me the first side: "))
side2 = int(input("Give me the second side: "))
side3 = int(input("Give me the third side: "))

if side1 == side2 == side3:
    print("equilater")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("isosceles")
else:
    print("scalene")