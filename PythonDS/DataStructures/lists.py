
print("\n---List Operations---")

data = ["Hello AI", 42, 3.14, True, None, [1, 2, 3], {"API": "OpenAI"}]
# This is a list containing different data types, including a string, integer, float, boolean, NoneType, another list, and a dictionary.

print("Original List:", data)

# List slicing

data[3:5]
print("Sliced List (index 3 to 5):", data[3:5])


data.extend(['pop', 10])
print("List after extending:", data)

data.insert(2, "Inserted Value")
print("List after inserting at index 2:", data)

data.append("Appended Value")
print("List after appending:", data)

# Change the element based on the index
print("\n---Modifying List Elements---")

A = ["hi", 100, 1.72]
print('Before change:', A)
A[0] = 'Hello'
print('After change:', A)

## We can convert a string to a list using split. For example, the method split translates
# every group of characters separated by a space into an element in a list:

print("\n---String to List using split---")
string_data = "Hello AI enthusiasts, welcome to the world of Python."
list_data = string_data.split(" ")
print("String Data:", string_data)
print("List Data after split:", list_data)

print("String to List using split by comma:")
string_data_comma = "apple,banana,cherry,date"
list_data_comma = string_data_comma.split(",")
print("String Data:", string_data_comma)
print("List Data after split by comma:", list_data_comma)

## Copy (copy by reference) the list A
print("\n---Copying Lists---")
A = [1, 2, 3, 4, 5]
B = A
print("List A:", A)
print("List B (copy of A):", B)

# Verify the copy by reference
B[0] = 100
print("After modifying B:")
print("List A:", A)
print("List B:", B)

# Clone (clone by value) the list A
C = A.copy()
print("\nList C (clone of A):", C)

# Verify the clone by value
C[1] = 200
print("After modifying C:")
print("List A:", A)
print("List C:", C)

'''
Output:
---List Operations---
Original List: ['Hello AI', 42, 3.14, True, None, [1, 2, 3], {'API': 'OpenAI'}]
Sliced List (index 3 to 5): [True, None]
List after extending: ['Hello AI', 42, 3.14, True, None, [1, 2, 3], {'API': 'OpenAI'}, 'pop', 10]
List after inserting at index 2: ['Hello AI', 42, 'Inserted Value', 3.14, True, None, [1, 2, 3], {'API': 'OpenAI'}, 'pop', 10]
List after appending: ['Hello AI', 42, 'Inserted Value', 3.14, True, None, [1, 2, 3], {'API': 'OpenAI'}, 'pop', 10, 'Appended Value']

---Modifying List Elements---
Before change: ['hi', 100, 1.72]
After change: ['Hello', 100, 1.72]

---String to List using split---
String Data: Hello AI enthusiasts, welcome to the world of Python.
List Data after split: ['Hello', 'AI', 'enthusiasts,', 'welcome', 'to', 'the', 'world', 'of', 'Python.']
String to List using split by comma:
String Data: apple,banana,cherry,date
List Data after split by comma: ['apple', 'banana', 'cherry', 'date']

---Copying Lists---
List A: [1, 2, 3, 4, 5]
List B (copy of A): [1, 2, 3, 4, 5]
After modifying B:
List A: [100, 2, 3, 4, 5]
List B: [100, 2, 3, 4, 5]

List C (clone of A): [100, 2, 3, 4, 5]
After modifying C:
List A: [100, 2, 3, 4, 5]
List C: [100, 200, 3, 4, 5]

'''