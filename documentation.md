# Documentation for QBITS_NLT6

## Table of contents

- [Documentation for QBITS\_NLT6](#documentation-for-qbits_nlt6)
  - [Table of contents](#table-of-contents)
- [Introduction](#introduction)
- [QPU](#qpu)
  - [Classes](#classes)
    - [qbit](#qbit)
      - [Parameters](#parameters)

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
```
The qbit class. Making an object of this class (`myQbit = qbit()`) creates a qbit.

#### Parameters

**vector:** *np.matrix with the shape 2x1*

