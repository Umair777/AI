import numpy as np

a = [[1,2,3,2], [3,4,5,3], [5,6,7,5]]
print(len(a))

b = np.array(a)
print(b.shape)


for i in range(len(a)):
    print("Row ", i, ":", a[i]) 
    for j in range(len(a[i])):
        print("Element at (", i, ",", j, ") :", a[i][j])
        
#product of all elements
print("Product of all elements:", np.prod(b))

#sum of all elements
print("Sum of all elements:", np.sum(b))
print('a shape : {}, b shape: {}'.format(np.array(a).shape, b.shape))
# b = b.transpose()
# print(b)
# #product of two arrays
# c = np.dot(b, b)
# print("Product of two arrays:\n", c)

# Calculate the sine of c
# sine_of_c = np.sin(c)
# print("Sine of the product array:\n", sine_of_c)  
'''
Output:
Element at ( 2 , 0 ) : 5
Element at ( 2 , 1 ) : 6
Element at ( 2 , 2 ) : 7
Element at ( 2 , 3 ) : 5
Product of all elements: 2268000
Sum of all elements: 46
a shape : (3, 4), b shape: (3, 4)'''
