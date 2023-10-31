Logic Gates in QC

- The AND gate is simply made by using a Toffoli gate, thus the usage of 3 qubits. The AND gate is simply T|x, y, 0⟩. 
  q0 is the measurement gate, so the Toffoli gate was applied such that q1 and q2 are controlled.
  
- The OR gate is made by using a Toffoli gate, thus the usage of 3 qubits. The OR gate is T|1, x, y⟩.
  Before the T gate is applied, two Cnot were applied from q2 (control) to q0 (target) and from q1 to q0.

- The XOR gate is even simpler than the OR. By removing the T gate, we have a XOR
