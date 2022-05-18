import random

input_list1 = [random.randrange(1, 9) for i in range(3)]
input_list2 = [random.randrange(1, 9) for j in range(3)]

print(input_list1)
print(input_list2)
# j = [j for i in range(1, 4) for j in range(1, 4)]
# print(j)
# i = [i for i in range(1, 4) for j in range(1, 4)]
# print(i)
# count = 0
# res = [i for i in range(1, 4) for j in range(1, 4)]
# print(res)

res = [x for x in input_list2 if x % 2 == 0]
print(res)
