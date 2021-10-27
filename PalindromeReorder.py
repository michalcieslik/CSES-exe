import sys
import math
import string

word = str(input())
endWord = ""
mid = ""
odd = 0
letters = string.ascii_uppercase
for j in range(len(letters)):
    howMany = word.count(letters[j])
    if howMany % 2 == 0:
        for i in range(int(howMany / 2)):
            endWord = endWord + letters[j]
    elif howMany % 2 == 1 and odd == 0:
        mid = letters[j]
        odd = odd + 1
        for i in range(int(howMany / 2)):
            endWord = endWord + letters[j]
    else:
        print("NO SOLUTION")
        sys.exit()
for i in range(len(endWord)):
    print(endWord[i], end="")
print(mid, end="")
for i in range(len(endWord) - 1, -1, -1):
    print(endWord[i], end="")