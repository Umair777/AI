
dict1 = {
"key1": 1,
"key2": "2",
"key3": "value3",
"key4": [1,2,3],
"key5": (4,5,6),
"key6": {"nestedKey1": "nestedValue1"},
(0,1): 7
}
print("Dictionary:", dict1)

# Access to the value by the key
print("Value for 'key3':", dict1["key3"])

# Access to the value by the key
print("value to 0-1 ", dict1[(0,1)])

dict2 = dict(keyA="valueA", keyB=100, keyC=[7,8,9])
print("Dictionary 2:", dict2)

# print keys and values
print("Keys of dict1:", dict2.keys())
print("Values of dict1:", dict2.values())
# Append value with key into dictionary
dict2["keyD"] = "valueD"
print("Updated Dictionary 2:", dict2)
#delete key-value pair from dictionary
del dict2["keyB"]
print("Dictionary 2 after deletion:", dict2)

'''
Output:Dictionary: {'key1': 1, 'key2': '2', 'key3': 'value3', 'key4': [1, 2, 3], 'key5': (4, 5, 6), 'key6': {'nestedKey1': 'nestedValue1'}, (0, 1): 7}
Value for 'key3': value3
value to 0-1  7
Dictionary 2: {'keyA': 'valueA', 'keyB': 100, 'keyC': [7, 8, 9]}
Keys of dict1: dict_keys(['keyA', 'keyB', 'keyC'])
Values of dict1: dict_values(['valueA', 100, [7, 8, 9]])
Updated Dictionary 2: {'keyA': 'valueA', 'keyB': 100, 'keyC': [7, 8, 9], 'keyD': 'valueD'}
Dictionary 2 after deletion: {'keyA': 'valueA', 'keyC': [7, 8, 9], 'keyD': 'valueD'}'''