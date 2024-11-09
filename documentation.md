# Documentation for QBITS_NLT6

# Table of contents

- [Documentation for QBITS\_NLT6](#documentation-for-qbits_nlt6)
- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
- [QPU](#qpu)
  - [Classes](#classes)
    - [qbit](#qbit)
      - [Attributes](#attributes)
    - [Gate](#gate)
  - [Functions](#functions)
    - [measure](#measure)
      - [Parameters](#parameters)
    - [gate](#gate-1)
      - [Parameters](#parameters-1)
  - [Built-in Gates](#built-in-gates)
    - [Hadamard](#hadamard)
    - [Pauli\_X](#pauli_x)
    - [Pauli\_Y](#pauli_y)
    - [Pauli\_Z](#pauli_z)
    - [Identity](#identity)
    - [S\_gate](#s_gate)
    - [S\_dagger](#s_dagger)
    - [T\_gate](#t_gate)
    - [T\_dagger](#t_dagger)
    - [CNOT](#cnot)
    - [C](#c)
- [GPU](#gpu)
  - [Bloch Sphere](#bloch-sphere)

# Introduction

The library is made up of two important components: the QPU and de GPU.
The QPU (Quantum Processing Unit) is used for all qbit-related stuff. E.g. quantum gates and measuring.
The GPU (Graphical Processing Unit) is used for all, you guessed it, graphical stuff.
Namely, displaying Bloch spheres and graphing measurement results.

# QPU

## Classes

### qbit

``` python
class qbit
    def __init__(self, vector: np.matrix = np.matrix([[1.+0j], [0.+0j]])):
        ...
```

The qbit class. Making an object of this class (`myQbit = qbit()`) creates a qbit.

#### Attributes

---

**vector:** *np.matrix with the shape $m\times1$*

The vector of the qbit which defines the wave function $|\psi\rangle$ of the qbit.
If left unspecified when making a qbit object, the vector will be
$\begin{bmatrix} 1 \\ 0 \end{bmatrix} \equiv 1|0\rangle + 0|1\rangle = |0\rangle$
which is a qbit orientated in the $+z$ direction ($|0\rangle$). See [Bloch Sphere](#bloch-sphere).

The standard shape of this vector is $2\times1$
($\begin{bmatrix} \alpha \\ \beta \end{bmatrix} \equiv \alpha|0\rangle + \beta|1\rangle$),
but when entangled with another qbit, the vector of both qbits will be
$4\times1 \ (\begin{bmatrix} \alpha \\ \beta \\ \gamma \\ \delta \end{bmatrix} \equiv \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle)$.

Do note that
$\Vert\psi\Vert \stackrel{\text{def}}{=} 1$.
Therefore, $\sqrt{\alpha^2+\beta^2} = 1$.
When using de built-in quantum gates this will always be true.
However, when the user manually sets the qbit's vector,
the length of the vector must equal to $1$.
This can be done as follows:
`myQbit.vector = np.matrix([[a], [b]])`, where `myQbit` is an object of `qbit`, and `a` and `b` are chosen floats which may be complex numbers. Note that the imaginary unit $i$ is denoted in python by `j` placed directly after any number (e.g. `.5 + 1.0j` = $0.5+i$).

---

**entangledQbit:** *qbit*

When two qbit objects get entangled, of the attribute `entangledQbit` of both objects is set to the other object. This is done automatically.

### Gate

## Functions

### measure

``` python
measure(q: qbit, Print=True) -> str
```

Measures the qbit, prints the measurement and returns the measurement.
When a qbit is measured, its wave function collapses. The function returns either the string `'|0>'` or `'|1>'`.

#### Parameters

---
**q:** *qbit*

The qbit which is measured. After measurement, the wave function of the qbit collapses. This is mathematically noted as follows:

$$|\psi\rangle = \sum_i c_i |\phi_i\rangle \rightarrow |\psi'\rangle = |\phi_i\rangle$$

E.g. a qbit denoted by $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{1}{2}\sqrt3|1\rangle$ can collapse to either $|\psi\rangle = |0\rangle$ or $|\psi\rangle = |1\rangle$. Which one, is determined by chance based on the coefficients squared of the states. In this case, there is a chance of $\left( \frac{1}{2} \right)^2 = 0.25$ that $\psi$ collapses to $|0\rangle$, and a chance of $\left(\frac{1}{2}\sqrt3\right)$ that $\psi$ collapses to $|1\rangle$.

When `q` is set to an entangled qbit, the wave function of both qbits collapses to either $|0\rangle$ or $|1\rangle$. Only the measurement of the initial qbit which `q` is set to, is returned by the function.

---

**Print:** *boolean, standard value is `True`*

When true, the function prints the measurement to the terminal.

---
---

### gate

``` python
gate(type: Gate, q0: qbit, q1: qbit = None) -> None
```

Applies a gate to qbit(s).

#### Parameters

---
**type:** *Gate*

Requires an object of the `Gate` class (see [Gate](#gate)). This gate will be applied to the qbit. This is done by multiplying the matrix of the gate with the qbit's vector. See the example below of a Hadamard gate applied to a qbit orientated in the $|0\rangle$ direction:

$$H\left(|\psi\rangle\right) = H\left(|0\rangle\right) \equiv \begin{bmatrix} \frac{1}{\sqrt2} & \frac{1}{\sqrt2} \\ \frac{1}{\sqrt2} & -\frac{1}{\sqrt2} \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt2} \\ \frac{1}{\sqrt2} \end{bmatrix} \equiv \frac{1}{\sqrt2}|0\rangle + \frac{1}{\sqrt2}|1\rangle$$

---
**q0:** *qbit*

The qbit the gate will be applied to.

---
**q1:** *qbit, standard value is `None`*

If `type` is set to a gate which requires two qbits, like CNOT, `q0` will be the control and `q1` the target qbit. If, however, the gate `type` is set to requires just one qbit, `q1` is must be left empty.

When a gate requiring two qbits is applied, `q0` and `q1` get entangled. See below the example of a CNOT being applied to two qbits:

$$\begin{align*}
    &|\psi\rangle_{A} = \alpha|0\rangle + \beta|1\rangle \\
    &|\phi\rangle_{B} = \gamma|0\rangle + \delta|1\rangle \\
    & \\
    &\begin{align*}
        |\psi\rangle_{AB} & = |\psi\rangle_A \otimes |\phi\rangle_B \\
        & = \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle \\
    \end{align*} \\
    & \\
    &\begin{align*}
        CNOT(|\psi\rangle_{AB}) & = CNOT(\alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle) \\
        & \equiv \underbrace{\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}}_{CNOT} \cdot \begin{bmatrix}\alpha\gamma \\ \alpha\delta \\ \beta\gamma \\ \beta\delta\end{bmatrix} \\
        & = \begin{bmatrix}\alpha\gamma \\ \alpha\delta \\ \beta\delta \\ \beta\gamma \end{bmatrix} \\
        & \equiv \frac{1}{4}\sqrt3|00\rangle + \frac{3}{4}|01\rangle + \frac{1}{4}\sqrt3|10\rangle + \frac{1}{4}|11\rangle
        \end{align*} \\
\end{align*}$$

## Built-in Gates

Most built-in gates are objects of the `Gate` class. To apply a built-in gate to a `qbit` object, the `gate` function can be used (see [gate](#gate-1)). Every gate has a matrix, and a certain amount of qbits the gate can be applied to (e.g. Hadamard can be applied to one qbit, CNOT to two). A few gates are 'variable' gates, like Rx. These gates are built in as function.

### Hadamard
*The Hadamard gate is a single-qubit operation that maps the basis state $|0\rangle$ to $\frac{|0\rangle + |1\rangle}{\sqrt2}$ and $|1\rangle$ to $\frac{|0\rangle - |1\rangle}{\sqrt2}$​, thus creating an equal superposition of the two basis states.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:**
$\begin{bmatrix} \frac{1}{\sqrt2} & \frac{1}{\sqrt2}\\
\frac{1}{\sqrt2} & -\frac{1}{\sqrt2} \end{bmatrix}$

**amountOfQbits:** 1

### Pauli_X

*The Pauli-X gate is a single-qubit rotation through $\pi$ radians around the x-axis.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}0&1\\1&0\end{bmatrix}$

**amountOfQbits:** 1

### Pauli_Y

*The Pauli-Y gate is a single-qubit rotation through $\pi$ radians around the y-axis.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}0&-i\\i&0\end{bmatrix}$

**amountOfQbits:** 1

### Pauli_Z

*The Pauli-Y gate is a single-qubit rotation through $\pi$ radians around the y-axis.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$

**amountOfQbits:** 1

### Identity

*The Identity gate is a single-qubit operation that leaves the basis states $|0\rangle$ and $|1\rangle$ unchanged.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}1&0\\0&1\end{bmatrix}$

**amountOfQbits:** 1

### S_gate

*The S gate is also known as the phase gate or the Z90 gate, because it represents a 90-degree rotation around the z-axis. The S gate is related to the T gate by the relationship  $S=T^2$.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}1&0\\0&i\end{bmatrix}$

**amountOfQbits:** 1

### S_dagger

*The $S^\dagger$ gate is the conjugate transpose of the S gate.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}1&0\\0&-i\end{bmatrix}$

**amountOfQbits:** 1

### T_gate

*The T gate is related to the S gate by the relationship  $S=T^2$.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}1&0\\0&e^{\frac{i\pi}{4}}\end{bmatrix}$

**amountOfQbits:** 1

### T_dagger

*The $T^\dagger$ gate is the conjugate transpose of the T gate.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}1&0\\0&e^{-\frac{i\pi}{4}}\end{bmatrix}$

**amountOfQbits:** 1

### CNOT

*The CNOT gate is two-qubit operation, where the first qubit is usually referred to as the control qubit and the second qubit as the target qubit. Expressed in basis states, the CNOT gate:*
- *leaves the control qubit unchanged and performs a Pauli-X gate on the target qubit when the control qubit is in state $|1\rangle$;*
- *leaves the target qubit unchanged when the control qubit is in state $|0\rangle$.*

Voorhoede, D. (n.d.). Quantum inspire. Quantum Inspire. https://www.quantum-inspire.com/kbase/

**matrix:** $\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}$

**amountOfQbits:** 2

### CZ

*The Controlled-Z (CZ) gate is a two-qubit gate used in quantum computing. It operates on a pair of qubits, with one qubit acting as the control and the other as the target. In layman's terms, the CZ gate applies a phase flip (change in the relative phase) to the target qubit only when the control qubit is in the state $|1\rangle$. If the control qubit is in the state $|0\rangle$, the CZ gate does not affect the target qubit.*

Quantum Computing | ShareTechnote. (n.d.). https://www.sharetechnote.com/html/QC/QuantumComputing_Gate_cZ.html

**matrix:** $\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{bmatrix}$

**amountOfQbits:** 2

# GPU

## Bloch Sphere
