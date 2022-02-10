# 10 II 2022, 0.1

input_string = input('Enter the words you want to check seperated by spaces (NOT COMMAS): \n') # The input is a single string
words = input_string.split()    # Here the program separates the input into many strings in each place where a space is

long = words[0]                 # Setting the current longest word to the first word in the list
for i in range(len(words)):     # The loop repeats as many times as there are words in the list
    x = words[i]                # x = current word
    if(len(x) > len(long)):     # If the current word is longer than the longest word
        long = x                # Sets the current word as longest

print(long)
input('Press anything to exit.')
# This might have too many comments, however i like to keep them so i can easily understand the code
