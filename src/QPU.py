from math import *
import cmath #for complex numbres
import random as r
import numpy as np
from itertools import product




class qbit:

    def __init__(self, vector: np.matrix = np.matrix([[1.+0j], [0.+0j]])):
        self.vector = vector

        if self.vector.shape[1] != 1:
            raise Exception(f"Error: qbit vector has shape {self.vector.shape}, expected shape (m, 1).")
        
        if round(sqrt(abs(self.vector.item((0, 0))**2) + abs(self.vector.item(1, 0)**2)), 5) != 1: #* round to prevent floating point errors.
            raise ValueError(f"|Ψ> is {sqrt(self.vector.item((0, 0))**2 + self.vector.item(1, 0)**2)}, expected |Ψ> to equal 1.")


        self.entangledQbits: list[qbit] = None


q: list[qbit] = []

def prep(qbit: qbit):
    q.append(qbit)


def measure(q: qbit, Print=True) -> str: 
    """Measures the qbit, and prints the results if `Print` is True."""

    if q.entangledQbits == None:
        m = r.choices(
            population=["|0>","|1>"],
            weights=[abs(q.vector.item((0, 0))**2), abs(q.vector.item((1,0))**2)] 
        )

        if m == ["|0>"]:
            q.vector = np.matrix([[1], [0]])
            output = "|0>"
        elif m == ["|1>"]:
            q.vector = np.matrix([[0], [1]])
            output = "|1>"
        
    else: 
        entangledStates = [i for i in product(range(2), repeat=int(log(len(q.vector), 2)))]

        entangledStatesStrings = []
        for entangledState in entangledStates:
            stateStr = "|"
            for singleState in entangledState:
                stateStr += str(singleState)
            stateStr += ">"
            entangledStatesStrings.append(stateStr)

        coefficientChances = []
        for row in range(q.vector.shape[0]):
            coefficientChances.append(abs(q.vector.item((row, 0))**2))

        m = r.choices(
            population=entangledStates,
            weights=coefficientChances 
        )
        
        m = m[0]
        print(m)
        print(q.entangledQbits)
        print(len(m))
        for i in range(len(m)):
            if m[i] == 0:
                q.entangledQbits[i].vector = np.matrix([[1], [0]])
            elif m[i] == 1:
                q.entangledQbits[i].vector = np.matrix([[0], [1]])

        for qbit in q.entangledQbits:
            qbit.entangledQbits = None

        stateStr = "|"
        for state in m:
            stateStr += str(state)
        stateStr += ">"
        output = stateStr


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


def sortQbitList(qbitList: list[qbit]) -> list[qbit]:
    sortedList = []
    for qbit in q:
        if qbit in qbitList:
            sortedList.append(qbit)
    
    return sortedList

def addEntangledQbit(q0: qbit, q1: qbit):
    if q0.entangledQbits == None and q1.entangledQbits == None:
        entangledQbits = [q0, q1]
        entangledQbits = sortQbitList(entangledQbits)
    elif q0.entangledQbits == None:
        entangledQbits = q1.entangledQbits
        entangledQbits.append(q0)
        entangledQbits = sortQbitList(entangledQbits)
    elif q1.entangledQbits == None:
        entangledQbits = q0.entangledQbits
        entangledQbits.append(q1)
        entangledQbits = sortQbitList(entangledQbits)
    else:
        entangledQbits = q0.entangledQbits
        entangledQbits += q1.entangledQbits
        entangledQbits = list(dict.fromkeys(entangledQbits)) #* remove duplicates
        entangledQbits = sortQbitList
    
    for qbit in entangledQbits:
        qbit.entangledQbits = entangledQbits


def gate(type: Gate, q0: qbit, q1: qbit = None) -> None:
    """Applies the gate set with `type` to the qbit set with `q0`. 
    When the specified gate requires two qbits, like with the CNOT, 
    `q0` will be used as the control, and `q1` will be the target qbit."""
    if q1 == None:
        if type.amountOfQbits != 1: #? Error cathcing (:
            raise Exception(f"Error: Only one qbit given. Expected {type.amountOfQbits} qbits.")
        

        O = type.matrix
        for i in range(int(log(q0.vector.shape[0],2) - 1)):
            O = np.kron(Identity.matrix, O)
        q0.vector = np.matmul(O, q0.vector)
    else:
        if not type.amountOfQbits > 1:
            raise TypeError(f"{type} takes one qbit, but two were given.")

        addEntangledQbit(q0, q1)

            qbitsVector = np.kron(q0.vector, q1.vector)
        
        else:
            qbitsVector = q0.vector #* = q1.vector

        qbitsVector = np.matmul(type.matrix, qbitsVector)

        q0.vector = qbitsVector
        q1.vector = qbitsVector



