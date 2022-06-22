total = 0
for i in range(601):
    if i % 7 == 0 and i % 9 == 0:
        continue
    elif i % 7 == 0 or i % 9 == 0:
        total = total + i
print(total)
        