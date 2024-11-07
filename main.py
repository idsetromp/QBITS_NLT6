import GPU.blochSphere
from QPU import *
import GPU.measurementGraph

m = []
for shot in range(100):
    A = qbit()
    B = qbit()

    #gate(Rz(115, 'degree'), A)
    gate(Hadamard, A)
    gate(Hadamard, B)
    gate(CNOT, A, B)

    m.append(measure(A, False))

GPU.measurementGraph.showGraph(m)

C = qbit()
D = qbit()


gate(Rx(30, 'degree'), D)
gate(Rx(30, 'degree'), C)
gate(Rz(60, 'degree'), C)
GPU.blochSphere.drawBlochSphere([C, D])




