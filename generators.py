# Python: Generators

# Generetors work like list comprehesions but it not return a list it return a generator object

candies = ['Kitkat', 'lollipop', 'Marshmallow', 'Nougat', 'Oreo', 'Pie', 'Honeycomb']

# List comprehension:
exemple = [len(candy) < 5 for candy in candies]
print(type(exemple))

print(any([len(candy) < 5 for candy in candies]))

# Work like a list comprehension but using () 
exemple2 = (len(candy) < 5 for candy in candies)
print(type(exemple2))

print(any(len(candy) < 5 for candy in candies))

# If compared generators and lists  we can see that generators consume less memory and have a 
# better performace

from sys import getsizeof


candies = ['Kitkat', 'Klollipop', 'Marshmallow', 'Nougat', 'Oreo', 'Katy', 'Kaslov']

# Empty list
print(getsizeof([]))
# List
print(getsizeof([10]))
# Tuple
print(getsizeof(10,))
# Set
print(getsizeof({10}))

# List
list_comprehension = [candy for candy in candies if candy[0] is 'K']
print(list_comprehension)
print(type(list_comprehension))
print(getsizeof(list_comprehension))

# Dict
dict_comprehension = {candy: 10 for candy in candies if candy[0] is 'K'}
print(dict_comprehension)
print(type(dict_comprehension))
print(getsizeof(dict_comprehension))

# Set
set_comprehension = {candy for candy in candies if candy[0] is 'K'}
print(set_comprehension)
print(type(set_comprehension))
print(getsizeof(set_comprehension))

# Generator
generator = (candy for candy in candies if candy[0] is 'K')
print(generator)
print(type(generator))
print(getsizeof(generator))
