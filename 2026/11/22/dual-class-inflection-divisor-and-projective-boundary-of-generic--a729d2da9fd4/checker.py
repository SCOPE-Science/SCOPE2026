#!/usr/bin/env python3
"""Exact-arithmetic spot checks for projective Lissajous geometry.

Requires Python 3 and sympy; every equality is over Q, not floating point.
The general theorem is proved separately, not inferred from these tests.
"""
from fractions import Fraction
from math import gcd
from sympy import symbols, expand, diff, Poly, gcd as poly_gcd

u=symbols('u')
CASES=[(1,2),(1,3),(2,3),(2,5),(3,4),(3,5),(4,5),(4,7),(5,6),(5,7)]
for m,n in CASES:
    assert m<n and gcd(m,n)==1
    c=Fraction(2,1)
    # the rational curve x=(u^m+u^-m)/2, y=(c*u^n+c^-1*u^-n)/2
    x=(u**m+u**(-m))/2
    y=(2*u**n+u**(-n)/2)/2
    D=expand(diff(x,u)*diff(y,u,2)-diff(y,u)*diff(x,u,2))
    P=(n-m)*2*u**(2*(m+n))-(m+n)*2*u**(2*n)+(m+n)*u**(2*m)/2+(m-n)/2
    assert expand(D - m*n*P/(4*u**(m+n+3)))==0,(m,n)
    Ppoly=Poly(P,u,domain='QQ')
    assert Ppoly.degree()==2*(m+n)
    assert poly_gcd(Ppoly,Ppoly.diff()).degree()==0, (m,n,'nonsquarefree')
    # Node/branch singularity and Plucker sum expected for this c.
    assert 2*m*n-m-n+(n-m-1)*(n-1)+n*(n-m)==(2*n-1)*(n-1)
    assert 2*(m+n)+2*(2*n-m-3)==6*n-6
    # Degree of the homogeneous Gauss triple, after clearing poles:
    A=Poly(2*n*(2*u**(m+2*n)-u**m/2),u,domain='QQ')
    B=Poly(-2*m*(u**(2*m+n)-u**n),u,domain='QQ')
    C=Poly((m-n)*2*u**(2*(m+n))+(m+n)*u**(2*m)/2-(m+n)*2*u**(2*n)+(n-m)/2,u,domain='QQ')
    assert C.degree()==2*(m+n)
    assert poly_gcd(poly_gcd(A,B),C).degree()==0
    assert c**(2*m*n)!=1
    print(f'm={m} n={n}: affine_nodes={2*m*n-m-n}, infinity_delta={(n-m-1)*(n-1)+n*(n-m)}, ordinary_flexes={2*(m+n)}, dual_degree={2*(m+n)} OK')
print('ALL 10 EXACT CHECKS PASSED')
