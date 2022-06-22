n = int(input("please input your desire number:"))
x = n
total = 0
for i in range(1, n+1):
    if n % i == 0:

        if i == n:
            continue
        total = total + i
if total == x:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")


