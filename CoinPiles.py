import sys
import math

number = int(input())
numbers = []
for i in range(number):
    numbers.append(list(map(int, input().split())))

for i in range(number):
    if numbers[i][0] > 2 * numbers[i][1] or 2 * numbers[i][0] < numbers[i][1] or (numbers[i][0] + numbers[i][1]) % 3 != 0:
        print("NO")
    else:
        print("YES")