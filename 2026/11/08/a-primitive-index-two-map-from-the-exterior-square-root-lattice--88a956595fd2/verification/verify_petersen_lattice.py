#!/usr/bin/env python3
"""Exact integral S5-lattice verification for the Petersen cycle lattice.

Needs Python >=3.9 and sympy. Pure integer/rational arithmetic; no network.
"""
from itertools import combinations, permutations
from math import gcd
from functools import reduce
from sympy import Matrix, zeros

V = list(combinations(range(5), 2))
E = [(i,j) for i in range(10) for j in range(i+1,10)
     if set(V[i]).isdisjoint(V[j])]
assert len(V)==10 and len(E)==15
D=zeros(10,15)
for col,(i,j) in enumerate(E):
    D[i,col]=-1
    D[j,col]=1
assert D.rank()==9
N=Matrix.hstack(*D.nullspace())
assert N.shape==(15,6) and all(x.q==1 for x in N)
assert D*N==zeros(10,6)
left=(N.T*N).inv()*N.T
assert left*N==Matrix.eye(6)

pairs=list(combinations(range(4),2))

def actions(p):
    vmap=[V.index(tuple(sorted(p[i] for i in v))) for v in V]
    edge=zeros(15,15)
    for j,(u,v) in enumerate(E):
        a,b=vmap[u],vmap[v]
        edge[E.index(tuple(sorted((a,b)))),j]=1 if a<b else -1
    A=left*edge*N
    assert N*A==edge*N and all(x.q==1 for x in A)
    C=zeros(4,4)
    for i in range(4):
        if p[i]<4:C[p[i],i]+=1
        if p[4]<4:C[p[4],i]-=1
    W=zeros(6,6)
    for j,(a,b) in enumerate(pairs):
        for i,(c,d) in enumerate(pairs):
            W[i,j]=C[c,a]*C[d,b]-C[d,a]*C[c,b]
    return A,W

U=Matrix([
[ 1, 0, 0, 0,-1, 0],
[ 0, 0, 0,-1, 0, 1],
[ 0, 0, 0, 1, 1, 0],
[-1,-1, 0, 0, 0, 0],
[-1, 0,-1, 0, 0, 0],
[ 0, 1, 1, 0, 0, 0]
])
assert U.det()==-2
assert reduce(gcd, (abs(int(x)) for x in U))==1
assert len(U.nullspace())==0
for p in permutations(range(5)):
    A,W=actions(p)
    assert A*U==U*W, p
print('All 120 permutations: A(g) U = U wedge^2(C(g))')
print('Petersen graph: 10 vertices, 15 edges, cycle rank 6')
print('det(U)=-2: index exactly 2; U primitive')

# Verify that equivariant maps wedge^2 A4 -> H1(P,Z) form Z U.
# An intertwiner X has 36 unknown entries. For each of two generators,
# A X - X W=0 supplies 36 linear homogeneous constraints.
p1=(1,0,2,3,4)
p2=(1,2,3,4,0)
rows=[]
for p in (p1,p2):
    A,W=actions(p)
    for i in range(6):
        for j in range(6):
            rows.append([int(A[i,k])*(l==j) - (i==k)*int(W[l,j])
                         for k in range(6) for l in range(6)])
assert len(rows)==72 and len(rows[0])==36

def rank_mod_prime(rows,p):
    mat=[[v%p for v in row] for row in rows]
    m,n=len(mat),len(mat[0]);rank=0
    for col in range(n):
        pivot=next((r for r in range(rank,m) if mat[r][col]),None)
        if pivot is None: continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        mul=pow(mat[rank][col],-1,p)
        mat[rank]=[(x*mul)%p for x in mat[rank]]
        for r in range(rank+1,m):
            if mat[r][col]:
                f=mat[r][col]
                mat[r]=[(x-f*y)%p for x,y in zip(mat[r],mat[rank])]
        rank+=1
    return rank

rk=rank_mod_prime(rows,101)
assert rk==35, rk
# Exact rank over Q is at least rank 35 mod 101; exact U solution bounds rank at most 35.
print('72x36 intertwining constraint matrix: rank mod 101 = 35')
print('Consequently rational solution dimension exactly 1')
print('Primitivity implies Hom_Z[S5](wedge^2 A4,H1(P,Z)) = Z U')
print('No equivariant integral isomorphism; all nonzero maps have index 2*|m|^6')

# Rational representation equality and modulo-two cokernel.
assert U.rank()==6
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
S=smith_normal_form(U,domain=ZZ)
assert [abs(int(S[i,i])) for i in range(6)]==[1,1,1,1,1,2]
print('Smith invariants:',[abs(int(S[i,i])) for i in range(6)])
print('ALL_CHECKS_PASSED')
