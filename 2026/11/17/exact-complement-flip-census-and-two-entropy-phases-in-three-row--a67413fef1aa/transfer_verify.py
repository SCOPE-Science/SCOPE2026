#!/usr/bin/env python3
"""Exact integer transfer and characteristic polynomial for Day & Night complement flips."""
from math import comb

W = [comb(3, i) for i in range(4)]
PAIRS = [(a, b) for a in range(4) for b in range(4)]
N = len(PAIRS)
M = [[0] * N for _ in range(N)]
for i, (a, b) in enumerate(PAIRS):
    for c in range(4):
        if a + b + c in (3, 6):
            M[i][PAIRS.index((b, c))] = W[b]

def mult(A, B):
    size = len(A)
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j, v in enumerate(A[i]):
            if v:
                for k, v2 in enumerate(B[j]):
                    C[i][k] += v * v2
    return C

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

# Newton identities: det(tI-M) = sum_{k=0}^N c_k t^(N-k).
I = [[int(i == j) for j in range(N)] for i in range(N)]
P = I
traces = []
for k in range(1, N + 1):
    P = mult(P, M)
    traces.append(trace(P))
cs = [1]
for k in range(1, N + 1):
    numerator = -sum(cs[k-j] * traces[j-1] for j in range(1, k+1))
    assert numerator % k == 0
    cs.append(numerator // k)

def poly_mul(p, q):
    x = [0] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            x[i+j] += a*b
    return x
# Coefficients in ascending order of t.
poly = [1]
for q in ([0,1], [0,1], [0,1], [0,1], [-3,1],[-3,1],[-18,0,0,1],[-18,0,0,1],[-1,-1,1],[1,1,1]):
    poly = poly_mul(poly, q)
assert len(poly) == N+1
assert list(reversed(cs)) == poly, (cs,poly)
print('characteristic_polynomial_coefficients_ascending=',poly)
print('factorization=t^4*(t-3)^2*(t^3-18)^2*(t^2-t-1)*(t^2+t+1)')

lucas = [2,1]
for _ in range(30):
    lucas.append(lucas[-1]+lucas[-2])
P = I
for n in range(1, 21):
    P = mult(P, M)
    actual = trace(P)
    omega = 2 if n % 3 == 0 else -1
    predicted = 2*3**n + lucas[n] + omega + (6*18**(n//3) if n % 3 == 0 else 0)
    assert actual == predicted, (n,actual,predicted)
    if n >= 3:
        print('n=',n,'phase_inverting_states=',actual,'two_cycle_orbits=',actual//2)
print('ALL_CHECKS_PASS')
