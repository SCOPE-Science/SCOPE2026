#!/usr/bin/env python3
"""Exhaustive binary first-periodic-entry check on four small toroidal grids.

Run: python3 verify_orbits.py. Standard library only. Direct state iteration
uses four independent graph-neighbor XORs, not any Jordan decomposition.
"""
from collections import Counter
from math import gcd


def predicted(m,n):
    mm,nn=m,n;a=b=1
    while mm%2==0:mm//=2;a*=2
    while nn%2==0:nn//=2;b*=2
    g=gcd(mm,nn);k=min(a,b);L=max(a,b)
    if L==1:
        C=lambda t:min(t,1)*(2*g-1)
        T=1
    else:
        C=lambda t:2*k*min(t,L//2)+2*(g-1)*k*min(t,L)
        T=L if g>1 else L//2
    d=m*n-C(T)
    counts={0:2**d}
    for t in range(1,T+1):counts[t]=2**d*(2**C(t)-2**C(t-1))
    return counts,T


def direct(m,n):
    N=m*n
    neighbors=[]
    for i in range(m):
        for j in range(n):
            neighbors.append(tuple(((i+di)%m)*n+((j+dj)%n) for di,dj in ((1,0),(-1,0),(0,1),(0,-1))))
    def step(v):
        w=0
        for k,nei in enumerate(neighbors):
            x=0
            for p in nei:x^=(v>>p)&1
            w|=x<<k
        return w
    T=predicted(m,n)[1]
    image=[step(1<<i) for i in range(N)]
    def faststep(v):
        out=0
        while v:
            lb=v&-v
            out^=image[lb.bit_length()-1]
            v^=lb
        return out
    # Directly iterate to Fitting image then test first entry via equality
    # with its periodic representative; no predetermined orbit period used.
    seen=Counter()
    for state in range(1<<N):
        hist=[]; cur=state; visits={}
        for t in range(T+20):
            if cur in visits:
                seen[visits[cur]]+=1
                break
            visits[cur]=t
            cur=faststep(cur)
        else:raise AssertionError('no cycle detected')
    return dict(seen)


def main():
    total=0
    for m,n in ((3,3),(3,4),(3,5),(4,4)):
        p,t=predicted(m,n)
        d=direct(m,n)
        assert d==p,(m,n,d,p)
        total+=1<<(m*n)
        print('PASS {}x{}: {} states; first-entry counts {}'.format(m,n,1<<(m*n),d))
    print('PASS exhaustive trajectories: {} labelled binary configurations'.format(total))
if __name__=='__main__':main()
