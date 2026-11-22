#!/usr/bin/env python3
"""Check a Gaussian-binomial closed form by two different exact polynomial calculations."""
from collections import defaultdict
from math import comb
from functools import lru_cache

def plus(a,b):
    c=defaultdict(int,a)
    for x,v in b.items():c[x]+=v
    return {k:v for k,v in c.items() if v}

@lru_cache(None)
def gaussian(n,k):
    if k<0 or k>n:return {}
    if k==0 or k==n:return {0:1}
    a=gaussian(n-1,k)
    b={x+n-k:v for x,v in gaussian(n-1,k-1).items()}
    return plus(a,b)

def form(A,B):
    if A==0:return {(0,0):1}
    out=defaultdict(int)
    for j in range(min(A-1,B)+1):
        g1=gaussian(A-1,j)
        g2=gaussian(A+B-j,A)
        for e1,v1 in g1.items():
            for e2,v2 in g2.items():
                for h in range(j+1):
                    out[(e1+e2+j*(j+1)//2,h)]+=v1*v2*comb(j,h)*(-1)**(j-h)
    return {p:v for p,v in out.items() if v}

def product(A,B):
    # Each slot has a series sum_{v>=0} t^v q^{slot*v} u^{(v>0 and slot internal)}.
    dp={(0,0,0):1}
    for i in range(A+1):
        nd=defaultdict(int)
        for (b,c,h),v in dp.items():
            for j in range(B-b+1):
                nd[(b+j,c+i*j,h+int(j>0 and 0<i<A))]+=v
        dp=nd
    return {(c,h):v for (b,c,h),v in dp.items() if b==B}

def verify():
    cases=0
    for A in range(0,14):
        for B in range(0,14):
            if A+B>20:continue
            a=form(A,B);b=product(A,B)
            assert a==b,(A,B,len(a),len(b),[(k,a.get(k),b.get(k)) for k in a.keys()|b.keys() if a.get(k)!=b.get(k)][:5])
            assert sum(a.values())==comb(A+B,A)
            for r in range(max(0,A-1)+1):
                lhs=defaultdict(int)
                for (c,h),v in b.items():
                    if h>=r:lhs[c]+=v*comb(h,r)
                rhs=defaultdict(int)
                if r<=B and A:
                    for e1,v1 in gaussian(A-1,r).items():
                        for e2,v2 in gaussian(A+B-r,A).items():
                            rhs[e1+e2+r*(r+1)//2]+=v1*v2
                elif A==0 and r==0:rhs[0]=1
                assert dict(lhs)==dict(rhs),(A,B,r,lhs,rhs)
            for (c,h),v in a.items():
                assert a.get((A*B-c,h),0)==v,(A,B,c,h)
            for h in range(min(A-1,B)+1) if A else [0]:
                v=sum(num for (c,r),num in a.items() if r==h)
                assert v==(comb(A-1,h)*comb(B+1,h+1) if A else 1)
            cases+=1
    print('PASS:',cases,'(A,B) pairs; independent Gaussian and slot-product coefficient calculations')
if __name__=='__main__':verify()
