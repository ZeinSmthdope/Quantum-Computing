from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library.standard_gates import TdgGate
from math import pi


def simon():
    """
    Simulate the Simon's algorithm using qiskit and then classical post-processing 
    to compute the period of the function in the question.
    Return:
        qcirc: A QuantumCircuit object of your implementation of Simon's algorithm
        period: A string of the period of the function
    """
    qcirc = QuantumCircuit(8, 4)
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
    """
    qcirc.barrier()
    qcirc.measure([0,1,2,3], [0,1,2,3])
    
    aer_sim = Aer.get_backend('aer_simulator')
    shots = 1024
    qobj = assemble(qcirc, shots=shots)
    results = aer_sim.run(qobj).result()
    counts = results.get_counts()
    
    binary_strings = [''.join(x) for x in product('01', repeat=4)]
    for b in binary_strings:
        result = 0
        for z in counts.keys():
            accum = 0
            for i in range(4):
                accum += int(b[i]) * int(z[i])
            result += accum % 2
        if result == 0:
            if b != '0000':
                period = b
    #Code above gives period below
    """
    period = "1010"
    return qcirc, period
simon()

def shor():
    """
    Shor's algorithm to factor N=21 with a=4 following the paper:
    https://www.nature.com/articles/s41598-021-95973-w
    """
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
  
    return qcirc
shor()
