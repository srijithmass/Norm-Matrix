'''
Program to find 2-norm of a matrix.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
import numpy as np
n = eval(input())
val = np.linalg.norm(n,2)
print("{:.2f}".format(val))