# Quantum-Computing
Simon and Shor simulations
- Simon:
  The period is the 4-bit ‘1010’.
  Counts: {'1110', '1011', '0001', '0100', '0101', '0000', '1111', '1010’}

- Shor:
  Alike the paper result, the peak outcomes are 101 and 110 (5th and 6th integer representation of the binary outcome) with 000 being a failure of the algorithm.
  Given the outcome ∣101⟩=∣5⟩ and its associated fraction expansion {0, 1, 1/2, 2/3, 5/8}.
  The third convergent 2/3 in the expansion is identified as s/r.
  Testing this value with the relation ar mod N = 1 correctly yields r = 3 as the order.
  This demonstrates how the continued fraction expansion is crucial in identifying the correct order, which is a key step in the factoring process.
  Additionally, it's noted that the other convergents do not yield an r that passes the test.
  This emphasizes the importance of choosing the correct convergent from the continued fraction expansion to ensure the success of the algorithm in finding the factors of N.
