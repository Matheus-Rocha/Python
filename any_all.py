# Python iterable function: Any and All

# all() return True if all elements in iterable are true or if it's empty

# all() exemple:

number_list = [0, 1, 2, 3, 5, 8, 13] # zero return False
string_list = ['Learning', 'advanced ', 'Python']
string_list2 = ['Learning', 'advanced ', 'Python', ''] # '' return False
empty_list = []

print(all(number_list))
print(all([1, 2, 3, 5, 8, 13]))
print(all(string_list))
print(all(string_list2))
print(all(empty_list))

name_list = ['Matheus', 'Makarenna ', 'Marcos']
name_list2 = ['Matheus', 'Makarenna ', 'Marcos', 'Katy']
name_list3 = ['Matheus', 'Marcos']

# Checking if all names in list starts with M
print(all([name[0] == 'M' for name in name_list]))
print(all([name[0] == 'M' for name in name_list2]))

# Checking if all names in list ends with s
print(all([name[-1] == 's' for name in name_list3]))

# any() return True if at least one element is true in iterable if its empty return False

# Any exemples:

print(any([0, 1, 2, 3, 5, 8, 13]))
print(any([1, 2, 3, 5, 8, 13]))
print(any(['Learning', 'advanced ', 'Python']))
print(any(['Learning', 'advanced ', 'Python', '']))
print(any(['']))
print(any([]))


# Checking if there is the word Dragon in the sentence
sentece = 'I love my baby dragon'
sentece = sentece.split()
print(any([word == 'dragon' for word in sentece]))
