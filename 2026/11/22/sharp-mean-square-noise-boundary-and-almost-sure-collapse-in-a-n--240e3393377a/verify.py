#!/usr/bin/env python3
"""Finite exact checks of a reflection fixed-point iteration and numerical asymptotics."""
from fractions import Fraction as Q
from itertools import product
from math import gamma, sqrt

def finite_exact():
    h=Q(3,2)  # sigma / sqrt(2)
    u0,v0=Q(1),Q(0)
    states=[(u0,v0)]
    U,V=Q(1),Q(0)
    checks=0
    for step in range(4):
        beta=Q(1,step+4)
        a=h*beta
        new=[]
        for u,v in states:
            for xi,zeta in product((-1,1),repeat=2):
                new.append((u*(1+a*xi), (1-2*beta)*v+a*zeta*u))
        states=new
        U=(1+a*a)*U
        V=(1-2*beta)**2*V+a*a*(U/(1+a*a))
        count=Q(len(states))
        exactU=sum((u*u for u,v in states),Q(0))/count
        exactV=sum((v*v for u,v in states),Q(0))/count
        assert exactU==U and exactV==V,(step,exactU,U,exactV,V)
        assert all((u.denominator>0 and v.denominator>0 for u,v in states))
        checks+=2
    return checks

def numerical_asymptotics():
    checks=0
    for b,B,sigma in ((.5,.5,1.5),(.5,.5,2.),(.5,.5,2.5),(.3,.4,1.3)):
        c=sigma*sigma/2
        U=1.
        q=0.
        n=100000
        for k in range(n):
            beta=B/(k+1)**b
            q=((1-2*beta)**2*q+c*beta*beta)/(1+c*beta*beta)
            U*=1+c*beta*beta
        bn=B/(n+1)**b
        assert abs(q/bn-c/4)/(c/4)<.02, (b,q/bn,c/4)
        checks+=1
        if b==.5:
            p=c*B*B
            prediction=c*B*gamma(1)/gamma(1+p)*n**(p-.5)
            actual=4*q*U
            assert abs(actual/prediction-1)<.02,(sigma,actual,prediction)
            checks+=1
    return checks

if __name__=='__main__':
    print('VERIFY_OK',finite_exact()+numerical_asymptotics(),'finite_exact_and_asymptotic_checks')
