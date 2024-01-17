from datetime import date

name = input("Give me your name: ")
age = int(input("Give me your age: "))
printing = int(input("Give me the amount of how many times you want this messages to shown: "))
years_until_100 = date.today().year + (100 - age)

for i in range(printing):
    print("Your name is " + name + "! " + "In year " + str(years_until_100)
        + " you are going to turn 100 years old!")