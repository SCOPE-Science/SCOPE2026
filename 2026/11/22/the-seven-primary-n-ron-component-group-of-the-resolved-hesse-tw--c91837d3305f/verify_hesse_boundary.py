#!/usr/bin/env python3
"""Exact Hesse-boundary graph and integer-lattice computation.
Only Python standard library and SymPy are required."""
from itertools import combinations, product
from sympy import Matrix, factor, symbols
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Q(omega), omega**2+omega+1=0; coefficient pairs are rational integers.
O=(1,0); W=(0,1); W2=(-1,-1); Z=(0,0)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def sub(a,b):return add(a,neg(b))
def cross(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
def samept(p,q):return all(c==Z for c in cross(p,q))
lines=[(O,Z,Z),(Z,O,Z),(Z,Z,O),
       (O,O,O),(O,W2,W),(O,W,W2),
       (O,W,W),(O,O,W2),(O,W2,O),
       (O,O,W),(O,W2,W2),(O,W,O)]
# Above list is 12 classical Hesse lines, partitioned into four triangles.
assert len(lines)==12
pairs=list(combinations(range(12),2)); groups=[]
for a,b in pairs:
 p=cross(lines[a],lines[b])
 assert any(c!=Z for c in p)
 for g in groups:
  if samept(p,g['p']):
   g['pairs'].append((a,b));break
 else:groups.append({'p':p,'pairs':[(a,b)]})
counts={k:sum(len(g['pairs'])==k for g in groups) for k in [1,6]}
assert counts=={1:12,6:9},counts
quad=[];ordinary=[]
for g in groups:
 ps=g['pairs']; involved=set(v for pair in ps for v in pair)
 if len(ps)==6:
  assert len(involved)==4
  quad.append(tuple(sorted(involved)))
 elif len(ps)==1:
  ordinary.append(ps[0])
 else:raise AssertionError('unexpected multiplicity')
assert all(i//3==j//3 for i,j in ordinary)
# Graph: 12 strict transforms + 9 exceptionals at the quadruple points.
V=21; E=[]
for j,qs in enumerate(quad):
 E.extend((i,12+j) for i in qs)
E.extend(ordinary)
assert len(E)==48
L=Matrix.zeros(V)
for i,j in E:
 L[i,i]+=1; L[j,j]+=1; L[i,j]-=1; L[j,i]-=1
assert sorted(int(L[i,i]) for i in range(V))==[4]*9+[5]*12
assert L*Matrix.ones(V,1)==Matrix.zeros(V,1)
x=symbols('x')
assert factor(L.charpoly(x).as_expr())==x*(x-3)**11*(x-7)**9
R=L[:20,:20]
assert R.det()==3**10 *7**8
S=smith_normal_form(R,domain=ZZ)
factors=[abs(int(S[i,i])) for i in range(20) if abs(int(S[i,i]))>1]
assert factors==[3,3]+[21]*8,factors
# Independent combinatorial model: AG(2,3) lines in four directions.
pts=list(product(range(3),repeat=2))
aff_lines=[(a,b,c) for a,b in [(1,0),(0,1),(1,1),(1,2)] for c in range(3)]
B=Matrix([[int((a*u+b*v-c)%3==0) for u,v in pts] for a,b,c in aff_lines]);C=Matrix.zeros(12)
for k in range(4):
 for i,j in combinations(range(3*k,3*k+3),2):C[i,j]=C[j,i]=1
assert B*B.T==2*Matrix.eye(12)+Matrix.ones(12,12)-C
assert B.T*B==3*Matrix.eye(9)+Matrix.ones(9,9)
L2=(5*Matrix.eye(12)-C).row_join(-B).col_join((-B.T).row_join(4*Matrix.eye(9)))
assert sorted(abs(int(x)) for x in smith_normal_form(L2[:20,:20],domain=ZZ).diagonal() if abs(int(x))>1)==[3,3]+[21]*8
# Finite-field rank check of the FULL laplacian.
def rank_mod(A,p):
 rows=[[int(A[i,j])%p for j in range(A.cols)] for i in range(A.rows)]
 r=0
 for col in range(A.cols):
  pivot=next((i for i in range(r,len(rows)) if rows[i][col]%p),None)
  if pivot is None:continue
  rows[r],rows[pivot]=rows[pivot],rows[r]
  inv=pow(rows[r][col],-1,p)
  rows[r]=[(v*inv)%p for v in rows[r]]
  for i in range(len(rows)):
   if i!=r and rows[i][col]:
    f=rows[i][col];rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[r])]
  r+=1
 return r
assert rank_mod(L,3)==10 and rank_mod(L,7)==12
print('HESSE_RESOLVED_NERON_COMPONENT_GROUP_OK; 21 vertices, 48 nodes, genus 28, SNF 3^2 21^8')
