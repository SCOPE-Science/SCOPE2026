"""Independent direct-neighborhood exhaustive check (no root-degree identity used).
Tests all subsets of vertices of the triangular graphs for n=3,...,7.
"""
from itertools import combinations

for n in range(3,8):
    edges=list(combinations(range(n),2)); m=len(edges)
    neighborhoods=[]
    for i,(a,b) in enumerate(edges):
        neigh=0
        for j,(c,d) in enumerate(edges):
            if i==j or len({a,b,c,d})<4:
                neigh|=1<<j
        neighborhoods.append(neigh)
    counts=[0]*(m+1)
    maximal=[0]*(m+1)
    for mask in range(1<<m):
        if any((mask & nm).bit_count()>3 for nm in neighborhoods):
            continue
        k=mask.bit_count(); counts[k]+=1
        if not any(
            not (mask & (1<<i)) and all((((mask|(1<<i))&nm).bit_count()<=3) for nm in neighborhoods)
            for i in range(m)
        ):
            maximal[k]+=1
    print(n,','.join(f'{k}:{v}' for k,v in enumerate(counts) if v),','.join(f'{k}:{v}' for k,v in enumerate(maximal) if v),sep='\t')
