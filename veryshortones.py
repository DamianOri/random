# Fast Inverse Square Root
x = input()
print(x**-0.5)

# Spelling out words
word = input()
print(list(word))

# Cheap uwu talk
x = input()
x = x.replace('r', 'w')
x = x.replace('l', 'w')
print(x.replace('u', 'w'))

# Potato counter

i = 0                           # Sets up the potato counter
x = True
while(x == True):               # The loop goes on for as long as x = True
    word = str.lower(input())   # The input is turned all lowercase so typing POTATO still counts
    if(word == "potato"):       # If you wrote potato
        i = i + 1               # The counter goes up by one
    elif(word == "exit"):       # If you type exit
        x = False               # x is now not equal to True, therefore after printing the potato count the loop ends and the program closes
    else:                       # If you didn't
        i = i                   # The counter stays the same
    print(f"Potato count: {i}") # After typing a word it prints the state of the counter and goes back to the beginning of the loop
input("Press ENTER to leave")   # It now doesnt' close automatically
