import random

rand = random.randint(1, 50)  #random number generated
attempts = 0 #total number of attempts at start

while True:
    num = int(input("Enter a number between 1 and 50: "))
    attempts += 1 #attemps after each guess are increased by one

    if num < 1 or num > 50:
        print ("Invalid number! Please enter between 1 and 50.")
        continue
    if num < rand:
        print ("Too low, try again.")
    elif num > rand:
        print ("Too high, try again.")
    else:
        print (" You guessed the number in",attempts,"attempts!")
        break
