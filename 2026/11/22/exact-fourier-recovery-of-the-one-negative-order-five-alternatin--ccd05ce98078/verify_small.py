"""Independent exact enumerator and direct low-degree signed sums, no FFT used."""
from itertools import product,combinations
from collections import Counter

def enumerate_asms(n):
    rows=[]
    for r in product([-1,0,1],repeat=n):
        partial=0; good=True
        for x in r:
            partial+=x
            if partial not in (0,1): good=False; break
        if good and partial==1: rows.append(r)
    def go(k,cols,grid):
        if k==n:
            if all(x==1 for x in cols):yield grid
            return
        for r in rows:
            nxt=tuple(cols[j]+r[j] for j in range(n))
            if all(v in (0,1) for v in nxt):yield from go(k+1,nxt,grid+(r,))
    return list(go(0,(0,)*n,tuple()))

asms=enumerate_asms(5)
assert len(asms)==429
one=[a for a in asms if sum(x==-1 for r in a for x in r)==1]
assert len(one)==200
# Encode by occupied cells independently of the C++ row-backtracker.
masks=[sum(1<<(5*i+j) for i,r in enumerate(a) for j,x in enumerate(r) if x) for a in one]
assert len(set(masks))==200
zero_counts=[]
for k in (1,2,3):
    zeros=[]
    for coords in combinations(range(25),k):
        character=sum(1<<p for p in coords)
        signed=sum(1 if (character & m).bit_count()%2==0 else -1 for m in masks)
        if signed==0:zeros.append(coords)
    zero_counts.append(len(zeros))
assert zero_counts==[0,12,200]
print('INDEPENDENT_LOW_DEGREE_PASS',len(asms),len(one),zero_counts)
