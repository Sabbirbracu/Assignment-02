count = 63
total = 0
while count <= 600:
    if count % 7 == 0 and count % 9 == 0:
        if count == 567:
            print(count, end="=")
        else:
            print(count, end="+")
        total = total + count
    else:
        pass
    count = count+1

print(total)
