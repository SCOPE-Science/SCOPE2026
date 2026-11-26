#!/usr/bin/env python3
"""Exact algebraic checks for the planar quadratic five-slot bound.

The accompanying proof establishes the general theorem; these checks target
its finite coefficient identities and explicit reaction-network witness.
"""
import itertools
import sympy as s

A, B, C = s.symbols('A B C')
rows = s.Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [-2, -1, 0],
    [0, -1, -2],
    [1, 1, 1],
])
for i, j in itertools.combinations(range(6), 2):
    pair = s.Matrix([list(rows.row(i)), list(rows.row(j))])
    assert pair.rank() == 2
    assert len(pair.nullspace()) == 1

X, Y, u, v = s.symbols('X Y u v')
shifted = A * (X - 1)**2 + B * (X - 1)*(Y - 1) + C * (Y - 1)**2
expected = A*X**2 + B*X*Y + C*Y**2 + (-2*A-B)*X + (-B-2*C)*Y + A+B+C
assert s.expand(shifted - expected) == 0

# Five directed reactions: 0 -> X+Y, X -> 0, Y -> 0, 2X -> 3X, 2Y -> 3Y.
reactions = [((0,0), (1,1), 1),
             ((1,0), (0,0), 2),
             ((0,1), (0,0), 2),
             ((2,0), (3,0), 1),
             ((0,2), (0,3), 1)]
assert len(reactions) == 5 and len({r[0] for r in reactions}) == 5
assert all(sum(inp) <= 2 and rate > 0 for inp, out, rate in reactions)
field = [s.Integer(0), s.Integer(0)]
for inp, out, rate in reactions:
    for k in range(2):
        field[k] += rate * (out[k] - inp[k]) * X**inp[0] * Y**inp[1]
assert [s.factor(z) for z in field] == [(X-1)**2, (Y-1)**2]
J = s.Matrix(field).jacobian([X, Y])
assert J.subs({X:1,Y:1}) == s.zeros(2)
assert s.solve(field, (X, Y)) == [(1,1)]
print('VERIFY_OK independent_coefficient_pairs=15 sharp_reactions=5 isolated_positive_equilibrium=1 zero_full_jacobian=1')
