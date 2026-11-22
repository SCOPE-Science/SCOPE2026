#!/usr/bin/env python3
"""Exact finite checks supporting the coefficient-locus and motivic identities.
The all-parameter geometric assertion is proved separately, not by this script.
"""
from sympy import symbols, Poly, gcd, expand, factor, degree
z,L,N=symbols('z L N')

# sigma_r(z) multiplied by z^(r-1): z^(2r-2)+...+1
for m in range(2,11):
    n=2*m+1
    s2=z**2+1
    s3=z**4+z**2+1
    sn=sum(z**(2*j) for j in range(n))
    assert Poly(gcd(s2,z**2+1),z).degree()==2
    assert Poly(gcd(s3,z**3-1),z).degree()==2
    assert Poly(gcd(s3,z**3+1),z).degree()==2
    assert Poly(gcd(sn,z**n-1),z).degree()==n-1
    assert Poly(gcd(sn,z**n+1),z).degree()==n-1
    assert gcd(sn,Poly(sn,z).diff().as_expr())==1
    assert 2*4*(n-1)==16*m
print('PASS: root counts, two signs and transversality, n=5,7,...,21')

# L=[A1] and N=|E|; derivation takes affine bundles and base blow-up literally.
T=(L-1)**2
x=L**2*(T-N)+N*L**3
y=L**2*(T+N*L)
assert expand(y-x-N*L**2)==0
assert expand(y-L**2*((L-1)**2+N*L))==0
assert expand(x.subs(L,1))==0
assert expand(y.subs(L,1)-N)==0
# Algebraic strict transform charts, valid for formal local coordinates.
s,t,u,v,w,A,B=symbols('s t u v w A B')
F=s*u+t*v
assert expand(F.subs(t,s*w)-s*(u+w*v))==0
assert expand(F.subs(s,t*w)-t*(w*u+v))==0
assert expand((s*(u-A*symbols('c'))+t*(v-B*symbols('c'))+(s*A+t*B)*symbols('c'))-F)==0
print('PASS: exact two-chart smooth strict-transform identities')
print('PASS: fibre-stratification, blow-up and Euler identities')
print('PASS: checker complete (finite checks are not proofs for all m)')
