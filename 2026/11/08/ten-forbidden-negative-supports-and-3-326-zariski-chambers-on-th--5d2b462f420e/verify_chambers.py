"""Exact chamber-support verification for an I9+I1+I1+I1 rational elliptic surface.

Run: python3 elliptic_chamber_verify.py
Uses only the Python standard library.
"""
from collections import Counter
from fractions import Fraction

N=12
A=[[0]*N for _ in range(N)]
for i in range(9):
    A[i][i]=2
    A[i][(i+1)%9]=A[(i+1)%9][i]=-1
for k,vertex in enumerate((0,3,6)):
    i=9+k
    A[i][i]=1
    A[i][vertex]=A[vertex][i]=-1

def positive_definite(mask):
    idx=[i for i in range(N) if mask>>i&1]
    b=[[Fraction(A[i][j]) for j in idx] for i in idx]
    while b:
        pivot=b[0][0]
        if pivot<=0:return False
        if len(b)==1:return True
        b=[[b[i][j]-b[i][0]*b[0][j]/pivot
            for j in range(1,len(b))] for i in range(1,len(b))]
    return True

def encode(indices):
    return sum(1<<i for i in indices)

full=encode(range(9))
star=[encode([i,(i-1)%9,(i+1)%9,9+i//3]) for i in (0,3,6)]
paths=[]
for i,j in ((0,3),(3,6),(6,0)):
    for step in (1,-1):
        cur=i;verts=[cur]
        while cur!=j:
            cur=(cur+step)%9
            verts.append(cur)
        paths.append(encode(verts+[9+i//3,9+j//3]))
forbidden=sorted([full]+star+paths)
assert len(forbidden)==10 and len(set(forbidden))==10
poly=Counter(); valid=set(); invalid=set(); differing=[]
for mask in range(1<<N):
    by_forbidden=all(mask & b != b for b in forbidden)
    by_sylvester=positive_definite(mask)
    if by_forbidden != by_sylvester:
        differing.append(mask)
    (valid if by_sylvester else invalid).add(mask)
    if by_sylvester:poly[mask.bit_count()]+=1
assert not differing, differing
minimal=sorted(m for m in invalid
               if all((m ^ (1<<i)) in valid for i in range(N) if m>>i&1))
assert minimal==forbidden,(minimal,forbidden)
expected=[1,12,66,220,492,768,837,612,270,48,0,0,0]
assert [poly[i] for i in range(N+1)]==expected,poly
assert sum(expected)==3326
print('ALL_4096_SUBSETS_CHECKED')
print('MINIMAL_FORBIDDEN_MASKS',forbidden)
print('MINIMAL_FORBIDDEN_COUNT',len(forbidden))
print('CHAMBER_SUPPORT_POLYNOMIAL',expected)
print('ZARISKI_CHAMBERS',sum(expected))
print('MAXIMAL_SUPPORT_SIZE',max(poly))
print('EXACT_FORBIDDEN_AND_SYLVESTER_METHODS_AGREE')
