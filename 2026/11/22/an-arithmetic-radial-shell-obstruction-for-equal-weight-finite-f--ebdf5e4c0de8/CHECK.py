"""Exact finite checks for Gaussian-radial moment identities.

This file checks polynomial identities and a degree-three example. The
all-degree obstruction is proved analytically in RESULT.md and uses the
classical Hermite--Lindemann transcendence theorem.
"""
from fractions import Fraction as F
from math import comb, factorial

checks = 0
for m in range(1, 13):
    # Monic signed Laguerre polynomial: (-1)^m m! L_m(X).
    coeff = [(-1)**(m+k)*factorial(m)*comb(m,k)//factorial(k)
             for k in range(m+1)]
    assert coeff[-1] == 1
    checks += 1
    # Orthogonality against all lower monomials in e^{-x} dx.
    for j in range(m):
        assert sum(coeff[k]*factorial(k+j) for k in range(m+1)) == 0
        checks += 1
    # Norm is positive; moment-matrix rank cannot fall below m.
    square = [sum(coeff[i]*coeff[t-i]
                  for i in range(m+1) if 0 <= t-i <= m)
              for t in range(2*m+1)]
    assert sum(c*factorial(t) for t, c in enumerate(square)) == factorial(m)**2
    checks += 1

# Exact arithmetic in Q(sqrt(2)) for the two-node Laguerre formula.
def add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def mul(u, v):
    return (u[0]*v[0] + 2*u[1]*v[1],
            u[0]*v[1] + u[1]*v[0])

def power(u, n):
    out = (F(1), F(0))
    for _ in range(n):
        out = mul(out, u)
    return out

nodes = ((F(2), F(-1)), (F(2), F(1)))
# Gauss weights alpha_small, alpha_large are algebraic.
weights = ((F(1, 2), F(1, 4)), (F(1, 2), F(-1, 4)))
for k in range(4):
    lhs = (F(0), F(0))
    for a, x in zip(weights, nodes):
        lhs = add(lhs, mul(a, power(x, k)))
    assert lhs == (F(factorial(k)), F(0)), (k, lhs)
    checks += 1

print('RADIAL_GAUSS_CHECKS_PASS', checks)
