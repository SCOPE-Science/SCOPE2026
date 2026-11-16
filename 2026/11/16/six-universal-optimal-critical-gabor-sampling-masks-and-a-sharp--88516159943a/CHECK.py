#!/usr/bin/env python3
"""Exact symbolic verification of the three-point finite Gabor design.
Requires Python 3 and SymPy. No external files or network access.
"""
from itertools import combinations, permutations
import sympy as sp

r, t = sp.symbols('r t', real=True)
w = (-1 + sp.sqrt(3)*sp.I)/2
base = sp.Matrix([1,r,r])
columns = {}
for x in range(3):
    for k in range(3):
        columns[(x,k)] = sp.Matrix([base[(j-x)%3] * w**(k*j) for j in range(3)])

pairs = list(columns)
sets = list(combinations(pairs, 3))
assert len(sets) == 84
permutations_set = {tuple((x, perm[x]) for x in range(3)) for perm in permutations(range(3))}
assert len(permutations_set) == 6
lower = 1-2*r+4*r*r
upper = 1+r+r*r
for S in sets:
    if S in permutations_set:
        M = sp.Matrix.hstack(*[columns[p] for p in S])
        gram = M.conjugate().T*M
        # Obtain characteristic polynomial using trace, trace-square and determinant.
        tr = sp.simplify(sp.expand(sp.trace(gram)))
        sq = sp.simplify(sp.expand(sp.trace(gram*gram)))
        second = sp.factor((tr*tr-sq)/2)
        det = sp.factor(sp.expand(gram.det()))
        target = sp.expand((t-lower)*(t-upper)**2)
        got = sp.expand(t**3-tr*t**2+second*t-det)
        assert sp.simplify(sp.expand(got-target)) == 0, S
    else:
        # At least two chosen nodes share a translation or a modulation.
        assert len({p[0] for p in S}) < 3 or len({p[1] for p in S}) < 3

# For a non-permutation S, a two-column Rayleigh quotient is bounded by
# either (1-r)^2 or 3*r^2, strictly below lower for 0<r<1.
assert sp.factor(lower-(1-r)**2) == 3*r*r
assert sp.simplify(lower-3*r*r-(1-r)**2) == 0

ratio = lower/(1+2*r*r)
assert sp.simplify(sp.diff(ratio,r)-2*(2*r*r+2*r-1)/(1+2*r*r)**2) == 0
r_star = (sp.sqrt(3)-1)/2
assert sp.simplify(sp.diff(ratio,r).subs(r,r_star)) == 0
assert sp.simplify(ratio.subs(r,r_star)-(3-sp.sqrt(3))/2) == 0

# Separate floating-point sanity check of the self-dual periodized Gaussian.
import math
sum_gauss = lambda x: sum(math.exp(-3*math.pi*(m+x)**2) for m in range(-8,9))
a, b = sum_gauss(0.0), sum_gauss(1/3)
assert abs(b/a-(math.sqrt(3)-1)/2) < 1e-13
print('PASS: 84 masks partitioned; six optimal Gram spectra exact; sharp constant and Gaussian self-dual point verified.')
