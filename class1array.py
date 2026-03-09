# Using NumPy
# Once you've installed NumPy you can import it as a library:

import numpy as np

# Numpy has many built-in functions and capabilities.
# We won't cover them all but instead we will focus on some of the most important aspects of Numpy:
# vectors, arrays, matrices, and number generation.
# Let's start by discussing arrays.

# Numpy Arrays
# NumPy arrays are the main way we will use Numpy throughout the course.
# Numpy arrays essentially come in two flavors: vectors and matrices.
# Vectors are strictly 1-d arrays and matrices are 2-d
# (but you should note a matrix can still have only one row or one column).

# Let's begin our introduction by exploring how to create NumPy arrays.

# Creating NumPy Arrays
# From a Python List
# We can create an array by directly converting a list or list of lists:

lis = [1,2,3,4]
arr = np.array(lis)
print(arr)

# Lets create a matrix using list

lis = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(lis)
print(arr)

# Now lets see how matrix looks like using numpy arrays

matrix = np.array([[1,2,3,4],[5,6,7,12],[8,9,10,11]])
print(matrix)

# Built-in Methods
# there are lots of built in methods to create an array lets create some and see

# np.zeros(), np.ones(), np.full()
# np.arange(), np.linspace()
# np.eye()

arr = np.zeros(5)
print(arr)

arr = np.ones([5,3])
print(arr)

arr = np.full([5,5],10)
print(arr)

arr = np.arange(1,11)
print(arr)

arr = np.linspace(1,10,5)
print(arr)

arr = np.eye(5)
print(arr)

arr = np.random.rand(5)
print(arr)

arr = np.random.randint(1,10,5)
print(arr)

arr = np.random.rand(2,5)
print(arr)

# Explanation Notes

# arange → step-based values
# linspace → fixed number of values
# eye → identity matrix
# rand → random floats (0–1)
# randint → random integers in a range
# randn → random values from bell curve distribution