#!/usr/bin/env python3
"""Exact symbolic checks and independent sampling diagnostics for real Grassmannian fourth moments.
Requires sympy and numpy; run: python3 verify.py
"""
import math
import numpy as np
import sympy as sp

n,k=sp.symbols('n k', integer=True, positive=True)
s=k*(n-k)
D=n*(n-3)*(n-2)*(n-1)*(n+1)*(n+2)*(n+4)*(n+6)
A0=s*(n*n+5*n+18)-8*n*n-12*n+24
B=n*(n*n+n+2)-(5*n+6)*s
V=2*s/(n*(n-1)*(n+2))
C22=12*s*A0/D
C4=48*s*B/D

def rising(z,r):
    return sp.rf(z,r)

def beta_mixed(a,b):
    return rising(k/sp.Integer(2),a)*rising((n-k)/sp.Integer(2),b)/rising(n/sp.Integer(2),a+b)

def mixed(a,b):
    # P11=S is beta; conditional P22 is a spherical quadratic form in dimension n-1.
    return sum(sp.binomial(b,j)*rising((k-1)/sp.Integer(2),b-j)*rising(sp.Rational(1,2),j)*beta_mixed(a,j) for j in range(b+1))/rising((n-1)/sp.Integer(2),b)

M1=sp.factor(sum(sp.binomial(4,a)*(-k/n)**(4-a)*beta_mixed(a,0) for a in range(5)))
M2=sp.factor(sum((-1)**b*sp.binomial(4,b)*mixed(4-b,b) for b in range(5)))
p2_1=(n-1)/n
p4_1=sp.factor(((n-1)**4+(n-1))/n**4)
assert sp.factor(M1-(C22*p2_1**2+C4*p4_1))==0
assert sp.factor(M2-(4*C22+2*C4))==0
assert sp.factor(V-2*k*(n-k)/(n*(n-1)*(n+2)))==0
assert sp.factor(B-(n*(n*n+n+2)-(5*n+6)*k*(n-k)))==0
print('SYMBOLIC_TWO_INDEPENDENT_FOURTH_MOMENT_WITNESSES_OK')
# A=diag(1,-1), n=4, k=2 is an exact conditional probability check.
assert M1.subs({n:4,k:2})==sp.Rational(1,80)
assert M2.subs({n:4,k:2})==sp.Rational(8,75)
print('EXACT_BETA_AND_TWO_ROW_CONDITIONAL_INTEGRATION_OK')

# Check the sharp spectral endpoints without assuming their ordering.
factor=sp.factor((C22+C4*sp.Symbol('r'))/V**2)
for nn in range(4,91):
    p=nn//2; q=nn-p
    rmin=sp.Rational(nn,p*q)-sp.Rational(3,nn)
    rmax=sp.Rational(nn*nn-3*nn+3,nn*(nn-1))
    assert rmin<rmax
    vals=[]
    for kk in range(1,nn):
        subs={n:nn,k:kk}; bb=B.subs(subs)
        l=sp.factor(factor.subs('r',rmin).subs(subs)); h=sp.factor(factor.subs('r',rmax).subs(subs))
        assert (h>l)==(bb>0) if bb!=0 else h==l
        assert min(l,h)>=1
        vals.append(sp.sign(bb))
    assert vals[0]>0 and min(vals)<0
print('EXACT_ALL_RANK_SPECTRAL_PHASE_DIAGNOSTICS_OK n=4..90')

# n=2,3 exception from rank-one spherical Dirichlet moments.
for nn,expected in [(2,sp.Rational(3,2)),(3,sp.Rational(15,7))]:
    rr=sp.Rational(1,2) if nn<=3 else None
    fourth=(12+48*rr)/(nn*(nn+2)*(nn+4)*(nn+6))
    second=sp.Rational(2,nn*(nn+2))
    assert sp.factor(fourth/second**2)==expected
print('LOW_DIMENSION_HILBERTIAN_CHECKS_OK')

# Independent seeded Haar projection sampling; this is not a proof.
rng=np.random.default_rng(290730)
for nn,kk in [(4,1),(4,2),(5,2),(7,2),(8,3)]:
    a=rng.standard_normal(nn)
    a-=a.mean()
    count=22000
    g=rng.normal(size=(count,nn,kk))
    Q,R=np.linalg.qr(g)
    # QR sign orientation does not matter for the projected subspace.
    diag=np.einsum('sik,sik->si',Q,Q)
    xx=diag@a
    p2=np.dot(a,a)
    r4=np.sum(a**4)/p2**2
    sub={n:nn,k:kk}
    t2=float(V.subs(sub))*p2
    t4=float((C22+C4*sp.Rational(str(r4))).subs(sub))*p2**2
    obs2=np.mean(xx**2);obs4=np.mean(xx**4)
    assert abs(obs2/t2-1)<0.09, (nn,kk,obs2,t2)
    assert abs(obs4/t4-1)<0.16, (nn,kk,obs4,t4)
print('INDEPENDENT_GAUSSIAN_QR_HAAR_SAMPLING_DIAGNOSTICS_OK 110000')

# Three-variable zero-sum fourth-power identity, used in extremum reduction.
x,y=sp.symbols('x y');z=-x-y
assert sp.expand((x**4+y**4+z**4)-sp.Rational(1,2)*(x*x+y*y+z*z)**2)==0
print('THREE_ROOT_SMOOTHING_IDENTITY_OK')
print('ALL_REAL_GRASSMANNIAN_FOURTH_MOMENT_CHECKS_PASSED')
