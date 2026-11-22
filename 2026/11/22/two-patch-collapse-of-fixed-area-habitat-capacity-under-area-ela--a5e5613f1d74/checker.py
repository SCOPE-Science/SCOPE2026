"""Numerical and exact boundary checks for the habitat-capacity design theorem.

Requires Python 3.10+ and numpy. Run: python checker.py
This is not a substitute for the universal analytic proof.
"""
from fractions import Fraction
from math import log
import random
import numpy as np

checks=0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

# Exact three-site equal-area eigenvalue: off-diagonal constant c has eigenvalues 2c,-c,-c.
check(2 * Fraction(1, 9) < Fraction(1, 4), 'bilinear three-site comparison')
check(2 * Fraction(1, 3) > Fraction(1, 2), 'square-root three-site comparison')
check(abs(log(2)/log(Fraction(9, 4)) - 0.8547556456757274) < 1e-12,
      'three-site sufficient counterexample exponent')

rng=random.Random(274218)
for n in range(2, 11):
    for gamma in (1., 1.25, 1.5, 2., 3.):
        for _ in range(90):
            W=np.array([[rng.random() for j in range(n)] for i in range(n)],dtype=float)
            W=(W+W.T)/2
            np.fill_diagonal(W,0)
            B=rng.uniform(0.2,10)
            aa=np.array([rng.expovariate(1) for i in range(n)])
            aa=B*aa/aa.sum()
            M=W*np.outer(aa**gamma,aa**gamma)
            largest=float(np.linalg.eigvalsh(M)[-1])
            wmax=float(W.max())
            bound=wmax*(B*B/4)**gamma
            check(largest <= bound*(1+4e-12), 'spectral upper bound')
            i,j=np.unravel_index(W.argmax(),W.shape)
            pair=np.zeros(n)
            pair[i]=pair[j]=B/2
            Mp=W*np.outer(pair**gamma,pair**gamma)
            val=float(np.linalg.eigvalsh(Mp)[-1])
            check(abs(val-bound)<=max(1e-12,abs(bound)*1e-11), 'sharp pair attainment')
print(f'PASS: {checks} checks')
