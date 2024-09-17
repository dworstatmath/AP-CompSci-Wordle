import random
words =["apple","stove","pizza","games","piles"]
word = random.choice(words)
#colors for printing
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

def generate_hint(user_guess):
    hint=""
    for i in range(5):
        if user_guess[i]==word[i]:
            hint+=(green+user_guess[i])
        elif user_guess[i] in word:
            hint+=(yellow+user_guess[i])
        else:
            hint+=(default+user_guess[i])
    print(hint+default)


def game_loop():
    guess=""
    for i in range(6):
        guess=input("what is your guess: ")
        if guess == word:
            print ("you win")
            break
        generate_hint(guess)
game_loop()