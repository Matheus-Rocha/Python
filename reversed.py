# Python iterable function: Reversed


# Differences between reverse() and reversed()
# reverse()
# - only works with lists
# - modify the list
# - return a list

# reversed()
# - works with any kind of iterable
# - return a list reverse iterator
# - clear memory after used or converted


number_list = [10, 20, 50, 30, 40, 32]
reversed_obj = reversed(number_list)

print(type(reversed_obj))
print(reversed_obj)

# Its possible to convert a reverse object into List and Tuple
print(list(reversed_obj))

print(tuple(reversed_obj)) # The reversed obj clear the memory after used or converted

print(set(reversed_obj)) # Set dont change becouse it dont have an order



# print by default break line in the end
# end param will put it in the same line
for i in reversed('Advanced python'):
    print(i, end='')   

print('\n')
# Another way to print the string reversed:
print(''.join(list(reversed('Advanced python'))))

# We can do it without reversed and using strings slice:
print('Advanced python'[::-1])

# Countdown using reverse
for i in reversed(range(0, 10)):
    print(i, end=' ')

print('\n')

# without reverse
for i in range(9, -1, -1):
    print(i, end=' ')