import sys
import math

number = int(input())
maximum = 0
i = 5
while i <= number:
    maximum = maximum + int(number / i)
    i = i * 5
print(maximum)