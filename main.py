from src.QPU import *
from src import GPU
from itertools import product

a = qbit()

a.vector = np.matrix([[1/sqrt(2)], [0], [1/sqrt(2)], [0]])

gate(Hadamard, a)

print(a.vector)


