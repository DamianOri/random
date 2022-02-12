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

i = 0
x = True
while(x == True):
    word = str.lower(input())
    if(word == "potato"):
        i = i + 1
    elif(word == "exit"):
        x = False
    else:
        i = i
    print(f"Potato count: {i}")
input("Press ENTER to leave")
