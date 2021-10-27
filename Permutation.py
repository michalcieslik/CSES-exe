import sys

number = int(input())

if number == 1:
    print(1)
    sys.exit()
if 1 < number < 4 or number < 0:
    print("NO SOLUTION")
    sys.exit()
for i in range(2, number + 1, 2):
    print(i, end= ' ')
for i in range(1, number + 1, 2):
    print(i, end= ' ')
