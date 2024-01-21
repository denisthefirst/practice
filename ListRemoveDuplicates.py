list = [1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8]
newList = []

for i in range(len(list)):
    if list[i] in list and list[i] not in newList:
        newList.append(list[i])

print(newList)

