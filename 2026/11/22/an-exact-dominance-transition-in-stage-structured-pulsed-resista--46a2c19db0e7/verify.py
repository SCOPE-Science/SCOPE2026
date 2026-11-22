"""Standalone checks of a two-stage pulsed genotype-selection model.

Run with: python3 verify.py
No dependencies outside the Python standard library.
"""
from fractions import Fraction as F
from math import exp, sqrt, log, isclose

def pair_matvec(M, v):
    return [M[i][0]*v[0]+M[i][1]*v[1] for i in range(2)]

def perron(M):
    a,b=M[0]
    c,d=M[1]
    lam=(a+d+sqrt((a-d)**2+4*b*c))/2
    v=[b,lam-a]
    z=sum(v)
    v=[t/z for t in v]
    ell=[c,lam-a]
    z=sum(ell[i]*v[i] for i in range(2))
    ell=[t/z for t in ell]
    assert all(t>0 for t in v+ell)
    for i in range(2):
        assert abs(pair_matvec(M,v)[i]-lam*v[i])<1e-12
    return lam,v,ell

def pulse(z,w,E,d,s,h,lam):
    Z=pair_matvec(E,z)
    W=pair_matvec(E,w)
    q=[W[i]/(Z[i]+W[i]) for i in range(2)]
    zn=[d[i]*Z[i]*(1-h*s[i]*q[i])/lam for i in range(2)]
    wn=[d[i]*W[i]*(1-h*s[i]-(1-h)*s[i]*q[i])/lam for i in range(2)]
    return zn,wn

# Verify allele-density pulse identities by independent Hardy--Weinberg formula.
for q in [F(1,7),F(2,5),F(9,10)]:
    y=1-q
    for h in [F(0),F(1,3),F(1)]:
        s=F(1,2); d=F(9,10)
        sus_homo=d*(1-s)
        hetero=d*(1-h*s)
        res_homo=d
        mean=q*q*sus_homo+2*q*y*hetero+y*y*res_homo
        res_density=y*(y*res_homo+q*hetero)
        sus_density=q*(q*sus_homo+y*hetero)
        assert mean==res_density+sus_density
        assert res_density==d*y*(1-h*s*q)
        assert sus_density==d*q*(1-h*s-(1-h)*s*q)

# A = [[-2,2],[1,-1]] has eigenvalues 0,-3, so E = exp(A)
c=(1-exp(-3))/3
E=[[1-2*c,2*c],[c,1-c]]
d=[.9,.7]; s=[.5,.25]
M=[[d[i]*E[i][j] for j in range(2)] for i in range(2)]
lam,v,ell=perron(M)
S=sum(ell[i]*v[i]*s[i] for i in range(2))
expected=1/S
assert 2.8<expected<3.

z0=[.4,2.1]; w0=[1.6,.9]
for h,N in [(0.,30000),(.3,500)]:
    z=z0[:]; w=w0[:]
    for k in range(1,N+1):
        z,w=pulse(z,w,E,d,s,h,lam)
    q=[w[i]/(z[i]+w[i]) for i in range(2)]
    if h==0:
        assert all(abs(N*qi/expected-1)<.001 for qi in q), (q,expected)
        print('h=0, k=30000, k*q:', [N*qi for qi in q])
        print('Perron-selection coefficient S=',S,' predicted limit=',expected)
    else:
        Mh=[[(1-h*s[i])*M[i][j] for j in range(2)] for i in range(2)]
        lh,*_=perron(Mh)
        predicted=log(lh/lam)
        observed=[log(qi)/N for qi in q]
        assert all(abs(ri-predicted)<.015 for ri in observed),(observed,predicted)
        assert lh<lam
        print('h=0.3, asymptotic log(rate) predicted=',predicted,' observed=',observed)
print('All checks passed; finite iterations test formulas but do not establish limits.')
