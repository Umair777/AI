import numpy as np

# Create a 1D array
array_1d = np.array([10, 20, 30, 40, 50])

# Print the array
print("1D Array:", array_1d)
print("Type of array:", type(array_1d))

# Slicing the numpy array
c = array_1d[1:4]
print("Sliced Array (index 1 to 3):", c)

# Create the index list
select = [0, 2, 3]

# Indexing using a list
d = array_1d[select]
print("Selected elements from original array:", d)

# Get the number of dimensions of numpy array
print("Dimension: ", array_1d.ndim)

#Get the shape and size of numpy array
print("numpy array: ", array_1d.shape)

## STATS
# Create a numpy array

a = np.array([1, 2, 3, -1])
mean = a.mean()
print("Mean:", mean)

standard_deviation=a.std()
print("Standard Deviation:", standard_deviation)
variance=a.var()
print("Variance:", variance)

# Sum of all elements
sum_of_elements = a.sum()
print("Sum of all elements:", sum_of_elements)
# Product of all elements
product_of_elements = a.prod()
print("Product of all elements:", product_of_elements)
# Minimum element
min_element = a.min()
print("Minimum element:", min_element)
# Maximum element
max_element = a.max()
print("Maximum element:", max_element)
# Index of minimum element
index_of_min = a.argmin()
print("Index of minimum element:", index_of_min)
# Index of maximum element
index_of_max = a.argmax()
print("Index of maximum element:", index_of_max)
# Cumulative sum
cumulative_sum = a.cumsum()
print("Cumulative sum:", cumulative_sum)

## array operations
# addition




