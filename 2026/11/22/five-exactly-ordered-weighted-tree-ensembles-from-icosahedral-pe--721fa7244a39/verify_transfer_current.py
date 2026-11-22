#!/usr/bin/env python3
"""Independent rational transfer-current verification of matching-weighted trees."""
from collections import Counter, defaultdict
from fractions import Fraction as F

N=12
# Fixed adjacency of the standard 12-vertex icosahedral graph.
NBR=( (1,5,7,8,11),(0,2,5,6,8),(1,3,6,8,9),
      (2,4,6,9,10),(3,5,6,10,11),(0,1,4,6,11),
      (1,2,3,4,5),(0,8,9,10,11),(0,1,2,7,9),
      (2,3,7,8,10),(3,4,7,9,11),(0,4,5,7,10) )
E=tuple(sorted((i,j) for i in range(N) for j in NBR[i] if i<j))
assert len(E)==30 and all(len(x)==5 for x in NBR)
assert all(i in NBR[j] for i in range(N) for j in NBR[i])
# Explicit relabeling onto the 2-pentagonal-ring icosahedral representation.
TO_RING=(0,1,6,11,8,2,7,4,5,10,9,3)
RING=set()
for i in range(5):
    u=1+i;v=6+i
    for a,b in ((0,u),(11,v),(u,1+(i+1)%5),(v,6+(i+1)%5),
                (u,v),(u,6+(i+1)%5)):
        RING.add(tuple(sorted((a,b))))
assert {tuple(sorted((TO_RING[a],TO_RING[b]))) for a,b in E}==RING

def all_matching_edges(free):
    if not free:
        yield frozenset()
    else:
        # Use highest vertex to make search independent of the other verifier.
        u=max(free)
        for v in sorted(set(NBR[u])&free,reverse=True):
            edge=(min(u,v),max(u,v))
            for rest in all_matching_edges(free-{u,v}):
                yield frozenset({edge})|rest
MATCHINGS=list(all_matching_edges(set(range(N))))
assert len(MATCHINGS)==125 and len(set(MATCHINGS))==125

def gaussian_det(a):
    a=[[F(v) for v in row] for row in a]
    n=len(a);det=F(1)
    for k in range(n):
        z=next((i for i in range(k,n) if a[i][k]!=0),None)
        if z is None:return F(0)
        if z!=k:a[z],a[k]=a[k],a[z];det=-det
        p=a[k][k];det*=p
        for i in range(k+1,n):
            factor=a[i][k]/p
            for j in range(k+1,n):a[i][j]-=factor*a[k][j]
    return det

def inv_rational(a):
    n=len(a);m=[[F(a[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        r=next(i for i in range(k,n) if m[i][k]!=0)
        m[k],m[r]=m[r],m[k]
        d=m[k][k];m[k]=[z/d for z in m[k]]
        for i in range(n):
            if i!=k:
                d=m[i][k]
                m[i]=[m[i][j]-d*m[k][j] for j in range(2*n)]
    return [row[n:] for row in m]

# Unit weighted reduced Laplacian at vertex 11.
L=[[0]*11 for _ in range(11)]
for u,v in E:
    if u<11:L[u][u]+=1
    if v<11:L[v][v]+=1
    if u<11 and v<11:L[u][v]-=1;L[v][u]-=1
Z=gaussian_det(L)
assert Z==5184000
K=inv_rational(L)

def transfer_matrix(m):
    b=[]
    for u,v in sorted(m):
        row=[F(0)]*11
        if u<11:row[u]=F(1)
        if v<11:row[v]=F(-1)
        b.append(row)
    return [[sum(b[i][u]*K[u][v]*b[j][v] for u in range(11) for v in range(11))
             for j in range(6)] for i in range(6)]

def poly_value(H,t):
    T=[[F(i==j)+F(t-1)*H[i][j] for j in range(6)] for i in range(6)]
    z=Z*gaussian_det(T)
    assert z.denominator==1
    return int(z)

# Independently computed class polynomials, coefficient ordering t^0,...,t^6.
EXPECTED={
 5:(331776,1161216,1686528,1300992,562176,129024,12288),
 20:(324900,1158810,1697916,1307580,558084,125178,11532),
 60:(315400,1157480,1713170,1313640,552340,121120,10850),
 30:(306432,1159936,1725248,1315200,547712,118912,10560),
 10:(301056,1161216,1732608,1316352,544896,117504,10368),
}
COUNTS=Counter()
for m in MATCHINGS:
    H=transfer_matrix(m)
    values=tuple(poly_value(H,t) for t in range(7))
    # Classify using seven exact evaluation points (unique degree <=6 polynomial).
    matches=[j for j,c in EXPECTED.items()
             if all(values[t]==sum(c[i]*t**i for i in range(7)) for t in range(7))]
    assert len(matches)==1
    COUNTS[matches[0]]+=1
    assert poly_value(H,8)==sum(EXPECTED[matches[0]][i]*8**i for i in range(7))
assert COUNTS==Counter({5:5,20:20,60:60,30:30,10:10})
print('UNIT SPANNING-TREE NUMBER',Z)
print('INDEPENDENT RATIONAL TRANSFER-CURRENT CLASS SIZES',dict(COUNTS))
print('EXACT TRANSFER-CURRENT CHECKS',len(MATCHINGS)*8)
print('PASS')
