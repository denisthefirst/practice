import sys

player1 = input("Enter first players name: ")
player2 = input("Enter second players name: ")
stop = "y"

while(stop == "y"):
    game1 = input(player1 + "´s turn: ")
    game2 = input(player2 + "´s turn: ")

    def compare(u1, u2):
        if u1 == u2:
            print("it´s tie")
        elif u1 == "rock" and u2 == "paper":
            print(player2 + " wins")
        elif u1 == "paper" and u2 == "scissors":
            print(player2 + " wins")
        elif u1 == "scissors" and u2 == "rock":
            print(player2 + " wins")
        elif u1 == "paper" and u2 == "rock":
            print(player1 + " wins")
        elif u1 == "scissors" and u2 == "paper":
            print(player1 + " wins")
        elif u1 == "rock" and u2 == "scissors":
            print(player1 + " wins")
        else:
            return ("Invalid input! You have not entered rock, paper or scissors, try again.")
            sys.exit()

    print(compare(game1, game2))
    stop = input("type y if you want to continue if not type any other letter and press enter: ")

sys.exit()




