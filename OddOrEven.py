num = int(input("Give a number: "))
check = int(input("Give a number to divide by: "))
if num % 4 == 0:
    print("Different Message")
elif num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num % check == 0:
    print(str(check) + " divides evenly into " + str(num))
else:
    print(str(check) + " doesn´t divide evenly into " + str(num))