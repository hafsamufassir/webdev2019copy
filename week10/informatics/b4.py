array = []
n = int(input())

for i in range(n):
    num = input()
    array.append(num)
i = 1
for i in range(n):
    if((i+1) % 2 == 0):
        print(i+1, end=" ")
