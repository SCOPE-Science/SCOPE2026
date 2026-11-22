#!/usr/bin/env python3
"""Independently compute finite trace complexes for deranged pairings."""
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def pm_count(n):
    # Number of pairings avoiding all n prescribed disjoint edges.
    def double_fact(k):
        v=1
        for x in range(k, 0, -2):v*=x
        return v
    return sum((-1)**j*comb(n,j)*double_fact(2*n-2*j-1) for j in range(n+1))


def match_count(n,k):
    return sum((-1)**j*comb(n,j)*factorial(2*n-2*j)//(2**(k-j)*factorial(k-j)*factorial(2*n-2*k)) if j%2==0 else -comb(n,j)*factorial(2*n-2*j)//(2**(k-j)*factorial(k-j)*factorial(2*n-2*k)) for j in range(k+1))


def exact_family(n):
    verts=2*n
    edges=[(i,j) for i in range(verts) for j in range(i+1,verts) if i//2!=j//2]
    @lru_cache(None)
    def completions(mask):
        if mask==0:return ((),)
        a=(mask&-mask).bit_length()-1
        result=[]
        for b in range(a+1,verts):
            if (mask>>b)&1 and a//2!=b//2:
                for tail in completions(mask^(1<<a)^(1<<b)):
                    result.append(((a,b),)+tail)
        return tuple(result)
    pms=completions((1<<verts)-1)
    masks={e:0 for e in edges}
    for i,p in enumerate(pms):
        for e in p:masks[e]|=1<<i
    return edges, pms, masks


def shatter(S, positive_masks, fullmask):
    branches=[fullmask]
    for e in S:
        t=positive_masks[e]
        branches=[v&t for v in branches]+[v&~t for v in branches]
        if not all(branches):return False
    return True


def predicted(S,n):
    occupied=set()
    for a,b in S:
        if a in occupied or b in occupied:return False
        occupied.update((a,b))
    if len(S)>=n:return False
    if len(S)==n-1:
        a,b=sorted(set(range(2*n))-occupied)
        return a//2!=b//2
    return True


def run():
    instances=0
    for n in range(2,6):
        edges,pms,positive_masks=exact_family(n)
        fullmask=(1<<len(pms))-1
        counts=[]
        for k in range(n):
            found=0
            for S in combinations(edges,k):
                if k<=n-2:
                    for bits in range(1<<k):
                        target=tuple(e for i,e in enumerate(S) if bits>>i&1)
                        positive=fullmask
                        for i,e in enumerate(S):
                            positive &= positive_masks[e] if bits>>i&1 else ~positive_masks[e]
                        ismatching=len({v for e in target for v in e})==2*len(target)
                        assert bool(positive)==ismatching, (n,S,bits,"trace",bool(positive),ismatching)
                observed=shatter(S,positive_masks,fullmask)
                expected=predicted(S,n)
                assert observed==expected,(n,S,observed,expected)
                found+=observed
                instances+=1
            target=n*pm_count(n) if k==n-1 else match_count(n,k)
            assert found==target,(n,k,found,target)
            counts.append(found)
        assert len(pms)==pm_count(n),(n,len(pms),pm_count(n))
        print('n',n,'perfect_matchings',len(pms),'coefficients',counts)
    print('COCKTAIL_TRACE_PASS',instances,'direct support checks')

if __name__=='__main__':run()
