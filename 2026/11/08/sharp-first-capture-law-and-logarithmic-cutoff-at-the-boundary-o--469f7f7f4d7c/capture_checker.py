#!/usr/bin/env python3
"""Exact rational checks for first capture into the invariant interval of a two-branch affine interval map."""
from fractions import Fraction as Q
from math import ceil

def P(a,b=1): return Q(a,b)

def valid(lam,mu,a,b,c):
    s=lam*mu
    return (0<lam<1 and mu>0 and 0<=c<b<=1 and (s<=1 or mu*(1-b)<=1-c)
            and b*(1-lam)<a<b-lam*c and (1-lam)*(c-mu*b)<(1-mu)*a)

def map_f(x,v):
    lam,mu,a,b,c=v
    eta=(b-a)/lam
    return lam*x+a if x<eta else lam*mu*(x-eta)+c

def tail(n,v):
    lam,mu,a,b,c=v
    A=a/(1-lam)
    left=max(Q(0), A-(A-c)*lam**(-n))
    s=lam*mu; d=mu*(b-a)-c
    if s==1:
        right=max(Q(0),1-b-n*d)
    else:
        r=d/(s-1)
        right=max(Q(0),1-r-(b-r)*s**(-n))
    return left+right

def brute_tau(x,v,maxn=300):
    b,c=v[3],v[4]
    for n in range(maxn+1):
        if c<=x<b:return n
        x=map_f(x,v)
    raise AssertionError('capture bound exceeded')

def check_grid(v,res=211,n_max=20):
    assert valid(*v),v
    total=0
    ts=[]
    for i in range(res):
        x=Q(i,res)
        t=brute_tau(x,v)
        ts.append(t)
    for n in range(n_max):
        survival=sum(t>n for t in ts)
        theoretical=tail(n,v)*res
        # A half-open interval threshold can introduce only two one-grid-point errors.
        assert abs(survival-theoretical)<=2,(v,n,survival,theoretical)
        total+=1
    return total

vlist=[
    (P(3,4),P(2),P(1,5),P(1,2),P(0)), # s>1, c=0, epsilon=1/20
    (P(3,4),P(2),P(1,5),P(3,5),P(1,5)), # s>1, c>0; equality mu(1-b)=1-c
    (P(1,2),P(1),P(1,2),P(4,5),P(1,5)), # s<1
    (P(1,2),P(2),P(1,2),P(3,4),P(1,10)), # s=1
    (P(1,3),P(3,2),P(3,5),P(4,5),P(1,10)), # s<1
]

checks=0
for v in vlist:
    checks+=check_grid(v)
    for n in range(20):
        # Tail is a weakly decreasing, nonnegative rational, initially 1-(b-c).
        assert tail(n,v)>=tail(n+1,v)>=0
        checks+=1
    assert tail(0,v)==1-v[3]+v[4]
    checks+=1

# One-parameter singular family: exact entire finite-time survivor sequence.
for num,den in [(1,16),(1,32),(1,64),(1,128),(1,256),(1,1024)]:
    eps=Q(num,den)
    v=(Q(3,4),Q(2),Q(1,4)-eps,Q(1,2),Q(0))
    assert valid(*v)
    for n in range(31):
        predicted=max(Q(0),(Q(1,2)+4*eps)*Q(2,3)**n -4*eps)
        assert tail(n,v)==predicted
        checks+=1

# Endpoint parameter, outside the strict admissible family, has a geometric tail.
v=(Q(3,4),Q(2),Q(1,4),Q(1,2),Q(0))
for n in range(40):
    assert tail(n,v)==Q(1,2)*Q(2,3)**n
    checks+=1

print('PIECEWISE_AFFINE_CAPTURE_RATIONAL_CHECKS_OK', checks)
