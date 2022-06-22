start = 18
while start <= 63:
    if start % 2 == 0:
        print(start, end=",")

    elif start % 2 != 0:
        if start == 63:
            print(start * -1, end="")
        else:
            print(start * -1, end=",")
    start = start + 9
