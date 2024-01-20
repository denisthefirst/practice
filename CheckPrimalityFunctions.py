def get_integer(helptext):
    return int(input(helptext))

num = get_integer("Enter a number: ")
divisors = range(1, num + 1)
divisorList = []

for elem in divisors:
    if num % elem == 0:
        divisorList.append(elem)

if len(divisorList) < 3:
    print(str(num) + " is a prime number!")
else:
    print(str(num) + " is not a prime number!")
