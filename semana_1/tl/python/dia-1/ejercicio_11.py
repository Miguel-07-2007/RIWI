temp = int(input("Give me your temp: "))
if temp < 10:
    print("cold")
elif 10 <= temp < 25:
    print("tempered")
elif 25 <= temp < 35:
    print("warm")
else:
    print("hot")