# This script is an example.
# Feel free to add to and delete from this script as you like,
# in order to create your own script.

# Importing libararies,
# namely the Quantum Processing Unit (QPU),
# and the Graphical Processing Unit (GPU).
from src.QPU import *
from src import GPU

# This script creates two qbits,
# applies a couple of gates to them,
# and finally displays both qbits on the bloch sphere.

# Creating the two qbits.
q0 = qbit()
q1 = qbit()

# Applying the gates.
gate(Rx(45, angleUnit='degree'), q0) # Here, we want to rotate q0 45°.
				     # Therefore, `angleUnit` is set to 'degree'.
				     # The standard angleUnit is radians.
gate(T_dagger, q1)

gate(CNOT, q0, q1)

gate(Hadamard, q0)

# Finally, the two qbits are displayed on the bloch sphere.
GPU.drawBlochSphere([q0, q1])

# See documentation.md for more functionallity!


