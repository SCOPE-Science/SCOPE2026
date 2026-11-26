#!/usr/bin/env python3
"""Independent integer checks of the odd-modulus digit-parity identity.

Uses only the Python standard library. The matrix checks are finite tests;
the proof for all odd moduli and all arguments is algebraic.
"""
from math import comb

def matmul(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for k, v in enumerate(a[i]):
            if v:
                for j, w in enumerate(b[k]):
                    c[i][j] += v * w
    return c

def matrix_test(n):
    assert n >= 3 and n % 2 == 1
    b = [[0 if (i+j) % n == n-1 else (-1) ** ((i+j) % n)
          for j in range(n)] for i in range(n)]
    square = matmul(b, b)
    m = (n-1)//2
    # Horner evaluation of \sum_{j=0}^m (-1)^j C(n,2j+1) (B^2)^j.
    q = [[int(i == j) * ((-1)**m) * comb(n, 2*m+1)
          for j in range(n)] for i in range(n)]
    for deg in range(m-1, -1, -1):
        q = matmul(q, square)
        c = (-1)**deg * comb(n, 2*deg+1)
        for i in range(n):
            q[i][i] += c
    assert all(entry == 1 for row in q for entry in row), n

def parity_digit_sum(u, b):
    parity = 0
    while u:
        u, d = divmod(u, b)
        parity ^= d & 1
    return -1 if parity else 1

def direct_test(n, xmax):
    b = n - 1
    m = (n-1)//2
    cutoffs = set()
    for x in range(1, xmax+1):
        for j in range(m+1):
            cutoffs.add((b**(2*j))*x)
    max_cutoff = max(cutoffs)
    partial = 0
    sums = {}
    for i in range(max_cutoff):
        if i % n == 0:
            partial += parity_digit_sum(i,b)
        if i+1 in cutoffs:
            sums[i+1] = partial
    for x in range(1,xmax+1):
        lhs = sum((-1)**j * comb(n,2*j+1) * sums[(b**(2*j))*x]
                  for j in range(m+1))
        rhs = sum(parity_digit_sum(t,b) for t in range(x))
        assert lhs == rhs, (n,x,lhs,rhs)
    return max_cutoff

if __name__ == '__main__':
    for n in range(3, 42, 2):
        matrix_test(n)
    checked = [(n, x, direct_test(n,x)) for n,x in [(3,120),(5,40),(7,12)]]
    print('VERIFY_OK: all odd transfer matrices n=3..41; direct digit tests:', checked)
