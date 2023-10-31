'''
Use Shor’s algorithm to factor N = 35 with a = 17.
(a) Show that gcd(a, N ) = 1.
(b) What is the period of ax modN?
(c) Calculate the factors p = gcd(ar/2 − 1, N ) and q = gcd(ar/2 + 1, N ).
'''

import math
from sympy import gcd
N = 35 a = 17
#a) Check if gcd(a, N) = 1
G = math.gcd(a, N)
print(f"a) gcd(17,35) is: {G}")
#b) Find the period r of a^x mod N r=0
for x in range(1, N):
if (a ** x) % N == 1: r=x
break
#c) Calculate factors p and q p = gcd(a**(r//2) - 1, N)
q = gcd(a**(r//2) + 1, N)
# Print the results
print(f"b) The period r is: {r}")
print(f"c) The factors p and q are: {p} and {q}")
