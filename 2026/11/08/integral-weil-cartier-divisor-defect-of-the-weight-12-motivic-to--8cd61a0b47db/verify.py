#!/usr/bin/env python3
"""Exact integral facet and divisor-lattice calculations for the specified toric threefold."""
from itertools import combinations
from math import gcd

def det(A):
    n=len(A)
    if n==0:return 1
    if n==1:return A[0][0]
    return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(n))

def rank(A):
    for k in range(min(len(A),len(A[0])),0,-1):
        if any(det([[A[i][j] for j in js] for i in ii]) for ii in combinations(range(len(A)),k) for js in combinations(range(len(A[0])),k)):
            return k
    return 0

def minors_gcd(A,k):
    return gcd(*(abs(det([[A[i][j] for j in js] for i in ii])) for ii in combinations(range(len(A)),k) for js in combinations(range(len(A[0])),k)))

pts={'a':(1,0,0),'b':(0,1,0),'c':(0,0,1),'d':(0,0,0),'e':(0,-1,2),'f':(-1,2,0),'g':(0,-1,1)}
R=[[1,1,1],[0,0,-1],[-3,-1,0],[-2,-1,-1],[1,-1,0],[0,-1,-1]]
h=[1,0,1,0,1,0]
facets=[set(('a','e','f')),set(('a','d','f')),set(('e','f','g')),set(('d','f','g')),set(('a','e','g')),set(('a','d','g'))]
for i,row in enumerate(R):
    assert gcd(*row)==1
    values={key:sum(x*y for x,y in zip(row,pt)) for key,pt in pts.items()}
    assert all(z<=h[i] for z in values.values())
    assert {key for key,z in values.items() if z==h[i] and key in {"a","d","e","f","g"}}==facets[i]
assert set.union(*facets)=={'a','d','e','f','g'}
# Exhaust every triple of supporting hyperplanes, including all polytope vertices.
from fractions import Fraction
vertices=set()
for ids in combinations(range(6),3):
    A=[R[i] for i in ids]; rhs=[h[i] for i in ids]; denom=det(A)
    if denom==0:continue
    x=tuple(Fraction(det([[rhs[ii] if jj==col else A[ii][jj] for jj in range(3)] for ii in range(3)]),denom) for col in range(3))
    if all(sum(a*b for a,b in zip(row,x))<=bound for row,bound in zip(R,h)):
        vertices.add(x)
assert vertices=={tuple(Fraction(v) for v in pts[k]) for k in ('a','d','e','f','g')}

assert rank(R)==3 and minors_gcd(R,3)==1
M=[row+[b] for row,b in zip(R,h)]
assert rank(M)==4 and minors_gcd(M,3)==1 and minors_gcd(M,4)==2
# Relations among the four ray normals at three nonsimplicial cones.
for rel in [[1,-1,0,0,-1,2],[1,-1,-1,2,0,0],[0,0,1,-2,-1,2]]:
    assert [sum(rel[i]*R[i][j] for i in range(6)) for j in range(3)]==[0,0,0]
assert rank([[1,-1,0,0,-1,2],[1,-1,-1,2,0,0],[0,0,1,-2,-1,2]])==2
D=[0,0,2,1,0,0]
assert [2*z-h[i]+R[i][0] for i,z in enumerate(D)]==[0]*6
print('WEIGHT12_GLOBAL_DIVISOR_LATTICES_OK; facets=6; cl_rank=3; pic_rank=1; quotient=Z^2+Z/2')
