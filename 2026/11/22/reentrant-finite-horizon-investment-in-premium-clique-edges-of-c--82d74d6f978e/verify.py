#!/usr/bin/env python3
"""Standalone finite checks for split-graph heat-trace design; stdlib only.

No finite run substitutes for the analytical all-size proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import exp, log, isclose
import random


def exact_laplacian(p, q, a, b):
    n = p + q
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    edges = [(i, j, b) for i in range(p) for j in range(i+1, p)]
    edges += [(i, j, a) for i in range(p) for j in range(p, n)]
    for i, j, w in edges:
        L[i][i] += w; L[j][j] += w
        L[i][j] -= w; L[j][i] -= w
    return L


def mv(A, x):
    return [sum(a*y for a,y in zip(row, x)) for row in A]


def check_spectrum(p, q, a, b):
    n=p+q; L=exact_laplacian(p,q,a,b)
    vectors=[([Q(1)]*n,Q(0))]
    for i in range(1,p):
        v=[Q(0)]*n; v[0]=Q(1);v[i]=Q(-1)
        vectors.append((v,q*a+p*b))
    for i in range(p+1,n):
        v=[Q(0)]*n; v[p]=Q(1);v[i]=Q(-1)
        vectors.append((v,p*a))
    v=[Q(q)]*p+[Q(-p)]*q
    vectors.append((v,n*a))
    assert len(vectors)==n
    for v,lam in vectors:
        assert mv(L,v)==[lam*x for x in v]
    return n


def heat(p,q,B,r,t,b):
    m=p*(p-1)/2; a=(B-r*m*b)/(p*q)
    return 1+(q-1)*exp(-p*a*t)+exp(-(p+q)*a*t)+(p-1)*exp(-(q*a+p*b)*t)


def edge_threshold(p,q,B,t):
    x=B*t/(p*q)
    # The stable form is sufficient for checker test sizes.
    return 2*p*q/(p*(q-1)*exp((q-p)*x)+(p+q)*exp(-p*x)+q*(p-1))


def derivative(p,q,B,r,t,b):
    m=p*(p-1)/2; a=(B-r*m*b)/(p*q)
    c=r*(p-1)/(2*q)
    return t*(c*p*(q-1)*exp(-p*a*t) + c*(p+q)*exp(-(p+q)*a*t)
      + (p-1)*(q*c-p)*exp(-(q*a+p*b)*t))


def bisect_opt(p,q,B,r,t):
    cap=2*B/(r*p*(p-1))
    if derivative(p,q,B,r,t,0)>=0:return 0.
    assert derivative(p,q,B,r,t,cap)>0
    lo,hi=0.,cap
    for _ in range(70):
        mid=(lo+hi)/2
        if derivative(p,q,B,r,t,mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def reentrant_roots(p,B,r):
    q=p+1
    star=p/B*log((2*p+1)/p)
    assert 1<r<edge_threshold(p,q,B,star)
    def f(t):return edge_threshold(p,q,B,t)-r
    lo,hi=0.,star
    for _ in range(75):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    minus=(lo+hi)/2
    lo,hi=star, max(10*star,100)
    while f(hi)>0:hi*=2
    for _ in range(75):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    return minus,(lo+hi)/2,star


def run():
    count=0
    for p in range(2,11):
        for q in range(2,11):
            for aa,bb in ((Q(1,3),Q(2,5)),(Q(3,7),Q(0)),(Q(4,11),Q(2,9))):
                count+=check_spectrum(p,q,aa,bb)
            for B,r,t in ((1.,1.04,.5),(1.,1.04,2.),(1.,1.04,5.),(2.5,1.4,1.2)):
                cap=2*B/(r*p*(p-1))
                d0=derivative(p,q,B,r,t,0)
                Rt=edge_threshold(p,q,B,t)
                assert (d0>=-1e-11)==(r>=Rt-1e-11)
                opt=bisect_opt(p,q,B,r,t)
                assert abs(opt)<=cap+1e-12
                h0=heat(p,q,B,r,t,opt)
                for k in range(21):
                    b=cap*k/20
                    assert h0<=heat(p,q,B,r,t,b)+1e-10
                    count+=1
                # derivative by central finite difference at a non-boundary point
                mid=.4*cap; eps=1e-5*cap
                fd=(heat(p,q,B,r,t,mid+eps)-heat(p,q,B,r,t,mid-eps))/(2*eps)
                assert isclose(fd,derivative(p,q,B,r,t,mid),rel_tol=2e-6,abs_tol=2e-8)
                count+=2
    for p in range(2,51):
        q=p+1; B=1.
        u=((2*p+1)/p)**(1/(p+1))
        Rmax=2*p*(p+1)/(p*(p+1)*u+p*p-1)
        star=p*log((2*p+1)/p)
        assert isclose(Rmax,edge_threshold(p,q,B,star),rel_tol=2e-13)
        r=(1+Rmax)/2
        left,right,peak=reentrant_roots(p,B,r)
        assert 0<left<peak<right
        assert edge_threshold(p,q,B,left*.5)<r
        assert edge_threshold(p,q,B,(left+right)/2)>r
        assert edge_threshold(p,q,B,right*1.5)<r
        assert bisect_opt(p,q,B,r,(left+right)/2)>0
        assert bisect_opt(p,q,B,r,left*.5)==0
        assert bisect_opt(p,q,B,r,right*1.5)==0
        count+=9
    p=2; q=3; r=26/25; B=1
    lo,hi,peak=reentrant_roots(p,B,r)
    assert abs(lo-0.56223001029132)<1e-10
    assert abs(hi-3.19870796504315)<1e-10
    for p in (100,1000,10000):
        u=exp(log(2+1/p)/(p+1))
        Rmax=2*p*(p+1)/(p*(p+1)*u+p*p-1)
        assert abs(p*(Rmax-1)-(1-log(2))/2)<0.00001
        count+=1
    print('PASS:',count,'finite checks; p=2, q=3, r=26/25, B=1, transitions',lo,hi)

if __name__=='__main__':run()
