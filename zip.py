# Python iterable function: Zip

# zip() create a zip object 

list1 = [1, 2, 3, 4, 5] # 5 elements
list2 = ['Matheus', 'Makarenna', 'Charlie', 'Anubis', 'Bastet']
tuple1 = (1, 2, 3, 'a', 'b', 'c') # 6 elements
set1 = {1, 2, 3, 4, 5}

zip1 = zip(list1, list2)
zip2 = zip(list1, tuple1) # only make pairs of the existing elements so 'c' will not be zipped
zip3 = zip(list2, set1)
zip4 = zip(list1, list2, tuple1, set1)

print(type(zip4))

print(dict(zip1))
print(tuple(zip2)) 
print(set(zip3))
print(list(zip4))

# using python unpacking 
list_values = [(0, 10), (20, 30), (40, 50), (60, 70), (80, 90)]
print(list(zip(*list_values)))

# Classroom grade exemple

test1 = [ 67, 93, 72, 45, 82]
test2 = [ 81, 65, 66, 32, 71]
students = ['Charlie', 'Clair', 'Allan', 'Jake', 'Mathew']
# Getting avarege of grades
avarage = {student[0]: sum([student[1], student[2]]) / 2 for student in zip(students, test1, test2)}
# Build a dict with only approved students
final = {student[0]: 'Approved' for student in zip(students, test1, test2) if sum([student[1], student[2]]) / 2 > 50.0}

print('\n\n')
print(avarage)
print(final)

print('\n\n')
# Using map() with zip

# Getting avarege of grades
avg2 = zip(students, map(lambda avg: (avg[0] + avg[1]) / 2, zip(test1, test2)))

# Comparing each item from iterable 
final2 = map(lambda x: f'{x[0]}: Approved' if x[1] > 60.0 else f'{x[0]}: Repproved', avg2)
print(list(final2))
