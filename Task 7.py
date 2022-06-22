
total = 0
count = 0
for i in range(10):
    num = int(input("please enter the number"))
    if num % 2 != 0:
        total += num
        count += 1
avg = total / count
print("The total of the odd number is", total, "and their average is", avg)


