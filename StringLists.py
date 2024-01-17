text = input("Give me a word: ")
reverse = text[::-1]

if text == reverse:
    print(text + " is a palindrome!")
else:
    print(text + " is not a palindrome!")
