"""
Algorithm:
    _________ == [ ]
        win
    else:
        reduce the turn
        figure
        the figure die

1) Develop the interface
2) Add a predefined list
3) instructions
4) check the words
    if right:    then enter in empty list
    if not: the draw figure
5) reduce the turns
6) Generate the figure

Enter Word
        checking it validor not
guessMade

Word    Main
Main == word ==> User Wins
"""
import random


def hangman():
    word = random.choice(["hello", "little", "sleep", "avengers", "doremon", "pokemon", "hangman", "python", "google", "netflix"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessMade = ''

    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in  guessMade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You won... ")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print("Enter a valid Character...")
            guess = input()

        if guess not in word:
            turns -= 1
            """
            for i in range(9):
                print(i, "turns left")
                print(" ---------------- ")
                i -= 1
            """
            if turns == 9:
                print("9 turns left")
                print(" ---------------- ")
            if turns == 8:
                print("8 turns left")
                print(" ----------------")
                print("         O       ")
            if turns == 7:
                print("7 turns left")
                print(" ---------------- ")
                print("         O       ")
                print("         |       ")
            if turns == 6:
                print("6 turns left")
                print(" ---------------- ")
                print("         O       ")
                print("         |       ")
                print("        /        ")
            if turns == 5:
                print("5 turns left")
                print(" ---------------- ")
                print("         O       ")
                print("         |       ")
                print("        / \      ")
            if turns == 4:
                print("4 turns left")
                print(" ---------------- ")
                print("       \ O      ")
                print("         |       ")
                print("        / \      ")
            if turns == 3:
                print("3 turns left")
                print(" ---------------- ")
                print("       \ O /     ")
                print("         |       ")
                print("        / \      ")
            if turns == 2:
                print("2 turns left")
                print(" ---------------- ")
                print("       \ O / |   ")
                print("         |       ")
                print("        / \      ")
            if turns == 1:
                print("1 turns left")
                print(" ----------------")
                print("       \ O_|/    ")
                print("         |       ")
                print("        / \      ")
            if turns == 0:
                print("You Lost!!! Try Again ;-( ")
                print("         O_|    ")
                print("       / | \     ")
                print("        / \      ")
                break



# interface

name = input("Enter your Name: ")
print("Welcome, ", name)
print("------------------------------")
print("Try to Guess the word in less than 10 tries...")

hangman()
