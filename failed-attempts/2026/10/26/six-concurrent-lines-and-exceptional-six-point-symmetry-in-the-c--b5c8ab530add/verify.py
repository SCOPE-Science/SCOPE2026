#!/usr/bin/env python3
"""Exact finite-field certificate for the exceptional characteristic-five Bring curve."""
from itertools import product, permutations
from math import comb
P=5

def norm(v):
    for a in v:
        if a%P:
            t=pow(a,-1,P)
            return tuple((x*t)%P for x in v)
    raise ValueError('zero')

def base(y):
    v=list(y)+[(-sum(y))%P,0]
    return sum(x*x for x in v)%P==0 and sum(x*x*x for x in v)%P==0

directions=sorted({norm(y) for y in product(range(P),repeat=3) if any(y) and base(y)})
assert len(directions)==6, directions
assert len({(a,b,c) for a,b,c in directions})==6
for i,j in [(2,2),(3,3)]: pass

def rank(M):
    A=[list(row) for row in M]
    if not A: return 0
    rows,cols=len(A),len(A[0]); r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if A[i][j]%P),None)
        if pivot is None:continue
        A[pivot],A[r]=A[r],A[pivot]
        t=pow(A[r][j]%P,-1,P); A[r]=[(z*t)%P for z in A[r]]
        for i in range(rows):
            if i!=r and A[i][j]%P:
                s=A[i][j]
                A[i]=[(u-s*v)%P for u,v in zip(A[i],A[r])]
        r+=1
    return r

def monomials(deg):
    return [(a,b,deg-a-b) for a in range(deg+1) for b in range(deg-a+1)]

ranks=[]
for n in range(5):
    mons=monomials(n)
    M=[[(x**a*y**b*z**c)%P for a,b,c in mons] for x,y,z in directions]
    ranks.append(rank(M))
assert ranks==[1,3,5,6,6],ranks

def F(v):
    return all(sum(x**d for x in v)%P==0 for d in (1,2,3))
projective=set()
for v in product(range(P),repeat=5):
    if any(v):projective.add(norm(v))
points=[v for v in projective if F(v)]
assert len(points)==31,len(points)
E=(1,1,1,1,1)
lines=[]
for a,b,c in directions:
    d=(-a-b-c)%P
    delta=(a,b,c,d,0)
    pts={norm(tuple(s*E[i]+t*delta[i] for i in range(5))) for s,t in product(range(P),repeat=2) if s or t}
    assert len(pts)==6
    lines.append(pts)
assert len(set.union(*lines))==31
assert all(lines[i]&lines[j]=={E} for i in range(6) for j in range(i+1,6))

all_affine=set()
for perm in permutations(range(P)):
    y=tuple((perm[i]-perm[4])%P for i in range(3))
    all_affine.add(norm(y))
assert all_affine==set(directions), (all_affine,directions)
# The stabilizer of any direction consists of the affine F5 transformations.
root=(0,1,2,3,4)
fix=0
for p in permutations(range(P)):
    test=norm(tuple((root[p[i]]-root[p[4]])%P for i in range(3)))
    if test==directions[0]:fix+=1
assert fix==20,fix
# Faithful six-point action induced by all 120 coordinate permutations.
act=set()
for p in permutations(range(P)):
    dest=[]
    for a,b,c in directions:
        v=(a,b,c,(-a-b-c)%P,0)
        u=tuple((v[p[i]]-v[p[4]])%P for i in range(3))
        dest.append(directions.index(norm(u)))
    act.add(tuple(dest))
assert len(act)==120,len(act)

# Quadric Q=-p2/2 on a 3-dim complement: confirm nondegeneracy.
def Q(y):
    v=tuple(y)+((-sum(y))%P,0)
    return sum(x*x for x in v)%P
basis=[(1,0,0),(0,1,0),(0,0,1)]
Gram=[[ (Q(tuple((basis[i][t]+basis[j][t])%P for t in range(3)))-Q(basis[i])-Q(basis[j]))%P for j in range(3)] for i in range(3)]
det=(Gram[0][0]*(Gram[1][1]*Gram[2][2]-Gram[1][2]*Gram[2][1])-Gram[0][1]*(Gram[1][0]*Gram[2][2]-Gram[1][2]*Gram[2][0])+Gram[0][2]*(Gram[1][0]*Gram[2][1]-Gram[1][1]*Gram[2][0]))%P
assert det!=0,(Gram,det)
print('CHECK_OK six_directions=',directions, 'rank_by_degree=',ranks, 'projective_F5_points=',len(points), 'affine_stabilizer_size=',fix, 'quadratic_polar_det=',det, 'six_point_action_size=',len(act))
