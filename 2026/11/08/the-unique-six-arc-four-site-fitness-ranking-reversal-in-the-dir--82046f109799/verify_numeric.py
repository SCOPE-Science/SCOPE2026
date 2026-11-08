"""Independent exact-rational four-vertex Markov absorption calculation.

Requires only Python standard library. Run: python verify_numeric.py
"""
from fractions import Fraction as F

A = [[0, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 0], [1, 1, 1, 0]]

def solve(B, b):
    n = len(b)
    C = [row[:] + [b[i]] for i, row in enumerate(B)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if C[i][k] != 0)
        C[k], C[pivot] = C[pivot], C[k]
        div = C[k][k]
        C[k] = [z/div for z in C[k]]
        for i in range(n):
            if i == k:
                continue
            z = C[i][k]
            C[i] = [u-z*v for u,v in zip(C[i], C[k])]
    return [C[i][-1] for i in range(n)]


def fixation(r):
    r = F(r)
    n = len(A)
    states = list(range(1, 2**n-1))
    ix = {s: k for k, s in enumerate(states)}
    B = [[F(0) for _ in states] for _ in states]
    b = [F(0) for _ in states]
    for mask in states:
        i = ix[mask]
        for v in range(n):
            for w in range(n):
                if (bool(mask & (1<<v)) == bool(mask & (1<<w))) or not A[v][w]:
                    continue
                rate = (r if mask & (1<<v) else F(1)) / sum(A[v])
                nxt = mask ^ (1<<w)
                B[i][i] += rate
                if nxt == 2**n-1:
                    b[i] += rate
                elif nxt:
                    B[i][ix[nxt]] -= rate
    x = solve(B,b)
    return [x[ix[1<<k]] for k in range(n)]


def polynomial(r):
    r = F(r)
    P = (77760*r**10 + 163944*r**9 - 423738*r**8 - 2023272*r**7
       - 3747633*r**6 - 4662639*r**5 - 4212709*r**4
       - 2570307*r**3 - 956688*r**2 - 185526*r - 11880)
    coeff = [116640,1165428,5613462,17204508,37727010,63686499,
             86411496,95625178,86411496,63686499,37727010,
             17204508,5613462,1165428,116640]
    D = F(0)
    for c in coeff:
        D=D*r+c
    return r**3 * P / D

for r in (F(1), F(3,2), F(2), F(3), F(4), F(5), F(10)):
    q = fixation(r)
    assert q[1]-q[3] == polynomial(r)
    assert all(F(0)<z<F(1) for z in q)
    print('r=',r,'difference=',q[1]-q[3])
print('PASS')
