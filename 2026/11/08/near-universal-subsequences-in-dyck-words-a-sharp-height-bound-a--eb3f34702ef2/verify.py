#!/usr/bin/env python3
"""Independent finite checks for the Dyck subsequence-universality formulas.
Run: python3 verify.py. Requires only the Python standard library.
"""
from collections import Counter
from functools import lru_cache
from math import comb

@lru_cache(None)
def dyck(n):
    if n == 0:
        return ('',)
    return tuple('0'+a+'1'+b for i in range(n) for a in dyck(i) for b in dyck(n-1-i))

def index_greedy(w):
    k=0; seen=None
    for c in w:
        if seen is None:
            seen=c
        elif seen!=c:
            k+=1;seen=None
    return k

def is_subsequence(v,w):
    p=0
    for c in w:
        if p<len(v) and c==v[p]:p+=1
    return p==len(v)

def index_definition(w):
    k=0
    while all(is_subsequence(format(a,'0%db'%(k+1)),w) for a in range(1<<(k+1))):
        k+=1
    return k

def height(w):
    s=h=0
    for c in w:
        s+=1 if c=='0' else -1
        h=max(h,s)
    assert s==0
    return h

cases=0
for n in range(1,12):
    words=dyck(n)
    counts=Counter(index_greedy(w) for w in words)
    assert counts[n]==1
    if n>=2: assert counts[n-1]==2**(n-1)-1,(n,counts)
    if n>=3: assert counts[n-2]==(n-2)*(n+1)*2**(n-5),(n,counts)
    high=[w for w in words if index_greedy(w)>=n-1]
    assert len(high)==2**(n-1)
    assert all((height(w)<=2)==(index_greedy(w)>=n-1) for w in words)
    assert all(index_greedy(w)<=n-height(w)+1 for w in words)
    peak_counts=Counter(sum(w[i:i+2]=='01' for i in range(2*n-1)) for w in high)
    assert peak_counts==Counter({p:comb(n,2*p-n) for p in range((n+1)//2,n+1)}),(n,peak_counts)
    if n<=6:
        assert all(index_greedy(w)==index_definition(w) for w in words)
    cases+=len(words)
print(f'VERIFY_OK n=1..11 dyck_words={cases} direct_definition_n=1..6 height_bound=PASS peak_distribution=PASS')
