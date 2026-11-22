#!/usr/bin/env python3
"""Exact integral two-particle graph-configuration homology on K_{2,3,4}.

Standard library only. Every matrix, cycle, torus and relation is constructed
from the graph. All linear algebra certificates use exact integer arithmetic.
"""
from itertools import combinations
from collections import Counter

PARTS = (range(0,2),range(2,5),range(5,9))
V = tuple(range(9))
part = {v:k for k,P in enumerate(PARTS) for v in P}
E = tuple((a,b) for a,b in combinations(V,2) if part[a]!=part[b])
eidx = {e:i for i,e in enumerate(E)}
C0 = tuple(combinations(V,2))
C1 = tuple((v,i) for v in V for i,(a,b) in enumerate(E) if v!=a and v!=b)
C2 = tuple((i,j) for i,(a,b) in enumerate(E) for j in range(i+1,len(E)) if a not in E[j] and b not in E[j])
i0={x:i for i,x in enumerate(C0)}
i1={x:i for i,x in enumerate(C1)}
i2={x:i for i,x in enumerate(C2)}
assert (len(E),len(C0),len(C1),len(C2)) == (26,36,182,198)

def d1(col):
 v,i=C1[col];a,b=E[i]
 return {i0[tuple(sorted((v,b)))]:1, i0[tuple(sorted((v,a)))]:-1}

def d2(col):
 i,j=C2[col];a,b=E[i];c,d=E[j]
 return {i1[(b,j)]:1,i1[(a,j)]:-1,i1[(c,i)]:1,i1[(d,i)]:-1}

D2=[d2(i) for i in range(len(C2))]

def add_scaled(dst,src,coeff):
 for k,v in src.items():
  dst[k]=dst.get(k,0)+coeff*v
  if dst[k]==0:del dst[k]

def boundary(v, cols):
 out={}
 for k,c in v.items():add_scaled(out,cols[k],c)
 return out

for col in D2:assert boundary(col,[d1(k) for k in range(len(C1))])=={}

# Sparse Gaussian elimination over a finite field: gives only a lower bound on Q-rank.
def rank_mod(columns,p):
 basis={}
 for col in columns:
  v={k:a%p for k,a in col.items() if a%p}
  while v:
   r=min(v)
   if r not in basis:
    t=pow(v[r],-1,p)
    basis[r]={k:(a*t)%p for k,a in v.items()}
    break
   t=v.pop(r)
   for k,a in basis[r].items():
    if k==r:continue
    z=(v.get(k,0)-t*a)%p
    if z:v[k]=z
    elif k in v:del v[k]
 return len(basis)

assert rank_mod(D2,101)==129
assert rank_mod(D2,103)==129

adj={v:tuple(w for w in V if tuple(sorted((v,w))) in eidx) for v in V}
cycles=[]
for start in V:
 def dfs(path):
  for w in adj[path[-1]]:
   if w==start and len(path)>=3:
    if path[1]<path[-1]:cycles.append(tuple(path))
   elif w>start and w not in path:dfs(path+[w])
 for w in adj[start]:
  if w>start:dfs([start,w])
assert len(cycles)==4395

def signed_edges(c):
 out={}
 for a,b in zip(c,c[1:]+c[:1]):out[eidx[tuple(sorted((a,b)))]]=1 if a<b else -1
 return out

cyc_data=[(set(c),signed_edges(c),len(c)) for c in cycles]
tori=[];labels=[];types=Counter()
for k,(vs,ed,le) in enumerate(cyc_data):
 for other,ed2,le2 in cyc_data[k+1:]:
  if vs&other:continue
  t={}
  for i,a in ed.items():
   for j,b in ed2.items():
    index=i2[tuple(sorted((i,j)))]
    t[index]=a*b*(1 if i<j else -1)
  assert boundary(t,D2)=={}
  tori.append(t); labels.append(tuple(sorted((le,le2))))
  types[labels[-1]]+=1
assert len(tori)==1206
assert types=={(3,3):72,(3,4):288,(3,5):288,(3,6):144,(4,4):198,(4,5):216}

tri=[i for i,t in enumerate(labels) if t==(3,3)]
assert len(tri)==72

# Exact integer unit-pivot elimination for triangle-pair cycles.
# Every pivot is a unit. This gives a 69x69 unimodular minor.
basis={};based_on={};basis_tori=[];rel=[];dependents=[]
for j in tri:
 v=tori[j].copy();coeff={j:1}
 while v and min(v) in basis:
  r=min(v);a=v.pop(r)
  for k,b in basis[r].items():
   if k==r:continue
   z=v.get(k,0)-a*b
   if z:v[k]=z
   elif k in v:del v[k]
  add_scaled(coeff,based_on[r],-a)
 if v:
  r=min(v);a=v[r]
  assert abs(a)==1, ('nonunit pivot',j,a)
  basis[r]={k:a*b for k,b in v.items()}
  based_on[r]={k:a*b for k,b in coeff.items()}
  basis_tori.append(j)
 else:
  assert boundary(coeff,tori)=={}
  rel.append(coeff);dependents.append(j)
assert len(basis_tori)==69 and len(rel)==3
assert all(len(r)==36 for r in rel)

# Directly reconstruct the selected integral square-cell minor and verify
# unimodularity using integer-preserving Bareiss elimination.
rows=sorted(basis)
def determinant(A):
 A=[list(x) for x in A];n=len(A);prev=1;sign=1
 for k in range(n-1):
  if A[k][k]==0:
   q=next((q for q in range(k+1,n) if A[q][k]),None)
   if q is None:return 0
   A[k],A[q]=A[q],A[k];sign=-sign
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    q=A[i][j]*pivot-A[i][k]*A[k][j]
    assert q%prev==0
    A[i][j]=q//prev
   A[i][k]=0
  prev=pivot
 return sign*A[n-1][n-1]
minor=[[tori[j].get(r,0) for j in basis_tori] for r in rows]
assert determinant(minor) in (1,-1)

# Every other geometric product torus is in the integral span of the 69.
def reduce_by_basis(v):
 v=v.copy()
 for r,b in sorted(basis.items()):
  a=v.pop(r,0)
  for k,x in b.items():
   if k==r:continue
   z=v.get(k,0)-a*x
   if z:v[k]=z
   elif k in v:del v[k]
 return v
assert all(not reduce_by_basis(t) for t in tori)

# The three dependent triangle tori have unit coefficients in distinct
# relation rows; therefore the three relations form the *entire* integral
# kernel of Z^72 -> H_2, not merely a rational spanning family.
assert [r.get(j,0) for r,j in zip(rel,dependents)] == [1,1,1]
assert all(not any(j in r for j in dependents[k+1:]) for k,r in enumerate(rel))

# Symmetry action on the full relation lattice. Each selected vertex
# transposition induces a signed permutation of the 72 triangle-pair tori.
tri_pos={j:k for k,j in enumerate(tri)}
lookup={tuple(sorted(t.items())):(k,1) for k,j in enumerate(tri) for t in [tori[j]]}
lookup.update({tuple(sorted((i,-c) for i,c in tori[j].items())):(k,-1) for k,j in enumerate(tri)})
relarray=[]
for r in rel:
 a=[0]*72
 for j,c in r.items():a[tri_pos[j]]=c
 relarray.append(a)

# For any relation-vector combination, its coordinates in the relation
# basis are the coefficients at the three dependent torus positions.
deps=[tri_pos[j] for j in dependents]
def relation_action(sw):
 perm=list(V);a,b=sw;perm[a],perm[b]=perm[b],perm[a]
 image=[]
 for a,b in E:
  c,d=perm[a],perm[b]
  image.append((eidx[tuple(sorted((c,d)))],1 if c<d else -1))
 sq_image=[]
 for i,j in C2:
  a,s=image[i];b,t=image[j]
  sq_image.append((i2[tuple(sorted((a,b)))],s*t*(1 if a<b else -1)))
 mapped=[]
 for j in tri:
  t={}
  for row,c in tori[j].items():
   k,s=sq_image[row];t[k]=s*c
  mapped.append(lookup[tuple(sorted(t.items()))])
 def apply(v):
  z=[0]*72
  for k,c in enumerate(v):
   if c:
    a,s=mapped[k];z[a]+=s*c
  return z
 out=[[0]*3 for _ in range(3)]
 for j,r in enumerate(relarray):
  v=apply(r)
  coords=[v[d] for d in deps]
  assert [sum(coords[k]*relarray[k][i] for k in range(3)) for i in range(72)]==v
  for k in range(3):out[k][j]=coords[k]
 return out

def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def trace(A):return sum(A[i][i] for i in range(3))
Id=[[int(i==j) for j in range(3)] for i in range(3)]
M=[relation_action(s) for s in ((0,1),(2,3),(3,4),(5,6),(6,7),(7,8))]
assert all(A==[[-int(i==j) for j in range(3)] for i in range(3)] for A in M[:3])
assert all(trace(A)==-1 and matmul(A,A)==Id for A in M[3:])
assert trace(matmul(M[3],M[5]))==-1  # double transposition
assert trace(matmul(M[3],M[4]))==0  # 3-cycle
assert trace(matmul(matmul(M[3],M[4]),M[5]))==1  # 4-cycle
# S4 character is the parity twist of its three-dimensional standard irrep.

print('K234_TWO_POINT_TRIANGLE_TORUS_INTEGRAL_PRESENTATION_OK')
print('cells 36 182 198; rank_d2 129; rank_H2 69; tori 1206')
print('shortest tori 72; independent integral basis 69; three full relations')
print('relation character: S2 and S3 sign, S4 parity-twisted standard')
