#!/usr/bin/env python3
"""Exact independent-increment/conditional-return/orthogonal checks."""
from itertools import product
from fractions import Fraction
from math import comb

def closed(q,m):
    mu=Fraction((q-1)**2*m*m+(q*q-1)*m+2*q,2*q*q)
    var=Fraction((m-1)*(q-1)*(2*m*m*(q-1)**2+m*(-2*q*q+5*q-3)+2*q*q-4*q),2*q**4)
    return mu,var

def conditional_check(q,m):
    p=Fraction(q-1,q)
    alpha=Fraction(1,q-1)
    mu,var=closed(q,m)
    Eg=Eg2=E_cond_var=Fraction(0)
    for a in product((0,1),repeat=m):
        s=sum(a)
        j=sum(a[i]*a[i+1] for i in range(m-1))
        h=1+s-a[0]-a[-1]-j
        g=Fraction(s*(s+1),2)+h-alpha*j
        weight=p**s*(1-p)**(m-s)
        Eg+=weight*g
        Eg2+=weight*g*g
        E_cond_var+=weight*alpha*(1-alpha)*j
        y=[Fraction(z)-p for z in a]
        decomp=(m-1)*p*sum(y)+sum(y[i]*y[k] for i in range(m) for k in range(i+2,m))-alpha*sum(y[i]*y[i+1] for i in range(m-1))
        if g-mu!=decomp:
            raise AssertionError(('orthogonal',q,m,a,g-mu,decomp))
        if m<=5:
            counts={}
            total=0
            choices=[range(1,q) if z else (0,) for z in a]
            for d in product(*choices):
                t=sum(d[i]!=0 and d[i+1]!=0 and (d[i]+d[i+1])%q==0 for i in range(m-1))
                counts[t]=counts.get(t,0)+1; total+=1
            for t in range(j+1):
                got=Fraction(counts.get(t,0),total)
                expected=Fraction(comb(j,t))*alpha**t*(1-alpha)**(j-t)
                if got!=expected:
                    raise AssertionError(('binomial',q,m,a,t,got,expected))
    if Eg!=mu or Eg2-Eg*Eg+E_cond_var!=var:
        raise AssertionError(('totalvariance',q,m,Eg,mu,Eg2-Eg*Eg+E_cond_var,var))
    print('OK conditional',q,m+1)

if __name__=='__main__':
    for q in (3,4,5):
        for m in range(2,10): conditional_check(q,m)
    print('CONDITIONAL_VERIFY_OK')
