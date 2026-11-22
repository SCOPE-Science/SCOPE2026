#!/usr/bin/env python3
"""Exact-rational checks for star-graph weighted fusion, independent of nonstandard packages.
This finite checker illustrates the mathematical proof; it is not an exhaustive certificate.
"""
from fractions import Fraction as F
from random import Random


def clip(x, a):
    return max(-a, min(x, a))


def solve(y, m, a, lam):
    """Solve the star TV prox via its scalar monotone KKT root, exactly over Q."""
    assert len(y) == len(m) == len(a) + 1
    y = list(map(F, y)); m = list(map(F, m)); a = list(map(F, a)); lam=F(lam)
    bp = sorted(set([min(y)-1, max(y)+1] +
                    [y[i] + s*lam*a[i-1]/m[i]
                     for i in range(1,len(y)) for s in (-1,1)]))
    root = None
    for l, r in zip(bp, bp[1:]):
        mid=(l+r)/2
        fused=[i for i in range(1,len(y)) if abs(m[i]*(mid-y[i]))<lam*a[i-1]]
        unfused=[i for i in range(1,len(y)) if i not in fused]
        d=m[0]+sum((m[i] for i in fused),F(0))
        num=m[0]*y[0]+sum((m[i]*y[i] for i in fused),F(0))
        num-=sum((lam*a[i-1]*(1 if mid>y[i] else -1) for i in unfused),F(0))
        h=num/d
        if l<=h<=r and m[0]*(h-y[0])+sum((clip(m[i]*(h-y[i]),lam*a[i-1]) for i in range(1,len(y))),F(0))==0:
            root=h;break
    if root is None:
        # A root at a breakpoint: exact strict monotonicity makes it unique.
        for h in bp:
            if m[0]*(h-y[0])+sum((clip(m[i]*(h-y[i]),lam*a[i-1]) for i in range(1,len(y))),F(0))==0:
                root=h;break
    assert root is not None
    u=[root]
    for i in range(1,len(y)):
        d=y[i]-root
        threshold=lam*a[i-1]/m[i]
        u.append(root + (1 if d>=0 else -1)*max(abs(d)-threshold,F(0)))
    p=[clip(m[i]*(root-y[i]),lam*a[i-1]) for i in range(1,len(y))]
    assert m[0]*(u[0]-y[0])+sum(p)==0
    for i in range(1,len(y)):
        assert m[i]*(u[i]-y[i])-p[i-1]==0
        if u[i]>u[0]: assert p[i-1]==-lam*a[i-1]
        if u[i]<u[0]: assert p[i-1]==lam*a[i-1]
    return u


def good(m,a):
    return all(m[i]*sum((a[j-1] for j in range(1,len(m)) if j!=i),F(0))
               <=(m[0]+m[i])*a[i-1] for i in range(1,len(m)))


def main():
    y=list(map(F,[0,1,100,100,100]));m=[F(1)]*5;a=[F(1)]*4
    assert not good(m,a)
    assert solve(y,m,a,F(1,2))==[F(5,4),F(5,4),F(199,2),F(199,2),F(199,2)]
    assert solve(y,m,a,F(3,2))==[F(3),F(5,2),F(197,2),F(197,2),F(197,2)]
    tests=2
    r=Random(240117)
    for k in range(1,9):
        for repetition in range(75):
            masses=[F(r.randint(1,12)) for _ in range(k)]
            hubmass=F(k*15+r.randint(1,20))
            m=[hubmass]+masses
            ti=[mass/(hubmass+2*mass) for mass in masses]
            assert sum(ti)<1
            a=[x+(1-sum(ti))/k for x in ti]
            assert good(m,a)
            y=[F(r.randint(-15,15),r.randint(1,5)) for _ in range(k+1)]
            lams=[F(v,4) for v in range(0,65)]
            fused_prev=[False]*k
            for lam in lams:
                out=solve(y,m,a,lam)
                for j in range(k):
                    now=out[j+1]==out[0]
                    assert not (fused_prev[j] and not now), (k,repetition,j,lam)
                    fused_prev[j]=now
                tests+=k
    for k in range(3,9):
        m=[F(1)]*(k+1);a=[F(1)]*k
        if k>=4:
            assert not good(m,a)
            y=[F(0),F(1)]+[F(100000)]*(k-1)
            B=F(k-1); M=F(2); c=M*a[0]/m[1]
            lo=F(1)/(B+c);hi=F(1)/(B-c)
            lin=(lo+hi)/2; lout=hi+lo/3
            U1=solve(y,m,a,lin);U2=solve(y,m,a,lout)
            assert U1[0]==U1[1] and U2[0]!=U2[1]
            tests+=2
    print('PASS exact-rational KKT, explicit unfusion, weight-budget and monotone-grid tests:', tests)

if __name__=='__main__':main()
