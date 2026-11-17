#!/usr/bin/env python3
"""Exact lattice proof for the affine ternary plane independence complex.
Self-contained Python 3 standard library; integral determinants and rational linear systems.
"""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
from math import gcd
from functools import reduce

pts=list(product(range(3),repeat=2))
assert len(pts)==9
lines=set()
for i,j in combinations(range(9),2):
 p,q=pts[i],pts[j]
 k=pts.index(tuple((2*q[u]-p[u])%3 for u in range(2)))
 lines.add(tuple(sorted((i,j,k))))
assert len(lines)==12 and all(len([l for l in lines if i in l])==4 for i in range(9))
tri=[t for t in combinations(range(9),3) if t not in lines]
tri_ix={t:i for i,t in enumerate(tri)}
quads=[q for q in combinations(range(9),4) if all(t in tri_ix for t in combinations(q,3))]
assert len(tri)==72 and len(quads)==54
edges=list(combinations(range(9),2));edge_ix={e:i for i,e in enumerate(edges)}
B=[[0]*len(tri) for _ in edges]
for j,t in enumerate(tri):
 for k in range(3):
  sub=t[:k]+t[k+1:]
  B[edge_ix[sub]][j]=(-1)**k

# 28 integral basis boundary triangles, predetermined by deterministic lexicographic pivot rule.
basecols=list(range(25))+[32,36,37]
free=[j for j in range(len(tri)) if j not in basecols]
assert len(basecols)==28 and len(free)==44
minorrows=[0,1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19,21,22,23,24,26,27,28,30,31,33]

def determinant(A):
 A=[list(row) for row in A];n=len(A)
 assert all(len(row)==n for row in A)
 if n==0:return 1
 d=1;sgn=1
 for k in range(n-1):
  if A[k][k]==0:
   r=next((i for i in range(k+1,n) if A[i][k]),None)
   if r is None:return 0
   A[k],A[r]=A[r],A[k];sgn=-sgn
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    numerator=A[i][j]*pivot-A[i][k]*A[k][j]
    assert numerator%d==0
    A[i][j]=numerator//d
  for i in range(k+1,n):A[i][k]=0
  d=pivot
 return sgn*A[n-1][n-1]

A=[[B[i][j] for j in basecols] for i in minorrows]
assert determinant(A)==-1

def integer_inverse(A):
 n=len(A)
 aug=[[Fraction(a) for a in row]+[Fraction(i==j) for j in range(n)] for i,row in enumerate(A)]
 for k in range(n):
  i=next(i for i in range(k,n) if aug[i][k])
  aug[k],aug[i]=aug[i],aug[k]
  h=aug[k][k];aug[k]=[x/h for x in aug[k]]
  for i in range(n):
   if i!=k and aug[i][k]:
    h=aug[i][k];aug[i]=[x-h*y for x,y in zip(aug[i],aug[k])]
 inv=[[aug[i][n+j] for j in range(n)] for i in range(n)]
 assert all(x.denominator==1 for row in inv for x in row)
 return [[int(x) for x in row] for row in inv]
inv=integer_inverse(A)
ker_basis=[]
for j in free:
 rhs=[-B[i][j] for i in minorrows]
 vals=[sum(inv[i][k]*rhs[k] for k in range(28)) for i in range(28)]
 z=[0]*72;z[j]=1
 for i,b in enumerate(basecols):z[b]=vals[i]
 assert all(sum(B[i][c]*z[c] for c in range(72))==0 for i in range(36))
 ker_basis.append(z)
# Every integral kernel element is uniquely determined by its 44 free coordinates.
print('K9_boundary_basis_unimodular_minor=-1 H2=Z^44 H1=0')

R=[[0]*len(quads) for _ in range(44)]
for j,q in enumerate(quads):
 for k in range(4):
  t=q[:k]+q[k+1:]
  ix=tri_ix[t]
  if ix in free:R[free.index(ix)][j]=(-1)**k
Rrows=list(range(41))+[42,43]
Rcols=list(range(27))+[28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44]
assert len(Rrows)==43 and len(Rcols)==43
minor=[[R[i][j] for j in Rcols] for i in Rrows]
assert determinant(minor)==-1

# Area orientation on noncollinear triples. Exact F3 sign is +1 or -1.
def area(t):
 a,b,c=[pts[i] for i in t]
 d=((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))%3
 assert d in (1,2)
 return 1 if d==1 else -1
phi=[area(t) for t in tri]
assert all(sum((-1)**k*phi[tri_ix[q[:k]+q[k+1:]]] for k in range(4))==0 for q in quads)
vals=[sum(a*b for a,b in zip(phi,z)) for z in ker_basis]
assert Counter(vals)=={0:32,6:6,-6:6}
assert reduce(gcd,vals)==6
# Since this 43x43 minor is unimodular and phi annihilates all cap boundaries,
# they are the full primitive kernel of phi/6 in H2; quotient is Z.
print('quadrangles=54 rank=43 unit_43_minor=-1 area_values=(0:32,+6:6,-6:6)')

# AGL(2,3) preserves independence and acts on the quotient by det sign.
GL=[]
for a,b,c,d in product(range(3),repeat=4):
 det=(a*d-b*c)%3
 if det:GL.append(((a,b,c,d),1 if det==1 else -1))
assert len(GL)==48
perms=set()
for (a,b,c,d),sgn in GL:
 for u,v in pts:
  g=[pts.index(((a*x+b*y+u)%3,(c*x+d*y+v)%3)) for x,y in pts]
  perms.add(tuple(g))
  assert all(tuple(sorted(g[t] for t in l)) in lines for l in lines)
  for t in tri:
   mapped=tuple(g[x] for x in t)
   parity=(-1)**sum(mapped[i]>mapped[j] for i in range(3) for j in range(i+1,3))
   assert parity*area(tuple(sorted(mapped)))==sgn*area(t)
assert len(perms)==432
quad_orbit={tuple(sorted(g[x] for x in quads[0])) for g in perms}
assert len(quad_orbit)==54
print('AGL(2,3)_order=432 quadrangles_transitive=True determinant_sign_on_quotient=True')
print('AG23_GEOMETRIC_CYCLES_PRIMITIVE_CODIM_ONE_PASS')
