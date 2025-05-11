import numpy as np

def my_convolution(arr1, arr2):
    m1 = len(arr1)
    m2 = len(arr2)
    result = [0] * (m1 + m2 - 1)
    for i in range(m1):
        for j in range(m2):
            result[i + j] += arr1[i] * arr2[j]
    
    return result


first_array = [5, 12, 25, 6, 11, 8, 15, 10]
second_array = [6, 17, 19, 3, 21, 7, 7, 35, 17, 18]

my_result = my_convolution(first_array, second_array)
np_result = np.convolve(first_array, second_array, mode='full')

print("Custom convolution result:")
print(my_result)

print("Numpy convolution result:")
print(np_result)

are_equal = np.array_equal(my_result, np_result) 
print(f"Are the results equal? {are_equal}")