import numpy as np

y = np.array([-9, 2, 2, 5, 8, 8])

yy = np.array([2, 2, 3, 5, 7, 8])

x = np.array([[1, 2, 0], [4, 5, 6], [7, 8, 9], [1, 2, 3]])

y = np.array([[1, 2, 0], [-4, 5, 6], [7, 8, 9]])

B = np.random.choice(6, 6, replace = True)

a = 1 
b = 2
c = -1
A = []
A = [a, b, c]

A = np.maximum(A, 0)

print(A)
