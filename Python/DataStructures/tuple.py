# Create your first tuple

tuple1 = ("disco",10,1.2 )
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])

# sorting a tuple

tuple2 = (2,5,3,1,4)
print("Original Tuple:", tuple2)
sorted_tuple = sorted(tuple2)
print("Sorted Tuple:", sorted_tuple)

# nested tuple

nested_tuple = ("python", ('a','b','3ba'),[1,2,3], (4,5,6))
print("Nested Tuple:", nested_tuple)

# Print element on each index

print("Element 0 of Tuple: ", nested_tuple[0])
print("Element 1 of Tuple: ", nested_tuple[1])
print("Element 2 of Tuple: ", nested_tuple[2])

# Print the first element in the first econd nested tuples

print(nested_tuple[1][2][0])

'''
OUTPUT:
First element: disco
Last element: 1.2
Original Tuple: (2, 5, 3, 1, 4)
Sorted Tuple: [1, 2, 3, 4, 5]
Nested Tuple: ('python', ('a', 'b', '3ba'), [1, 2, 3], (4, 5, 6))
Element 0 of Tuple:  python
Element 1 of Tuple:  ('a', 'b', '3ba')
Element 2 of Tuple:  [1, 2, 3]
3
'''