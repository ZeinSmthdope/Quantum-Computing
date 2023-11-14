from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library.standard_gates import TdgGate
from math import pi


def simon():
    """
    Simulate the Simon's algorithm using qiskit and then classical post-processing 
    to compute the period of the function in the question.
    Return the period as a string. i.e., if the period is 1111, you would return "1111"
    Args: 
        None
    Return:
        qcirc: A QuantumCircuit object of your implementation of Simon's algorithm
        period: A string of the period of the function (This can be hard coded)
    """
    qcirc = None
    period = ""
    
    ############################################################################
    # Student code begin
    ############################################################################
    
    qcirc = QuantumCircuit(8, 4)
    period = "1010"
    
    qcirc.h([0,1,2,3])
    qcirc.barrier()
    qcirc.cx(0, 4)
    qcirc.cx(1, 5)
    qcirc.cx(2, 6)
    qcirc.cx(3, 7)
    qcirc.cx(1, 5)
    qcirc.cx(1, 7)
    qcirc.barrier()
    qcirc.h([0,1,2,3])
    
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc, period
simon()



def qft_1_qubit():
    """
    Create a 1-qubit Quantum Fourier Transform circuit.
    Args:
        None
    Return:
        A QuantumCircuit object
    """
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################
    qcirc = QuantumCircuit(1)
    qcirc.h(0)
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc
qft_1_qubit()


def qft_2_qubit():
    """
    Create a 2-qubit Quantum Fourier Transform circuit.
    Args:
        None
    Return:
        A QuantumCircuit object
    """
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################
    qcirc = QuantumCircuit(2)
    qcirc.h(0)
    qcirc.cp(pi/2, 0, 1)
    qcirc.h(1)
    qcirc.swap(0,1)
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc
qft_2_qubit()


def qft_3_qubit():
    """
    Create a 3-qubit Quantum Fourier Transform circuit.
    Args:
        None
    Return:
        A QuantumCircuit object
    """
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################
    qcirc = QuantumCircuit(3)
    qcirc.h(0)
    qcirc.cp(pi/2, 0, 1)
    qcirc.cp(pi/4, 0, 2)
    qcirc.h(1)
    qcirc.cp(pi/2, 1, 2)
    qcirc.h(2)
    qcirc.swap(0,2)
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc
qft_3_qubit()


def iqft_3_qubit():
    """
    Create a 3-qubit inverse Quantum Fourier Transform circuit.
    Args:
        None
    Return:
        A QuantumCircuit object
    """
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################
    qcirc = QuantumCircuit(3)
    qcirc.swap(0,2)
    qcirc.h(2)
    qcirc.cp(-pi/2, 1, 2)
    qcirc.h(1)
    qcirc.cp(-pi/4, 0, 2)
    qcirc.cp(-pi/2, 0, 1)
    qcirc.h(0)
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc
iqft_3_qubit()    


def shor():
    """
    Implement a simplified Shor's algorithm to factor N=21 with a=4 following the paper:
    https://www.nature.com/articles/s41598-021-95973-w
    """
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################
    qcirc = QuantumCircuit(5)
    qcirc.h([0,1,2])
    qcirc.barrier()

    qcirc.cx(2,4)
    qcirc.barrier()

    qcirc.cx(1,4)
    qcirc.cx(4,3)
    qcirc.ccx(1,3,4)
    qcirc.cx(4,3)
    qcirc.barrier()

    qcirc.x(4)
    qcirc.ccx(0,4,3)
    qcirc.x(4)
    qcirc.cx(4,3)
    qcirc.ccx(0,3,4)
    qcirc.cx(4,3)
    qcirc.barrier()

    qcirc.h(2)
    qcirc.csdg(1,2)
    ctdggate = TdgGate().control(1)
    qcirc.append(ctdggate, [0, 2])
    qcirc.h(1)
    qcirc.csdg(0,1)
    qcirc.h(0)
    qcirc.barrier()
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc
shor()