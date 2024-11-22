from src.QPU import *
from src import GPU
from itertools import product

prep(qbit())
prep(qbit())
gate(Hadamard, q[0])
gate(CNOT, q[0], q[1])

print("yay")
gate(Pauli_Z, q[0])
GPU.drawBlochSphere([q[0]])

measurements = [measure(q[0])]

GPU.drawGraph(measurements)



