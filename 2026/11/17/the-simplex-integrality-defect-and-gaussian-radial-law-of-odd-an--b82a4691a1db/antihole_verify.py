#!/usr/bin/env python3
"""Exact finite checks for odd-antihole clique-relaxation cap geometry.

No external packages required. Finite checks corroborate, but do not replace,
the independent all-rank determinant and probabilistic arguments in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def det_bareiss(A):
    M = [list(map(int,row)) for row in A]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n-1):
        if M[k][k] == 0:
            j = next((j for j in range(k+1,n) if M[j][k]),None)
            if j is None: return 0
            M[k],M[j]=M[j],M[k]
            sign=-sign
        piv=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=M[i][j]*piv-M[i][k]*M[k][j]
                assert num % prev==0
                M[i][j]=num//prev
            M[i][k]=0
        prev=piv
    return sign*M[n-1][n-1]

def max_cycle_stable_sets(n):
    m=(n-1)//2
    return [set(S) for S in combinations(range(n),m)
            if all((i+1)%n not in S for i in S)]

def test_one(n):
    m=(n-1)//2
    sets=max_cycle_stable_sets(n)
    check(len(sets)==n, f'number maximum cliques n={n}')
    A=[[int(j in S) for j in range(n)] for S in sets]
    check(abs(det_bareiss(A))==m,f'clique normal determinant n={n}')
    B=[[int(i==j)+int(i==(j+1)%n) for j in range(n)] for i in range(n)]
    check(det_bareiss(B)==2, f'edge incidence determinant n={n}')
    M=[[m*b-1 for b in row] for row in B]
    check(det_bareiss(M)==-m**(n-1), f'volume determinant n={n}')
    for j in range(n):
        v={j,(j+1)%n}
        check(sum(len(v&S)==1 for S in sets)==n-1, f'pair clique incidence {n},{j}')
        check(sum(len(v&S)==0 for S in sets)==1, f'exception clique {n},{j}')
    check(F(abs(det_bareiss(M)),m**n*factorial(n)) == F(1,m*factorial(n)),f'volume {n}')
    R=[[F(B[i][j])-F(1,m) for j in range(n)] for i in range(n)]
    sum_sq=sum(sum(r*r for r in row) for row in R)
    sum_col=[sum(R[i][j] for j in range(n)) for i in range(n)]
    exact_moment=(sum_sq+sum(t*t for t in sum_col))/((n+1)*(n+2))
    formula=F(n,(n+1)*(n+2))*(2-F(2,m)+F(2,m*m))
    check(exact_moment==formula, f'radial mean {n}')
    print(f'n={n:2} clique_det_abs={m} cap_vol={F(1,m*factorial(n))} expected_radial_mean={formula}')

for n in (5,7,9,11,13): test_one(n)
# E~Exp(1), A=E+F with independent E,F. Mixed moment identities
EY=6; EY2=120; varY=EY2-EY**2
# E[(E+F)^2*(F+G)^2] = E[(F^2+2F+2)^2] = 76
lag=76-EY**2
# E[E*(E+F)^2] = 6+4+2 = 12; minus 6 = 6
cov=12-6
V=varY+2*lag; C=2*cov
check((varY,lag,V,C)==(84,40,164,12),'1-dependent asymptotic covariance')
check(144+164-24*12==20,'delta-method Gaussian variance')
print(f'PASS {checks} exact checks; asymptotic variance 20, finite calculations only.')
