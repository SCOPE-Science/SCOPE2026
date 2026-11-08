#!/usr/bin/env python3
"""Exact polynomial and norm identity checks for SO(4) Haar matrix coefficients.
Uses only Python standard library; all arithmetic is integral or rational.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations

def quaternion_multiply(a, b):
    x,y,z,w=a; u,v,t,s=b
    return (x*u-y*v-z*t-w*s,
            x*v+y*u+z*s-w*t,
            x*t-y*s+z*u+w*v,
            x*s+y*t-z*v+w*u)

unit=[tuple(int(i==j) for i in range(4)) for j in range(4)]
def H(a,b):
    bar=list(unit[b]); bar[1:]=[-v for v in bar[1:]]
    columns=[quaternion_multiply(quaternion_multiply(unit[a],e),bar) for e in unit]
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))

h=[[H(a,b) for b in range(4)] for a in range(4)]
for a in range(4):
 for b in range(4):
  for c in range(4):
   for d in range(4):
    dot=sum(h[a][b][i][j]*h[c][d][i][j] for i in range(4) for j in range(4))
    assert dot==4*(a==c and b==d)
print('QUATERNION_SIXTEEN_MATRIX_BASIS_ORTHOGONAL_OK')

# Sparse homogeneous polynomials in sixteen independent variables.
# Monomials are sorted tuples of variable indices.
def add_into(p,q,scale=1):
 for k,v in q.items(): p[k]=p.get(k,0)+scale*v

def product(p,q):
 out=defaultdict(int)
 for k,v in p.items():
  for j,w in q.items(): out[tuple(sorted(k+j))]+=v*w
 return {k:v for k,v in out.items() if v}

def item(i,j): return {(4*i+j,):1}
B={}
for a in range(4):
 for b in range(4):
  B[a,b]={(4*i+j,):h[a][b][i][j] for i in range(4) for j in range(4) if h[a][b][i][j]}
C={}
for i in range(4):
 for j in range(4):
  z={}
  for a in range(4): add_into(z,product(B[a,i],B[a,j]))
  C[i,j]={k:v for k,v in z.items() if v}
trc2={}
for i in range(4):
 for j in range(4): add_into(trc2,product(C[i,j],C[j,i]))
S={}
for i in range(4):
 for j in range(4): add_into(S,product(item(i,j),item(i,j)))
S2=product(S,S)
U={}
for i in range(4):
 for j in range(4):
  for k in range(4):
   for l in range(4):
    key=tuple(sorted([4*k+i,4*k+j,4*l+j,4*l+i]))
    U[key]=U.get(key,0)+1
D={}
for p in permutations(range(4)):
 inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
 key=tuple(sorted(4*i+p[i] for i in range(4)))
 D[key]=(-1)**inversions
res={}
for pol,factor in [(trc2,1),(S2,-12),(U,8),(D,-96)]: add_into(res,pol,factor)
assert all(v==0 for v in res.values()), [(k,v) for k,v in res.items() if v][:5]
print('ALL_COEFFICIENTS_QUARTIC_QUATERNION_TO_MATRIX_INVARIANTS_OK',len(set(trc2)|set(S2)|set(U)|set(D)))

# Exact fourth-moment formula and lower/upper endpoint identity.
def determinant(A):
 return sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*
            __import__('math').prod(A[i][p[i]] for i in range(4)) for p in permutations(range(4)))
def mom(A):
 S=sum(v*v for row in A for v in row)
 M=[[sum(A[k][i]*A[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
 U=sum(M[i][j]*M[j][i] for i in range(4) for j in range(4))
 det=determinant(A)
 fourth=Fraction(5*S*S-2*U,24)+det
 ratio=16*fourth/Fraction(S*S)
 return fourth,ratio
I=[[int(i==j) for j in range(4)] for i in range(4)]
reflection=[[int(i==j)*(1 if i!=3 else -1) for j in range(4)] for i in range(4)]
rankone=[[int(i==0 and j==0) for j in range(4)] for i in range(4)]
assert mom(I)==(Fraction(4),Fraction(4))
assert mom(reflection)==(Fraction(2),Fraction(2))
assert mom(rankone)==(Fraction(1,8),Fraction(2))
print('SHARP_EQUATION_AND_THREE_EQUALITY_FAMILIES_OK')

# Independent quaternion integration from the 4th-moment tensor on two spheres.
def via_quaternions(A):
 Bmat=[[sum(A[i][j]*h[a][b][i][j] for i in range(4) for j in range(4)) for b in range(4)] for a in range(4)]
 Cmat=[[sum(Bmat[a][i]*Bmat[a][j] for a in range(4)) for j in range(4)] for i in range(4)]
 T=sum(Cmat[i][i] for i in range(4))
 V=sum(Cmat[i][j]*Cmat[j][i] for i in range(4) for j in range(4))
 return Fraction(T*T+2*V,192)

cases=[I,reflection,rankone,[[1,2,3,4],[0,3,-1,2],[4,0,-2,3],[-1,1,1,-3]],
       [[0,1,2,3],[4,-1,3,1],[3,5,1,-2],[2,1,0,4]]]
for A in cases:
 assert via_quaternions(A)==mom(A)[0]
print('INDEPENDENT_DOUBLE_SPHERE_FOURTH_MOMENT_IDENTITIES_OK',len(cases))
print('ALL_SO4_SHARP_FOURTH_MOMENT_CHECKS_OK')
