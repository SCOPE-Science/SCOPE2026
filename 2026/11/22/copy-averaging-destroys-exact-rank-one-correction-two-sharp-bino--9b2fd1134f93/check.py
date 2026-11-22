"""Reproducible finite and asymptotic checks for an exact two-mode preconditioner model.

Run with python3 check.py. Python stdlib is sufficient.
The all-copy and asymptotic conclusions are proved analytically, not by finite tests.
"""
from fractions import Fraction as F
from math import comb, factorial, atan, sqrt, pi, exp
from itertools import product
import random


def risk_sum(D, u, delta, alpha=F(1, 2)):
    """Exact multinomial sum over four programming outcomes."""
    u, delta, alpha = F(u), F(delta), F(alpha)
    probs = (u*(1+delta)/2, u*(1-delta)/2,
             (1-u)*(1+delta)/2, (1-u)*(1-delta)/2)
    ans = F(0)
    for a in range(D+1):
        for b in range(D-a+1):
            for c in range(D-a-b+1):
                d = D-a-b-c
                ns = (a,b,c,d)
                w = F(factorial(D),factorial(a)*factorial(b)*factorial(c)*factorial(d))
                for m,p in zip(ns,probs): w *= p**m
                ans += w * min((a-b)**2, (c-d)**2)
    return alpha**2 * ans / D**2


def risk_brute(D,u,delta,alpha=F(1,2)):
    """Independent enumeration of sequences for small D."""
    u,delta,alpha=F(u),F(delta),F(alpha)
    probs=(u*(1+delta)/2,u*(1-delta)/2,(1-u)*(1+delta)/2,(1-u)*(1-delta)/2)
    ret=F(0)
    for words in product(range(4),repeat=D):
        s1=sum(1 if x==0 else -1 if x==1 else 0 for x in words)
        s2=sum(1 if x==2 else -1 if x==3 else 0 for x in words)
        mass=F(1)
        for x in words: mass*=probs[x]
        ret+=mass*min(s1*s1,s2*s2)
    return alpha**2*ret/D**2


def unsigned_binomial(D,u,alpha=F(1,2)):
    u,alpha=F(u),F(alpha)
    return alpha**2*sum(F(comb(D,k))*u**k*(1-u)**(D-k)*min(k,D-k)**2 for k in range(D+1))/D**2


def unclipped_risk(D,u,delta,alpha=F(1,2)):
    u,delta,alpha=F(u),F(delta),F(alpha)
    c=delta**2*(u**2+(1-u)**2)
    return alpha**2*(c+(1-c)/D)


def simple_walk_abs(D):
    """Exact first absolute moment of a D-step fair simple walk."""
    if D % 2 == 0:
        return F(D * comb(D,D//2),2**D)
    return F((D+1)*comb(D,(D-1)//2),2**D)


def balanced_centered(D,alpha=F(1,2)):
    alpha=F(alpha)
    m=simple_walk_abs(D)
    return alpha**2*(D-m*m)/(2*D*D)


def balanced_biased(D,alpha=F(1,2)):
    alpha=F(alpha)
    m=simple_walk_abs(D)
    return alpha**2*(F(1,4)+F(1,4*D)-m/F(2*D))


def balanced_abs(D):
    if D%2==0:
        m=D//2
        return F(m*comb(2*m,m),4**m)
    m=(D-1)//2
    return F((m+1)*comb(2*m+1,m),2**(2*m+1))


def centered_constant(u):
    u=float(u); v=1-u
    t=atan(sqrt(u/v))
    return u+2*(v-u)*t/pi-2*sqrt(u*v)/pi


def run():
    assertions=0
    us=[F(1,5),F(1,3),F(1,2),F(3,4)]
    ds=[F(-1),F(-1,2),F(0),F(1,3),F(1)]
    for D in range(1,7):
        for u in us:
            for delta in ds:
                r=risk_sum(D,u,delta)
                assert r==risk_brute(D,u,delta)
                assertions+=1
                assert F(0)<=r<=unclipped_risk(D,u,delta)
                assertions+=1
                if D==1: assert r==0; assertions+=1
                if D==2: assert r==F(1,2)**2*u*(1-u)/2; assertions+=1
                if abs(delta)==1:
                    assert r==unsigned_binomial(D,u)
                    assertions+=1
    for D in range(1,19):
        # The centered law follows from two independent rotated random walks.
        assert risk_sum(D,F(1,2),F(0),alpha=F(1))==balanced_centered(D,alpha=1)
        assertions+=1
        assert unsigned_binomial(D,F(1,2),alpha=F(1))==balanced_biased(D,alpha=1)
        assertions+=1
    for D in range(1,91):
        u=F(1,2)
        r=unsigned_binomial(D,u,alpha=F(1))
        rhs=F(1,4)+F(1,4*D)-balanced_abs(D)/D
        assert r==rhs; assertions+=1
        assert 0<=r<F(1,4); assertions+=1
    # Cross-check spectral projection with arbitrary unit vectors on 2x2 diagonal errors.
    import math
    for s1,s2 in [(F(1,3),F(2,3)),(F(-4,5),F(1,5)),(F(0),F(1,2)),(F(1,2),F(-1,2))]:
        minrisk=float(min(s1*s1,s2*s2))
        assert abs((float(s1*s1+s2*s2)-max(float(s1*s1),float(s2*s2)))-minrisk)<1e-13
        assertions+=1
        for j in range(501):
            t=math.pi*j/1000
            x,y=math.cos(t),math.sin(t)
            captured=(x*float(s1))**2+(y*float(s2))**2
            residual=float(s1*s1+s2*s2)-captured
            assert residual>=minrisk-1e-12
            assertions+=1
    # Independently check the Gaussian limit constant via a deterministic quadrature.
    for u in [0.1,0.2,0.5,0.77,0.9]:
        N=20000
        integ=sum(min(u*math.cos((j+.5)*math.pi/(2*N))**2,(1-u)*math.sin((j+.5)*math.pi/(2*N))**2) for j in range(N))
        numerical=4*integ/N/2  # 4/pi * integral over [0,pi/2]
        assert abs(centered_constant(u)-numerical)<1e-8, (u, centered_constant(u),numerical)
        assertions+=1
    print('PASS',assertions,'assertions; risk D=2, u=1/2, alpha=1:',unsigned_binomial(2,F(1,2),alpha=1))
    print('Centered asymptotic constant u=1/2:',centered_constant(0.5),'= 1/2 - 1/pi')
    print('Balanced centered risks D=1...8:',[str(balanced_centered(D,alpha=1)) for D in range(1,9)])
    print('Balanced biased risks D=1...8:',[str(unsigned_binomial(D,F(1,2),alpha=1)) for D in range(1,9)])

if __name__=='__main__':
    run()
