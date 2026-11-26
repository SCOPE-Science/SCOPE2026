#!/usr/bin/env python3
"""Exact algebraic verification of a three-site exclusion counting polynomial.

Dependency: sympy (tested with recent 1.x versions). No external data needed.
"""
import sympy as sp

a, b, c, e, u, z = sp.symbols('a b c e u z')
weights = [a, b, c]
states = [m for m in range(8) if m.bit_count() == 2]
L = sp.zeros(3)
for row, mask in enumerate(states):
    for site in range(3):
        for direction in (1, -1):
            next_site = (site + direction) % 3
            if (mask >> site) & 1 and not ((mask >> next_site) & 1):
                rate = weights[site] * (1 + direction * e) / 2
                new_mask = mask ^ (1 << site) ^ (1 << next_site)
                col = states.index(new_mask)
                L[row, col] += rate * (u if direction == 1 else 1 / u)
                L[row, row] -= rate

S1 = a + b + c
S2 = a*a + b*b + c*c
Spair = a*b + b*c + c*a
expected = (z**3 + S1*z*z +
    ((1-e*e)*S2 + 2*(1+e*e)*Spair)*z/4 -
    a*b*c*((1+e)**3*(u**3-1)+(1-e)**3*(u**(-3)-1))/8)
assert sp.factor(L.charpoly(z).as_expr() - expected) == 0
assert sp.factor(expected - expected.subs({e: -e, u: 1/u}, simultaneous=True)) == 0

example_poly = expected.subs({a: 1, b: 2, c: 4})
# implicit derivative of dominant eigenvalue at the zero tilt
mean = sp.factor(-sp.diff(example_poly,u).subs({u:1,z:0})/
                 sp.diff(example_poly,z).subs({u:1,z:0}))
assert sp.factor(mean - 24*e*(e*e+3)/(7*(e*e+7))) == 0
print('PASS: exact characteristic polynomial, all-bias parity, and mean example')
