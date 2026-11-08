#!/usr/bin/env python3
"""Exact rational incidence and Picard-lattice span checks for the Clebsch cubic."""
from itertools import combinations
from fractions import Fraction

def rank(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    r=0
    if not a:return 0
    m=len(a[0])
    for c in range(m):
        k=next((i for i in range(r,len(a)) if a[i][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        z=a[r][c];a[r]=[x/z for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

lines=[]
for z in range(5):
    rr=[i for i in range(5) if i!=z]
    for pairs in [((rr[0],rr[1]),(rr[2],rr[3])),
                  ((rr[0],rr[2]),(rr[1],rr[3])),
                  ((rr[0],rr[3]),(rr[1],rr[2]))]:
        a=[0]*5;b=[0]*5
        a[pairs[0][0]]=1;a[pairs[0][1]]=-1
        b[pairs[1][0]]=1;b[pairs[1][1]]=-1
        lines.append((a,b))
assert len(lines)==15
meet=lambda i,j: rank([*lines[i],*lines[j]])<4
A=[[int(i!=j and meet(i,j)) for j in range(15)] for i in range(15)]
assert all(sum(row)==6 for row in A)
assert sum(sum(row) for row in A)==90
M=[[(-1 if i==j else A[i][j]) for j in range(15)] for i in range(15)]
assert rank(M)==6
# The incidence matrix has strongly regular (15,6,1,3) parameters.
assert all(sum(A[i][k]*A[k][j] for k in range(15)) == (1 if A[i][j] else 3)
           for i in range(15) for j in range(i+1,15))
# Each line contains precisely the two triple points at a=0 and b=0;
# the two additional intersections occur at a=b and a=-b.
print('VERIFY_CLEBSCH_INCIDENCE_OK lines=15 graph_edges=45 picard_span=6')
