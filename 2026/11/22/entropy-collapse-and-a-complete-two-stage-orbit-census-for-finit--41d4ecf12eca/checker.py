"""Reproducible finite-state checks for two-stage differentiability shifts.

Run: python3 checker.py
Requires: Python 3.10+ and SymPy.
The entropy inequalities use an independent measure-theoretic argument in RESULT.md;
this script verifies the finite-state polynomial and periodic-word identities.
"""
from itertools import product
from math import log
import sympy as sp

FORBIDDEN = ('111', '222', '12121', '21212', '112211', '221122')

def legal(block):
    return all(f not in block for f in FORBIDDEN)

states = [''.join(c) for c in product('12', repeat=5) if legal(''.join(c))]
assert len(states) == 14
indices = {word: i for i, word in enumerate(states)}
A = sp.zeros(len(states))
for i, word in enumerate(states):
    for next_letter in '12':
        candidate = word + next_letter
        if legal(candidate):
            A[i, indices[candidate[1:]]] += 1
assert sum(A) == 18
z, lam = sp.symbols('z lambda')
Q = (1 + z + z**2) * (z**4 + z - 1) * (z**6 - z**5 - z**4 + z**3 - 1)
P = lam**2 * (lam**2 + lam + 1) * (lam**4 - lam**3 - 1) * (lam**6 - lam**3 + lam**2 + lam - 1)
assert sp.expand((sp.eye(14) - z*A).det() - Q) == 0
assert sp.expand(A.charpoly(lam).as_expr() - P) == 0
assert any(x == 0 for x in A**14)
assert all(x > 0 for x in A**15)
# Symbol interchange commutes with the graph. Perron eigenvector is invariant.
flip = lambda w: ''.join('2' if x == '1' else '1' for x in w)
assert all(A[i,j] == A[indices[flip(states[i])],indices[flip(states[j])]]
           for i in range(14) for j in range(14))
reps, seen = [], set()
for word in states:
    if word not in seen:
        reps.append(word)
        seen.update((word, flip(word)))
assert len(reps) == 7
B = sp.zeros(7)
for i, w in enumerate(reps):
    for j, v in enumerate(reps):
        B[i,j] = A[indices[w],indices[v]] + A[indices[w],indices[flip(v)]]
assert sp.expand(B.charpoly(lam).as_expr() - lam*(lam**2 + lam + 1)*(lam**4 - lam**3 - 1)) == 0
root = float(max(float(sp.re(x)) for x in sp.nroots(lam**4 - lam**3 - 1) if abs(float(sp.im(x))) < 1e-12))
assert abs(root - 1.3802775690976141) < 1e-12
assert (2/3)*log((1+5**.5)/2) < log(root) < (3/4)*log((1+5**.5)/2)
periods = (0,0,6,0,0,18,0,8,42,10,22,90)
for n in range(1,13):
    # Distinct cyclic configurations indexed by position, no quotient by rotation.
    num = 0
    for bits in product('12', repeat=n):
        word = ''.join(bits)
        # Repeating 6 times detects all forbidden words (max length six)
        if legal(word*6):
            num += 1
    assert num == int(sp.trace(A**n)) == periods[n-1], (n, num)
print('PASS: 14 states, 18 edges, determinant and characteristic polynomial')
print('PASS: primitive exponent 15, seven-state interchange quotient')
print('PASS: exact cyclic word counts through length 12')
print('PASS: first two levels satisfy entropy comparison bounds')
