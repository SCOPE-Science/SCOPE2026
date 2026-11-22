#!/usr/bin/env python3
"""Exact finite reproducibility checks for two Narayana residue sections."""
from collections import Counter

def matmul(A, B):
    return [[sum(A[i][h] * B[h][j] for h in range(3)) for j in range(3)] for i in range(3)]

def matpow(A, n):
    out = [[int(i == j) for j in range(3)] for i in range(3)]
    while n:
        if n & 1:
            out = matmul(out, A)
        A = matmul(A, A)
        n >>= 1
    return out

def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(3)) for i in range(3)]

def v2(n):
    assert n != 0
    return (abs(n) & -abs(n)).bit_length() - 1

def recurrence(N, mod=None):
    vals = [1, 1, 1]
    for n in range(3, N):
        vals.append(vals[n-1] + vals[n-3])
        if mod is not None:
            vals[-1] %= mod
    return vals[:N]

M = [[0, 1, 0], [0, 0, 1], [1, 0, 1]]
B = [[1, 1, 2], [2, 1, 3], [3, 2, 4]]
C = [[10, 7, 15], [15, 10, 22], [22, 15, 32]]
I = [[int(i == j) for j in range(3)] for i in range(3)]
assert matpow(M, 7) == [[I[i][j] + 2*B[i][j] for j in range(3)] for i in range(3)]
assert matpow(M, 14) == [[I[i][j] + 4*C[i][j] for j in range(3)] for i in range(3)]
assert C == [[B[i][j] + matmul(B, B)[i][j] for j in range(3)] for i in range(3)]
v = [1, 1, 1]
expected = [(1,0,0),(1,0,1),(1,1,1),(2,1,1),(3,1,0),(4,0,1),(6,1,0)]
for j in range(7):
    assert (v[0], matvec(B,v)[0]%2, matvec(C,v)[0]%2) == expected[j]
    v = matvec(M,v)

assert [x%2 for x in recurrence(7)] == [1,1,1,0,1,0,0]
for k in range(1, 13):
    q = 1 << k
    half = q // 2
    period = 7 * half
    vals = recurrence(2*period + 12, q)
    assert vals[:period] == vals[period:2*period]
    # The modulus-two projection forces the period to be a multiple of seven.
    # A candidate 7*h with 0<h<2^(k-1) must fail at index two.
    for h in range(1,half):
        assert vals[7*h+2] != vals[2]
    for j, parity in [(2,1),(3,0)]:
        selections = [vals[7*t+j] for t in range(half)]
        assert len(set(selections)) == half
        assert set(selections) == set(range(parity,q,2))
    if k < 10:
        sample_t = min(half, 96)
        unbounded = recurrence(7*sample_t+4)
        for j in (2,3):
            for s in range(sample_t):
                for t in range(s+1,sample_t):
                    assert v2(unbounded[7*t+j]-unbounded[7*s+j]) == 1+v2(t-s)
for j in (0,1,4,5,6):
    a = recurrence(7*2+j+1)
    if expected[j][1] == 0:
        assert v2(a[j+7]-a[j]) >= 2
    else:
        assert expected[j][2] == 0
        assert v2(a[j+14]-a[j]) >= 3
print("CHECK_OK")
