import random

number = random.randint(0,100)
guesses = [0]
while True:
    guess = int(input("Guess a number between 0 t0 100: "))
    #print(number)
    guesses.append(guess)
    if guess == number:
        print("congrats! thats right!")
        break
    elif guess < 1 or guess > 100:
        print("Out of bound!")
    elif guesses[-2]:
        if abs(guesses[-2] - number) > abs(guess - number):
            print("warmer")
        else:
            print("colder")
