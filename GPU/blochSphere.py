import matplotlib.pyplot as plt
import numpy as np
import QPU
import cmath

def configurePlot():
    resolution = 100

    ax = plt.figure().add_subplot(projection='3d')

# Hide grid lines
    ax.grid(b=0)
    ax.axis('off')

    return ax, resolution


def gridSphere(ax, resolution):

# xy circle
    for z in range(-100, 100, 40):
        theta = np.linspace(-2*np.pi, 2*np.pi, resolution)
        r = np.sqrt(1-(z/100)**2)
        y = r * np.sin(theta)
        x = r * np.cos(theta)

        Z = np.linspace(z/100, z/100, resolution)

        ax.plot3D(x, y, Z, ':', color='lightgrey')

#xz circle
    for y in range(-100, 100, 40):
        theta = np.linspace(-2*np.pi, 2*np.pi, resolution)
        r = np.sqrt(1-(y/100)**2)
        z = r * np.sin(theta)
        x = r * np.cos(theta)

        Y = np.linspace(y/100, y/100, resolution)

        ax.plot3D(x, Y, z, ':', color='lightgrey')

#yz circle
    for x in range(-100, 100,40):
        theta = np.linspace(-2*np.pi, 2*np.pi, resolution)
        r = np.sqrt(1-(x/100)**2)
        y = r * np.sin(theta)
        z = r * np.cos(theta)

        X = np.linspace(x/100, x/100, resolution)

        ax.plot3D(X, y, z, ':', color='lightgrey')


def lineSphere(ax, resolution):

# xy circle
    theta = np.linspace(-2*np.pi, 2*np.pi, resolution)
    r = 1
    y = r * np.sin(theta)
    x = r * np.cos(theta)

    z = np.linspace(0, 0, resolution)

    ax.plot3D(x, y, z, ':', color='lightgrey')

#xz circle
    theta = np.linspace(-2*np.pi, 2*np.pi, resolution)
    r = 1
    z = r * np.sin(theta)
    x = r * np.cos(theta)

    y = np.linspace(0, 0, resolution)

    ax.plot3D(x, y, z, ':', color='lightgrey')

#yz circle
    theta = np.linspace(-2*np.pi, 2*np.pi, resolution)
    r = 1
    y = r * np.sin(theta)
    z = r * np.cos(theta)

    x = np.linspace(0, 0, resolution)

    ax.plot3D(x, y, z, ':', color='lightgrey')


def axes(ax):
#x axis
    x = np.linspace(-1, 1, 2)
    y = np.linspace(0, 0, 2)
    z = np.linspace(0, 0, 2)
    ax.plot3D(x, y, z, color='grey', linewidth=1)

    ax.plot3D(1.3, 0, 0, marker='$+x$', markersize=15, color='#000000')
    ax.plot3D(-1.3, 0, 0, marker='$-x$', markersize=15, color='#000000')
    ax.plot3D(1, 1, 1, color='#FFFFFF', label='+x: |+\u27E9')
    ax.plot3D(1, 1, 1, color='#FFFFFF', label='-x: |-\u27E9')

#y axis
    y = np.linspace(-1, 1, 2)
    x = np.linspace(0, 0, 2)
    z = np.linspace(0, 0, 2)
    ax.plot3D(x, y, z, color='grey', linewidth=1)

    ax.plot3D(0, 1.3, 0, marker='$+y$', markersize=15, color='#000000')
    ax.plot3D(0, -1.3, 0, marker='$-y$', markersize=15, color='#000000')
    ax.plot3D(1, 1, 1, color='#FFFFFF', label='+y: |+i\u27E9')
    ax.plot3D(1, 1, 1, color='#FFFFFF', label='-y: |-i\u27E9')

#z axis
    z = np.linspace(-1, 1, 2)
    y = np.linspace(0, 0, 2)
    x = np.linspace(0, 0, 2)
    ax.plot3D(x, y, z, color='grey', linewidth=1)

    ax.plot3D(0, 0, 1.3, marker='$+z$', markersize=15, color='#000000')
    ax.plot3D(0, 0, -1.3, marker='$-z$', markersize=15, color='#000000')
    ax.plot3D(1, 1, 1, color='#FFFFFF', label='+z: |0\u27E9')
    ax.plot3D(1, 1, 1, color='#FFFFFF', label='-z: |1\u27E9')


def drawBlochSphere(qbits: list[QPU.qbit], sphereType='grid'):
    """Function to draw Bloch sphere(s) of qbit(s). \n
    The parameter `qbits` requires a list of the qbits to render the bloch sphere of.\n
    `sphereType` sets whether the\n
    ![grid example](/assets/grid.png)"""

    for qbit in qbits:
    #? ========================================
    #$      Configure plot, axes, etc.         
    #? ========================================

        ax, resolution = configurePlot()

        if sphereType == 'grid':
            gridSphere(ax, resolution)
        elif sphereType == 'axis-lines':
            lineSphere(ax, resolution)
        else:
            raise ValueError(f"sphereType is {sphereType}, expected \'grid\' or \'axis-lines\'.")
    
        axes(ax)


    #? ========================================
    #$         Calculate and plot |Ψ>          
    #? ========================================


    
        alpha = qbit.matrix.item((0, 0)) #* α|0> 
        beta = qbit.matrix.item((1, 0)) #* β|1> π φ θ

        #* |Ψ> = α|0> + β|1>
        #* |Ψ> = cos(θ/2)|0> + exp(iφ)*sin(θ/2)|1>
        #* ---------------------------------------
        #* α = cos(θ/2)
        #* θ = 2*arccos(α)
        #* ---------------------------------------
        #* β = exp(iφ)*sin(θ/2)
        #* φ = ln(β / sin(θ/2))

        theta = np.real(2*np.arccos(alpha))
 
        try:
            phi = np.imag(np.log(beta/np.sin(theta/2)))
        except ZeroDivisionError:
            phi = 0

        #* r, θ en φ zijn de bolcoördinaten van |Ψ> op de bloch sphere. Aangezien |Ψ> = 1, geldt r = 1.

        r = 1

        psix = r * np.sin(theta) * np.cos(phi)
        psiy = r * np.sin(theta) * np.sin(phi)
        psiz = r * np.cos(theta)

        x = np.linspace(0, psix, 2)
        y = np.linspace(0, psiy, 2)
        z = np.linspace(0, psiz, 2)

        ax.plot3D(x, y, z, color='#FF00FF', linewidth=2)
        ax.plot3D(psix, psiy, psiz, 'o', color='#FF00FF', label='|Ψ\u27E9')

        plt.legend(
            loc="upper left"
 #           reverse=True, draggable=True, shadow=True #! werkt niet >:(
                   
        )

    #? ========================================
    #$               Execute plot              
    #? ========================================
        
    plt.show()


