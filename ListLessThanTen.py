a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num = int(input("Enter a number: "))

for i in range (len(a)):
    if a[i] < num:
        b.append(a[i])

print(b)