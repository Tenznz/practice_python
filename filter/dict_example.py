dict_data = {
    '1': 11,
    '2': 22,
    '3': 33,
    '4': 44
}


def even(x):
    if int(x) % 2 == 0:
        return True
    else:
        return False


data = filter(even, dict_data.values())
for i in data:
    print(i)
data = filter(even, dict_data.keys())
for i in data:
    print(i)
