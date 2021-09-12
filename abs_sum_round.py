# Python iterable functions: Abs, Sum and Round

# abs() Only works with integer or float numbers and returns an absolute value of it

# abs exemples

print(abs(-3.14))
print(abs(3.14))
print(abs(12))
print(abs(-12))


# sum() Only works with integer or float numbers and returns the summation of the iterable values

# sum exemples

# List
print(sum([1, 2, 3, 5, 8, 13]))
# Tuple
print(sum((1, 2, 3, 5, 8, 13)))
# Set
print(sum({1, 2, 3, 5, 8, 13}))
# Dict
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 8, 'f': 13}.values()))

# sum function u can pass the default value to be added after the summation of the iterable values
print(sum([1, 2, 3, 5, 8, 13], 10))

# round() Only works with integer or float numbers and returns rounding of the iterable values
# recives 2 arguments: number that u want to round and the decimal places

# round exemples

print(round(3.14)) # 3
print(round(3.1)) # 3
print(round(3.14, 1)) # 3.1
print(round(3.1417, 2)) # 3.14
print(round(223.1443123564, 3)) # 223.144
print(round(223.11111111, 2)) # 233.11
print(round(223.19999999, 2)) # 233.20 == 233.2
print(round(223.19999999, 4)) # 233.2000 == 233.2
