num = int(input("Enter a number: "))
divisors = range(1, num + 1)
divisorList = []

for elem in divisors:
    if num % elem == 0:
        divisorList.append(elem)

print(divisorList)

