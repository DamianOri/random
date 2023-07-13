# Guessing game v1.1
# Damian, 13-07-2023
import random
count = 0
randNum = random.randint(1, 100)

print("In this \"game\" you need to guess a randomly generated integer from 1 to 100.\nThankfully your job is made a bit easier by the computer telling you if your guess is too high or too low.\nYou can type \"exit\" to leave.")

while True:
    count += 1
    guess = input("Input a guess: ")
    if(guess.lower() == "exit"):
        quit()
    elif(guess.isdigit() == False):
        print("Input an integer, smh.")
    elif(int(guess) < randNum):
        print("Too low")
    elif(int(guess) > randNum):
        print("Too high")
    else:
        break
print(f"Congrats! You guessed the number! You needed {count} guesses.")
input("Press ENTER to leave.")
