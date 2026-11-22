#!/usr/bin/env python3
"""Exact integral certificate for the third homology of three points on GP(12,5).

Run: python3 verify_nauru.py NAURU_WITNESS.json
Requires Python 3.10+; no external packages. Every rank and determinant is exact.
"""
import json
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations

W = json.load(open(sys.argv[1] if len(sys.argv)>1 else 'NAURU_WITNESS.json',encoding='utf-8'))
N=12
edges=sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} |
             {tuple(sorted((i,N+i))) for i in range(N)} |
             {tuple(sorted((N+i,N+(i+5)%N))) for i in range(N)})
assert len(edges)==36
edge_number={e:i for i,e in enumerate(edges)}
adj=[set() for _ in range(24)]
for a,b in edges:adj[a].add(b);adj[b].add(a)
assert all(len(a)==3 for a in adj)
local={v:sorted(edge_number[tuple(sorted((v,w)))] for w in adj[v]) for v in range(24)}

# All simple cycles up to length twelve, oriented canonically.
cycles=set()
def dfs(path):
 v=path[-1];start=path[0]
 if len(path)>=6 and start in adj[v] and start==min(path):
  p=tuple(path);cycles.add(min(p,p[::-1]))
 if len(path)==12:return
 for w in sorted(adj[v]):
  if w>start and w not in path:dfs(path+[w])
for start in range(24):dfs([start])
count=Counter(map(len,cycles))
assert count=={6:24,8:108,10:216,12:492},count
short=sorted([c for c in cycles if len(c)==6])+sorted([c for c in cycles if len(c)==8])
assert [list(c) for c in short]==W['cycles_short']
mask=lambda c:sum(1<<v for v in c)
masks=[mask(c) for c in short]
triples=[]
for i,j,k in combinations(range(len(short)),3):
 if not (masks[i]&masks[j] or masks[i]&masks[k] or masks[j]&masks[k]):triples.append((i,j,k))
assert len(triples)==1040
pair_unions=[]
for i,j in combinations(range(len(short)),2):
 if not (masks[i]&masks[j]):pair_unions.append(masks[i]|masks[j])
assert all(all(mask(c)&u for u in pair_unions) for c in cycles if len(c)>=10), 'missed longer-cycle triple'

# The degree-three part of the reduced Swiatkowski chain complex.
# A basis element is (three distinct vertices, two half-edge choices at each).
cols=[]; col_number={}
for vs in combinations(range(24),3):
 for bits in range(8):
  ts=(1+(bits&1),1+((bits>>1)&1),1+((bits>>2)&1))
  col_number[(vs,ts)]=len(cols);cols.append((vs,ts))
assert len(cols)==16192
row_number={}
column_boundaries=[]
for vs,ts in cols:
 b={}
 for j in range(3):
  u=tuple(vs[i] for i in range(3) if i!=j)
  t=tuple(ts[i] for i in range(3) if i!=j)
  for side,e in enumerate((local[vs[j]][0],local[vs[j]][ts[j]])):
   key=(u,t,e)
   if key not in row_number:row_number[key]=len(row_number)
   r=row_number[key]
   b[r]=b.get(r,0)+(-1)**(j+side+1)
   if b[r]==0:del b[r]
 column_boundaries.append(b)
assert len(row_number)==39600

# Modular rank bounds the characteristic-zero rank from below.
pivots={}
for b in column_boundaries:
 x={r:v%3 for r,v in b.items() if v%3}
 while x:
  k=max(x)
  if k not in pivots:
   inv=pow(x[k],-1,3)
   pivots[k]={r:c*inv%3 for r,c in x.items()};break
  a=x[k]
  for r,c in pivots[k].items():
   x[r]=(x.get(r,0)-a*c)%3
   if not x[r]:del x[r]
assert len(pivots)==16132,len(pivots)

def zero_boundary(chain):
 result={}
 for idx,coeff in chain.items():
  for r,c in column_boundaries[idx].items():
   result[r]=result.get(r,0)+coeff*c
   if not result[r]:del result[r]
 return not result

def local_cycle(c):
 arr=[]
 for j,v in enumerate(c):
  outgoing=edge_number[tuple(sorted((v,c[(j+1)%len(c)])))]
  incoming=edge_number[tuple(sorted((v,c[(j-1)%len(c)])))]
  for e,sgn in ((outgoing,1),(incoming,-1)):
   if e!=local[v][0]:arr.append((v,local[v].index(e),sgn))
 return arr

def sort_sign(a,b,c):
 z=(a>b)+(a>c)+(b>c)
 return -1 if z%2 else 1

def torus(i,j,k):
 out={}
 for v,t,a in local_cycle(short[i]):
  for w,u,b in local_cycle(short[j]):
   for x,z,c in local_cycle(short[k]):
    ordered=sorted(((v,t),(w,u),(x,z)))
    idx=col_number[(tuple(p for p,q in ordered),tuple(q for p,q in ordered))]
    out[idx]=out.get(idx,0)+a*b*c*sort_sign(v,w,x)
    if not out[idx]:del out[idx]
 return out

# Exact characteristic-zero rank of all geometric simple-cycle product tori.
torus_pivots={};chosen=[]
for triple in triples:
 z=torus(*triple)
 assert zero_boundary(z)
 x=z.copy()
 while x:
  k=max(x)
  if k not in torus_pivots:
   a=x[k];torus_pivots[k]={r:Fraction(v,a) for r,v in x.items()}
   chosen.append(triple);break
  a=x[k]
  for r,c in torus_pivots[k].items():
   x[r]=x.get(r,0)-a*c
   if not x[r]:del x[r]
assert len(torus_pivots)==59,len(torus_pivots)

# A rank-sixty integral cycle basis with a unimodular coordinate minor.
nonproduct={int(i):int(c) for i,c in W['nonproduct_cycle']}
assert len(nonproduct)==5034 and max(map(abs,nonproduct.values()))==4
assert zero_boundary(nonproduct)
assert len(W['torus_triples'])==59
assert all(tuple(t) in triples for t in W['torus_triples'])
basis=[torus(*t) for t in W['torus_triples']]+[nonproduct]
assert len(set(tuple(t) for t in W['torus_triples']))==59
assert all(zero_boundary(x) for x in basis)
minor_rows=W['minor_rows']
assert len(minor_rows)==60 and len(set(minor_rows))==60
matrix=[[z.get(r,0) for z in basis] for r in minor_rows]

def determinant_bareiss(m):
 m=[row[:] for row in m];n=len(m);den=1;sgn=1
 for k in range(n-1):
  if not m[k][k]:
   swap=next((j for j in range(k+1,n) if m[j][k]),None)
   if swap is None:return 0
   m[k],m[swap]=m[swap],m[k];sgn=-sgn
  pivot=m[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    numerator=m[i][j]*pivot-m[i][k]*m[k][j]
    assert numerator%den==0
    m[i][j]=numerator//den
   m[i][k]=0
  den=pivot
 return sgn*m[n-1][n-1]
minor=determinant_bareiss(matrix)
assert abs(minor)==1,minor
print('NAURU_THREE_PARTICLE_TOP_HOMOLOGY_OK')
print('simple_cycles:',dict(sorted(count.items())))
print('all_product_tori:',len(triples),'integral_rank:',len(torus_pivots))
print('degree_three_generators:',len(cols),'boundary_mod3_rank:',len(pivots))
print('integral_cycle_basis:',len(basis),'coordinate_minor_determinant:',minor)
print('nonproduct_cycle_terms:',len(nonproduct))
