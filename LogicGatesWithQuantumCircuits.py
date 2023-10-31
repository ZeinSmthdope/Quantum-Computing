from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator

def quantum_and():
    
    qc = QuantumCircuit(3,1)
    qc.ccx(1,2,0)
    qc.measure(0,0)

    return qc
quantum_and    



def quantum_or():
    
    qc = QuantumCircuit(3,1)
    qc.x(1)
    qc.x(2)
    qc.cx(2,0)
    qc.cx(1,0)
    qc.ccx(2,1,0)
    qc.measure(0,0)

    return qc
quantum_or()



def quantum_xor():

    qc = QuantumCircuit(3,1)
    qc.cx(2,0)
    qc.cx(1,0)
    qc.measure(0,0)

    return qc
quantum_xor()    
