#!/usr/bin/env python3
"""Exact finite Markov checks and distribution checks for fixed-grid unbiased rounding.
No external dependencies required.
"""
from fractions import Fraction as F
from collections import deque
from math import floor, sqrt
import random

def kernel(q, theta, x):
    z=theta+q*(F(x)-theta)
    lo=z.numerator//z.denominator
    f=z-F(lo)
    d={lo:1-f}
    if f:d[lo+1]=f
    return {a:b for a,b in d.items() if b}

def states(q,theta):
    done={0};work=deque([0]);
    while work:
        z=work.popleft()
        for t in kernel(q,theta,z):
            if t not in done:
                done.add(t);work.append(t)
                assert len(done)<400
    return sorted(done)

def solve(A,b):
    n=len(A)
    for k in range(n):
        p=next(i for i in range(k,n) if A[i][k])
        A[k],A[p]=A[p],A[k];b[k],b[p]=b[p],b[k]
        v=A[k][k]
        for j in range(k,n):A[k][j]/=v
        b[k]/=v
        for i in range(n):
            if i==k:continue
            v=A[i][k]
            if not v:continue
            for j in range(k,n):A[i][j]-=v*A[k][j]
            b[i]-=v*b[k]
    return b

def stationary(q,theta):
    st=states(q,theta); n=len(st);index={x:i for i,x in enumerate(st)}
    P=[[F(0) for j in range(n)] for i in range(n)]
    for i,x in enumerate(st):
        for y,p in kernel(q,theta,x).items():P[i][index[y]]=p
    A=[[P[j][i]-F(i==j) for j in range(n)] for i in range(n)]
    A[-1]=[F(1)]*n
    b=[F(0)]*(n-1)+[F(1)]
    pi=solve(A,b)
    assert all(z>=0 for z in pi)
    assert sum(pi)==1
    mean=sum(F(x)*p for x,p in zip(st,pi));variance=sum((F(x)-theta)**2*p for x,p in zip(st,pi))
    assert mean==theta
    assert (1-q*q)*variance==sum(p*sum(prob*(F(y)-(theta+q*(F(x)-theta)))**2 for y,prob in kernel(q,theta,x).items()) for x,p in zip(st,pi))
    return st,pi,variance

def exact_tests():
    theta=F(1,4)
    for den in [2,3,4,5,8,16,32]:
        r=F(den-1,den)
        a,pi,v=stationary(r,theta)
        assert a==[0,1] and pi==[F(3,4),F(1,4)] and v==F(3,16)
        a,pi,v=stationary(-r,theta)
        assert v>0
        print('r',r,'negative support',len(a),'V-',str(v),'scaled',float((1-r*r)*v),'target',.25)
    print('Exact stationary tests: PASS')

def monte_carlo():
    rng=random.Random(20261105)
    theta=.25
    for r in [.75,.9,.97,.99]:
        x=0
        for _ in range(20000):
            y=(1+r)*theta-r*x
            lo=floor(y);p=y-lo;x=lo+int(rng.random()<p)
        v=0; m=0; n=300000
        for _ in range(n):
            y=(1+r)*theta-r*x
            lo=floor(y);p=y-lo;x=lo+int(rng.random()<p)
            v+=(x-theta)**2;m+=x
        scaled=(1-r*r)*v/n
        assert abs(scaled-.25)<.045, (r,scaled)
        print('r=',r,'sim scaled variance=',round(scaled,5),'mean=',round(m/n,4))
    print('Monte Carlo checks: PASS (not proof)')

if __name__=='__main__':exact_tests();monte_carlo()
