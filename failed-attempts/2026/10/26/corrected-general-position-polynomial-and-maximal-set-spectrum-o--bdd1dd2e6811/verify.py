"""Verify shortest-path general-position sets of crown graphs independently."""
from collections import Counter
from itertools import combinations
from math import comb

def bfs_distances(n):
    size=2*n
    neighbors=[[] for _ in range(size)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                neighbors[i].append(n+j)
                neighbors[n+j].append(i)
    out=[]
    for source in range(size):
        ds=[-1]*size
        ds[source]=0
        q=[source]
        for v in q:
            for w in neighbors[v]:
                if ds[w]<0:
                    ds[w]=ds[v]+1
                    q.append(w)
        assert all(d>=0 for d in ds)
        out.append(ds)
    return out

def census(n):
    d=bfs_distances(n)
    size=2*n
    bad_masks=[]
    for a,b,c in combinations(range(size),3):
        if (d[a][b]==d[a][c]+d[c][b] or d[a][c]==d[a][b]+d[b][c] or
            d[b][c]==d[b][a]+d[a][c]):
            bad_masks.append((1<<a)|(1<<b)|(1<<c))
    good=set()
    counts=Counter()
    for mask in range(1<<size):
        if not any((mask&bad)==bad for bad in bad_masks):
            good.add(mask)
            counts[mask.bit_count()]+=1
    expected=[0]*(n+1)
    expected[0]=1
    expected[1]=2*n
    expected[2]=comb(2*n,2)
    for k in range(3,n+1):expected[k]=2*comb(n,k)
    assert [counts.get(i,0) for i in range(n+1)]==expected,(n,counts,expected)
    assert max(counts)==n
    maximals={mask for mask in good if not any(mask | (1<<v) in good for v in range(size) if not mask & (1<<v))}
    target={((1<<n)-1),(((1<<n)-1)<<n)}
    target|={(1<<i)|(1<<(n+j)) for i in range(n) for j in range(n)}
    assert maximals==target,(n,maximals.symmetric_difference(target))
    print(f'n={n} subsets={1<<size} forbidden_triples={len(bad_masks)} GP_counts={expected} maximal_pairs={n*n} maximal_sides=2')

for n in range(3,9):census(n)
# Table/formula as printed in Iršič et al., Results Math 79 (2024), Prop. 4.3.
for r in range(3,9):
    actual_cubic=2*comb(r,3)
    printed_cubic=4*comb(r,2)+2*comb(r,3)
    actual_quartic=2*comb(r,4)
    printed_quartic=comb(r,2)+2*comb(r,4)
    assert printed_cubic-actual_cubic==4*comb(r,2)
    assert printed_quartic-actual_quartic==comb(r,2)
    print(f'printed_gap_r={r} cubic_excess={printed_cubic-actual_cubic} quartic_excess={printed_quartic-actual_quartic}')
print('VERIFY_OK')
