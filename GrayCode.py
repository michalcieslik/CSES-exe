import sys

number = int(input())
get_bin = lambda x, n: format(x, 'b').zfill(n)
binnary = ["0", "1"]
reverse = []
if number == 1:
    print("0")
    print("1")
    sys.exit()
for i in range(1, number):
    reverse.clear()
    for j in range(len(binnary) - 1, -1, -1):
        binnary.append(binnary[j])
    for j in range(int(len(binnary) / 2)):
        binnary[j] = "0" + binnary[j]
        binnary[int(len(binnary) / 2) + j] = "1" + binnary[int(len(binnary) / 2) + j]
for i in range(len(binnary)):
    print(binnary[i])
