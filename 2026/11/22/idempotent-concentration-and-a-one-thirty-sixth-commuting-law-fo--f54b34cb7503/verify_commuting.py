"""Reproduce small-degree commuting-pair counts for chain partial isometries.
The proof for all sizes is analytic; this finite test is corroborative only.
"""
from itertools import combinations

def monoid(n):
    maps=set()
    maps.add((-1,)*n)
    for a in range(n):
        for b in range(n):
            x=[-1]*n; x[a]=b; maps.add(tuple(x))
    for sign in (-1,1):
        for offset in range(-2*n,2*n+1):
            support=[i for i in range(n) if 0<=sign*i+offset<n]
            for k in range(2,len(support)+1):
                for chosen in combinations(support,k):
                    f=[-1]*n
                    for i in chosen: f[i]=sign*i+offset
                    maps.add(tuple(f))
    return sorted(maps)

def compose(a,b):
    return tuple(b[x] if x>=0 else -1 for x in a)

for n in range(2,8):
    maps=monoid(n)
    assert len(maps)==6*2**n-n*n-4*n-5,(n,len(maps))
    ids={f for f in maps if all(y<0 or y==x for x,y in enumerate(f))}
    assert len(ids)==2**n
    commuting=0; nonidem=0
    for a in maps:
        for b in maps:
            if compose(a,b)==compose(b,a):
                commuting+=1
                if a not in ids or b not in ids: nonidem+=1
    assert commuting==4**n+nonidem
    print(f'n={n}: elements={len(maps)}, commuting_pairs={commuting}, idempotent_pairs={4**n}, other_commuting_pairs={nonidem}, probability={commuting/len(maps)**2:.9f}')
print('CHAIN_PARTIAL_ISOMETRY_COMMUTING_CHECKS_PASSED')
