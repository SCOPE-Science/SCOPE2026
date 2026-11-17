#!/usr/bin/env python3
"""Exact cyclic three-clock count on a two-row periodic Moore graph."""
import sympy as S
from collections import Counter

columns = [(a, b) for a in range(3) for b in range(3)]
T = S.zeros(81)
for a in range(9):
    for b in range(9):
        for c in range(9):
            left, mid, right = columns[a], columns[b], columns[c]
            if all(((mid[r] + 1) % 3 in
                    (mid[1-r], *left, *right)) for r in (0, 1)):
                T[9*a+b, 9*b+c] = 1
x = S.symbols('x')
q = S.factor(T.charpoly(x).as_expr())
expected = x**74 * (x*x+3*x+9)**2 * (x**3-6*x*x-9*x-18)
assert S.expand(q - expected) == 0
print('matrix_order=81 matrix_nonzeros=',sum(v != 0 for v in T))
print('characteristic_polynomial=',q)
# Obtain traces efficiently from ordinary integer matrix multiplication.
for n in range(3, 11):
    t = int(S.trace(T**n))
    print(f'n={n} primitive_states={t} primitive_orbits={t//3}')
    assert t > 0 and t % 3 == 0
print('dominant_cubic_root=', S.nroots(x**3-6*x*x-9*x-18)[0])
