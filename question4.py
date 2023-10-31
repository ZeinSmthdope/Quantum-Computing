from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit


def q4():
    
    q = QuantumRegister(5)
    c = ClassicalRegister(5)
    qcirc = QuantumCircuit(q, c)

    for j in range(5):
      qcirc.h(q[j])

    ''' 
    #from qiskit import Aer, and execute 
    #The commented out code below generates random numbers.
    #Measure the qubits
    qcirc.measure(q, c)

    #Simulate the circuit and get the result
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qcirc, backend, shots=8192)
    result = job.result()

    #Get the counts
    counts = result.get_counts(qcirc)

    #Convert bit strings to integers and normalize the counts
    total_shots = sum(counts.values())
    normalized_counts = {int(bitstring, 2): count / total_shots for bitstring, count in counts.items()} 
    print(normalized_counts)
 
    return qcirc
q4()