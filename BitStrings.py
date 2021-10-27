import sys
import math

number = int(input())
sum = pow(2, number) % (1000000000 + 7)
print(sum)