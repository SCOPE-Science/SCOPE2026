#!/usr/bin/env python3
"""Separate elementary bit-count census and parity-correspondence check.
Requires Python 3.10+ only. Run: python verify_parity.py
"""
from collections import Counter
from math import comb

def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0

def formula(n,t):
    u=n-t;k=n//2
    per={}
    for a in range(t+1):
        if n%2:
            x=choose(u,k-a)+choose(u,k+1-a)
            y=choose(u,k-t+a)+choose(u,k+1-t+a)
        else:
            x=choose(u,k-a)
            y=choose(u,k-t+a)
        if x*y:per[a]=x*y
    total=sum(choose(t,a)*v for a,v in per.items())
    classes= sum(choose(t,a) for a in per) if n%2 else total
    return total,classes,per

def cut(a,b,n,t):
    x=a.bit_count();y=b.bit_count()
    return x*(n-x)+y*(n-y)+((a^b)&((1<<t)-1)).bit_count()

def census(n,t):
    m=(1<<n)-1
    target=2*(n*n//4)+t
    per=Counter()
    max_observed=-1
    for a in range(1<<n):
        for b in range(1<<n):
            q=cut(a,b,n,t)
            if q>max_observed:max_observed=q
            if q==target:
                per[(a&((1<<t)-1)).bit_count()]+=1
                # Check every one-step allowed update stays within maximizers.
                bits=[(a>>i)&1 for i in range(n)]+[(b>>i)&1 for i in range(n)]
                for side in range(2):
                    c= a if side==0 else b
                    other= b if side==0 else a
                    for i in range(n):
                        state=(c>>i)&1
                        own= c.bit_count() if state else n-c.bit_count()
                        if i<t:
                            own += int(((other>>i)&1)==state)
                            opposite=n+1-own
                        else:
                            opposite=n-own
                        if own>opposite:
                            c2=c^(1<<i)
                            nxt=cut(c2,other,n,t) if side==0 else cut(other,c2,n,t)
                            assert nxt==target,(n,t,a,b,side,i,nxt)
    assert max_observed==target,(n,t,max_observed,target)
    return sum(per.values()),per

if __name__=='__main__':
    total_configs=0;instances=0
    counts={}
    for n in range(2,9):
        for t in range(n+1):
            actual,per=census(n,t)
            total,classes,f=formula(n,t)
            assert total==actual,(n,t,total,actual)
            assert per==Counter({a:choose(t,a)*v for a,v in f.items()}),(n,t,per,f)
            counts[n,t]=total
            total_configs+=1<<(2*n);instances+=1
            print(f'n={n} t={t} recurrent={total} classes_formula={classes}')
    for n in (3,5,7):
        for t in range(n+1):
            assert counts[n,t]==counts[n+1,t],(n,t)
    print(f'PASS parity: instances={instances}, labelled_configurations={total_configs}, odd-even_pairs=3, equalities=15')
