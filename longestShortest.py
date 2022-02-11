# 11 II 2022, 0.2

input_string = input('Enter the words you want to check seperated by spaces (NOT COMMAS): \n') 
words = input_string.split() 

long = words[0] 
short = words[0]
for i in range(len(words)): 
    x = words[i] 

    if(len(x) > len(long)):
        long = x
    if(len(x) < len(short)):
        short = x

print(f"Longest: {long} \n")
print(f"Shortest: {short} \n")

input('Press anything to exit.')
