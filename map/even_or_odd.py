import random

input_list = [random.randrange(1, 100) for i in range(101)]
check = map(lambda x: 'even' if x % 2 == 0 else 'odd', input_list)
print([i for i in input_list])
print([i for i in check])

