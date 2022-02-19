import math


# check if number is fibonacci
def isFibonacci(num):
    i = int(math.sqrt(num))
    return i*i == num

print(isFibonacci(4))

