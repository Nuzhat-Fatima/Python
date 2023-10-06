#NUMPY

#1:Creating arrays:
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])                         # Creating a 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])                  # Creating a 2D array

#2:Mathematical operations:

sum_result = np.sum(arr1)                                # Sum of array elements
addition_result = arr1 + arr1                            # Element-wise addition
matrix_product = np.dot(arr1, arr2)                      # Matrix multiplication

#3:Array Manipulation:

reshaped = arr1.reshape((5, 1))                          # Reshaping arrays
transposed = arr2.T                                      # Transposing a matrix
stacked = np.vstack((arr1, arr2))                        # Stacking arrays vertically

#4:Random Number Generation:

random_numbers = np.random.rand(3, 3)                    # Generating random numbers
random_integers = np.random.randint(1, 10, size=(3, 3))  # Generating random integers

#5:File I/O:

data = np.loadtxt('data.txt')                            # Reading data from a text file
np.save('data.npy', data)                                # Saving data to a binary file


#6:Square of numbers:
num=np.array([2,4,8])
z= num**2
print(z)
