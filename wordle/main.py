# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
my_file = open("word.txt")
words = my_file.readlines()
my_file.close()
newWords = []
for word in words:
    newWords.append(word[:len(word) - 1])
words = newWords
print(newWords)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def checkGuess(guess):
    if guess in words:
        return True
    return False

def wordle(actual):
    answer = ["", "", "", "", ""]
    check = False
    while not check:
        guess = input("Guess:")
        check = checkGuess(guess)
    guess = list(guess)
    for i in range(0, 5):
        if actual[i] == guess[i]:
            answer[i] = actual[i]
            actual = actual.replace(guess[i], "3", 1)
    for i in range(0, 5):
        if answer[i] == "":
            if guess[i] in actual and answer[actual.index(guess[i])] != guess[i]:
                answer[i] = "yell"
                actual = actual.replace(guess[i], "3", 1)
    return answer

def randWord():
    return random.choice(words)
#guess word
#check if each space matches (for greens)
#if not check if letter in word in not green spots (yellow)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    actual = randWord()
    poopy = True
    while poopy:
        subhon = wordle(actual)
        print(subhon)
        poopy = False
        for letter in subhon:
            if letter == "":
                poopy = True






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
