# Quantum-Computing
# SimpleQuantumCircuits

- qc1:
    When the 1st Cnot is applied, nothing happens because the control qubit qreg0 is at 0 (|01⟩) after the X gate has been initially applied.
    |00⟩X = |01⟩
    When the 2nd is applied, the state changes to |11⟩ because here the control qreg1 is at 1.
    Finally when the last Cnot is applied, the state goes to |10⟩ since the control qreg0 is at 1, qreg1 flips to 0.
    The triple consecutive Cnot swapped the states of the 2 qubits; it is basically a SWAP gate.
  
- qc2:
    This is an example of an entangled state. The state of one qubit is dependent on the state of the other, and vice versa.
    ”The Cnot entangles the qubits so that it is not possible to talk about their states separately”. The circuit in question is equivalent to a regular Cnot where the 2nd qubit is controlled (p.80).
    When the Cnot is applied, the state does not changes because the initial state is |00⟩ and the control is on qreg1 which is 0 here.
  
- qc3:
    This combination is the same as a Z gate. The output does not change; it is still |0⟩ as shown by the histogram below. HXH = Z
  
- qc4:
    This combination is the same as a X gate. The output is flipped; |0⟩ becomes |1⟩. HZH = X
  
- qc5:
    After multiple simulation, the probability amplitude of |0⟩ is between 0.85 and 0.89 and 0.11 and 0.15 for |1⟩.
    Consider the Bloch sphere, after the first H, the qubit state is on the x-axis halfway between 0 and 1 (0.5 probability).
    Next the T gate rotate the state 45 degrees on phi, thus putting it halfway between x and y while still being at 0.5 probability.
    Finally, the 2nd H flip the state between -y and z. A similar outcome cannot be reproduced using X,Y,Z gates.
    These gates only flip the state between 0 and 1 without really creating superposition.
    In term of Bloch sphere, the state goes from up to down along the z-axis with these gates which is exactly why you can not get the interesting rotations and superpositions you get with T and H gates.
  
- qc6:
    The output is the same as a regular H gate with the probability amplitudes of |0⟩ and |1⟩ at 0.5, however the signs are different.
    The first X does not change anything. Then the first Y changes the sign to -x and the 2nd X flips the sign the imaginary part of |1⟩ (also changes phi from 180 to -180).
    Finally the last Y flips back +x, and the qubit is at the same position it started with the first H with the exception of the signs of the real parts changed to a negative due to the combination of the second XY.
