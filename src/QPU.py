from math import *
import cmath #for complex numbres
import random as r
import numpy as np




class qbit:

    def __init__(self, vector: np.matrix = np.matrix([[1.+0j], [0.+0j]])):
        self.vector = vector

        if self.vector.shape[1] != 1:
            raise Exception(f"Error: qbit vector has shape {self.vector.shape}, expected shape (m, 1).")
        
        if round(sqrt(abs(self.vector.item((0, 0))**2) + abs(self.vector.item(1, 0)**2)), 5) != 1: #* round to prevent floating point errors.
            raise ValueError(f"|Ψ> is {sqrt(self.vector.item((0, 0))**2 + self.vector.item(1, 0)**2)}, expected |Ψ> to equal 1.")


        self.entangledQbit = None


def measure(q: qbit, Print=True) -> str: 
    """Measures the qbit, and prints the results if `Print` is True."""

    if q.entangledQbit == None:
        m = r.choices(
            population=["|0>","|1>"],
            weights=[abs(q.vector.item((0, 0))**2), abs(q.vector.item((1,0))**2)] #! KLOPT HET DAT DIT DE ABS MOET ZIJN?
        )

        if m == ["|0>"]:
            q.vector = np.matrix([[1], [0]])
            output = "|0>"
        elif m == ["|1>"]:
            q.vector = np.matrix([[0], [1]])
            output = "|1>"
        

    else: 
        m = r.choices(
            population=["|00>", "|01>", "|10>", "|11>"],
            weights=[abs(q.vector.item((0, 0))), 
                     abs(q.vector.item((1, 0))),
                     abs(q.vector.item((2, 0))),
                     abs(q.vector.item((3, 0)))] #! KLOPT HET DAT DIT DE ABS MOET ZIJN?
        )
        if m == ["|00>"]:
            q.vector = np.matrix([[1], [0]])
            q.entangledQbit.vector = np.matrix([[1], [0]])
            output = "|0>"
        elif m == ["|01>"]:
            q.vector = np.matrix([[1], [0]])
            q.entangledQbit.vector = np.matrix([[0], [1]])
            output = "|0>"
        elif m == ["|10>"]:
            q.vector = np.matrix([[0], [1]])
            q.entangledQbit.vector = np.matrix([[1], [0]])
            output = "|1>"
        elif m == ["|11>"]:
            q.vector = np.matrix([[0], [1]])
            q.entangledQbit.vector = np.matrix([[0], [1]])
            output = "|1>"

        q.entangledQbit.entangledQbit = None
        q.entangledQbit = None


    if Print:
        if q.vector.item((0,0)) == 1:
            print("|Ψ> = |0>")
        elif q.vector.item((1,0)) == 1:
            print("|Ψ> = |1>")

    return output

#?=============================================
#$                  Gates                      
#?=============================================


class Gate:

    def __init__(self, matrix: np.matrix, amountOfQbits: int):
        self.matrix = matrix
        self.amountOfQbits = amountOfQbits 

#? Gates
Hadamard = Gate(
    np.matrix([[1/sqrt(2), 1/sqrt(2)],
               [1/sqrt(2), -1/sqrt(2)]]),              
    1
)

Pauli_X = Gate(
    np.matrix([[0, 1],
               [1, 0]]),
    1
)

Pauli_Y = Gate(
    np.matrix([[0, 0-1j],
               [0+1j, 0]]),
    1
)

Pauli_Z = Gate(
    np.matrix([[1, 0],
               [0, -1]]),
    1
)

Identity = Gate(
    np.matrix([[1, 0],
               [0, 1]]),
    1
)

S_gate = Gate(
    np.matrix([[1, 0],
               [0, 1j]]),
    1
)

S_dagger = Gate(
    np.matrix([[1, 0],
               [0, -1j]]),
    1
)

T_gate = Gate(
    np.matrix([[1, 0],
               [0, np.exp((pi*1j)/4)]]),
    1
)

T_dagger = Gate(
    np.matrix([[1, 0],
               [0, np.exp(-(pi*1j)/4)]]),
    1
)

CNOT = Gate(
    np.matrix([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 1, 0]]),
    2
)

CZ = Gate(
    np.matrix([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]]),
    2
)

SWAP = Gate(
    np.matrix([[1, 0, 0, 0],
               [0, 0, 1, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 1]]),
    2
)

def Rx(theta: float, angleUnit='radian') -> Gate:
    """Rotates the qbit theta radians around the x axis, 
    unless `angleUnit` is set to 'degree', 
    in which case theta is in degrees."""
    if angleUnit == 'degree':
        theta = theta*pi/180
    elif angleUnit != 'radian':
        raise ValueError(f"angleUnit is \'{angleUnit}\', expected angleUnit to be \'radian\' or \'degree\'.")
    
    return Gate(
        np.matrix([[cos(theta/2), -1j*sin(theta/2)],
                   [-1j*sin(theta/2), cos(theta/2)]]),
        1
    )

def Ry(theta: float, angleUnit='radian') -> Gate:
    """Rotates the qbit theta radians around the x axis, 
    unless `angleUnit` is set to 'degree', 
    in which case theta is in degrees."""
    if angleUnit == 'degree':
        theta = theta*pi/180
    elif angleUnit != 'radian':
        raise ValueError(f"angleUnit is \'{angleUnit}\', expected angleUnit to be \'radian\' or \'degree\'.")
    
    return Gate(
        np.matrix([[cos(theta/2), -sin(theta/2)],
                   [sin(theta/2), cos(theta/2)]]),
        1
    )

def Rz(theta: float, angleUnit='radian') -> Gate:
    """Rotates the qbit theta radians around the z axis, 
    unless `angleUnit` is set to 'degree', 
    in which case theta is in degrees."""
    if angleUnit == 'degree':
        theta = theta*pi/180
    elif angleUnit != 'radian':
        raise ValueError(f"angleUnit is \'{angleUnit}\', expected angleUnit to be \'radian\' or \'degree\'.")
    
    return Gate(
        np.matrix([[np.exp(-1j*theta/2), 0],
                   [0, np.exp(1j*theta/2)]]),
        1
    )

def CR(theta: float, angleUnit='radian') -> Gate:
    if angleUnit == 'degree':
        theta = theta*pi/180
    elif angleUnit != 'radian':
        raise ValueError(f"angleUnit is \'{angleUnit}\', expected angleUnit to be \'radian\' or \'degree\'.")
    
    return Gate(
        np.matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, np.exp(1j*theta)]]),
        2
    )


def gate(type: Gate, q0: qbit, q1: qbit = None) -> None:
    """Applies the gate set with `type` to the qbit set with `q0`. 
    When the specified gate requires two qbits, like with the CNOT, 
    `q0` will be used as the control, and `q1` will be the target qbit."""
    if q1 == None:
        if type.amountOfQbits != 1: #? Error cathcing (:
            raise Exception(f"Error: Only one qbit given. Expected {type.amountOfQbits} qbits.")
        

        O = type.matrix
        for i in range(int(q0.vector.shape[0]/2 - 1)):
            O = np.kron(Identity.matrix, O)
        q0.vector = np.matmul(O, q0.vector)
    else:
        if not type.amountOfQbits > 1:
            raise TypeError(f"{type} takes one qbit, but two were given.")

        if q1.entangledQbit == None:
            q0.entangledQbit = q1
            q1.entangledQbit = q0

            qbitsVector = np.kron(q0.vector, q1.vector)
        
        else:
            qbitsVector = q0.vector #* = q1.vector

        qbitsVector = np.matmul(type.matrix, qbitsVector)

        q0.vector = qbitsVector
        q1.vector = qbitsVector



