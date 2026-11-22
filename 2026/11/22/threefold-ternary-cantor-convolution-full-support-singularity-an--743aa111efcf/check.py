#!/usr/bin/env python3
"""Exact-arithmetic checks for ternary triple Cantor convolution.

The mathematical proof is given in RESULT.md. This checker tests finite
levels and certifies the identities used in the all-depth transfer argument.
"""
from math import comb
from fractions import Fraction
from itertools import product

BASE = 3
N_INDEPENDENT = 3
# M[d][incoming carry][outgoing carry].
M = [[[0] * 2 for _ in range(2)] for _ in range(3)]
for carry in range(2):
    for raw_sum in range(4):
        d = (raw_sum + carry) % 3
        next_carry = (raw_sum + carry) // 3
        M[d][carry][next_carry] += comb(3, raw_sum)
assert M == [ [[1, 1], [0, 3]],
              [[3, 0], [1, 1]],
              [[3, 0], [3, 0]] ]

def vec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x)))
            for i in range(len(A))]

T = [[sum(M[d][i // 2][j // 2] * M[d][i % 2][j % 2]
          for d in range(3)) for j in range(4)] for i in range(4)]
assert T == [[19, 1, 1, 1], [12, 6, 0, 3],
             [12, 0, 6, 3], [10, 1, 1, 10]]
w0 = [1, 1, 1, 1]
w1 = vec(T, w0)
w2 = vec(T, w1)
assert w1 == [22, 21, 21, 22]
assert w2 == [482, 456, 456, 482]
# This identity proves the infinite recurrence, not only sample levels.
assert w2 == [26 * w1[i] - 90 * w0[i] for i in range(4)]

# Stochastic carry transition Q=(M[0]+M[1]+M[2])/8.
Q8 = [[sum(M[d][i][j] for d in range(3)) for j in range(2)]
      for i in range(2)]
assert Q8 == [[7, 1], [4, 4]]
pi = [Fraction(4, 5), Fraction(1, 5)]
assert [sum(pi[i] * Q8[i][j] / 8 for i in range(2))
        for j in range(2)] == pi
out = [sum(pi[c] * sum(M[d][c]) / 8 for c in range(2))
       for d in range(3)]
assert out == [Fraction(11, 40), Fraction(14, 40),
               Fraction(15, 40)]

energy = [1, 22]
for k in range(2, 10):
    energy.append(26 * energy[-1] - 90 * energy[-2])
state = w0[:]
assert state[0] == energy[0]
checks = 0
for k in range(1, 10):
    state = vec(T, state)
    assert state[0] == energy[k], (k, state[0], energy[k])
    checks += 1

# Independent digit-matrix enumeration of every residue at each depth.
for k in range(1, 9):
    mod = 3 ** k
    R = [0] * mod
    for t in range(mod):
        c0, c1 = 1, 0
        x = t
        for _ in range(k):
            d = x % 3
            x //= 3
            c0, c1 = (c0*M[d][0][0] + c1*M[d][1][0],
                      c0*M[d][0][1] + c1*M[d][1][1])
        R[t] = c0+c1
    assert min(R) > 0
    assert sum(R) == 8 ** k
    z = [1,1,1,1]
    for _ in range(k):
        z=vec(T,z)
    assert sum(v*v for v in R) == z[0]
    checks += len(R)+3

# Direct three-summand enumeration, independent of the carry matrices.
for k in range(1, 5):
    mod=3 ** k
    A=[sum(b*(3**j) for j,b in enumerate(bits))
       for bits in product((0,1),repeat=k)]
    direct=[0]*mod
    for a in A:
        for b in A:
            for c in A:
                direct[(a+b+c)%mod]+=1
    for t in range(mod):
        digits=[]
        x=t
        for j in range(k):
            digits.append(x%3)
            x//=3
        v=[1,0]
        for d in digits:
            v=[v[0]*M[d][0][0]+v[1]*M[d][1][0],
               v[0]*M[d][0][1]+v[1]*M[d][1][1]]
        assert sum(v)==direct[t]
        checks+=1

print('VERIFY_OK', checks, 'finite and exact checks')
print('carry matrices=',M)
print('energy transfer=',T)
print('stationary digit probabilities=',[str(x) for x in out])
print('energy first values=',[1,22,482,10552,230972])
