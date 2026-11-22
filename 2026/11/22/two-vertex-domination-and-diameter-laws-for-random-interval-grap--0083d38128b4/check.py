#!/usr/bin/env python3
"""Exact equal-weight endpoint-pairing checks for random interval-graph domination and diameter."""
from fractions import Fraction
from math import comb
from collections import deque

def pairings(points):
    if not points:
        yield ()
        return
    a=points[0]
    for k in range(1,len(points)):
        b=points[k]
        for rest in pairings(points[1:k]+points[k+1:]):
            yield ((a,b),)+rest

def masks_of(iv):
    n=len(iv); m=[1<<i for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if max(iv[i][0],iv[j][0])<min(iv[i][1],iv[j][1]):
                m[i] |= 1<<j
                m[j] |= 1<<i
    return m

def diameter(m):
    n=len(m); dmax=0
    for root in range(n):
        q=deque([root]); dist={root:0}
        while q:
            i=q.popleft()
            for j in range(n):
                if ((m[i]>>j)&1) and j not in dist:
                    dist[j]=dist[i]+1;q.append(j)
        if len(dist)!=n:return -1
        dmax=max(dmax,max(dist.values()))
    return dmax

def run(n):
    totals=[0]*6
    # all order types are equiprobable under independent atomless endpoints
    for iv in pairings(tuple(range(2*n))):
        totals[0]+=1
        m=masks_of(iv); full=(1<<n)-1
        universal=any(x==full for x in m)
        complete=all(x==full for x in m)
        connected_pair=any((m[i]|m[j])==full and ((m[i]>>j)&1)
                            for i in range(n) for j in range(i+1,n))
        diam=diameter(m)
        assert (diam!=-1 and diam<=2)==universal
        assert (diam==1)==complete
        assert not connected_pair or (diam!=-1 and diam<=3)
        totals[1]+=universal
        totals[2]+=complete
        totals[3]+=connected_pair
        totals[4]+=(diam==2)
        totals[5]+=(diam==3)
        # Deterministic covering lemma at rational quantile endpoints.
        if n>=3:
            b=Fraction(1,5)
            l=[Fraction(x+1,2*n+1) for x,y in iv]
            r=[Fraction(y+1,2*n+1) for x,y in iv]
            t=min(r); M=max(l)
            left=any(l[i]<=b and r[i]>=Fraction(1,2) for i in range(n))
            right=any(l[i]<=Fraction(1,2) and r[i]>=1-b for i in range(n))
            if t>=b and M<=1-b and left and right:
                assert connected_pair
    N=totals[0]
    assert Fraction(totals[1],N)==Fraction(2,3)
    assert Fraction(totals[2],N)==Fraction(2**n,comb(2*n,n))
    assert Fraction(totals[4],N)==Fraction(2,3)-Fraction(2**n,comb(2*n,n))
    print(f'n={n}, order_types={N}, universal={Fraction(totals[1],N)}, complete={Fraction(totals[2],N)}, adjacent_dominating_pair={Fraction(totals[3],N)}, diameter3={Fraction(totals[5],N)}')

if __name__=='__main__':
    for n in range(2,8): run(n)
    print('All exhaustive order-type and deterministic implication tests passed.')
