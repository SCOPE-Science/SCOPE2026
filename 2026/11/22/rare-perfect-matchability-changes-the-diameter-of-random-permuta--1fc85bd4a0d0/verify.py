#!/usr/bin/env python3
"""Exact independent checks for matching and leaf laws of random permutation inversion trees."""
import itertools, math, collections
from functools import lru_cache

def permutation_from_word(word):
    p=[2,1]
    for op in word:
        n=len(p)
        if op==0: p.insert(-1,n+1)
        else: p=[(n+1 if v==n else v) for v in p]+[n]
    return p

def tree_edges(p):
    return {(min(p[i],p[j]),max(p[i],p[j])) for i in range(len(p)) for j in range(i+1,len(p)) if p[i]>p[j]}

def has_perfect_matching(n,edges):
    # Independent exact subset recursion, not the four-state derivation
    if n%2: return False
    N=[0]*(n+1)
    for u,v in edges: N[u]|=1<<(v-1);N[v]|=1<<(u-1)
    memo={0:True}
    def search(mask):
        if mask in memo:return memo[mask]
        b=mask & -mask; i=b.bit_length()
        z=mask^b; q=z&N[i]
        while q:
            bb=q&-q;q-=bb
            if search(z^bb): memo[mask]=True;return True
        memo[mask]=False;return False
    return search((1<<n)-1)

def structural_flags(n, edges, last, greatest):
    # Independent subset matching test for every prescribed terminal-status pair.
    nbr=[0]*(n+1)
    for u,v in edges:
        nbr[u]|=1<<(v-1);nbr[v]|=1<<(u-1)
    @lru_cache(None)
    def can_cover(mask):
        if not mask:return True
        bit=mask&-mask; i=bit.bit_length()
        rest=mask^bit
        v=rest&nbr[i]
        while v:
            b=v&-v;v-=b
            if can_cover(rest^b):return True
        return False
    base=((1<<n)-1)^((1<<(last-1))|(1<<(greatest-1)))
    return {(a,b) for a in (0,1) for b in (0,1) if
            can_cover(base|(a<<(last-1))|(b<<(greatest-1)))}

def symbolic_flags(bits):
    state={(0,0),(1,1)}
    for op in bits:
        nxt=set()
        if op==0:
            if (0,1) in state:nxt|={(0,0),(1,1)}
            if (1,1) in state:nxt.add((1,0))
        else:
            if (1,0) in state:nxt|={(0,0),(1,1)}
            if (1,1) in state:nxt.add((0,1))
        state=nxt
    return state

def run():
    ntests=0
    for n in range(2,15):
        counter=collections.Counter(); seen=set()
        for bits in itertools.product((0,1),repeat=n-2):
            p=permutation_from_word(bits)
            E=tree_edges(p)
            assert len(E)==n-1
            assert tuple(p) not in seen;seen.add(tuple(p))
            degrees=collections.Counter(v for edge in E for v in edge)
            L=sum(degrees[v]==1 for v in range(1,n+1))
            eq=2+sum(bits[i]==bits[i-1] for i in range(1,len(bits)))
            if n>=3:assert eq==L
            pm=has_perfect_matching(n,E)
            expected=(n%2==0 and all(bits[i]!=bits[i+1] for i in range(0,len(bits),2)))
            assert pm==expected, (n,bits,p,E)
            assert structural_flags(n,E,p[-1],n)==symbolic_flags(bits), (n,bits,p,E)
            counter[(pm,L)]+=1; ntests+=(5 if n>=3 else 4)
        if n%2==0:
            m=n//2
            assert sum(c for (pm,l),c in counter.items() if pm)==2**(m-1)
            ntests+=1
            if m>=2:
                for r in range(0,m-1):
                    assert counter[(True,r+2)]==2**(m-1-(m-2))*math.comb(m-2,r)
                    assert sum(c for (pm,l),c in counter.items() if l==r+2)==2*math.comb(n-3,r)
                    ntests+=2
        print('n',n,'perfect',sum(c for (pm,l),c in counter.items() if pm),'trees',len(seen),'hist',sorted((l,c) for (pm,l),c in counter.items() if pm))
    print('VERIFIED: exhaustive checks',ntests,'independent subset matching recursion')
if __name__=='__main__':run()
