#!/usr/bin/env python3
"""Independent finite enumeration of VC/Littlestone dimensions for maximal-chain membership."""
from itertools import combinations, permutations
from math import factorial, comb
from functools import lru_cache

def stirling(n,k):
    if n==0: return int(k==0)
    if k<=0 or k>n: return 0
    return stirling(n-1,k-1)+k*stirling(n-1,k)

def eulerian(n,k):
    if n==1: return int(k==0)
    if k<0 or k>=n:return 0
    return (k+1)*eulerian(n-1,k)+(n-k)*eulerian(n-1,k-1)

def families(n):
    queries=list(range(1,(1<<n)-1))
    chains=[]
    for p in permutations(range(n)):
        cur=0;chain=set()
        for i in p:
            cur|=1<<i
            if cur!=(1<<n)-1:chain.add(cur)
        chains.append(chain)
    return queries, chains

def verify_faces(n):
    qs, cs=families(n)
    counts=[0]*n
    for k in range(n):
        for support in combinations(qs,k):
            traces={tuple(q in c for q in support) for c in cs}
            shattered=len(traces)==(1<<k)
            comparable=all((a&b)==a or (a&b)==b for a,b in combinations(support,2))
            assert shattered==comparable, (n,k,support)
            counts[k]+=shattered
        assert counts[k]==factorial(k+1)*stirling(n,k+1),(n,k,counts[k])
    return counts

def verify_ldim(n):
    qs,cs=families(n)
    full=(1<<len(cs))-1
    p_masks=[sum((1<<i) for i,c in enumerate(cs) if q in c) for q in qs]
    @lru_cache(None)
    def can(mask,depth):
        if depth==0: return mask!=0
        if mask.bit_count()<(1<<depth): return False
        for q in p_masks:
            yes=mask&q;no=mask&(~q)
            if yes.bit_count()>=(1<<(depth-1)) and no.bit_count()>=(1<<(depth-1)):
                if can(yes,depth-1) and can(no,depth-1): return True
        return False
    assert can(full,n-1)
    assert not can(full,n)
    return can.cache_info().currsize

if __name__=='__main__':
    for n in range(1,6):
        faces=verify_faces(n)
        states=verify_ldim(n)
        print('n',n,'faces',faces,'ldim',n-1,'DP_states',states)
    for n in range(1,10):
        f=[factorial(k+1)*stirling(n,k+1) for k in range(n)]
        h=[sum(f[k]*comb(n-1-k,j-k)*(-1)**(j-k) for k in range(j+1)) for j in range(n)]
        assert h==[eulerian(n,j) for j in range(n)],(n,h)
    print('BOOLEAN_CHAIN_SHATTERING_PASS face_n=1..5 ldim_n=1..5 eulerian_n=1..9')
