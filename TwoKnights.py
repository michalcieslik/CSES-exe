import sys
import math

number = int(input())
for i in range(1, number + 1):
    board = i * i
    sum = 0
    if i == 1:
        print(0)
    elif i == 2:
        print(6)
    elif i == 3:
        print(28)
    else:
        # for j in range(1, board + 1):
        #     varieable = 0
        #     if j <= 4 + 2 * (i - 2) + (i - 4) + 2 * (i - 2) + (i - 4) * (i - 2):
        #         varieable = 4
        #     if j <= 4 + 2 * (i - 2) + (i - 4) + 2 * (i - 2):
        #         varieable = 3
        #     if j <= 4 + 2 * (i - 2) + (i - 4):
        #         varieable = 2
        #     if j <= 4:
        #         varieable = 1
        #     sum = sum + board - varieable - j
        sum = board * board - int(((board*(board+1)) / 2)) - 4 * 1 - (2 * (i - 2) + (i - 4)) * 2 - (2 * (i - 2)) * 3 - ((i - 4) * (i - 2)) * 4
        print(sum)

