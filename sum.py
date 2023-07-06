# Sum of numbers from 1 to n
# Damian, 06-07-2023
def sumToN(n):
    for i in range(1, n):
        n = i+n
    return n
n = input("n = ")
print("Sum of integers from 1 to n: " + str(sumToN(int(n))))
