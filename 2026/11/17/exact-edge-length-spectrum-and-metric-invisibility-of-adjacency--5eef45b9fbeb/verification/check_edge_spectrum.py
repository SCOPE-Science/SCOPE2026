"""Exact independent checks for the Euclidean edge spectrum of derangement matching polytopes.

Uses only the Python standard library. Execute with:
    python verification/check_edge_spectrum.py
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def rook_cycle(k):
    return [2*k * comb(2*k-j,j) // (2*k-j) for j in range(k+1)]


def permitted_pairs(n,k):
    # Count permutations avoiding one forbidden diagonal outside k selected rows
    # and both cycle-generated forbidden diagonals inside them.
    r=rook_cycle(k)
    return sum((-1)**j * factorial(n-j) * sum(
        comb(n-k,j-t)*r[t]
        for t in range(max(0,j-(n-k)), min(j,k)+1)
    ) for j in range(n+1))


def theoretical_spectrum(n):
    return {k:comb(n,k)*factorial(k-1)*permitted_pairs(n,k)//2
            for k in range(2,n+1)}


def nontrivial_cycle_lengths(a,b):
    n=len(a)
    inv=[None]*n
    for i,v in enumerate(a):
        inv[v]=i
    t=[inv[v] for v in b]
    seen=set()
    cyc=[]
    for i in range(n):
        if i in seen:
            continue
        x=i; length=0
        while x not in seen:
            seen.add(x); length+=1; x=t[x]
        if length>1:
            cyc.append(length)
    return cyc


def direct_spectrum(n):
    arr=[p for p in permutations(range(n)) if all(i!=p[i] for i in range(n))]
    tally=Counter()
    pair_distances=Counter()
    for i,p in enumerate(arr):
        for q in arr[:i]:
            shared=sum(x==y for x,y in zip(p,q))
            pair_distances[shared]+=1
            c=nontrivial_cycle_lengths(p,q)
            if len(c)==1:
                assert 2*(n-shared)==2*c[0]
                tally[c[0]]+=1
    return dict(tally),len(arr),pair_distances


def independently_count_cycle_rooks(k):
    # Matchings in the forbidden 2k-cycle: each chosen edge excludes both neighbours.
    n=2*k
    out=Counter()
    for size in range(k+1):
        for edges in combinations(range(n),size):
            s=set(edges)
            if all((i+1)%n not in s for i in s):
                out[size]+=1
    return [out[j] for j in range(k+1)]


def main():
    for k in range(2,7):
        assert independently_count_cycle_rooks(k)==rook_cycle(k)
    for n in range(3,8):
        spectrum,verts,pairs=direct_spectrum(n)
        target=theoretical_spectrum(n)
        assert all(spectrum.get(k,0)==v for k,v in target.items()),(n,spectrum,target)
        assert sum(pairs.values())==verts*(verts-1)//2
        assert sum(target.values())<=sum(pairs.values())
        print('n',n,'vertices',verts,'edge_counts',target)
    print('DERANGEMENT_EDGE_SPECTRUM_PASS n=3..7; cycle_rooks k=2..6')

if __name__=='__main__':
    main()
