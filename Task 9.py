num = int(input("please enter your number"))
coun=0
#hile count < 5:
 #   num = int(input("please enter your number"))
#print(num)



list_input = []
list_order = ['first', 'second', 'third', 'fourth', 'fifth']
sum_integers = 0
for i in range(0, 5):
    a = input(f"Insert {list_order[i]} element: ")
    list_input.append(int(a))
for x in list_input:
    sum_integers += x
    if x != sum_integers:
        print(sum_integers)
