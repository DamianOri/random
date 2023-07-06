# Divisibility checks
# Damian, 06-07-2023
def isDivisible(num, divisor):
    if(num%divisor == 0):
        return True
    else:
        return False
def isEven(num):
    return isDivisible(num, 2)

num = input("Enter divident: ")
divisor = input("Enter divisor: ")
print("Divisible: " + str(isDivisible(int(num), int(divisor))))
print("Even: " + str(isEven(int(num))))
