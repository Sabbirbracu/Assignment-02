q = int(input("please input your quantity"))
m = 0
maxi = 0
mini = 0
n_first = 0
sum = 0
for i in range(q):
    n = int(input("please input your numbers"))
    if i == 0:
        n_first = n
    for j in range(1):
        if n > m:
            maxi = n
        if n_first < n:
            mini = n_first
        sum = sum + n
    m = n
avg = sum / q

print("maximum", maxi)
print("minimum", mini)
print("Average", avg)

