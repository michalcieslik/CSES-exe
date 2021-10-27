import sys


def calc(i):
    return (i - 1)*(i - 1) + i


number = int(input())
numbers = []
for i in range(number):
    numbers.append(list(map(int, input().split())))

for i in range(number):
    maximum = max(numbers[i][0], numbers[i][1])
    cross = calc(maximum)
    if numbers[i][0] == numbers[i][1]:
        print(cross)
        continue
    if numbers[i][0] < numbers[i][1] and maximum % 2 == 1:
        print(cross + (maximum - numbers[i][0]))
        continue
    if numbers[i][0] < numbers[i][1] and maximum % 2 == 0:
        print(cross - (maximum - numbers[i][0]))
        continue
    if numbers[i][0] > numbers[i][1] and maximum % 2 == 1:
        print(cross - (maximum - numbers[i][1]))
        continue
    if numbers[i][0] > numbers[i][1] and maximum % 2 == 0:
        print(cross + (maximum - numbers[i][1]))
        continue