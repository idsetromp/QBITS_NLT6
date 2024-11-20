from src.QPU import *
from src import GPU
from itertools import product

prep(qbit())
prep(qbit(np.matrix([[0], [1]])))
prep(qbit(np.matrix([[1/sqrt(2)], [1/sqrt(2)]])))

gate(CNOT, q[0], q[1])
print(q[0].entangledVector)

print("yay")
gate(CNOT, q[0], q[2])

print(q[0].entangledVector)


