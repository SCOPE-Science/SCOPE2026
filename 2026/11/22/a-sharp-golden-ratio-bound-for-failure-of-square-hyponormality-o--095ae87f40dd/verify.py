#!/usr/bin/env python3
"""Supplementary exact and randomized checks for a sharp one-fork square-defect bound.

Requires Python 3.10+ and SymPy. Finite tests supplement, but do not establish,
the infinite-dimensional theorem proved in RESULT.md.
"""
import math
import random
import sympy as sp

z = sp.symbols('z', real=True)
alpha = (sp.sqrt(5) - 1) / 4
critical = (sp.sqrt(5) - 2) / 4
sigma = (1 + sp.sqrt(5)) / 4
q = (5 - sp.sqrt(5)) / 10

# Check the pointwise majorant exactly in Q(sqrt(5))[z].
polynomial = (2/sigma - z/sigma**2) * (z**2 + critical) - z
certificate = (1-z) * (z-alpha)**2 / sigma**2
assert sp.simplify(sp.expand(polynomial-certificate)) == 0
assert sp.simplify(q*alpha + (1-q) - sigma) == 0

# Check exact two-ray equality and principal-minor positivity of D+critical*I.
b1sq = sp.simplify(q*alpha)
b2sq = sp.simplify(1-q)
b1b2 = sp.sqrt(b1sq*b2sq)
D = sp.diag(alpha**2, 1) - sigma*sp.Matrix([[b1sq, b1b2], [b1b2, b2sq]])
H = D + critical*sp.eye(2)
assert sp.simplify(H.det()) == 0
assert sp.simplify(H[0,0]) > 0
assert sp.simplify(sp.trace(H)) > 0
print('Exact polynomial identity and two-ray extremal certificate: PASS')

# Check random finite-coordinate reductions with unsaturated branch constraints.
# These tests are not a substitute for the affine-majorant proof.
rng = random.Random(20231115)
d = float(critical)
tests = 0
max_ratio = 0.0
for branches in range(2,18):
    for _ in range(500):
        X = [rng.uniform(0.00001, 1) for _ in range(branches)]
        raw = [rng.expovariate(1) for _ in range(branches)]
        total = sum(raw)
        P = [v/total for v in raw]
        mu = rng.random()**0.5
        b2 = [mu*p*x for p,x in zip(P,X)]
        s = sum(b2)
        ratio = s*sum(y/(x*x+d) for y,x in zip(b2,X))
        assert ratio <= 1 + 5e-13
        max_ratio = max(max_ratio, ratio)
        tests += 1
print(f'Random secular tests: {tests} PASS; maximum checked ratio {max_ratio:.12f}')

# Explicit sharp block: one eigenvalue is -critical and the other positive.
smallest = min(float(v) for v in D.eigenvals())
assert abs(smallest + d) < 1e-11
print(f'Extremal negative eigenvalue = {smallest:.14f}; sharp bound = {-d:.14f}')
