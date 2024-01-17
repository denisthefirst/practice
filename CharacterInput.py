from datetime import date

name = input("Give me your name: ")
age = int(input("Give me your age: "))
printing = int(input("Give me the amount of how many times you want this messages to shown: "))
current_year = date.today().year
years_until_100 = 100 - age
years_turn_100 = current_year + years_until_100

for i in range(printing):
    print("Your name is " + name + "! " + "In year " + str(years_turn_100)
        + " you are going to turn 100 years old!")