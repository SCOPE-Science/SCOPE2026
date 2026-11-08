#!/usr/bin/env python3
"""Finite checks of creation-word maximal independent set online shattering.
Only standard Python; deterministic, no files or network needed.
"""
from functools import lru_cache
from itertools import product

def concepts(word):
    n=len(word)
    fullzero=sum(1<<i for i in range(n) if word[i]=='0')
    assert word[0]=='0'
    out=[fullzero]
    for k in range(1,n):
        if word[k]=='1':
            s=(1<<k) | sum(1<<i for i in range(k+1,n) if word[i]=='0')
            out.append(s)
    return tuple(out)

def graph_concepts(word):
    n=len(word)
    edges={(i,j) for i in range(n) for j in range(i+1,n) if word[j]=='1'}
    ans=[]
    for s in range(1<<n):
        if any((s>>i)&1 and (s>>j)&1 for i,j in edges):continue
        if any(not((s>>i)&1) and not any((s>>j)&1 and ((min(i,j),max(i,j)) in edges) for j in range(n) if i!=j) for i in range(n)):continue
        ans.append(s)
    return tuple(ans)

def littlestone_brute(C, n):
    @lru_cache(None)
    def rec(X):
        if len(X)<2:return 0
        best=0
        for i in range(n):
            L=tuple(v for v in X if (v>>i)&1)
            R=tuple(v for v in X if not((v>>i)&1))
            if L and R:best=max(best,1+min(rec(L),rec(R)))
        return best
    return rec(tuple(sorted(C)))

def recurrence(word):
    d=word.count('1')
    if not d:return 0
    cuts=set()
    j=0
    for c in word:
        if c=='0':cuts.add(j+1)
        else:j+=1
    @lru_cache(None)
    def r(i,j):
        if i==j:return 0
        best=1
        for k in cuts:
            if i<k<=j:
                best=max(best,1+min(r(i,k-1),r(k,j)))
        return best
    return r(0,d)

def vc(C,n):
    ans=0
    for s in range(1<<n):
        if len({v&s for v in C}) == 1<<s.bit_count(): ans=max(ans,s.bit_count())
    return ans

tried=0
minimum={}
for n in range(1,12):
    bylevel={}
    for bits in product('01', repeat=n-1):
        w='0'+''.join(bits)
        C=concepts(w)
        if n<=8:
            assert tuple(sorted(C))==tuple(sorted(graph_concepts(w))),w
        x=littlestone_brute(C,n)
        y=recurrence(w)
        assert x==y,(w,x,y)
        z=vc(C,n)
        assert z==(0 if w.count('1')==0 else 1),(w,z)
        bylevel[x]=bylevel.get(x,0)+1
        minimum.setdefault(x,(n,w))
        tried+=1
    print('n=',n,'profiles=',2**(n-1),'rank_counts=',sorted(bylevel.items()))
print('all words',tried,'first rank examples',sorted(minimum.items()))
assert minimum[1][0]==2
assert minimum[2][0]==5
assert minimum[3][0]==11
print('THRESHOLD_ONLINE_PASS',tried,'minimum_ranks',sorted((k,v[0]) for k,v in minimum.items()))
