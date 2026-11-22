"""Exact integral certificate for the 30-vertex generalized-quadrangle graph state.
Run: python3 VERIFY_RANK.py (standard library only).
"""
from itertools import combinations

PAIRS=list(combinations(range(6),2))

def pair_partitions(vertices):
    if not vertices:
        yield ()
        return
    first=vertices[0]
    for partner in vertices[1:]:
        remaining=tuple(v for v in vertices[1:] if v!=partner)
        for tail in pair_partitions(remaining):
            yield ((first,partner),)+tail

LINES=list(pair_partitions(tuple(range(6))))
B=[[int(pair in line) for line in LINES] for pair in PAIRS]
FAULTS=[(9,0),(0,2),(5,6),(8,5),(6,10)]

def det_bareiss(A):
    n=len(A)
    if not n: return 1
    a=[row[:] for row in A]
    sign=1
    prev=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]!=0),None)
        if pivot is None: return 0
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*p-a[i][k]*a[k][j]
                assert value%prev==0
                a[i][j]=value//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def minor(A,rows,cols):
    return [[A[i][j] for j in cols] for i in rows]

assert len(PAIRS)==len(LINES)==15 and all(sum(row)==3 for row in B)
assert all(sum(B[i][j] for i in range(15))==3 for j in range(15))
assert all(B[i][j]==1 for i,j in FAULTS)
assert len({i for i,j in FAULTS})==len({j for i,j in FAULTS})==5
core_r=[i for i in range(15) if i not in {i for i,j in FAULTS}]
core_c=[j for j in range(15) if j not in {j for i,j in FAULTS}]
assert det_bareiss(minor(B,core_r,core_c))==-1
# Exhaustively establish a unit maximal minor for EVERY fault subset.
for mask in range(32):
    F=[(i,j) for k,(i,j) in enumerate(FAULTS) if mask>>k&1]
    C=[row[:] for row in B]
    for i,j in F:C[i][j]=0
    r=core_r+[i for i,j in F]
    c=core_c+[j for i,j in F]
    assert abs(det_bareiss(minor(C,r,c)))==1,(mask,'minor')
    if mask==31:assert det_bareiss(C)==-1
print('PASS: core determinant -1; all 32 fault subsets have the predicted unit maximal minors; full determinant -1.')
