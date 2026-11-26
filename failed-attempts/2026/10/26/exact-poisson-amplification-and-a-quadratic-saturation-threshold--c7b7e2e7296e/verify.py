#!/usr/bin/env python3
"""Exact checks for the rectangular rook-graph Poisson endpoint norm.

Standard-library-only verifier. Tests are finite checks; the general statements
are established separately by the spectral and sign arguments in RESULT.md.
"""
from fractions import Fraction as Q
from math import isqrt

checks = 0


def affirm(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)


def kernel(m, n, x, y):
    i, j = x
    k, ell = y
    a = Q(int(i == k)) - Q(1, m)
    b = Q(int(j == ell)) - Q(1, n)
    return (a + b) / (m * n) + a * b / (m + n)


def orbit(m, n):
    z = m*m*n*n*(m+n)
    d = Q(m*m*n*n + m*m*n - m*m + m*n*n - m*n - n*n, z)
    r = Q(-m*m + m*n*n - m*n - n*n, z)
    c = Q(m*m*n - m*m - m*n - n*n, z)
    f = Q(-m*m - m*n - n*n, z)
    return d, r, c, f


def claimed_norm(m, n):
    if m > n: m, n = n, m
    if m == 2 and n == 2: return Q(5, 8)
    if m == 2 and n == 3: return Q(47, 90)
    cnum = m*m*n - m*m - m*n - n*n
    return 2*Q(m-1, m*m) + 2*(m-1)*Q(max(cnum, 0), m*m*n*n*(m+n))


def invert(mat):
    n = len(mat)
    augmented = [[Q(mat[i][j]) for j in range(n)]
                 + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if augmented[i][k]), None)
        affirm(pivot is not None, 'noninvertible M')
        augmented[k], augmented[pivot] = augmented[pivot], augmented[k]
        p = augmented[k][k]
        augmented[k] = [x/p for x in augmented[k]]
        for i in range(n):
            if i != k and augmented[i][k]:
                c = augmented[i][k]
                augmented[i] = [x-c*y for x, y in zip(augmented[i], augmented[k])]
    return [row[n:] for row in augmented]


for m in range(2, 14):
    for n in range(m, 29):
        d, r, c, f = orbit(m, n)
        affirm(r-c == Q(n-m, m*n*(m+n)), ('order',m,n))
        affirm(f < 0 and d > 0, ('sign',m,n))
        affirm(d+(n-1)*r+(m-1)*c+(m-1)*(n-1)*f == 0, ('zero',m,n))
        norm = 2*(d+(n-1)*max(r, 0)+(m-1)*max(c, 0))
        affirm(norm == claimed_norm(m,n), ('norm',m,n,norm,claimed_norm(m,n)))
        if m >= 3:
            affirm(r >= 0, ('row positive',m,n))
        if m >= 4:
            discr = m*m*(m-3)*(m+1)
            cut = (m*(m-1)+isqrt(discr))//2+1
            affirm((c>0)==(n<cut), ('quadratic cutoff',m,n,cut))
        if m <= 8 and n <= 15:
            row_sum = sum(abs(kernel(m,n,(0,0),(i,j)))
                          for i in range(m) for j in range(n))
            affirm(row_sum == norm, ('entrywise sum',m,n))
            affirm(kernel(m,n,(0,0),(0,0)) == d, ('D',m,n))
            affirm(kernel(m,n,(0,0),(0,1)) == r, ('R',m,n))
            affirm(kernel(m,n,(0,0),(1,0)) == c, ('C',m,n))
            affirm(kernel(m,n,(0,0),(1,1)) == f, ('F',m,n))

# Independently invert the full rational matrix L+J/N on selected products.
for m, n in ((2,2),(2,3),(3,3),(3,4),(4,4),(4,5),(5,5)):
    verts = [(i,j) for i in range(m) for j in range(n)]
    N = len(verts)
    L = [[Q((m+n-2) if u==v else
             (-1 if (u[0] == v[0]) != (u[1] == v[1]) else 0))
          for v in verts] for u in verts]
    M = [[L[i][j]+Q(1,N) for j in range(N)] for i in range(N)]
    inv = invert(M)
    for i,u in enumerate(verts):
        for j,v in enumerate(verts):
            affirm(inv[i][j]-Q(1,N)==kernel(m,n,u,v), ('full inverse',m,n,i,j))
    affirm(max(sum(abs(inv[i][j]-Q(1,N)) for j in range(N)) for i in range(N))
           == claimed_norm(m,n), ('full matrix norm',m,n))

for m in range(4, 91):
    discr = m*m*(m-3)*(m+1)
    cut = (m*(m-1)+isqrt(discr))//2+1
    # Check both sides of the exact integer threshold, including far beyond it.
    for n in (m, cut-2, cut-1, cut, cut+1, 2*m*m):
        if n < m: continue
        d, r, c, f = orbit(m, n)
        affirm((c>0)==(n<cut), ('cut exact',m,n))
        affirm((claimed_norm(m,n)==Q(2*(m-1),m*m))==(n>=cut),
               ('plateau exact',m,n))

affirm(claimed_norm(2,2)==Q(5,8),'universal equality')
affirm(claimed_norm(2,3)==Q(47,90),'small prism')
affirm(claimed_norm(2,4)==Q(1,2),'2-by-4 plateau')
affirm(claimed_norm(3,3)==Q(4,9),'3-by-3 plateau')
for m in range(2,200):
    for n in (m,m+1,2*m,3*m,m*m,2*m*m):
        affirm(claimed_norm(m,n)<=Q(5,8),('global upper',m,n))

print('PASS',checks,'exact rational assertions')
