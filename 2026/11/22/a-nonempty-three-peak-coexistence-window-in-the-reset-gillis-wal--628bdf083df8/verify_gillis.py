#!/usr/bin/env python3
"""Reproducible numeric diagnostics for local-mode coexistence under resetting.

The exact threshold ordering and coexistence are proved analytically in RESULT.md;
finite computations here test the identities and demonstrate nonempty intervals.
Run with: python3 verify_gillis.py
"""
import math

checks=0

def test(assertion, label):
    global checks
    checks+=1
    if not assertion:raise AssertionError(label)

def hits(e,r,N=15000):
    s=1-r
    a=s/(1+math.sqrt(1-s*s))
    w=a
    w1=w2=0
    for n in range(N,0,-1):
        p=(1-e/n)/2
        q=(1+e/n)/2
        w=s*q/(1-s*p*w)
        if n==2:w2=w
        if n==1:w1=w
    return w1,w2

def thresholds(e):
    def bisection(j,target):
        lo=1e-12;hi=1-1e-12
        for _ in range(67):
            md=(lo+hi)/2
            if hits(e,md)[j]>target:lo=md
            else:hi=md
        return (lo+hi)/2
    return bisection(0,1+e),bisection(1,(2+e)/(2*(1-e)))

def stationary(e,r,N=5000):
    s=1-r
    alpha=s/(1+math.sqrt(1-s*s))
    w=[0.]*(N+2)
    w[N+1]=alpha
    for n in range(N,0,-1):
        w[n]=s*(1+e/n)/2/(1-s*(1-e/n)/2*w[n+1])
    pi0=r/(1-s*w[1])
    ms=1.0;v=1.0
    mass=[pi0]
    for n in range(1,N+1):
        if n==1:ms/=1+e
        else: ms*=((1-e/(n-1))/(1+e/n))
        v*=w[n]
        mass.append(pi0*ms*v)
    return mass

def direct(e,r,K=65,steps=2000):
    s=1-r
    a=[0.0]*(2*K+1);a[K]=1
    for _ in range(steps):
        b=[0.0]*(2*K+1);b[K]=r
        for j,x in enumerate(a):
            if x==0:continue
            n=j-K
            p=(1-e/n)/2 if n else .5
            if j<2*K:b[j+1]+=s*x*p
            if j>0:b[j-1]+=s*x*(1-p)
        a=b
    return a

for e in (-.48,-.4,-.25,-.1,-.02):
    r1,r2=thresholds(e)
    test(0<r1<r2<1,'nonempty interval')
    u1,u2=hits(e,r1)
    v1,v2=hits(e,r2)
    test(abs(u1-(1+e))<2e-10,'first threshold root')
    test(abs(v2-(2+e)/(2*(1-e)))<2e-10,'second threshold root')
    for rel in (.1,.4,.8):
        r=r1+rel*(r2-r1)
        pi=stationary(e,r)
        test(pi[0]>pi[1] and pi[2]>pi[1], 'strict central maximum with neighbor dip')
        test(max(pi[2:])>pi[1], 'nonzero side peak')
        test(pi[0]+2*sum(pi[1:])>1-1e-9, 'normalized distribution')
        test(abs(pi[1]- (1-r)*(.5*pi[0]+(2+e)/4*pi[2]))<2e-11,'stationary recurrence at site one')
        if r>=0.03:
            op=direct(e,r)
            for k in (0,1,2,3,4,5,8,12):
                test(abs(op[65+k]-pi[k])<2e-10,'independent forward propagation')
    p_at_r1=stationary(e,r1)
    test(p_at_r1[2]>p_at_r1[0], 'outer site dominates at first boundary')
    tiny=r1+min(1e-5,(r2-r1)*.0001)
    p_tiny=stationary(e,tiny)
    test(p_tiny[0]>p_tiny[1] and p_tiny[2]>p_tiny[0], 'outer dominates central local peak')
    for r in (r1*.5,(r1+r2)/2,min(.99,(r2+1)/2)):
        w1,w2=hits(e,r)
        ratio1=w1/(1+e)
        ratio2=2*(1-e)/(2+e)*w2
        p=stationary(e,r)
        test(abs(p[1]/p[0]-ratio1)<5e-11,'ratio 1')
        test(abs(p[2]/p[1]-ratio2)<5e-11,'ratio 2')

for r in (.01,.1,.5):
    p=stationary(0,r)
    s=1-r
    a=s/(1+math.sqrt(1-s*s))
    test(abs(p[0]-math.sqrt(r/(2-r)))<1e-11,'unbiased benchmark')
    for n in (1,2,5,10):test(abs(p[n]/p[n-1]-a)<1e-11,'geometric benchmark')
print('PASS:',checks,'deterministic tests; exact identities and finite-kernel dynamics agree.')
