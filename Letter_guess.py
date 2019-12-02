import random
import string
import codecs

turns_remaining = 5
words_list = list()
#with codecs.open("ukenglish.txt", "r",encoding= 'utf-8') as my_file:
with codecs.open("ukenglish.txt", "r",encoding="latin-1") as my_file:
    df = my_file.read()
    words_list = df.split("\n")
    #words_list.append(lf[0])

rand_word = random.choice(words_list)
rand_word = rand_word.lower()
disp_word = list()
word_found = False
letter_guess = False
word_len = 0
for i in range(len(rand_word)):
    disp_word.append("_")
for i in disp_word:
    print(i, end=" ")
print("")
while turns_remaining > 0:
    user_input = input("Enter a letter to guess the word as indicated above: ")
    pos = 0
    letter_guess = False
    #pos = rand_word.find(user_input)
    for i in rand_word:
        if i == user_input:
            disp_word[pos] = user_input
            letter_guess = True
        pos += 1
    for i in range(len(rand_word)):
        if disp_word[i] != rand_word[i]:
            break
        if i == ((len(rand_word)) - 1):
            word_found = True
    #print(len(rand_word))
    if word_found:
        print("You guessed it right! Its %s!!" % rand_word)
        break

    if not letter_guess:
        turns_remaining -= 1
        if turns_remaining > 0:
            print("Turns remaining:", turns_remaining)

    if turns_remaining > 0:
        for i in disp_word:
            print(i, end=' ')
    print(" ")

if (turns_remaining == 0) and (not word_found) :
    print("You did not guess the right word!")
