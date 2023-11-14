from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

def grover(n: int):
    '''
    This function output Grover's algorithm circuit for a specific target. 
    Implement the circuit for applying
        Rotation phase + Inversion around the mean
    n times, where n is a nonnegative integer.
    Args: 
        n: integer of the number of times to apply (rotation + inversion)
    Return:
        qcirc: A QuantumCircuit object of your implementation of Grover's algorithm
    '''
    qcirc.h([0, 1, 2])
    qcirc.barrier()
    
    for _ in range(n):
        qcirc.x(0)
        qcirc.h(2)
        qcirc.mcx([0, 1], 2)
        qcirc.x(0)
        qcirc.h(2)
        qcirc.barrier()
        
        qcirc.h([0, 1, 2])
        qcirc.x([0, 1, 2])
        qcirc.barrier()
    
        qcirc.h(2)
        qcirc.mcx([0, 1], 2)
        qcirc.h(2)
        qcirc.barrier()
        
        qcirc.x([0, 1, 2])
        qcirc.h([0, 1, 2])
        qcirc.barrier()
        qcirc.barrier()
    return qcirc
grover(1) 
grover(2) 
