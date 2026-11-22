#!/usr/bin/env python3
"""Independent certificate using only the published 5x31 code generator matrix.

Usage: python3 verify_incidence.py
Python 3 standard library only. It does not call verify_sections.py.
"""
from itertools import combinations, product
from collections import Counter
from math import comb

# Matrix printed in Blache et al., arXiv:1903.09397v1, PDF page 21.
ROWS = [
    '1304331312042123303230102114231',
    '0000000001111222233334444412320',
    '0012224441123012301221113413110',
    '1340130140331020400141231111100',
    '1111111111111111111111111100000',
]
assert all(len(s)==31 for s in ROWS)
G = [tuple(int(ROWS[i][j]) for i in range(5)) for j in range(31)]

def rank(a):
    a=[list(z) for z in a]; m=len(a); n=len(a[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if a[i][j]%5),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        t=pow(a[r][j],-1,5)
        a[r]=[x*t%5 for x in a[r]]
        for i in range(m):
            if i!=r:
                q=a[i][j]
                a[i]=[(a[i][k]-q*a[r][k])%5 for k in range(n)]
        r+=1
        if r==m:break
    return r

assert rank(G)==5
assert all(rank((a,b,c))==3 for a,b,c in combinations(G,3))
# Every four-point coplanar set is counted once and lies in a unique plane.
N4=sum(rank(v)==3 for v in combinations(G,4))
assert N4==640, N4
print('independent four-coplanar-point certificate',N4)
# In PG(4,5), #planes=20306, planes through point=806, through line=31.
N3=comb(31,3)-4*N4
N2=31*comb(31,2)-3*N3-6*N4
N1=806*31-2*N2-3*N3-4*N4
N0=20306-N1-N2-N3-N4
assert [N0,N1,N2,N3,N4]==[5880,7081,4770,1935,640]
print('plane sections from independent incidence moments', [N0,N1,N2,N3,N4])
# Independent direct hyperplane sections, using the printed matrix.
points=[v for v in product(range(5),repeat=5)
        if any(v) and next(a for a in v if a)==1]
h=Counter(sum(sum(a*b for a,b in zip(v,g))%5==0 for g in G) for v in points)
assert h=={0:1,2:46,3:62,4:63,5:122,6:126,7:124,8:108,9:82,10:47}
assert sum(s*n for s,n in h.items()) == 31*156
assert sum(comb(s,2)*n for s,n in h.items())==comb(31,2)*31
# Each unordered pair of points belongs to 31 hyperplanes.
print('hyperplanes from published matrix',sorted(h.items()))
# Using no-three-collinear geometry, every pair determines exactly one line.
L2=comb(31,2); L1=31*156-2*L2; L0=20306-L1-L2
assert [L0,L1,L2]==[15935,3906,465]
print('lines from pair incidence',[L0,L1,L2])
print('PASS')
