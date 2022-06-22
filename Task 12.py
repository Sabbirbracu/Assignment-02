n = int(input("please input your number"))
count = 0
m = n
for i in range(m):
    m = m // 10
    count += 1
    if m == 0:
        break

power = 10 ** (count - 1)
for j in range(n):
    x = n // power
    n = n % power
    power = power//10
    print(x, end=",")

    if n == 0:
        break


