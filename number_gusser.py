import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than zero next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print(f"You got it! You guessed {guesses} times")
        break
    elif user_guess > random_number:
        print(f"You were above the number. (Guess #{guesses})")
    else:
        print(f"You were below the number. (Guess #{guesses})")
