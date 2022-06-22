num = int(input("PLEASE INPUT THE NUMBER"))
for i in range(num):
    x = num % 10
    print(x, end=",")
    num = num//10
    if num == 0:
        break