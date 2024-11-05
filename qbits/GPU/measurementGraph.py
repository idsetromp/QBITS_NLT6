import matplotlib.pyplot as plt
import numpy as np
import cmath

def showGraph(measurements: list[str]):
    x = list(set(measurements))
    x = sorted(x)

    h=[]
    for element in x:
        h.append(measurements.count(element))

    ax = plt.subplot()


    ax.bar(x, h)

    plt.show()
