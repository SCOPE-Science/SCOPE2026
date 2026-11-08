#!/usr/bin/env python3
"""Exact reproducibility checks for the double-star edge-cost spectral design."""
from fractions import Fraction as Q
from itertools import combinations,product
from math import sqrt
import sympy as sp


def formula(a,b,l,r,z,B=Q(1)):
    l,r,z,B=map(Q,(l,r,z,B))
    n=a+b+2; S=(b+1)*z-a*l+b*r
    if S<0:
        F=a*l*l+b*r*r+(b+1)*z*z+2*b*z*r
        regime='left'; u=F and B/F
        L=u; R=u*(1+z/r); T=u*((b+1)*z+b*r)/z
        f=[-((b+1)*z+b*r)/a,0,z,z+r]
    elif S>n*z:
        F=a*l*l+b*r*r+(a+1)*z*z+2*a*z*l
        regime='right'; u=B/F
        L=u*(1+z/l); R=u; T=u*((a+1)*z+a*l)/z
        f=[-l,0,z,z+((a+1)*z+a*l)/b]
    else:
        mu=S/n
        F=a*l*l+b*r*r+(b+1)*z*z+2*b*z*r-S*S/n
        regime='center'; u=B/F
        L=u*(1+mu/l); R=u*(1+(z-mu)/r)
        T=u*(a*(l+mu)+mu)/z
        f=[-l,0,z,z+r]
    return regime,F,u,L,R,T,f


def verify_case(a,b,l,r,z,B=Q(1)):
    l,r,z,B=map(Q,(l,r,z,B))
    name,F,lam,wl,wr,wc,f=formula(a,b,l,r,z,B)
    n=a+b+2; m=[a,1,1,b]
    assert sum(mi*fi for mi,fi in zip(m,f))==0 if name=='left' else True
    assert a*l*l*wl+b*r*r*wr+z*z*wc==B
    assert all(w>0 for w in [wl,wr,wc])
    # The longitudinal eigenfunction is always centered after subtracting its weighted mean.
    mean=sum(mi*fi for mi,fi in zip(m,f))/n
    vec=sp.Matrix([sp.Rational(fi-mean) for fi in f])
    k=[a*wl,wc,b*wr]
    Qmat=sp.zeros(4)
    for i,wi in enumerate(k):
        Qmat[i,i]+=wi;Qmat[i+1,i+1]+=wi
        Qmat[i,i+1]-=wi;Qmat[i+1,i]-=wi
    D=sp.diag(*m)
    assert Qmat*vec==sp.Rational(lam)*D*vec
    # Exact PSD test of the weighted-quotient spectral lower bound.
    M=Qmat-sp.Rational(lam)*(D-(sp.Matrix(m)*sp.Matrix([m]))/n)
    for size in range(1,5):
        for ix in combinations(range(4),size):
            assert M.extract(ix,ix).det()>=0, (a,b,l,r,z,name,ix)
    assert wl>=lam and wr>=lam
    # Exact supporting embedding variance and edge-cost norms.
    if name=='center':
        S=(b+1)*z-a*l+b*r
        variance=a*l*l+b*r*r+(b+1)*z*z+2*b*z*r-S*S/n
    elif name=='left':
        K=(b+1)*z+b*r
        assert K<a*l
        # a left leaves: axial component -K/a, symmetric transverse polygon.
        variance=a*l*l+b*r*r+(b+1)*z*z+2*b*z*r
    else:
        K=(a+1)*z+a*l
        assert K<b*r
        variance=a*l*l+b*r*r+(a+1)*z*z+2*a*z*l
    assert variance==F and lam*F==B
    assert f[0]<f[1]<f[2]<f[3]
    return name


def main():
    cases=0;counts={'left':0,'center':0,'right':0}
    for a,b in product(range(2,8),repeat=2):
        for l,r,z in [(Q(1),Q(1),Q(1)),(Q(1),Q(2),Q(1)),(Q(2),Q(1),Q(1)),(Q(3),Q(1),Q(2)),(Q(1),Q(3),Q(2)),(Q(1),Q(1),Q(3)),(Q(4),Q(1),Q(1)),(Q(1),Q(4),Q(1)),(Q(2),Q(3),Q(1)),(Q(3),Q(2),Q(1))]:
            reg=verify_case(a,b,l,r,z)
            counts[reg]+=1;cases+=1
    for case in [(2,2,Q(5,2),1,1),(2,2,1,Q(5,2),1),(2,2,1,1,1),(100,2,1,1,1),(2,100,1,1,1),(3,3,1,1,1),(4,2,2,1,1),(2,4,1,2,1)]:
        reg=verify_case(*case)
        counts[reg]+=1;cases+=1
    print('PASS',cases,'exact rational cases',counts,'all principal-minor PSD, eigen equations, budgets and dual witnesses')

if __name__=='__main__': main()
