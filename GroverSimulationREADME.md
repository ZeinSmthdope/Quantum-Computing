# Quantum-Computing

- Grover:
  The target state of this algorithm ‘110’ as shown by the histograms.
  When we repeat the oracle and diffusion part of the circuit, we effectively amplify the probability amplitude of the target state while reducing the amplitudes of the other states.
  This is a key property of Grover's algorithm.
  The increase in probability from 6370 to 7743 (refer to the histograms) indicates that the algorithm is becoming more confident in the correctness of the target state.
  As we repeat the oracle and diffusion steps more times, we aim to amplify the probability of the target state.
  However, there's a limit to this amplification, my guess is around sqrt(N) iterations with N possible solutions.
  Beyond this point, additional iterations may reduce the probability of the target state due to interference effects within the quantum system.
  The fluctuations in probability indicate an interplay of quantum amplitudes maybe. The observed numbers (3: 2728, 4: 101, 5: 4569) suggest the presence of interference or other phenomena.
  In summary, Grover's algorithm is designed to find the target state with high probability,
  but the exact number of iterations required depends on factors like the initial state, the number of possible solutions, and the specifics of the oracle implementation.
