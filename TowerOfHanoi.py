import sys


def number_of_moves(n: int):
    if n == 1:
        return 1
    else:
        return 2 * number_of_moves(n - 1) + 1


def hanoi(n, source, destination, auxiliary):
    if n==1:
        print(source + " " + destination)
        return
    hanoi(n - 1, source, auxiliary, destination)
    print(source + " " + destination)
    hanoi(n - 1, auxiliary, destination, source)


number = int(input())
print(number_of_moves(number))
hanoi(number, "1", "3", "2")

