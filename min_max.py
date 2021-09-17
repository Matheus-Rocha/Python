# Python iterable function: Min and Max

# Both functions recives as argument an interable and an optional argument key

# min() returns minimum value in the iterable

# max() returns maximum value in the iterable


number_list = [item for item in range(10)]
number_tuple = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
number_set = {item for item in range(10)}
number_gen = (item for item in range(10))

print(max(number_list))
print(max(number_tuple))
print(max(number_set))
print(max(number_gen))

number_list = [item for item in range(10)]
number_tuple = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
number_set = {item for item in range(10)}
number_gen = (item for item in range(10))

print(min(number_list))
print(min(number_tuple))
print(min(number_set))
print(min(number_gen))

spotify_dict = {
    'In the end': 6304192,
    'Toxicity': 9794178,
    'Blue eyes': 3304104,
    'Nothing else metters': 82304105,
    'Voluspá': 904102,
    'Numb': 4704103,
}

# return maximum value of the key by default
print(max(spotify_dict))

# return maximum value of the list with values formed by method values()
print(max(spotify_dict.values()))

# return maximum value of the list with keys formed by method items()
print(max(spotify_dict.keys()))

# return maximum value of the tuples formed by method items()
print(max(spotify_dict.items()))

# Using lambda functions

names_list = [ 'Matheus', 'Makarenna', 'Ivar', 'Floki', 'Ragnar', 'Rollo' ]

# Consedering the lenght of strings
max_value = max(names_list, key=lambda views: len(views))
# Consedering the first letter of the names
min_value = min(names_list, key=lambda views: views[0])

# return the item type and value
print(type(max_value))
print(max_value)

print(min_value)

# Using lambda functions

spotify_dict = [
    {'music_name': 'In the end', 'views': 6304192},
    {'music_name': 'Toxicity', 'views': 9794178},
    {'music_name': 'Blue eyes', 'views': 3304104},
    {'music_name': 'Nothing else metters', 'views': 82304105},
    {'music_name': 'Voluspá', 'views': 904102},
    {'music_name': 'Numb', 'views': 4704103},
]

# Min and max views values
print(max(spotify_dict, key=lambda music: music['views']))
print(min(spotify_dict, key=lambda music: music['views']))

# Printing only the name:
print(max(spotify_dict, key=lambda music: music['views'])['music_name'])
print(min(spotify_dict, key=lambda music: music['views'])['music_name'])
