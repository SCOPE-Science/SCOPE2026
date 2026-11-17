#!/usr/bin/env python3
"""Exact rational checks of Grassmann first-harmonic fourth-moment formulas."""
from fractions import Fraction as Q
from math import comb

def rise(x, m):
    z = Q(1)
    for j in range(m): z *= x+j
    return z

def bmix(n, k, a, b):
    """E[Z^a (1-Z)^b] where Z~Beta(k/2,(n-k)/2)."""
    return rise(Q(k,2),a)*rise(Q(n-k,2),b)/rise(Q(n,2),a+b)

def zw(n,k,a,b):
    """E[Z^a W^b] from orthogonal-row conditional Dirichlet moments."""
    return sum((Q(comb(b,j)) * rise(Q(k-1,2),b-j) * rise(Q(1,2),j)
                * bmix(n,k,a,j)/rise(Q(n-1,2),b)) for j in range(b+1))

def moment_z(n,k):
    mu=Q(k,n)
    return sum(Q(comb(4,j))*(-mu)**(4-j)*bmix(n,k,j,0) for j in range(5))

def moment_diff(n,k):
    return sum(Q(comb(4,j))*(-1)**j*zw(n,k,4-j,j) for j in range(5))

def formulas(n,k):
    t=k*(n-k)
    D=n*(n-3)*(n-2)*(n-1)*(n+1)*(n+2)*(n+4)*(n+6)
    v=Q(2*t,n*(n-1)*(n+2))
    a=Q(12*t*((n*n+5*n+18)*t-8*n*n-12*n+24),D)
    b=Q(48*t*(n*(n*n+n+2)-(5*n+6)*t),D)
    return v,a,b

count=0
for n in range(4,23,2):
    for k in range(1,n):
        v,a,b=formulas(n,k)
        e1=Q(n-1,n); e2=Q((n-1)*(n*n-3*n+3),n**3)
        assert moment_z(n,k) == a*e1**2+b*e2, (n,k,'rankone')
        assert moment_diff(n,k) == 4*a+2*b, (n,k,'tworow')
        assert b == 0 if k*(n-k)==Q(n*(n*n+n+2),5*n+6) else b!=0
        assert b>0 if k*(n-k)<Q(n*(n*n+n+2),5*n+6) else b<=0
        count+=1
print('EXACT_GRASSMANN_BETA_DIRICHLET_MOMENTS_PASSED',count)
for n in range(4,23,2):
    from itertools import combinations_with_replacement
    for co in combinations_with_replacement(range(-3,4),n-1):
        eig=(*co,-sum(co)); s2=sum(x*x for x in eig)
        if not s2:continue
        ratio=Q(sum(x**4 for x in eig),s2*s2)
        assert Q(1,n)<=ratio<=Q(n*n-3*n+3,n*(n-1)),(n,eig)
        if n>=10:break
print('RATIONAL_EIGENVALUE_RATIO_BOUNDS_PASSED')
print('ALL_GRASSMANN_FIRST_HARMONIC_CHECKS_PASSED')
