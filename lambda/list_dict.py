get_list = lambda *a: [i for i in a]

get_dict = lambda a, b: dict(i for i in zip(a, b))

print(get_list(1, 2, 3, 4, 5, 6))
print(get_dict([1, 2, 3, 4], ['a', 'b', 'c', 'd']))