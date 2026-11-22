#!/usr/bin/env python3
"""Exact rational diagnostic for triangle-square bouquet jamming laws."""
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict

count=0

def insist(a,b):
    global count
    assert a == b,(a,b)
    count+=1

def make_graph(r):
    adj=[0]*(2*r+4)
    def edge(i,j):
        adj[i]|=1<<j; adj[j]|=1<<i
    for k in range(r):
        a,b=2*k+1,2*k+2
        edge(0,a);edge(0,b);edge(a,b)
    a,b,c=2*r+1,2*r+2,2*r+3
    edge(0,a);edge(a,b);edge(b,c);edge(c,0)
    return adj

def direct(r):
    adj=make_graph(r); n=len(adj); full=(1<<n)-1
    closed=[(1<<i)|adj[i] for i in range(n)]
    @lru_cache(None)
    def rec(avail):
        if not avail: return {0:Fraction(1)}
        choices=[j for j in range(n) if avail&(1<<j)]
        ans=defaultdict(Fraction)
        for j in choices:
            for k,p in rec(avail&~closed[j]).items():
                ans[k+1]+=p/len(choices)
        return dict(ans)
    freqs=defaultdict(int)
    for mask in range(1<<n):
        if any(mask&(1<<j) and mask&adj[j] for j in range(n)):continue
        if any(not(mask&(1<<j) or mask&adj[j]) for j in range(n)):continue
        freqs[mask.bit_count()]+=1
    total=sum(freqs.values())
    return rec(full),{k:Fraction(v,total) for k,v in freqs.items()}

def laws(r):
    p=Fraction(r+1,(r+2)*(2*r+1))
    q=Fraction(2*r,3*(2*r+1))
    a=Fraction(1,1+2**(r+1))
    b=Fraction(2**r,1+2**(r+1))
    return {2:p,r+1:q,r+2:1-p-q},{2:a,r+1:b,r+2:b}

for r in range(2,5):
    seq,stat=direct(r)
    exp_seq,exp_stat=laws(r)
    insist(seq,exp_seq);insist(stat,exp_stat)
    insist(sum(seq.values()),Fraction(1));insist(sum(stat.values()),Fraction(1))
for r in range(2,81):
    s,t=laws(r)
    insist(s[2]>t[2],True)
    insist(s[2]+s[r+1]<t[2]+t[r+1],True)
    insist(t[r+1]>s[r+1],True)
    tv=sum((abs(s[k]-t[k]) for k in s),Fraction(0))/2
    insist(tv,t[r+1]-s[r+1])
    insist(s[r+2]>t[r+2],True)
    # Independent integral evaluation via beta moments.
    denom=(2*r+1)*(2*r+2)*(2*r+3)
    hub=Fraction(1,2*r+3)+Fraction(2,denom)-Fraction(4,denom*(2*r+4))
    insist(hub,s[2])
print(f'PASS: {count} exact assertions')
