#!/usr/bin/env python3
"""Exact exhaustive Zariski-support enumerator for six blown-up conic points.

No external dependencies. Negative definiteness is tested by exact integer
Bareiss determinants of all leading principal minors; the search is exhaustive
because the intersection lattice has negative index six.
"""
from itertools import combinations
from collections import Counter
from math import comb

basis=[]
labels=[]
for i in range(6):
 v=[0]*7;v[i+1]=1;basis.append(tuple(v));labels.append('E'+str(i+1))
for i,j in combinations(range(6),2):
 v=[0]*7;v[0]=1;v[i+1]=-1;v[j+1]=-1
 basis.append(tuple(v)); labels.append('L'+str(i+1)+str(j+1))
basis.append((2,)+(-1,)*6);labels.append('C')
assert len(basis)==22

def pairing(x,y):
 return x[0]*y[0]-sum(a*b for a,b in zip(x[1:],y[1:]))
M=[[pairing(x,y) for y in basis] for x in basis]
assert Counter(M[i][i] for i in range(22))=={-1:21,-2:1}

def determinant(a):
 """Exact fraction-free elimination. Doesn't assume positive definiteness."""
 n=len(a)
 if n==0:return 1
 b=[list(row) for row in a]
 sign=1
 prev=1
 for k in range(n-1):
  p=next((j for j in range(k,n) if b[j][k]),None)
  if p is None:return 0
  if p!=k:
   b[k],b[p]=b[p],b[k];sign=-sign
  pivot=b[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=b[i][j]*pivot-b[i][k]*b[k][j]
    assert num%prev==0
    b[i][j]=num//prev
  for i in range(k+1,n):b[i][k]=0
  prev=pivot
 return sign*b[n-1][n-1]

def positive_definite(indices):
 # Symmetric integer -M: Sylvester principal-minor test.
 for r in range(1,len(indices)+1):
  rows=indices[:r]
  if determinant([[-M[i][j] for j in rows] for i in rows])<=0:
   return False
 return True

counts=Counter()
with_root=Counter()
for k in range(7):
 for indices in combinations(range(22),k):
  if positive_definite(indices):
   counts[k]+=1
   if 21 in indices:with_root[k]+=1
expected={0:1,1:22,2:156,3:490,4:725,5:447,6:57}
assert dict(counts)==expected,(counts,expected)
assert sum(counts.values())==1898
assert sum(with_root.values())==648
assert dict(with_root)=={1:1,2:21,3:120,4:260,5:210,6:36}

# Independent graph-count derivation: pairwise intersecting edge families on r vertices.
def F(r):
 d=Counter({0:1})
 if r>=2:d[1]+=comb(r,2)
 if r>=3:
  for k in range(2,r):d[k]+=r*comb(r-1,k)
  d[3]+=comb(r,3) # triangular triples
 return d
combinatorial=Counter()
for e in range(7):
 for k,v in F(6-e).items():
  combinatorial[e+k]+=comb(6,e)*v
for k,v in F(6).items():combinatorial[k+1]+=v
for k,v in F(5).items():combinatorial[k+2]+=6*v
assert combinatorial==counts

# Geometry checks:
for i in range(6):
 assert M[21][i]==1
for i in range(6,21):
 assert M[21][i]==0
for i in range(6):
 for j in range(i+1,6):assert M[i][j]==0
for k,(i,j) in enumerate(combinations(range(6),2),start=6):
 for z in range(6):assert M[k][z]==int(z in (i,j))

print('negative curves: 6 exceptional, 15 pair-lines, 1 (-2) conic')
print('support-size polynomial:', '+'.join(f'{counts[k]}t^{k}' for k in range(7)))
print('with (-2) conic:',','.join(f'{k}:{with_root[k]}' for k in range(1,7)))
print('Zariski chambers:',sum(counts.values()))
print('NEGATIVE_DEFINITE_ENUMERATION_OK')
