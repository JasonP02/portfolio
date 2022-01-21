words = []
with open(r'C:\Users\jason\OneDrive\Desktop\sowpods.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)

######
import random

random_word_index = random.randint(0, len(words))
word = words[random_word_index]
hangman_word = list(word)
len_hangman = len(hangman_word)
blanks = []

for i in range(0, len_hangman):
    blanks.append("_")

x = True
## GAME
while x == True:
    counter = 0
    for i in range(0, len_hangman):
        if blanks[i] != "_":
            counter = counter + 1
            print(counter)
            print(len_hangman)
            if counter == len_hangman:
                x = False

    print(blanks)
    Guess = (input("Please guess a letter")).upper()
    for i in range(0, len_hangman):
        if Guess == hangman_word[i]:
            blanks[i] = Guess
