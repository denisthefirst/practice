import random

num = int(input("Guess the number from 1-9: "))
randomNum = random.randint(1,9)
i = 1

while num != randomNum:
    i += 1
    if num < randomNum:
        num = int(input("Ouh, you guessed to low! Try again: "))
    else:
        num = int(input("Ouh, you guessed to high! Try again: "))

print("Congrats! You guessed right: " + str(num) + "=" + str(randomNum) + "\n It took you: " + str(i) + " guesses")




