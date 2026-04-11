# Understanding NumPy Arrays
# Exercise 1: Exercise: Exploring NumPy Arrays
# 1. Create Arrays: Create a 1D array with numbers from 1 to 5 and a 2D array with numbers from 1 to 6 (reshape it to have 2 rows and 3 columns).
# USE:(https://numpy.org/doc/stable/reference/generated/numpy.reshape.html), (https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
# 2. Inspect Attributes: For each array you created, print its shape, size, and data type.
# 3. Play with Data Types: Create a new array with numbers from 1 to 3, but specify the data type as float. Check and print its data type.
# Expected Output:
#     Prints of the created arrays with their respective shapes, sizes, and data types.
#     An array with a specified data type different from the default.
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5])
print('Shape:', array_1d.shape)
print('Size:', array_1d.size)
print('Data Type:', array_1d.dtype)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print('Shape:', array_2d.shape)
print('Size:', array_2d.size)
print('Data Type:', array_2d.dtype)
arr = np.array([1, 2, 3], dtype=float)
print(arr)
print(arr.dtype)
# Exercise: Create the following arrays
# A one dimensional array with the temperatures from this week.
# A two dimensional array of shape 2,5 with random values (choose them yourself) from 1 to 10.
# A 3D array with valid pixel values for a picture with 9 pixels.
week_temperatures = np.array([30, 32, 28, 31, 29, 27, 33])
array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
image = np.array([
    [[255, 0, 0],   [0, 255, 0],   [0, 0, 255]],   
    [[255, 255, 0], [0, 255, 255], [255, 0, 255]], 
    [[128, 128, 128],[64, 64, 64], [0, 0, 0]]    
], dtype=np.uint8)
# Array Indexing & Slicing
# Exercise: Practicing Indexing and Slicing
# 1. Basic Indexing: Create an array of 10 elements and access the 5th element in it.
arr_10 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr_10[4])  
# 2. Basic Slicing: From the same array, extract a slice containing the 3rd to the 8th elements.
arr_10 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
slice_arr = arr_10[2:8]
print(slice_arr)
# 3. Boolean Indexing: Create an array of 6 random integers between 10 and 50. Print the elements that are greater than 30.
random_arr = np.random.randint(10, 51, size=6)
print("Random Array:", random_arr)
greater_than_30 = random_arr[random_arr > 30]
print("Elements greater than 30:", greater_than_30)
# 4. Fancy Indexing: From the same array, use fancy indexing to access the 2nd, 4th, and 6th elements.
arr_10 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
fancy_indexed_elements = arr_10[[1, 3, 5]]
print("Selected elements (2nd, 4th, 6th):", fancy_indexed_elements)
# Expected Output:
#     The 5th element of the first array.
#     A slice of the array showing elements from the 3rd to the 8th position.
#     Elements greater than 30 from the random array.
#     Selected elements (2nd, 4th, 6th) from the random array using fancy indexing.

