#!/usr/bin/env python3
"""Exact finite checks of the square-root convolution Smith formulas.
Requires Python 3 and SymPy. Exact integer arithmetic throughout.
"""
from collections import Counter
from math import prod
from sympy import Matrix, eye
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

PRIMES = (3, 5, 7, 11, 13, 17, 19)
assertions = 0

def check(statement, context):
    global assertions
    assertions += 1
    if not statement:
        raise AssertionError(context)

def root_matrix(n):
    f = Counter((x * x) % n for x in range(n))
    return Matrix(n, n, lambda a, b: f[(b-a) % n])

def smith_multiset(M):
    S = smith_normal_form(M, domain=ZZ)
    return Counter(abs(S[i, i]) for i in range(M.rows))

def field_adjacency(p):
    squares = {(x*x) % p for x in range(1, p)}
    return Matrix(p, p, lambda a, b: int((b-a) % p in squares))

def rank_mod_p(M, p):
    a = [[int(M[i,j])%p for j in range(M.cols)] for i in range(M.rows)]
    rank = 0
    for c in range(M.cols):
        pivot = next((r for r in range(rank,M.rows) if a[r][c]),None)
        if pivot is None: continue
        a[rank],a[pivot] = a[pivot],a[rank]
        inv = pow(a[rank][c],-1,p)
        a[rank] = [(v*inv)%p for v in a[rank]]
        for r in range(rank+1,M.rows):
            if a[r][c]:
                mult=a[r][c]
                a[r] = [(a[r][j]-mult*a[rank][j])%p for j in range(M.cols)]
        rank+=1
    return rank

for p in PRIMES:
    H=field_adjacency(p)
    A=root_matrix(p)
    check(A==eye(p)+2*H, ('prime-root-reduction',p))
    expected=Counter({1:(p+1)//2, p:(p-3)//2, p*p:1})
    if expected[p]==0: del expected[p]
    check(smith_multiset(A)==expected, ('prime-Smith',p))
    check(rank_mod_p(A,p)==(p+1)//2, ('prime-rank',p))
    check(int(H.det())%p!=0, ('unit-adjacency',p))
    check(abs(int(A.det()))==p**((p+1)//2), ('prime-det',p))

for p in (3,5,7,11,13):
    n=p*p
    R=root_matrix(n)
    H=field_adjacency(p)
    for a in range(n):
        for b in range(n):
            expected=p*int(a==b)+2*int(H[a%p,b%p])
            check(R[a,b]==expected, ('square-lift',p,a,b))
    check(rank_mod_p(R,p)==p, ('prime-square-rank',p))
    if p in (3,5):
        expected=Counter({1:p,p:p*(p-2),p*p:(p+1)//2,p**3:(p-3)//2,p**4:1})
        if expected[p**3]==0: del expected[p**3]
        check(smith_multiset(R)==expected,('prime-square-Smith',p))
    # The claimed determinant is proved by the integral p-by-p coset block decomposition.

print('PASS:',assertions,'exact assertions; seven prime-level SNFs, two prime-square SNFs,',
      'five prime-square entrywise identity/rank tests.')
