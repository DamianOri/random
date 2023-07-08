# Guessing game
# Damian, 08-07-2023
import random
a = 0
x = random.randint(1, 100)

print("In this \"game\" you need to guess a randomly generated number.\nThankfully your job is made a bit easier by the computer telling you if your guess is too high or too low")

while True:
    a += 1
    y = input("Input a guess: ")
    if(int(y) < x):
        print("Too low")
    elif(int(y) > x):
        print("Too high")
    else:
        break
print(f"Congrats! You guessed the number! You needed {a} guesses.")
input("Press ENTER to leave.")
