"""
Python function: Map

import math

def lenght(r):
    return 2 * math.pi * r

number_list = [2, 4, 8, 10]

lenght_list = [lenght(item) for item in number_list]

print(lenght_list)

# using map

map_obj = map(lenght, number_list)

print(list(map_obj))
# or
print(list(map(lenght, number_list)))

# using lambda functions
print(list(map(lambda r: 2*math.pi*r, number_list)))

# Exemple:

# List of cities and weather in ºC

cities_c = [('Rio', 30), ('Recife', 33), ('Brasilia', 26), ('New York', 22), ('Berlim', 18), ('Oslo', 14)]

print(cities_c)

# Converting ºC to ºF = 9/5 * ºc + 32 to a dict

cities_f = dict(map(lambda t: (t[0], 9/5 * t[1] + 32), cities_c))

print(cities_f)

# Converting ºC to ºF to a list

print(list(map(lambda t: (t[0], 9/5 * t[1] + 32), cities_c)))

# the map object after used clean the memory
obj1 = map(lambda t: (t[0], 9/5 * t[1] + 32), cities_c)
print(list(obj1))
print(list(obj1))

"""

# Using filter() and map()
# Print the sentence "I like" and the name of candy that have less or iqual than 6 letters

candies = ['Kitkat', 'lollipop', 'Marshmallow', 'Nougat', 'Oreo', 'Pie', 'Honeycomb']

candy_list = list(map(lambda candy: f'I like {candy}', filter(lambda x: len(x) <= 6, candies)))

for candy in candy_list:
    print(candy)
