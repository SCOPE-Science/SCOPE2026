#!/usr/bin/env python3
"""Exact rational sixth-moment/Hessian certificate for the hexagonal torus aperture."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from math import sqrt

S=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
TR=defaultdict(list)
for abc in product(range(6),repeat=3):
    TR[tuple(sum(S[j][k] for j in abc) for k in (0,1))].append(abc)
assert sum(map(len,TR.values()))==216 and len(TR)==37
flat_numerator=sum(len(ts)**2 for ts in TR.values())
assert flat_numerator==2040 and F(flat_numerator,6**3)==F(85,9)

# The linear coefficient in (u+h)^3 is b_T(h)=sum_{triple in T}sum h_j/6.
B=[[F(0) for j in range(6)] for nu in TR]
D=[[F(0) for j in range(6)] for k in range(6)]
for row,(nu,ts) in enumerate(TR.items()):
    m=len(ts)
    for abc in ts:
        for j in abc: B[row][j]+=F(1,6)
        # 2 Re <C0,C2> = m/18 times sum of all three pair products.
        for j,k in ((abc[0],abc[1]),(abc[0],abc[2]),(abc[1],abc[2])):
            # store symmetric quadratic-form entries
            D[j][k]+=F(m,36)
            D[k][j]+=F(m,36)
N=[[sum(B[r][i]*B[r][j] for r in range(len(B))) for j in range(6)] for i in range(6)]
Hx=[[N[i][j]+D[i][j]-(F(85,3) if i==j else 0) for j in range(6)] for i in range(6)]
Hy=[[N[i][j]-D[i][j]-(F(85,3) if i==j else 0) for j in range(6)] for i in range(6)]
expected_x=[[-F(1,6),F(47,2),F(22),F(23),F(23),F(22)],
[F(47,2),-F(1,6),F(23),F(22),F(22),F(23)],
[F(22),F(23),-F(1,6),F(47,2),F(23),F(22)],
[F(23),F(22),F(47,2),-F(1,6),F(22),F(23)],
[F(23),F(22),F(23),F(22),-F(1,6),F(47,2)],
[F(22),F(23),F(22),F(23),F(47,2),-F(1,6)]]
expected_y=[[-F(23,2),-F(13,2),F(2),F(7),F(7),F(2)],
[-F(13,2),-F(23,2),F(7),F(2),F(2),F(7)],
[F(2),F(7),-F(23,2),-F(13,2),F(7),F(2)],
[F(7),F(2),-F(13,2),-F(23,2),F(2),F(7)],
[F(7),F(2),F(7),F(2),-F(23,2),-F(13,2)],
[F(2),F(7),F(2),F(7),-F(13,2),-F(23,2)]]
assert Hx==expected_x,(Hx,expected_x)
assert Hy==expected_y,(Hy,expected_y)

def rank(a):
    a=[[F(t) for t in row] for row in a];i=0
    for j in range(len(a[0])):
        z=next((k for k in range(i,len(a)) if a[k][j]),None)
        if z is None: continue
        a[i],a[z]=a[z],a[i]
        v=a[i][j];a[i]=[t/v for t in a[i]]
        for k in range(len(a)):
            if k!=i:
                t=a[k][j];a[k]=[a[k][h]-t*a[i][h] for h in range(len(a[k]))]
        i+=1
        if i==len(a): break
    return i
for M,spec in ((Hx,[(F(340,3),1),(-F(77,3),1),(-F(65,3),2),(-F(68,3),2)]),
               (Hy,[(F(0),3),(-F(15),1),(-F(27),2)])):
    assert sum(d for ev,d in spec)==6
    for ev,m in spec:
        assert 6-rank([[M[i][j]-(ev if i==j else 0) for j in range(6)] for i in range(6)])==m

# Verify phase/translation tangent directions and the least-stable phase vector.
def q(M,v):return sum(v[i]*M[i][j]*v[j] for i in range(6) for j in range(6))
ones=[1]*6
assert q(Hy,ones)==0
for k in (0,1): assert q(Hy,[v[k] for v in S])==0
least=[1,-1,1,-1,-1,1]
assert sum(least)==0 and all(sum(least[j]*S[j][k] for j in range(6))==0 for k in (0,1))
assert q(Hy,least)==-15*6

def moment(c):
    C=[]
    for ts in TR.values():C.append(sum(c[i]*c[j]*c[k] for i,j,k in ts))
    return sum(abs(z)**2 for z in C)/(sum(abs(z)**2 for z in c)**3)
flat=[1/sqrt(6)]*6
for eps in (0.01,0.001,0.0001):
    pert=[(1+1j*eps*least[i])/sqrt(6) for i in range(6)]
    # Tangent orthogonality implies distance to phase/translation orbit = eps+O(eps**2).
    deficit=85/9-moment(pert)
    assert abs(deficit/eps**2-15)<0.1, (eps,deficit/eps**2)
print('HEXAGONAL_L6_LOCAL_PASS triples=216 sums=37 numerator=2040 real_bands=4 phase_bands=3 gap=15')
