num = [5, 12, 17, 18, 24, 32]


def even(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


data = filter(even, num)

for i in data:
    print(i)
