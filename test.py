import math
import numpy as np

pi = 3.14

volume = 0.0

print(math.sqrt(pi))

a = 4

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# for loop
start = 1
stop = 10

for i in np.arange(0, 5.5, 0.5):
    print(i, end=" ")

start = 0
print()
while start < 5.5:
    print(start, end=" ")
    start = start + 0.5


def procedure():
    print("Something")


def some_function():
    return 0

""""
for (int i = start, i < stop; i=i+1) {
    system.println(i)
}
"""
