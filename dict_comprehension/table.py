def table(input_num):
    return {key: input_num * value for key, value in dict_data.items()}


dict_data = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10}
num = int(input('Enter number'))
print(table(num))
