import sys
import math

number = int(input())
sum = (number * (number + 1)) / 2
if sum % 2 == 1:
    print("NO")
    sys.exit()
else:
    print("YES")
    if number % 2 == 1:
        print(int(number/2))
        x = number
        i = 1
        while x > 0:
            print(x, end=" ")
            if i % 2 == 1:
                x = x - 3
            else:
                x = x - 1
            i = i + 1
        print(int(number / 2) + 1)
        x = number - 1
        i = 1
        while x > 0:
            print(x, end=" ")
            if i % 2 == 0:
                x = x - 3
            else:
                x = x - 1
            i = i + 1
    else:
        print(int(number/2))
        x = number
        i = 1
        while x > 0:
            print(x, end=" ")
            if i % 2 == 1:
                x = x - 3
            else:
                x = x - 1
            i = i + 1
        print(int(number / 2))
        x = number - 1
        i = 1
        while x > 0:
            print(x, end=" ")
            if i % 2 == 0:
                x = x - 3
            else:
                x = x - 1
            i = i + 1
