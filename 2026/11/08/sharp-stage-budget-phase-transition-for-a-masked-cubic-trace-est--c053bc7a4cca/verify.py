#!/usr/bin/env python3
"""Standalone reproducibility checks for a three-stage rank-one cubic trace benchmark."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, isclose


def theoretical(n, p):
    a = Q(n-1); b = Q(2)-Q(2,n)
    return (a+1/p[0])*(a+1/p[1])*(b+1/p[2])/Q(n*n)


def exhaustive(n, p):
    """Independently enumerate masks and sign probes using exact rationals."""
    probmask=[]
    for rate in p:
        probmask.append([(mask, rate**sum(mask)*(1-rate)**(n-sum(mask)))
                         for mask in product((0,1), repeat=n)])
    e=Q(0); e2=Q(0)
    for m1,w1 in probmask[0]:
      for m2,w2 in probmask[1]:
       for m3,w3 in probmask[2]:
        w=w1*w2*w3/Q(2**n)
        if not w: continue
        for signs in product((-1,1),repeat=n):
            # This is the matrix-product expression for A=11'/n, derived
            # independently by 3 repeated matvecs, not the moment formula.
            vec=list(map(Q,signs))
            for mask in (m1,m2,m3):
                v=sum(vec,Q(0))/n
                vec=[Q(z)*v for z in mask]
            val=sum(Q(s)*v for s,v in zip(signs,vec))/(p[0]*p[1]*p[2])
            e+=w*val
            e2+=w*val*val
    return e,e2


def opt(n,P):
    a=n-1.;b=2.-2./n
    if n==2:return (P/3, P/3, P/3)
    s0=(sqrt(1+4*a*(1+b))-1)/(2*a)
    if P>=1+2*s0:return ((P-1)/2,(P-1)/2,1.)
    lo=max(0,(P-1)/2);hi=min(1,P/2)
    for _ in range(90):
        s=(lo+hi)/2;t=P-2*s
        if s*(1+a*s)<t*(1+b*t):lo=s
        else:hi=s
    s=(lo+hi)/2
    return (s,s,P-2*s)


def objective(n,p):
    a=n-1;b=2-2/n
    return (a+1/p[0])*(a+1/p[1])*(b+1/p[2])/(n*n)-1


def run():
    cases=[(2,(Q(1,3),Q(2,3),Q(3,4))),
           (2,(Q(1,2),Q(1,2),Q(1,2))),
           (3,(Q(1,2),Q(2,3),Q(3,4))),
           (3,(Q(1,1),Q(1,2),Q(1,3)))]
    count=0
    for n,p in cases:
        e,e2=exhaustive(n,p)
        assert e==1,(n,p,e)
        assert e2==theoretical(n,p),(n,p,e2,theoretical(n,p))
        count+=2
    for n in (2,3,4,5,8,16,64,1000):
        for P in (.08,.35,.75,.95,1.,1.08,1.3,1.7,2.3,2.8,2.99):
            p=opt(n,P)
            assert all(0<v<=1+1e-12 for v in p)
            assert abs(sum(p)-P)<1e-11
            assert objective(n,p)<=objective(n,(P/3,)*3)+1e-10
            count+=3
            # Variance does not decrease on small feasible coordinate shifts.
            for ix in range(3):
             for iy in range(3):
              if ix==iy: continue
              for delta in (1e-5, 1e-4):
               pp=list(p); pp[ix]+=delta;pp[iy]-=delta
               if min(pp)>0 and max(pp)<=1:
                assert objective(n,pp)>=objective(n,p)-2e-10,(n,P,p,pp)
                count+=1
    for n in (10000,100000,1000000):
        P=.7;p=opt(n,P)
        assert abs(p[0]*sqrt(n)/sqrt(P*(1+2*P))-1)<.09
        assert abs(objective(n,p)-(1+1/P))<.14
        assert abs(objective(n,(P/3,)*3)-(1+3/P))<.09
        count+=3
    print('PASS',count,'exact rational / deterministic checks')
if __name__=='__main__':run()
