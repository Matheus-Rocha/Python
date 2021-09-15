"""
Python function: Reduce

Since python 3 the function reduce(func, iterable) need to be imported from functools

Understanding reduce function:

Iterable:

data = [a1, a2, a3, a4, ..., aN-1, aN]

The function that reduces use need 2 params

def func(x, y):
    return x + y

How it works:

   step 1: res1 = func(a1, a2)
   step 2: res2 = func(res1, a3)
   step 1: res3 = func(res2, a4)
   .
   .
   .
   step n: resN = func(aN-1, aN)
"""

from functools import reduce


number_list = [10, 25, 38, 40, 55, 90, 100, 12]

# Using lambda
sum_func = lambda x, y: x + y

# Using reduce()
sum_value = reduce(sum_func, number_list)

print(sum_value)

# Using loop for
sum1_value = 0
for n in number_list:
    sum1_value += n

print(sum1_value)
