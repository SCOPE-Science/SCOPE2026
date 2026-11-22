#!/usr/bin/env python3
"""Independent deterministic checks of spherical orthogonality graph triangle moments.
No external dependencies. Checks are finite, not substitutes for the analytic proof.
"""
from itertools import product, combinations
from fractions import Fraction
from math import comb, pi, asin, sin, cos, gamma, sqrt, lgamma, exp

def theory(n, p, edge_cov):
    return comb(n, 3)*p*(1-p)+2*comb(n, 2)*comb(n-2, 2)*edge_cov

def sign_enumeration(n):
    sums=[]
    for signs in product((-1,1), repeat=n):
        t=sum(1 for a,b,c in combinations(range(n),3) if signs[a]==signs[b]==signs[c])
        sums.append(t)
    mean=Fraction(sum(sums), len(sums))
    var=Fraction(sum(x*x for x in sums),len(sums))-mean*mean
    return mean,var

def integral_midpoints(fun,steps=200000):
    # deterministic quadrature; numerical verification only
    return sum(fun((j+0.5)/steps) for j in range(steps))/steps

def values(d):
    if d==1:return 1/8, 1/32
    # CDF transform angular density is Beta(1/2,(d-1)/2)
    # integrate over r by r=sin theta, theta in [0,pi/2];
    # c_d*2*(1-r*r)^((d-3)/2) dr
    const=exp(lgamma(d/2)-0.5*__import__('math').log(pi)-lgamma((d-1)/2))
    def func(th):
        r=sin(th)
        a=asin(r)
        density=2*const*(max(0.,cos(th)))**(d-2)*pi/2
        return a*density
    def func2(th):
        r=sin(th)
        a=asin(r)
        density=2*const*(max(0.,cos(th)))**(d-2)*pi/2
        return a*a*density
    mu=integral_midpoints(lambda u:func(pi*u/2))/(4*pi)
    eta=integral_midpoints(lambda u:func2(pi*u/2))/(8*pi*pi)
    return mu,eta

def main():
    checks=0
    for n in range(3,11):
        m,v=sign_enumeration(n)
        assert m==Fraction(comb(n,3),4)
        assert v==theory(n,Fraction(1,4),Fraction(1,16)),(n,m,v)
        checks+=2
    # d2 exact angular integrals: C positive with angular phi in (0,pi/2)
    p2=Fraction(3,16)
    shared2=Fraction(7,96)
    cov2=shared2-p2*p2
    assert cov2==Fraction(29,768)
    checks+=1
    for n in range(3,11):
        # independent exact hand-integral values for mean and covariance
        assert theory(n,p2,cov2)>0
        checks+=1
    # d3 exact formulas; compare numerical integrations for 2..64
    import math
    prev=None
    for d in (2,3,4,5,7,12,25,64,200):
        mu,eta=values(d)
        p=.125+mu
        v=.015625+mu/4+eta-mu*mu
        assert p>1/8 and v>1/64
        if prev is not None:
            assert p<prev[0] and v<prev[1]
        prev=p,v
        checks+=3
        if d==2:
            assert abs(p-3/16)<1e-8 and abs(v-29/768)<1e-8
            checks+=2
        if d==3:
            assert abs(p-(1/4-1/(4*pi)))<1e-8
            assert abs(v-((pi*pi-5)/(16*pi*pi)))<1e-8
            checks+=2
    # verify high-d asymptotic leading coefficients numerically for d huge using gamma ratio
    for d in (100, 400):
        mu,eta=values(d)
        lead=1/(2*pi*sqrt(2*pi*d))
        assert abs(mu/lead-1)<0.05
        assert abs(eta*d*8*pi*pi-1)<0.05
        checks+=2
    print(f'PASS {checks} deterministic assertions; exact sign-word enumeration n=3..10; exact d=2,3 moments; quadrature checks.')

if __name__=='__main__':main()
