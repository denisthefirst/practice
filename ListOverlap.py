import random
a = [random.randint(1, 20) for _ in range(random.randint(10, 15))]
b = [random.randint(1, 20) for _ in range(random.randint(10, 15))]
list = []

for i in range(len(a)):
    if a[i] in b and a[i] not in list:
        list.append(a[i])

print(list)