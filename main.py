from src.QPU import *
from src import GPU

a = qbit()
b = qbit()

gate(Ry(120, 'degree'), a)
gate(Hadamard, b)

gate(CNOT, a, b)
print(a.vector)
gate(CNOT, a, b)
print(b.vector)




