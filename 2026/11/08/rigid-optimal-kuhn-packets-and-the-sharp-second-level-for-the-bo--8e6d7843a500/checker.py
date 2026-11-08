#!/usr/bin/env python3
"""Exact rational verification of the BCC Kuhn-packet first-two-level theorem.

No nonstandard packages. This is a finite checker for the algebraic cases
used in the accompanying self-contained proof, not a substitute for that proof.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product

Z=(F(0),F(0),F(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,q):return tuple(q*x for x in a)
def sq(a):return sum(x*x for x in a)
def diff(a,b):return tuple(x-y for x,y in zip(a,b))
def determinant(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

# Every BCC point has all integral or all half-odd coordinates.
S=sorted(set((F(i,2),F(j,2),F(k,2))
    for i,j,k in product(range(-2,3),repeat=3)
    if i%2==j%2==k%2 and i*i+j*j+k*k>0 and i*i+j*j+k*k<=5))
assert len(S)==14
valid=[]; count_independent=0
for B in combinations(S,3):
 if determinant(*B)==0:continue
 count_independent+=1
 subset_sums=[sum((B[i][k] for i in J),F(0)) for J in ((0,),)] if False else []
 good=all(add(B[i],B[j]) in S for i,j in combinations(range(3),2)) and add(add(B[0],B[1]),B[2]) in S
 if good:valid.append(B)
assert len(valid)==8, len(valid)
assert count_independent==232, count_independent

# All three vectors are odd half diagonals from one of the two sign-parity tetrahedra.
for B in valid:
 assert all(all(abs(c)==F(1,2) for c in v) for v in B)
 assert abs(determinant(*B))==F(1,2)
 for p in permutations(B):
  vertices=[Z,p[0],add(p[0],p[1]),add(add(p[0],p[1]),p[2])]
  centroid=scale(tuple(sum(v[k] for v in vertices) for k in range(3)),F(1,4))
  assert [sq(diff(x,centroid)) for x in vertices]==[F(5,16)]*4

# Non-optimal witness attaining the discrete gap.
B=[(F(-1),F(0),F(0)),(F(0),F(-1),F(0)),(F(1,2),F(1,2),F(-1,2))]
assert abs(determinant(*B))==F(1,2)
centers={
 (0,1,2):(F(-1,2),F(-1,2),F(0)),
 (1,0,2):(F(-1,2),F(-1,2),F(0)),
 (0,2,1):(F(-1,2),F(0),F(-1,4)),
 (1,2,0):(F(0),F(-1,2),F(-1,4)),
 (2,0,1):(F(0),F(0),F(-1,2)),
 (2,1,0):(F(0),F(0),F(-1,2)),
}
for p in permutations(range(3)):
 v=[B[i] for i in p]
 vertices=[Z,v[0],add(v[0],v[1]),add(add(v[0],v[1]),v[2])]
 assert max(sq(diff(x,centers[p])) for x in vertices)<=F(1,2),(p,vertices)
assert sq(add(B[0],B[1]))==F(2)

# Nearest-vector certificate for the classical BCC deep-hole lower bound.
x=(F(1,2),F(1,4),F(0))
for a,b,c in product(range(-2,3),repeat=3):
 v=(F(a),F(b),F(c))
 assert sq(diff(v,x))>=F(5,16)
 v=(F(a,1)+F(1,2),F(b)+F(1,2),F(c)+F(1,2))
 assert sq(diff(v,x))>=F(5,16)
print('PASS: 14 short BCC vectors; 232 independent unordered short frames; exactly 8 admissible;')
print('       all 48 optimal packet tetrahedra have squared centroid-radius 5/16;')
print('       6 explicit second-level fitting balls have squared radius <=1/2;')
print('       deep-hole sanity checks pass (global proof is coordinatewise).')
