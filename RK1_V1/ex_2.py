import random

def print_list(l):
    for i in range(n):
        print(l[i])
    print()

n = int(input())
m = int(input())

list = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        list[i][j] = random.randint(1, 100)
    list[i].sort()
print_list(list)

for j in range(m):
    for prohodi in range(n):
        for i in range(n - 1):
            if list[i][j] > list[i+1][j]:
                list[i][j], list[i+1][j] = list[i+1][j], list[i][j]
print_list(list)

cntr = 0
flag = False
k = int(input("k = "))
for i in range(n):
    if k in list[i]:
        flag = True
        break
    cntr += 1
    
if flag:
    print(f"true\nколичество проходов {cntr + 1}")
else:
    print("false")
        


