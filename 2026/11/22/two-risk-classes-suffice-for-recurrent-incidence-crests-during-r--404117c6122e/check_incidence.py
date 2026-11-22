#!/usr/bin/env python3
"""Exact-rational sign certificates for a two-risk SIR incidence example.

No external dependencies. The infinite assertions are proved in RESULT.md;
this file checks the finite rational inequalities used in that proof.
"""
from fractions import Fraction as Q

S0=Q(999,1000)
I0=Q(1,1000)
P=Q(1,12)
C=Q(1,2)
K=20


def log_interval(r, terms=12):
    """Prove log(r) in [lower,upper] using positive atanh series."""
    assert r >= 1
    if r == 1:
        return Q(0),Q(0)
    z=(r-1)/(r+1)
    assert 0<z<1
    lower=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    remainder=2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return lower, lower+remainder


def values(r):
    """Return rigorous bounds for prevalence I, its dI/dx, and incidence derivative."""
    u=1/r
    slow=S0*(1-P)*u
    fast=S0*P*u**K
    a=slow+K*fast
    b=slow+K*K*fast
    assert b>0
    ell,elu=log_interval(r)
    # I(x) = 1 - slow - fast - (1/2)log(r)
    ileft=1-slow-fast-C*elu
    iright=1-slow-fast-C*ell
    # F(x) = A(A-c) - I(x)B ; dJ/dx = beta F
    fleft=a*(a-C)-iright*b
    fright=a*(a-C)-ileft*b
    return (ileft,iright),(fleft,fright),a,b,(ell,elu)

rvals=[Q(1),Q(9,8),Q(5,4),Q(3,2)]
expected=[1,-1,1,-1]
for r,sgn in zip(rvals,expected):
    ib,fb,a,b,lb=values(r)
    assert ib[0]>0 and ib[1]>0, (r,'positive I')
    if sgn==1:
        assert fb[0]>0,(r,'positive F')
    else:
        assert fb[1]<0,(r,'negative F')
    print('r=',r,'x=ln(r)', 'I in', [float(i) for i in ib],
          'F in', [float(v) for v in fb],
          'A=', float(a), 'sign',sgn)
assert values(Q(3,2))[2]>C
assert min(values(r)[0][0] for r in rvals)>0
# Interval verification of positivity, analytically guaranteed by monotone I'
# on the whole witnessed segment; these statements document endpoint inputs.
print('PASS: four exact derivative-sign certificates and rising prevalence endpoint.')
