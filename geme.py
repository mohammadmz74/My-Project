import random
#random number between 1 to 10
secret_number = random.randint(1, 10)

def run_game():
    guesses = []
    guess = 0
    while len(guesses) < 5:
        #safely make an int
        try:
            #get a number guess from player
            guess = int(input("guess a number between 1 to 10: "))
        except ValueError:
                print("{} isn't a number".format(guess))
        else:
            #compare guess secret number
            if guess == secret_number:
                #print hit/miss
                print("you got it! my number was{}".format(secret_number))
                break
            elif guess < secret_number:
                print("my number is higher than {}".format(guess))
            elif guess > secret_number:
                print("my number is lower than {}".format(guess))
            else:
                #print hit/miss
                print("that's not it!")
        guesses.append(guess)

    else:
        print("you didn't my number was {}".format(secret_number))

    play_again = input("do you want to play? [Y/N]")
    if play_again.lower() != 'n':
        run_game()
    else:
        print("bye")

run_game()
        