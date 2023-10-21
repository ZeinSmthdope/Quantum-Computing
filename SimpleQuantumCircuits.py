from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

def qc1():

    qr = QuantumRegister(2)
    qcirc = QuantumCircuit(qr)
   
    qcirc.x(0)
    qcirc.cx(0,1)
    qcirc.cx(1,0)
    qcirc.cx(0,1)
 
    return qcirc
qc1()




def qc2():

    qr = QuantumRegister(2, 'qreg')
    qcirc = QuantumCircuit(qr)
    
    qcirc.h(0)
    qcirc.h(1)
    qcirc.cx(0,1)
    qcirc.h(0)
    qcirc.h(1)

    return qcirc
qc2()




def qc3():

    qr = QuantumRegister(1, 'qreg')
    qcirc = QuantumCircuit(qr)
    
    qcirc.h(0)
    qcirc.x(0)
    qcirc.h(0)

    return qcirc
qc3()




def qc4():

    qr = QuantumRegister(1, 'qreg')
    qcirc = QuantumCircuit(qr)
    
    qcirc.h(0)
    qcirc.z(0)
    qcirc.h(0)

    return qcirc
qc4()





def qc5():

    qr = QuantumRegister(1, 'qreg')
    qcirc = QuantumCircuit(qr)
    
    qcirc.h(0)
    qcirc.t(0)
    qcirc.h(0)
   
    return qcirc
qc5()




def qc6():

    qr = QuantumRegister(1, 'qreg')
    qcirc = QuantumCircuit(qr)
    
    qcirc.h(0)
    qcirc.x(0)
    qcirc.y(0)
    qcirc.x(0)
    qcirc.y(0)

    return qcirc
qc6()