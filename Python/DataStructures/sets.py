# This is for creating examples of set operations in Python

# Creating two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union of sets
union_set = A.union(B)
print("Union of A and B:", union_set)

# Intersection of sets
intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)

# Difference of sets
# A - B (Elements in A but not in B)
difference_set = A.difference(B)
print("Difference of A and B (A - B):", difference_set)

# Symmetric Difference of sets
# Elements in either A or B but not in both
symmetric_difference_set = A.symmetric_difference(B)
print("Symmetric Difference of A and B:", symmetric_difference_set)

# Adding an element to set A
A.add(10)
print("Set A after adding 10:", A)
# Removing an element from set B
B.remove(6)
print("Set B after removing 6:", B)

# multi-variables set assignment
x, y, z = {1, 2}, {3, 4}, {5, 6}
print("Set x:", x)
print("Set y:", y)
print("Set z:", z)

movie_genres = [
    "Action",
    "Comedy",
    25,
    "Drama",
    "Horror",
    tuple({"Actors": tuple(["Actor1", "Actor2"])}.items())
]

unique_genres = set(movie_genres)
print(unique_genres)

'''
Output:
Set A: {1, 2, 3, 4, 5}
Set B: {4, 5, 6, 7, 8}
Union of A and B: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection of A and B: {4, 5}
Difference of A and B (A - B): {1, 2, 3}
Symmetric Difference of A and B: {1, 2, 3, 6, 7, 8}
Set A after adding 10: {1, 2, 3, 4, 5, 10}
Set B after removing 6: {4, 5, 7, 8}
Set x: {1, 2}
Set y: {3, 4}
Set z: {5, 6}
{'Action', 'Horror', (('Actors', ('Actor1', 'Actor2')),), 25, 'Comedy', 'Drama'}'''