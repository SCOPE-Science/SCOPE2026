#!/usr/bin/env python3
"""Independent finite-symbol verification of deterministic NEC fixed states."""
from math import comb
ORDER = [1, 3, 2, 6, 4, 5]

def valid(left, right):
    for r in range(3):
        a = (left >> r) & 1
        north = (left >> ((r + 1) % 3)) & 1
        east = (right >> r) & 1
        if ((a & north) | (a & east) | (north & east)) != a:
            return False
    return True

A = [[int(valid(a,b)) for b in range(8)] for a in range(8)]
assert all(A[a][b] == 1 for a in (0,7) for b in (0,7))
assert all(A[a][b] == 0 for a in ORDER for b in (0,7))
assert all(A[a][b] == (b in (a,ORDER[(j+1)%6])) for j,a in enumerate(ORDER) for b in ORDER)
assert all(A[a][b] == 1 for a in (0,7) for b in ORDER)

for n in range(1,21):
    M = [[int(i==j) for j in range(8)] for i in range(8)]
    for _ in range(n):
        M = [[sum(M[i][k]*A[k][j] for k in range(8)) for j in range(8)] for i in range(8)]
    trace = sum(M[i][i] for i in range(8))
    closed = 2**n+6*sum(comb(n,6*j) for j in range(n//6+1))
    assert trace == closed,(n,trace,closed)
    if 3<=n<=12:
        print(f'n={n} fixed={trace} uniform={2**n} mixed={trace-2**n}')
print('Eight-symbol edges:',sum(map(sum,A)))
print('Allowed fixed-state components: complete two-symbol digraph; 6-cycle with self-loops')
print('PASS: all 64 local pairs and closed-walk counts through n=20')
