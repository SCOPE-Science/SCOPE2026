#!/usr/bin/env python3
"""Exact, finite checks for the least-period result; no external dependencies."""
from math import gcd

def branch(p,r):
    for i in range(p):
        j=(r*r-r-1-i*r)%p
        if j<=i:
            return i,j
    raise AssertionError('No branch')

def by_formula(p,a):
    i,j=branch(p,a%p)
    num=a*a-(i+1)*a-(j+1)
    assert num%p==0
    return num//p

def direct_frobenius(p,a):
    # For pn = a Q + R, 0<=R<a, membership is exactly R<=Q.
    upper=(a*a-a-1)//p
    last=-1
    for n in range(upper+1):
        Q,R=divmod(p*n,a)
        if R>Q:
            last=n
    return last

assert all(branch(p,0)==(p-1,p-1) for p in range(2,61))
checks=0
for p in range(2,61):
    for q in range(1,p):
        if p%q==0:
            assert branch(p,0)!=branch(p,q),(p,q)
    for a in range(p+1,3*p+12):
        assert by_formula(p,a)==direct_frobenius(p,a),(p,a)
        checks+=1
print('VERIFY_OK', 'moduli=2..60', 'exact_frobenius_pairs='+str(checks),
      'proper_divisor_branches_distinct=yes', 'independent_membership_test=yes')
