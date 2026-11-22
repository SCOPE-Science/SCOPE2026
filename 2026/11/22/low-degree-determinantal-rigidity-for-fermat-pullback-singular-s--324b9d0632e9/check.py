#!/usr/bin/env python3
"""Exact standalone check for a Fermat-pullback degree-ten surface.

Requires Python 3.10+ and sympy. All rank computations use F_101 arithmetic.
The infinite-family proof is mathematical, not inferred from this example.
"""
from itertools import product
from math import comb
import sympy as sp

X = sp.symbols('x0:4')
G = [
    X[0]**2 + X[1]*X[2] + 2*X[3]**2,
    X[1]**2 + X[0]*X[3] + 3*X[2]*X[3],
    X[2]**2 + X[0]*X[1] + 5*X[1]*X[3],
]
J = sp.Matrix([[sp.diff(q, x) for x in X] for q in G])
minor = [
    sp.expand((-1)**j * J[:, [k for k in range(4) if k != j]].det())
    for j in range(4)
]
gcd = sp.Poly(minor[0], *X)
for q in minor[1:]:
    gcd = sp.gcd(gcd, sp.Poly(q, *X))
assert gcd.as_expr() == 1, gcd
for i in range(3):
    assert sp.expand(sum(J[i, j]*minor[j] for j in range(4))) == 0
F = sum(q**5 for q in G)
assert sp.expand(sum(sp.diff(F, X[j])*minor[j] for j in range(4))) == 0

# The three homogeneous quadrics have no common projective point at x3=0.
# Indeed g2=x1**2 gives x1=0, then g1=x0**2, g3=x2**2.
affine = [sp.expand(q.subs(X[3], 1)) for q in G]
affine_variables = X[:3]
gb = sp.groebner(affine, *affine_variables)
assert gb.is_zero_dimensional
univariate = [p for p in gb.polys if p.total_degree() == 8 and
              p.as_expr().free_symbols <= {X[2]}]
assert univariate, 'Expected a degree-eight elimination polynomial'
affine_jac = sp.Matrix([[sp.diff(q, v) for v in affine_variables]
                        for q in affine])
gb_singular = sp.groebner(affine + [affine_jac.det()], *affine_variables)
assert len(gb_singular.polys) == 1 and gb_singular.polys[0].as_expr() == 1

P = 101
D = []
for v in X:
    D.append([(exp, int(coeff) % P) for exp, coeff in
              sp.Poly(sp.diff(F, v), *X).terms() if int(coeff) % P])

def monomials(degree):
    for i in range(degree + 1):
        for j in range(degree - i + 1):
            for k in range(degree - i - j + 1):
                yield (i, j, k, degree - i - j - k)

def kernel_dimension(degree):
    index = {exp: i for i, exp in enumerate(monomials(degree + 9))}
    basis = {}
    column_count = 0
    for partial in D:
        for monomial in monomials(degree):
            column_count += 1
            vector = {
                index[tuple(a + b for a, b in zip(monomial, exp))]: val
                for exp, val in partial
            }
            while vector:
                pivot = max(vector)
                if pivot not in basis:
                    inverse = pow(vector[pivot], -1, P)
                    basis[pivot] = {idx: (val * inverse) % P
                                    for idx, val in vector.items()}
                    break
                scalar = vector[pivot]
                for idx, val in basis[pivot].items():
                    updated = (vector.get(idx, 0) - scalar * val) % P
                    if updated:
                        vector[idx] = updated
                    else:
                        vector.pop(idx, None)
    return column_count - len(basis)

expected = (0, 0, 0, 1, 4, 10, 20)
observed = tuple(kernel_dimension(r) for r in range(7))
assert observed == expected, (observed, expected)
print('PASS: exact primitive minors, Jacobian identities, and transverse base')
print('PASS: exact F_101 Jacobian syzygy dimensions:', *observed)
