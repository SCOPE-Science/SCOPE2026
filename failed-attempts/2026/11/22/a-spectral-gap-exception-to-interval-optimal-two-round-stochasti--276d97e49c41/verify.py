#!/usr/bin/env python3
"""Independent finite checks of a two-round, Markov-positive spectral minimax law.

No external packages needed. Finite tests supplement, never replace, the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose

COUNT = 0

def ck(test, context):
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(context)


def eigen_action(M, v):
    return [sum(a * b for a, b in zip(row, v)) for row in M]


def crown_matrix(m):
    out = [[F(0) for _ in range(2*m)] for _ in range(2*m)]
    for i in range(m):
        for j in range(m):
            if i != j:
                out[i][m+j] = out[m+j][i] = F(1, m-1)
    return out

# Exact invariant-subspace spectra and two-step contraction on an unbounded
# symbolic family (finite tested range, with exact arithmetic).
for m in range(7, 81):
    s = F(1, m-1)
    q = F(m-1, 2*m-3)
    rho = F(1, 2*m-3)
    ck(q == 1/(2-s), (m, 'second gain'))
    ck(rho == s/(2-s), (m, 'contraction'))
    f = lambda eig: eig * (1-q+q*eig)
    for eig in [-F(1), -s, s]:
        ck(abs(f(eig)) <= rho, (m, 'spectral factor', eig))
    ck(f(-F(1)) == rho and f(s) == rho, (m, 'active modes'))
    if m <= 16:
        M = crown_matrix(m)
        ck(all(sum(row) == 1 for row in M), (m, 'stochastic'))
        z = [F(1)]*m + [F(-1)]*m
        w = [F(1), F(-1)] + [F(0)]*(m-2)
        for vector, eig in [([F(1)]*(2*m), F(1)), (z, -F(1)),
                            (w+w, -s), (w+[-v for v in w], s)]:
            ck(eigen_action(M, vector) == [eig*v for v in vector],
               (m, 'exact crown matrix eigenspace', eig))

# Verify active endpoint bounds, intermediate eigenvalue bound, and strict
# improvement over both stationary tuning and interval-safe Chebyshev.
critical = 3 - 2*sqrt(2)
for numerator in [1, 2, 7, 19, 50, 99, 142, 166, 170, 171]:
    s = F(numerator, 1000)
    if float(s) >= critical:
        continue
    q = 1/(2-s)
    rho = s/(2-s)
    f = lambda z: z * (1-q+q*z)
    ck(f(s) == rho and f(-1) == rho, (s, 'endpoint match'))
    for j in range(201):
        z = -s + 2*s*F(j,200)
        ck(abs(f(z)) <= rho, (s, 'spectral interior', z))
    fixed = ((1+s)/(3-s))**2
    interval = (1+s)**2/(s*s-14*s+17)
    ck(fixed > rho and interval > rho, (s, 'separation'))
    ck(fixed-rho == 2*(1-s)**3/((3-s)**2*(2-s)),(s,'fixed gap'))
    ck(interval-rho == 2*(1-s)*(s*s-6*s+1)/((2-s)*(s*s-14*s+17)),
       (s,'interval gap'))
    # Exact endpoint minimax against a rational grid of competitors.
    for i in range(61):
        for j in range(61):
            a,b=F(i,60),F(j,60)
            lower=max(abs((1-a+a*s)*(1-b+b*s)),abs((1-2*a)*(1-2*b)))
            ck(lower >= rho, (s, 'candidate competitor',i,j))

# Illustration: the subthreshold crown threshold begins at m=7.
ck(F(1,6) < F(17,100), 'crown m=7 below .17')
ck(F(1,5) > F(17,100), 'crown m=6 above .17')
print(f'PASS: {COUNT} exact finite assertions. Infinite statements require the proof.')
