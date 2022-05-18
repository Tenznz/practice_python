from functools import reduce

# maxnumber
list_data = [1, 2, 3, 4, 10, 5, 6, 7, 8, 9, ]
max_number = reduce(lambda x, y: x if x > y else y, list_data)
print(max_number)

# sumall
sum_all = reduce(lambda x, y: x + y, list_data)
print(sum_all)






