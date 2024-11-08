from src.QPU import *
from src import GPU

a = qbit()

gate(Hadamard, a)
print(a.vector)

m = []
for shot in range(100):
    A = qbit()
    B = qbit()

    #gate(Rz(115, 'degree'), A)
    gate(Hadamard, A)
    gate(Hadamard, B)
    gate(CNOT, A, B)

    m.append(measure(A, False))

GPU.drawGraph(m)

C = qbit()
D = qbit()


gate(Rx(30, 'degree'), D)
gate(Rx(30, 'degree'), C)
gate(Rz(60, 'degree'), C)
GPU.drawBlochSphere([C, D])




