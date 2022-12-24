#guess word
#check if each space matches (for greens)
#if not check if letter in word in not green spots (yellow)
from words import *
def wordle(actual):
    answer = ["", "", "", "", ""]
    check = False
    while not check:
        guess = input("Guess:")
        check = checkGuess(guess)
    for i in range(0, 5):
        if actual[i] == guess[i]:
            answer[i] = actual[i]
    for i in range(0, 5):
        if answer[i] == "":
            if guess[i] in actual and answer[actual.index(guess[i])] == "":
                answer[i] = "yell"
    return answer
