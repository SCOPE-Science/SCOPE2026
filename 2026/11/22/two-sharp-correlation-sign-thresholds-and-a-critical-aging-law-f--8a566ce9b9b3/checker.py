#!/usr/bin/env python3
"""Exact finite-step checks of color-draw correlations in a symmetric urn mixture."""
from fractions import Fraction as Q
from math import gamma


def evolve(masses, T, a, b, p):
    B=a+b
    assert T>=2*B and Q(0)<p<Q(1)
    out={}
    cross=Q(0)
    for d,weight in masses.items():
        for s in (-1,1):
            pick=Q(T+s*d,2*T)
            for j,prob in ((a-b,p),(B,1-p)):
                x=d+j*s
                w=weight*pick*prob
                out[x]=out.get(x,Q(0))+w
                cross+=w*s*x
    assert sum(out.values())==1
    return out,cross


def analytic(a,b,T0,p,N):
    B=a+b
    h=B-2*p*b
    q=p*(a-b)**2+(1-p)*B*B
    d=B-2*h
    V=Q(0)
    W=Q(0)
    G=Q(1)
    out=[]
    for i in range(1,N+1):
        Tbefore=T0+(i-1)*B
        Tafter=Tbefore+B
        entry=(W+h)/Tafter
        V=(1+2*h/Tbefore)*V+q
        W=V/Tafter
        G*=Q(Tbefore+2*h,Tafter)
        if d!=0:
            assert W==q/d*(1-G)
        out.append((entry,W,G))
    return out


def exact_tests():
    total=0
    cases=[(1,3,8,Q(3,5)),(1,3,8,Q(2,3)),
           (1,3,8,Q(3,4)),(1,3,8,Q(5,6)),
           (1,3,8,Q(9,10)),(2,3,10,Q(8,9)),
           (2,5,14,Q(9,10)),(3,4,14,Q(19,20))]
    for a,b,T0,p in cases:
        n=14
        masses={0:Q(1)}
        formulas=analytic(a,b,T0,p,n)
        for i,(pred,W,G) in enumerate(formulas,1):
            T=T0+(i-1)*(a+b)
            assert sum(d*w for d,w in masses.items())==0
            assert sum(d*d*w for d,w in masses.items())/T == (Q(0) if i==1 else formulas[i-2][1])
            masses,cross=evolve(masses,T,a,b,p)
            assert cross/(T+a+b)==pred, (a,b,p,i,cross,pred)
            total+=4
    # Evaluate direct two-time covariance for selected pairs using tagged mass evolution.
    a,b,T0,p=1,3,8,Q(3,4)
    B=a+b
    h=B-2*p*b
    for i,j in [(1,2),(1,5),(2,5),(3,8),(5,10),(8,12)]:
        masses={0:Q(1)}
        for step in range(1,i):
            masses,_=evolve(masses,T0+(step-1)*B,a,b,p)
        tagged={}
        T=T0+(i-1)*B
        for d,w in masses.items():
            for s in (-1,1):
                draw=Q(T+s*d,2*T)
                for J,r in ((a-b,p),(B,1-p)):
                    key=(d+J*s,s)
                    tagged[key]=tagged.get(key,Q(0))+w*draw*r
        for step in range(i+1,j):
            nxt={}
            T=T0+(step-1)*B
            for (d,first),w in tagged.items():
                for s in (-1,1):
                    draw=Q(T+s*d,2*T)
                    for J,r in ((a-b,p),(B,1-p)):
                        key=(d+J*s,first)
                        nxt[key]=nxt.get(key,Q(0))+w*draw*r
            tagged=nxt
        T=T0+(j-1)*B
        cov=sum(w*first*Q(d,T) for (d,first),w in tagged.items())
        predicted=analytic(a,b,T0,p,i)[-1][0]
        for step in range(i+1,j):
            predicted*=Q(T0+(step-1)*B+h,T0+(step-1)*B)
        # predicted from previous first step's covariance includes denominator T_i,
        # whereas j-th draw has denominator T_{j-1}.
        predicted*=Q(T0+i*B,T0+(j-1)*B)
        assert cov==predicted,(i,j,cov,predicted)
        total+=1
    # Critical p* has strictly negative covariance every step; its asymptotic
    # exponent and crossover index are verified using exact rational products.
    a,b,T0=1,3,8
    p0=Q(a+b,2*b)
    ps=Q(a+3*b,4*b)
    assert p0==Q(2,3) and ps==Q(5,6)
    for p in [p0,Q(3,4),ps,Q(9,10)]:
        seq=analytic(a,b,T0,p,1000)
        signs=[(x[0]>0)-(x[0]<0) for x in seq]
        if p==p0:
            assert signs[0]==0 and set(signs[1:])=={1}
        if p==Q(3,4):
            assert signs[0]==-1 and signs[-1]==1
            assert signs==sorted(signs)
        if p>=ps:
            assert set(signs)=={-1}
        total+=4
    print('PASS:',total,'exact rational assertions and finite distributions')

if __name__=='__main__':
    exact_tests()
