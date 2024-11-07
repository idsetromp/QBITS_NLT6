#This script is an example.
#Feel free to add to and delete from this script as you like,
#in order to create your own script.

# Importing libararies,
# namely the Quantum Processing Unit (QPU),
# and the Graphical Processing Unit (GPU).
from QPU import *
import GPU.blochSphere
import GPU.measurementGraph

#This is script does 100 shots of a series of quantum gates with two qbit.
#At the end of each shot, one of the qbits is measured.
#The measured value is saved for later use.

# First, a container is created to save all the measured values.
measurements = []

# Now, the series of quantum gates will be executed 100 times.
for shot in range(100):
	
	# Two qbits are created.
	q0 = qbit()
	q1 = qbit()
	
	# Some gates are applied.
	gate(Pauli_X, q1)
	gate(Hadamard, q0)
	gate(Hadamard, q1)
	
	gate(CNOT, q0, q1)
	
	gate(Hadamard, q0)

	# After all of the gates have been applied, qbit q0 is measured.
	# Since this script is repeated 100 times,
	#  and we don't want every single measurement to be printed,
	# `Print` is set to `False`.
	measurements.append(measure(q0, Print=False))


# Finally, the measured values are graphed.
GPU.measurementGraph.showGraph(measurements) 

# See documentation.md for more functionallities!

