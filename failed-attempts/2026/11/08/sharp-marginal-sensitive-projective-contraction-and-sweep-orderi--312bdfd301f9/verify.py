#!/usr/bin/env python3
"""Reproduce algebraic and numerical checks for binary Sinkhorn contraction.

Run with: python3 verify.py
Requires only the Python standard library.
"""
from fractions import Fraction as Q
from math import exp, log, sqrt, isclose
import random


def formula_q(r, R):
    z2 = r * (1.0-r) * (R-1.0)**2 / R
    h = sqrt(1.0+z2)
    return z2/(h+1.0)**2


def p_and_derivative(K, r, u):
    a,b,c,d=K
    # All K entries are positive.
    A=a/b; C=c/d; x=exp(u)
    p1=A*x/(1+A*x); p2=C*x/(1+C*x)
    m=r*p1+(1-r)*p2
    derivative=r*(1-r)*(p1-p2)**2/(m*(1-m))
    return m,derivative


def mapping(K, r, s, u):
    m,_=p_and_derivative(K,r,u)
    return u+log(s/(1-s))+log((1-m)/m)


def maximizing_u(K,r):
    a,b,c,d=K
    A=a/b;C=c/d; R=A/C
    U=(1-r)+r*R
    V=r+(1-r)*R
    return .5*log(U/V)-.5*log(A*C)


def exact_fraction_test():
    cases=0
    for a in (1,2,5,11):
      for b in (1,3,7):
       for c in (1,2,6):
        for d in (1,4,9):
         A=Q(a,b);C=Q(c,d)
         for r in (Q(1,7),Q(1,2),Q(5,6)):
          for x in (Q(1,5),Q(2,3),Q(3,1)):
           p1=A*x/(1+A*x);p2=C*x/(1+C*x)
           m=r*p1+(1-r)*p2
           mp=r*p1*(1-p1)+(1-r)*p2*(1-p2)
           assert m*(1-m)-mp==r*(1-r)*(p1-p2)**2
           # Exact derivative rationalization through row probabilities.
           deriv=1-mp/(m*(1-m))
           assert deriv==r*(1-r)*(p1-p2)**2/(m*(1-m))
           cases+=1
    return cases


def numerical_tests():
    rng=random.Random(20261104)
    n=0
    max_err=0.
    for _ in range(4200):
        K=tuple(rng.randint(1,24) for _ in range(4))
        r=.01+.98*rng.random();s=.01+.98*rng.random()
        R=(K[0]*K[3])/(K[1]*K[2])
        u=-6+12*rng.random()
        q=formula_q(r,R)
        m,fp=p_and_derivative(K,r,u)
        assert 0<=fp<=q+8e-13
        eps=1e-5
        fd=(mapping(K,r,s,u+eps)-mapping(K,r,s,u-eps))/(2*eps)
        max_err=max(max_err,abs(fd-fp))
        assert abs(fd-fp)<1e-7, (K,r,s,u,fp,fd,abs(fd-fp))
        ustar=maximizing_u(K,r)
        _,fstar=p_and_derivative(K,r,ustar)
        assert abs(fstar-q)<1e-12
        v=-5+10*rng.random()
        diff=abs(mapping(K,r,s,u)-mapping(K,r,s,v))
        assert diff<=q*abs(u-v)+4e-12
        if R != 1:
            qb=((sqrt(R)-1)/(sqrt(R)+1))**2
            assert q<=qb+1e-12
            if abs(r-.5)>1e-3:
                assert q<qb
        # A full row-then-column sweep on scaling vectors agrees with the log map.
        x=exp(u);a,b,c,d=K
        v1,v2=x,1.
        row1=r/(a*v1+b*v2)
        row2=(1-r)/(c*v1+d*v2)
        w1=s/(a*row1+c*row2)
        w2=(1-s)/(b*row1+d*row2)
        assert abs(log(w1/w2)-mapping(K,r,s,u))<3e-12
        # The reverse-order exact envelope swaps the marginal parameter.
        q_rev=formula_q(s,R)
        if r*(1-r)<s*(1-s)-1e-12 and R != 1:
            assert q<q_rev
        n+=1
    return n,max_err

if __name__=='__main__':
    count=exact_fraction_test()
    n,err=numerical_tests()
    assert abs(formula_q(.01,400)-.3793949766865339)<1e-12
    assert abs(formula_q(.5,400)-.8185941043083901)<1e-12
    print(f'PASS: {count} exact Fraction identities and {n} randomized multi-property cases')
    print(f'Max central-difference discrepancy: {err:.3g}')
    print('No finite test substitutes for the quantified analytic proof.')
