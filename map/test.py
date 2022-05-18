import random


def check(x, y):
    if x == y:
        return x
    else:
        return y


input_list1 = [random.randrange(1, 100) for i in range(10)]
input_list2 = [random.randrange(1, 100) for j in range(10)]

print(input_list1)
print(input_list2)

try:
    # duplicate = map(lambda x: True if x == y else y, input_list)
    duplicate = map(lambda x, y: 1 if x == y else 0, input_list1, input_list2)
    print([i for i in duplicate])
except Exception as e:
    print(e)
