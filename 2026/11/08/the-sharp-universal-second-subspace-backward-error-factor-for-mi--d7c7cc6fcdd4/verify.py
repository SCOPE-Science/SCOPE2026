#!/usr/bin/env python3
"""Exact certificate and supplementary numerical tests for a two-step backward-error bound."""
import math
import random
import sympy as sp

r = sp.sqrt(2)
E = (r - 1) / 2
t = 1 / r
s = sp.symbols('s', real=True)
a, c = sp.symbols('a c', real=True)
p = 2 * (1 + r) - 4 * s
phi = s - 1 / p
assert sp.simplify(p.subs(s, 1) - 2 * (r-1)) == 0
assert sp.simplify(phi.subs(s, 0) + E) == 0
assert sp.simplify(phi.subs(s, t) - E) == 0
assert sp.simplify(phi.subs(s, 1) + E) == 0
assert sp.simplify(sp.diff(phi, s).subs(s, t)) == 0
assert sp.simplify(sp.diff(phi, s, 2) + 32 / p**3) == 0

values = [sp.Integer(0), t, sp.Integer(1)]
weights = [r - 1, r, sp.Integer(1)]
q = sp.expand(sum(w * ((lam * (a + c * lam)-1)**2 - E**2 * (a + c * lam)**2)
                  for w, lam in zip(weights, values)))
a0, c0 = 2 * (1+r), sp.Integer(-4)
A = 3-r
B = r
C = sp.Rational(3, 8) * (2+r)
centered = A*(a-a0)**2 + 2*B*(a-a0)*(c-c0) + C*(c-c0)**2
assert sp.simplify(q - centered) == 0
assert sp.simplify(A*C-B**2 - (3*r-4)/8) == 0
assert sp.simplify(q.subs({a:a0,c:c0})) == 0
assert float(A) > 0 and float(A*C-B**2) > 0

# The certificate is exact; these are only supplementary floating-point checks.
rng = random.Random(2473)
Efloat = float(E)
for _ in range(3000):
    eig = [1.0] + [rng.random() for _ in range(rng.randrange(1,9))]
    b = [rng.uniform(-2,2) for _ in eig]
    vals = [float(p.subs(s, lam)) for lam in eig]
    normsq = sum((v*bb)**2 for v,bb in zip(vals,b))
    residualsq = sum(((lam*v-1)*bb)**2 for lam,v,bb in zip(eig,vals,b))
    assert residualsq <= (Efloat**2 + 1e-12) * normsq

# Exact extremizer has all three nonzero component weights.
for lam in values:
    assert sp.simplify((lam - 1/p.subs(s,lam))**2 - E**2) == 0
print('PASS: exact symbolic inequalities, three-point extremizer, 3000 numerical checks')
