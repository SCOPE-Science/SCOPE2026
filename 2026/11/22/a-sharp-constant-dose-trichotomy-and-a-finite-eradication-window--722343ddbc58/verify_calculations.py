#!/usr/bin/env python3
"""Reproduce exact and numerical identities for the two-phenotype dose-response theorem.

Uses only Python standard-library arithmetic; numerical checks supplement the proof.
"""
from fractions import Fraction as Q
from math import sqrt, isclose


def eig(r, t, k, m, mu0, nu, c):
    s = r - k*c/(1+c)
    mu = mu0 + m*c
    aa, bb, cc, dd = s-mu, nu, mu, t-nu
    return (aa+dd+sqrt((aa-dd)**2+4*bb*cc))/2


def rate_derivative(r,t,k,m,mu0,nu,c):
    z=eig(r,t,k,m,mu0,nu,c)
    s=r-k*c/(1+c)
    mu=mu0+m*c
    return (-k/(1+c)**2*(z-t+nu)-m*(z-t))/(2*z-s+mu-t+nu)


def verify():
    r,t,k,m,mu0,nu=Q(19,33),Q(1,11),Q(2),Q(1),Q(1),Q(1)
    c=Q(2); s=r-k*c/(1+c);mu=mu0+m*c
    lam=-Q(1,11)
    assert (lam-s+mu)*(lam-t+nu)==mu*nu
    y=Q(1)+c
    rhs=2*k/y + k*(mu0-m)/(m*y*y)+nu*k/(m*y*y+k)
    assert k+t-r==rhs
    assert t-lam ==nu*k/(m*y*y+k)
    assert (s-mu)*(t-nu)-nu*mu == - (33*c*c-404*c+223)/(363*(1+c))
    assert (s-mu)+(t-nu) == -(c+4)*(3*c+1)/(3*(c+1))
    roots=((202-sqrt(33445))/33,(202+sqrt(33445))/33)
    assert 0<roots[0]<2<roots[1]
    for x in [0,roots[0]/2,2,roots[1]+1,1000]:
        z=eig(float(r),float(t),2,1,1,1,x)
        assert (z<0)==(roots[0]<x<roots[1])
    for d in [.2,.05,.01,.002]:
        r0=1+2-d # t=1
        z=lambda x:eig(r0,1,2,1,1,1,x)
        # bracket and bisect zero of derivative
        lo,hi=0.,max(10.,8/d)
        assert rate_derivative(r0,1,2,1,1,1,lo)<0
        assert rate_derivative(r0,1,2,1,1,1,hi)>0
        for _ in range(90):
            mid=(lo+hi)/2
            if rate_derivative(r0,1,2,1,1,1,mid)<0:lo=mid
            else:hi=mid
        cstar=(lo+hi)/2
        # Here second-order correction is -0.5
        assert abs(cstar-(4/d-.5))<2*d
        assert abs((1-z(cstar))/(d*d)-1/8)<2*d
    # Each test covers all of: no finite optimal dose, zero dose, unique interior.
    params=[
        (4.,1.,2.,1.,1.,1.,'down'),
        (2.,1.,2.,1.,1.,1.,'interior'),
        (1.,1.,2.,1.,1.,1.,'interior'),
        (-4.,1.,2.,1.,1.,1.,'up'),
        (.5,1.,2.,1.,1.,1.,'interior'),
        (-1.,1.,2.,1.,1.,1.,'up')]
    for r0,t0,k0,m0,u0,n0,mode in params:
        xs=[i*0.2 for i in range(1001)]
        sg=[rate_derivative(r0,t0,k0,m0,u0,n0,x) for x in xs]
        if mode=='down': assert all(v < -1e-13 for v in sg)
        if mode=='up': assert all(v>1e-13 for v in sg[1:])
        if mode=='interior':
            neg=[i for i,v in enumerate(sg) if v<-1e-9]
            pos=[i for i,v in enumerate(sg) if v>1e-9]
            assert neg and pos and max(neg)<min(pos)
    print('PASS exact rational witness, singular scaling, and representative derivative signs')


if __name__=='__main__':verify()
