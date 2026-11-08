#!/usr/bin/env python3
"""Independent exact and numerical checks for the odd-age geometric Leslie spectrum.
The analytical proof is in RESULT.md; these finite tests do not replace it.
"""
from fractions import Fraction as Q
import numpy as np
from math import isclose

checks=0

def assert_ok(condition, context):
    global checks
    if not condition: raise AssertionError(context)
    checks += 1

def poly(x,n,p,a):
    return x**n+a*sum(p**j*x**(n-1-j) for j in range(n))

def roots(n,p,a):
    coeffs=[1.0]+[float(a*p**j) for j in range(n)]
    return np.roots(coeffs)

for n in (3,5,7,9,11,13):
    for p in (Q(1,5),Q(1,2),Q(4,5),Q(19,20)):
        k=sum(p**j for j in range(n))
        a_plus=(1+p)/(1+p**n)
        a_minus=-1/k
        assert_ok(poly(Q(-1),n,p,a_plus)==0,(n,p,'flip'))
        assert_ok(poly(Q(1),n,p,a_minus)==0,(n,p,'invasion'))
        assert_ok((a_plus-p)+(a_plus*p**n)==1,(n,p,'factorization'))
        assert_ok(0<a_plus-p<1,(n,p,'strict gap'))
        assert_ok(a_minus<0<a_plus,(n,p,'phase order'))
        for a in (a_minus+Q(1,4)*(-a_minus), Q(0), a_plus*Q(1,5), a_plus*Q(4,5)):
            z=roots(n,p,a)
            assert_ok(max(abs(z))<1-1.e-7,(n,p,a,'stable',z))
        for a in (a_minus*Q(5,4), a_plus*Q(5,4)):
            z=roots(n,p,a)
            assert_ok(max(abs(z))>1+1.e-7,(n,p,a,'unstable',z))
        z=roots(n,p,a_plus)
        assert_ok(sum(abs(zi+1)<1e-6 for zi in z)==1,(n,p,'simple flip'))
        assert_ok(all(abs(zi)<1-1e-6 for zi in z if abs(zi+1)>1e-6),(n,p,'rest stable'))
        # Exact derivative of crossing eigenvalue from Q=(z-p)P(z):
        b=a_plus-p
        slope=-(1+p**n)/(1+n*(1-b))
        assert_ok(slope<0,(n,p,'outward derivative'))
        assert_ok(poly(Q(-1),n,p,a_plus+Q(1,10))>0,(n,p,'beyond flip sign'))

for n,p in ((7,Q(4,5)),(3,Q(4,5)),(5,Q(4,5))):
    B=1+sum(p**j for j in range(n))*(1+p)/(1+p**n)
    assert_ok(B==2*(1-p**(n+1))/((1-p)*(1+p**n)),(n,p,'population threshold'))
    if n==7:
        assert_ok(isclose(float(B),6.8795,abs_tol=6e-5),('published numerical example',B))
    for gamma in (Q(0),Q(-1,10),Q(-1,5),Q(-1,2)):
        den=1+gamma*B
        if den>0:
            x=B/den
            a=((1+gamma)*x-1)/(sum(p**j for j in range(n))*(1-gamma*x))
            assert_ok(a==(1+p)/(1+p**n),(n,p,gamma,'biological threshold'))

print(f'PASS {checks} checks: exact polynomial identities, boundary and example, sampled root locations')
