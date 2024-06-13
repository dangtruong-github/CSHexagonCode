import math


def checkprime(n):
    check = 1
    if n < 2:
        check = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            check = 0
            break
    return check


n = int(input())

if checkprime(n):
    print("so nguyen to")
else:
    print("deo phai so nguyen to")
""""""