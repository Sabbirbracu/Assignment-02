n = int(input("Please input Your desire number:"))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count = count + 1

if count > 2:
    print(n, "is not a prime number")
elif n == 0:
    pass
else:
    print(n, "is a prime number")
