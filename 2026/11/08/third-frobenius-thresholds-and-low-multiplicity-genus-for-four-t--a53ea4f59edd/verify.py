#!/usr/bin/env python3
"""Exact finite checks of four-generator representation thresholds (stdlib only)."""
from math import gcd

def threshold(a,d,t):
    def b(v): return v//3+1+(v%3==2)
    if t==0: u=d+b(a)
    elif t==1: u=d+b(a+1)
    elif t==2: u=d+(a+4)//3
    elif t==3: u=3
    else: u=(t+2)//3+1
    return a*u+d*t

def formulas(a,d):
    q,r=divmod(a,3)
    if r==0: f=a*(d+q)+2*d
    elif r==1: f=a*(d+q)+d+max(a,d)
    else: f=a*(d+q+1)+2*d
    h=3*d+2*a-1+(r==2)+sum((t+2)//3 for t in range(a))+(a-1)*(d-1)//2
    return f,h

def verify(a,d):
    assert a>=4 and d>=1 and gcd(a,d)==1
    mt=[threshold(a,d,t) for t in range(a)]
    f,h=formulas(a,d)
    assert max(mt)-a==f
    bound=max(mt)+2*a
    ways=[0]*(bound+1); ways[0]=1
    for coin in [a,a+d,a+2*d,a+3*d]:
        for n in range(coin,bound+1):
            ways[n]+=ways[n-coin]
    inv=pow(d,-1,a)
    for n,w in enumerate(ways):
        t=(inv*n)%a
        assert (w>=3)==(n>=mt[t]), (a,d,n,w,t,mt[t])
    assert sum(w<3 for w in ways)==h, (a,d,h)
    assert max(n for n,w in enumerate(ways) if w<3)==f
    return a,bound+1

def main():
    pairs=0; positions=0; residues=0
    for a in range(4,46):
        for d in range(1,29):
            if gcd(a,d)>1: continue
            aa,npos=verify(a,d)
            pairs+=1;positions+=npos;residues+=a
    for a,d in [(7,2),(7,9),(10,7),(13,17),(29,31),(37,53)]:
        aa,npos=verify(a,d)
        pairs+=1;positions+=npos;residues+=a
    print(f'VERIFY_OK parameter_pairs={pairs} residues={residues} checked_positions={positions} third_threshold_and_genus=exact')

if __name__=='__main__': main()
