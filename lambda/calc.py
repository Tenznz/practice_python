# add = lambda a, b: a + b
# sub = lambda a, b: a - b
# mul = lambda a, b: a * b
# div = lambda a, b: a / b

calc = {
    1: lambda a, b: a + b,
    2: lambda a, b: a - b,
    3: lambda a, b: a * b,
    4: lambda a, b: a / b,
}
num1 = int(input('Enter number1'))
num2 = int(input('Enter number2'))

opera = int(input('''1.add
2.sub
3.mul
4.div
'''))
print(calc.get(opera, 'wrong input')(num1, num2))
