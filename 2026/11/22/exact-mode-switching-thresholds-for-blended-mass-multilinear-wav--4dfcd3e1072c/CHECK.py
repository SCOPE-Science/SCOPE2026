"""Exact-rational regression checks for an orthotope Q1 mixed-mass wave spectrum.

Run: python3 CHECK.py
Finite tests only; the infinite-parameter theorem is proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

COUNT = 0

def eq(x, y):
    global COUNT
    assert x == y, (x, y)
    COUNT += 1

def tensor(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0]))
             for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]

def tensor_all(matrices):
    out = [[F(1)]]
    for A in matrices:
        out = tensor(out, A)
    return out

def matrices(lengths, alpha):
    d = len(lengths)
    one_mass = [[[h / 3, h / 6], [h / 6, h / 3]] for h in lengths]
    one_stiff = [[[1 / h, -1 / h], [-1 / h, 1 / h]] for h in lengths]
    consistent = tensor_all(one_mass)
    stiffness = [[F(0) for _ in range(2**d)] for _ in range(2**d)]
    for j in range(d):
        term = tensor_all([one_stiff[i] if j == i else one_mass[i]
                           for i in range(d)])
        stiffness = [[stiffness[i][k] + term[i][k]
                      for k in range(2**d)] for i in range(2**d)]
    volume = F(1)
    for h in lengths:
        volume *= h
    mass = [[alpha * consistent[i][j] +
             (1-alpha) * volume / 2**d * (i == j)
             for j in range(2**d)] for i in range(2**d)]
    return mass, stiffness

def critical_modes(lengths, alpha):
    rs = sorted((1 / (h*h) for h in lengths), reverse=True)
    s = F(0)
    vals = []
    for k,r in enumerate(rs, 1):
        s += r
        vals.append(12*s / (3**k * (1-alpha) + alpha))
    return vals

for raw_lengths in [[1], [1,1], [1,2], [1,1,1], [1,2,3],
                    [1,1,1,1], [1,2,3,4], [2,3,5,7]]:
    lengths = list(map(F, raw_lengths))
    d = len(lengths)
    r = sorted((1 / (h*h) for h in lengths), reverse=True)
    thresholds = []
    s = F(0)
    for k in range(1,d):
        s += r[k-1]
        z = 3**k*(2*s-r[k])
        thresholds.append(z / (z+r[k]))
    for i in range(len(thresholds)-1):
        assert thresholds[i] < thresholds[i+1]
        COUNT += 1
    alpha_values = sorted(set([F(0), F(1,3), F(1,2), F(3,4),
                               F(9,10), F(27,28), F(1)] + thresholds))
    grid = list(product((0,1),repeat=d))
    for a in alpha_values:
        M, K = matrices(lengths,a)
        theoretical = critical_modes(lengths,a)
        spectral = []
        for eps in grid:
            active = [i for i,v in enumerate(eps) if v]
            k = len(active)
            v = [F((-1)**sum(x[i]*eps[i] for i in range(d))) for x in grid]
            st = sum(1/(lengths[i]**2) for i in active)
            lam = F(0) if k==0 else 12*st/(3**k*(1-a)+a)
            spectral.append(lam)
            for i in range(2**d):
                lhs = sum(K[i][j]*v[j] for j in range(2**d))
                rhs = lam*sum(M[i][j]*v[j] for j in range(2**d))
                eq(lhs,rhs)
        eq(max(spectral),max(theoretical))
        best_k = max(range(1,d+1), key=lambda k: theoretical[k-1])
        eq(theoretical[best_k-1], max(spectral))
        for k in range(1,d):
            eq((theoretical[k] >= theoretical[k-1]), (a >= thresholds[k-1]))
for a in [F(0),F(1,2),F(3,4),F(9,10),F(27,28),F(1)]:
    values = critical_modes([F(1)]*3,a)
    eq(values[0],F(12)/(3-2*a))
    eq(values[1],F(24)/(9-8*a))
    eq(values[2],F(36)/(27-26*a))

eq(3*F(1)/(3*F(1)+F(1)),F(3,4))
eq(27*F(1)/(27*F(1)+F(1)),F(27,28))
print('VERIFY_OK', COUNT)
