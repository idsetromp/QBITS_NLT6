# Documentation for QBITS_NLT6

# Table of contents

- [Documentation for QBITS\_NLT6](#documentation-for-qbits_nlt6)
- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
- [QPU](#qpu)
  - [Classes](#classes)
    - [qbit](#qbit)
      - [Atributes](#atributes)
    - [Gate](#gate)
  - [Functions](#functions)
    - [measure](#measure)
      - [Parameters](#parameters)
    - [gate](#gate-1)
      - [Parameters](#parameters-1)
  - [Built-in Gates](#built-in-gates)
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

#### Atributes

---

**vector:** *np.matrix with the shape $m\times1$*

The vector of the qbit which defines the wave function $|\psi\rangle$ of the qbit.
If left unspecified when making a qbit object, the vector will be
$\begin{bmatrix} 1 \\ 0 \end{bmatrix} \equiv 1|0\rangle + 0|1\rangle = |0\rangle$
which is a qbit orientated in the $+z$ directon ($|0\rangle$). See [Bloch Sphere](#bloch-sphere).

The standard shape of this vector is $2\times1$
($\begin{bmatrix} \alpha \\ \beta \end{bmatrix} \equiv \alpha|0\rangle + \beta|1\rangle$),
but when entangeld with another qbit, the vector of both qbits will be
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

**entangeldQbit:** *qbit*

When two qbit objects get entangled, of the atribute `entangledQbit` of both objects is set to the other object. This is done automatically.

### Gate

## Functions

### measure

``` python
measure(q: qbit, Print=True) -> str
```

Measures the qbit, prints the measurement and returns the measurement.
When a qbit is meaured, its wave function collapses. The function returns either the string `'|0>'` or `'|1>'`.

#### Parameters

---
**q:** *qbit*

The qbit which is measured. After measurement, the wave function of the qbit collapses. This is mathematically noted as follows:

$$|\psi\rangle = \sum_i c_i |\phi_i\rangle \rightarrow |\psi'\rangle = |\phi_i\rangle$$

E.g. a qbit denoted by $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{1}{2}\sqrt3|1\rangle$ can collaps to either $|\psi\rangle = |0\rangle$ or $|\psi\rangle = |1\rangle$. Which one, is determened by chance based on the coefficents squared of the states. In this case, there is a chance of $\left( \frac{1}{2} \right)^2 = 0.25$ that $\psi$ collapses to $|0\rangle$, and a chance of $\left(\frac{1}{2}\sqrt3\right)$ that $\psi$ collapses to $|1\rangle$.

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

When a gate requireing two qbits is applied, `q0` and `q1` get entangled. See below the example of a CNOT being applied to two qbits:

$$$$

## Built-in Gates

# GPU

## Bloch Sphere
