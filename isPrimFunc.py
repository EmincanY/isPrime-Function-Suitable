from math import sqrt as sqrt

def isPrime(num):
    if num < 2 or type(num) == float:
        return False
    else:
        for i in range(2, int(sqrt(num)+1)):
            if num % i == 0:
                return False
        return True

# Fast running isPrime function. Probably fastest.
