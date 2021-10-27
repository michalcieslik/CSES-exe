import sys
import math
import string


def calc(n: str):
    total = 0
    divided = 1
    for i in string.ascii_lowercase:
        how_many = n.count(i)
        total = total + how_many
        if how_many > 1:
            divided = divided * math.factorial(how_many)
    return int(math.factorial(total) / divided)


word = str(input())
how_many = calc(word)
print(how_many)
