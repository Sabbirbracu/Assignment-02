n = int(input("please input your number:"))
count = 0
for i in range(n):
    n = n // 10
    count += 1
    if n == 0:
        break
print(count, "digits")

