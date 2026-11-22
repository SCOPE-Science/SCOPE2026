"""Exact symbolic checks for the six-unit-disk flower theorem.

Requires Python 3.10 or later and SymPy (tested with SymPy 1.14).
Run: python verify.py
The proof in RESULT.md is analytic; this verifies its finite identities.
"""
import sympy as sp

r = sp.sqrt(3)
p = [sp.Matrix([0, 0]), sp.Matrix([2, 0]), sp.Matrix([1, r]),
     sp.Matrix([-1, r]), sp.Matrix([-2, 0]), sp.Matrix([-1, -r])]
E = [(0, j) for j in range(1, 6)] + [(j, j + 1) for j in range(1, 5)]
assert len(E) == 9

# The columns are the gradients of the nine active distance functions.
G = sp.zeros(12, 9)
for k, (i, j) in enumerate(E):
    d = p[j] - p[i]
    assert sp.simplify(d.dot(d)) == 4
    u = d / 2
    for q in range(2):
        G[2 * j + q, k] = u[q]
        G[2 * i + q, k] = -u[q]

# Derivative of the perimeter of the outer pentagonal hull.
perimeter_gradient = sp.zeros(12, 1)
for k in range(5):
    i = k + 1
    a = ((k - 1) % 5) + 1
    b = ((k + 1) % 5) + 1
    da, db = p[i] - p[a], p[i] - p[b]
    va = da / sp.sqrt(da.dot(da))
    vb = db / sp.sqrt(db.dot(db))
    perimeter_gradient[2 * i] = sp.simplify(va[0] + vb[0])
    perimeter_gradient[2 * i + 1] = sp.simplify(va[1] + vb[1])

weights = sp.Matrix([2 / r, 1 / r, 1 / r, 1 / r, 2 / r]
                    + [1 - 1 / r] * 4)
assert all(sp.simplify(v)==0 for v in (G * weights - perimeter_gradient))
assert all(sp.N(w) > 0 for w in weights)

# Quotient by translations and a rotation: set c_0=(0,0), (c_1)_y=0.
# Remaining coordinate rows are x_1, x_2,y_2,...,x_5,y_5.
coordinate_rows = [2, 4, 5, 6, 7, 8, 9, 10, 11]
J = G.extract(coordinate_rows, list(range(9))).T
assert sp.simplify(J.det()) == sp.Rational(9, 16)
assert J.rank() == 9

# Strictly nonactive contacts at the reference configuration.
for i in range(6):
    for j in range(i + 1, 6):
        if (i, j) not in E:
            assert sp.simplify((p[j] - p[i]).dot(p[j] - p[i]) - 4) > 0

# The five extremal outer chords: four of length 2, one 2*sqrt(3).
outer_lengths = [sp.sqrt((p[j] - p[i]).dot(p[j] - p[i]))
                 for i, j in [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]]
assert sp.simplify(sum(outer_lengths) - (8 + 2 * r)) == 0
assert sp.simplify(min(weights) - (1 - 1 / r)) == 0
print('PASS: 9 contacts, exact gradient identity, 9/16 reduced determinant,')
print('      strict inactive gaps, exact perimeter, and sharp weight.')
