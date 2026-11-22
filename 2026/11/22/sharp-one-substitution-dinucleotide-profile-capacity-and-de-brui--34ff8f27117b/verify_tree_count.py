#!/usr/bin/env python3
"""Independent directed matrix-tree and BEST enumeration of order-three cycles."""
from math import factorial

def bareiss(A):
    a=[row[:] for row in A]
    n=len(a)
    sign=1
    last=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k]
            sign*=-1
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%last==0
                a[i][j]=numerator//last
        for i in range(k+1,n):a[i][k]=0
        last=pivot
    return sign*a[n-1][n-1]

for q in range(2,6):
    verts=[(a,b) for a in range(q) for b in range(q)]
    indices={v:i for i,v in enumerate(verts)}
    L=[[0]*(q*q) for _ in verts]
    for i,(a,b) in enumerate(verts):
        L[i][i]+=q
        for c in range(q):L[i][indices[(b,c)]]-=1
    arborescence=bareiss([row[:-1] for row in L[:-1]])
    assert arborescence==q**(q*q-3)
    cycles=arborescence*factorial(q-1)**(q*q)
    assert cycles==factorial(q)**(q*q)//q**3
    indexed=cycles*q**3
    assert indexed==factorial(q)**(q*q)
    print('q=%d arborescences=%d cyclic_debruijn=%d indexed_linear=%d'%
          (q,arborescence,cycles,indexed))
print('TREE_COUNT_PASS')
