#!/usr/bin/env python3
"""Exact-rational diagnostic checker for the sharp Krawtchouk two-level theorem.
The analytic all-dimensional proof is given in RESULT.md; finite checks are not a substitute.
"""
from fractions import Fraction as F
from math import comb

def mom(n,k):
    return sum(F(comb(n,j)*(n-2*j)**k,2**n) for j in range(n+1))

def vals(n):
    a=F(3*n-2,n)
    c=F(5*n-8,n)
    d=F(15*n*n-63*n+68,n*(n-1))
    m=F(15*n*n-33*n+20,n*(n+1))
    return a,c,d,m

for n in range(2,15):
    a,c,d,m=vals(n)
    mu=lambda k: mom(n,k)
    v=F(n*(n-1),2)
    assert mu(2)==n
    assert mu(4)==n*n*a
    assert mu(6)==15*n**3-30*n*n+16*n
    assert mu(8)==105*n**4-420*n**3+588*n*n-272*n
    assert mu(4)-n*mu(2)==2*n*(n-1)
    assert (mu(6)-2*n*mu(4)+n*n*mu(2))/4==n*v*c
    assert (mu(8)-4*n*mu(6)+6*n*n*mu(4)-4*n**3*mu(2)+n**4)/16==v*v*d
    assert F(n+n*(n-1),2)>0
    r=F(n-1,n+1)
    curv=F(2*(n+1)*(6*n-11),n*(n-1))
    assert curv>0 and 0<r<1
    assert a*(1-r)**2+6*c*r*(1-r)+d*r*r==m
    for i in range(13):
        z=F(i,12)
        k=a*(1-z)**2+6*c*z*(1-z)+d*z*z
        assert m-k==curv*(z-r)**2
    # Exact equality of raw coefficients for maximum: f=S+Q.
    assert F(v,n+v)==r
    assert 9*c*c>a*d
    assert (n==3 and a==d) or (n==2 and d<a) or (n>=4 and a<d)
    # Direct raw fourth moment independent of normalized variables.
    e_s4q4=mu(4)+F(6)*(mu(6)-2*n*mu(4)+n*n*mu(2))/4 + (mu(8)-4*n*mu(6)+6*n*n*mu(4)-4*n**3*mu(2)+n**4)/16
    assert e_s4q4==m*(n+v)**2
    # beta^2 exactly and dimension-three maximum.
    beta_sq=9*c*c/(a*d)
    assert beta_sq<=9 and beta_sq>1
    if n>=4:
        ap,cp,dp,_=vals(n-1)
        assert beta_sq<9*cp*cp/(ap*dp)
print('EXACT_RADEMACHER_MOMENTS_N_2_TO_14_OK')
print('EXACT_TWO_MODE_QUARTIC_DEFICIT_AND_EQUALITY_N_2_TO_14_OK')
print('EXACT_BETA_MONOTONICITY_SAMPLED_N_3_TO_14_OK')
print('ALL_RADIAL_KRAWTCHOUK_CHECKS_PASSED')
