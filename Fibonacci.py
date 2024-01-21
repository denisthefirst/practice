num = int(input("Enter the number of the numbers in sequence to generate: "))

list = []

def fibonacci():
    a = 0
    b = 1
    for i in range(num):
        c = b
        b = a + b
        a = c
        list.append(a)

fibonacci()
print(list)
