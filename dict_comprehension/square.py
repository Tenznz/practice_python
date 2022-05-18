input_list = [1, 2, 3, 4, 5, 6, 7]
dict_data = {}
# traditional
for i in input_list:
    dict_data.update({i: i ** 2})
print(dict_data)
# comprehension
res_data = {i: i ** 2 for i in input_list}
print(res_data)
