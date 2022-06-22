n = int(input("please input the number:"))
y = 0
for i in range(n+1):
    if i % 2 == 0:
        y = y-(i**2)
    else:
        y = y + (i**2)
print(y)
