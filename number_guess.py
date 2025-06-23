import random
range_num = int(input("Type a number: "))
random_number = random.randint(0, range_num)
attempts = 0
while True:
    attempts += 1
    your_guess = int(input("Make a guess: ")) 
    if your_guess == random_number:
        print("You got it!")
        break
    elif your_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
print("You got it in", attempts, "guesses")