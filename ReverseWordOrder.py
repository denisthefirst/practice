text = "Drying a car in the middle of the day is a good option"
list = text.split()
list_reserved = []
print(text)

for i in range(len(list)-1, -1, -1):
    list_reserved.append(list[i])

text_reserved = ' '.join(list_reserved)
print(text_reserved)