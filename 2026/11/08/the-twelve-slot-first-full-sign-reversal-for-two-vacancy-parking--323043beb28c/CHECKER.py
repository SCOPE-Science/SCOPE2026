#!/usr/bin/env python3
"""Exact integer certificate for pairwise occupancy correlations with two empty sites."""
from itertools import permutations, product
from math import factorial
from fractions import Fraction as F
def expected(n, m, mask):
    assert mask.bit_count() == m
    runs = []
    r = 0
    for i in range(n):
        if mask >> i & 1:
            r += 1
        elif r:
            runs.append(r)
            r = 0
    if r:
        runs.append(r)
    count = factorial(m)
    for r in runs:
        count *= (r+1)**(r-1)
        count //= 1 # ensure numerator intact
    denom = n**m
    for r in runs:
        denom *= factorial(r)
    return F(count,denom)

def evolve(n, previous, p):
    nxt={}
    for mask, mass in previous.items():
        for a in range(n):
            if not ((mask >> a) & 1):
                target=[(a,F(1))]
            else:
                left = next((j for j in range(a-1,-1,-1) if not (mask>>j)&1),None)
                right = next((j for j in range(a+1,n) if not (mask>>j)&1),None)
                target=[]
                if left is not None:
                    target.append((left,1-p))
                if right is not None:
                    target.append((right,p))
            for j,w in target:
                mm=mask|(1<<j)
                nxt[mm]=nxt.get(mm,F(0))+mass*w/n
    return nxt



def park_weights(n):
    assert n>=4
    m=n-2
    W={}
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            lengths=(a-1,b-a-1,n-b)
            v=factorial(m)
            for r in lengths:
                if r:
                    v*= (r+1)**(r-1)
                v//=1
            for r in lengths:
                v//=1 # keep exact integer until complete denominator
            denominator=1
            for r in lengths:
                denominator*=factorial(r)
            assert v%denominator==0
            W[a,b]=v//denominator
    return W

def certificate(n):
    W=park_weights(n)
    Z=sum(W.values())
    A={i:sum(w for pair,w in W.items() if i in pair) for i in range(1,n+1)}
    Q=[Z*W[i,i+1]-A[i]*A[i+1] for i in range(1,n)]
    assert all(q!=0 for q in Q)
    return Z,A,Q

def direct_counts(n):
    # Verify W by independent direct enumeration of preferences for all-forward parking.
    m=n-2
    counts={}
    for prefs in product(range(1,n+1),repeat=m):
        occ=0
        for a in prefs:
            j=next((j for j in range(a,n+1) if not (occ>>(j-1))&1),None)
            if j is None:break
            occ|=1<<(j-1)
        else:
            holes=tuple(i for i in range(1,n+1) if not (occ>>(i-1))&1)
            counts[holes]=counts.get(holes,0)+1
    return counts

def run():
    checks=0
    for n in range(4,13):
        Z,A,Q=certificate(n)
        positions=''.join('+' if q>0 else '-' for q in Q)
        print(n,'Z=',Z,'signs=',positions,'minQ=',min(Q),'maxQ=',max(Q))
        checks+=len(Q)
        if n<=7:
            counts=direct_counts(n)
            W=park_weights(n)
            assert counts==W,(n,counts,W)
            checks+=len(W)
    assert all(q>0 for q in certificate(12)[2]);checks+=11
    W=park_weights(12)
    Z,A,_=certificate(12)
    for (i,j),w in W.items():
        Q=Z*w-A[i]*A[j]
        assert (Q>0)==(j==i+1),(i,j,Q)
        checks+=1
    assert min((Z*W[i,i+1]-A[i]*A[i+1] for i in range(1,12))) == 581409157300000000
    assert max((Z*w-A[i]*A[j] for (i,j),w in W.items() if j>i+1)) == -3692131919133336000
    checks+=2
    for n in range(4,12):
        assert min(certificate(n)[2])<0
        checks+=1
    # Independently compute p=0,1/3,1, and alternating p_i for n<=7 with the separate DP.
    for n in range(4,8):
        for typ in range(4):
            pmf={0:F(1)}
            for step in range(n-2):
                p=(F(0),F(1),F(1,3),F((step%3)+1,4))[typ]
                pmf=evolve(n,pmf,p)
            W=park_weights(n)
            for (a,b),w in W.items():
                mask=((1<<n)-1)^(1<<(a-1))^(1<<(b-1))
                assert pmf.get(mask,F(0))==F(w,n**(n-2))
                checks+=1
    print('PASSED',checks,'independent exact assertions')
if __name__=='__main__':run()
