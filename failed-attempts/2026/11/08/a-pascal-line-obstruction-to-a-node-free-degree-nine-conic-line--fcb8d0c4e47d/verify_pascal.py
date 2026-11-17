"""Exact verification of a Pascal-line tangency obstruction over characteristic zero.
Run with: python verify_pascal.py (requires sympy).
"""
from itertools import combinations
import sympy as sp

# The adjacent-pair graph on six lines is C6. The two off-conic
# triples not involving the seventh line are forced by its complement.
vertices = tuple(range(6))
cycle = {frozenset((i, (i + 1) % 6)) for i in vertices}
independent_triples = [frozenset(T) for T in combinations(vertices, 3)
                       if all(frozenset(e) not in cycle for e in combinations(T, 2))]
assert set(independent_triples) == {frozenset((0, 2, 4)), frozenset((1, 3, 5))}
all_pairs = {frozenset(p) for p in combinations(vertices, 2)}
used = set(cycle)
for triple in independent_triples:
    used.update(frozenset(p) for p in combinations(triple, 2))
assert all_pairs - used == {frozenset((0, 3)), frozenset((1, 4)), frozenset((2, 5))}

X, Y, Z, t = sp.symbols('X Y Z t')
s = (t - 1) / t
Q = t**2*X**2 + Y**2 - t*X*Y - t*(t-1)*X*Z - Y*Z
# On each of the two pencils, the six adjacent intersections lie on Q.
points = [(0, 0), (0, 1), (1, 1), (1, t), (s, t), (s, 0)]
assert all(sp.cancel(Q.subs({X: x, Y: y, Z: 1})) == 0 for x, y in points)
# Opposite sides meet at (1,0), (0,t), (s,1) in the affine chart.
L = t*X + Y - t*Z
assert all(sp.cancel(L.subs({X: x, Y: y, Z: 1})) == 0
           for x, y in [(1, 0), (0, t), (s, 1)])
restrict = sp.factor(Q.subs(Y, t*Z-t*X))
discriminant = sp.factor(sp.discriminant(restrict.subs(Z, 1), X))
assert sp.simplify(discriminant - 4*t**2*(t**2-t+1)) == 0
M = sp.Matrix([[t**2, -t/2, -t*(t-1)/2],
               [-t/2, 1, -sp.Rational(1, 2)],
               [-t*(t-1)/2, -sp.Rational(1, 2), 0]])
determinant = sp.factor(M.det())
assert sp.simplify(determinant + t**2*(t**2-t+1)/4) == 0
assert sp.simplify(discriminant + 16*determinant) == 0
print('PASS: C6 complement incidence, six conic points, Pascal line,')
print('      discriminant and conic determinant; tangency forces singularity.')
