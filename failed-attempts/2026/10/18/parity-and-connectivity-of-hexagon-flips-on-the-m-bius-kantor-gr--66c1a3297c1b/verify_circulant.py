#!/usr/bin/env python3
"""Independent circulant-biadjacency computation: determinant, permanent, flips."""
from collections import Counter
from itertools import permutations
B=[[int((j-i)%8 in (0,1,3)) for j in range(8)] for i in range(8)]

def determinant(A):
    # Integer-preserving Bareiss elimination on an exact 8-by-8 matrix.
    A=[row[:] for row in A];sgn=1;old=1
    for k in range(len(A)-1):
        if not A[k][k]:
            r=next(i for i in range(k+1,len(A)) if A[i][k])
            A[k],A[r]=A[r],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,len(A)):
            for j in range(k+1,len(A)):
                n=A[i][j]*pivot-A[i][k]*A[k][j]
                assert n%old==0
                A[i][j]=n//old
        for i in range(k+1,len(A)):A[i][k]=0
        old=pivot
    return sgn*A[-1][-1]
assert determinant(B)==-27
permanent={0:1}
for row in range(8):
    new={}
    for used,n in permanent.items():
        for col in range(8):
            if B[row][col] and not(used>>col&1):
                new[used|1<<col]=new.get(used|1<<col,0)+n
    permanent=new
assert permanent=={255:33}
P=[p for p in permutations(range(8)) if all(B[i][p[i]] for i in range(8))]
assert len(P)==33
sig=[(-1)**sum(p[i]>p[j] for i in range(8) for j in range(i+1,8)) for p in P]
assert Counter(sig)=={1:3,-1:30} and sum(sig)==-27
N=[set() for _ in P]
for i in range(33):
    for j in range(i+1,33):
        if sum(a!=b for a,b in zip(P[i],P[j]))==3:
            N[i].add(j);N[j].add(i)
assert sum(map(len,N))==192
R=set(range(33));components=[]
while R:
    q=[min(R)];found={q[0]}
    for a in q:
        for b in N[a]:
            if b not in found:q.append(b);found.add(b)
    R-=found;components.append(found)
assert sorted(map(len,components))==[1,1,1,30]
assert all(sig[next(iter(c))]==1 for c in components if len(c)==1)
assert all(sig[i]==-1 for i in next(c for c in components if len(c)==30))
print('CIRCULANT_VERIFY_OK permanent=33 determinant=-27 sign_distribution=3+30')
print('CIRCULANT_VERIFY_OK 96_sixcycle_switches 30_connected_plus_3_isolated=true')
