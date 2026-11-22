#!/usr/bin/env python3
"""Independent exhaustive maximum-clique checks in the Hamming-weight-two layer."""
from itertools import combinations, product

def words(n,q):
    for i,j in combinations(range(n),2):
        for a,b in product(range(1,q),repeat=2):
            w=[0]*n; w[i]=a;w[j]=b
            yield tuple(w)

def compatible(u,v):
    return all(u[:k]!=v[-k:] and v[:k]!=u[-k:] for k in range(1,len(u)))

def bound(n,q):
    m=q-1
    return m*m*((n-1)//2) if n%2 else m*m*(n//2-1)+m*m//4

def maximum_clique(words):
    m=len(words)
    adj=[0]*m
    for i in range(m):
        for j in range(i+1,m):
            if compatible(words[i],words[j]):
                adj[i]|=1<<j;adj[j]|=1<<i
    best=0
    def solve(P,size):
        nonlocal best
        if not P:
            best=max(best,size);return
        if size+P.bit_count()<=best:return
        # Greedy coloring bound on this induced compatibility graph.
        chrom=[]
        remain=P
        while remain:
            free=remain
            cls=0
            while free:
                bit=free&-free;free-=bit
                i=bit.bit_length()-1
                cls|=bit
                free &= ~adj[i]
            chrom.append(cls); remain &= ~cls
        if size+len(chrom)<=best:return
        for cls_idx in range(len(chrom)-1,-1,-1):
            cls=chrom[cls_idx]
            while cls:
                bit=cls&-cls;cls-=bit
                i=bit.bit_length()-1
                if P & bit:
                    solve((P&~bit)&adj[i],size+1)
                    P &= ~bit
                    if size+P.bit_count()<=best:return
    solve((1<<m)-1,0)
    return best

if __name__=='__main__':
    cases=[]
    for q,nmax in [(2,9),(3,7),(4,5),(5,4)]:
        for n in range(3,nmax+1):
            W=[w for w in words(n,q) if compatible(w,w)]
            measured=maximum_clique(W)
            predicted=bound(n,q)
            assert measured==predicted,(q,n,measured,predicted)
            cases.append((q,n,len(W),measured))
    print('EXHAUSTIVE_CLIQUE_CASES',len(cases))
    for q,n,c,z in cases:print('q=%d n=%d self_unbordered=%d optimum=%d'%(q,n,c,z))
    print('PASS')
