#!/usr/bin/env python3
"""Reproducible finite and local-chain checks for a cycle-power neighborhood theorem.
Uses only Python's standard library; no network access or stored data files.
"""
from itertools import combinations
from collections import defaultdict, deque, Counter

FAMILIES = [
 ((0,1,2,4,5),(0,1,2,4,5,6)),
 ((0,1,2,4),(0,1,2,4,6)),
 ((0,1,2,5),(0,1,2,5,6)),
 ((0,1,3,4),(0,1,3,4,5)),
 ((0,1,2,-3),(0,1,2,-4,-3)),
 ((0,1,2,-4),(0,1,2,-4,-2)),
 ((0,1,3),(0,1,3,5)),
 ((0,2,-3),(0,2,-4,-3)),
 ((0,1,4),(0,1,4,5)),
 ((0,2,-4),(0,2,-4,-2)),
]
TEMPLATES = ((0,1,2,6),(0,1,5,6),(0,2,3,4),(0,2,4,5),(0,2,5,6))
CORRECTIONS = {
 1: [((-2,2,4),(-2,2,3,4))],
 2: [],
 3: [((-3,-2,1,2),(-3,-2,-1,1,2)),
     ((1,4,6),(1,4,5,6)),
     ((-3,-2,1),(-3,-2,-1,1)),
     ((-2,-1,1),(-2,-1,1,2))],
}
MISSING_BY_DIM = {1:{2:8,3:18,4:10,5:2},
                  2:{2:6,3:16,4:10,5:2},
                  3:{1:2,2:10,3:18,4:10,5:2}}

def mask(values,n,shift=0):
 ans=0
 for v in values:
  bit=1 << ((v+shift)%n)
  assert not(ans & bit)
  ans|=bit
 return ans

def subfaces(f):
 out=[0]
 x=f
 while x:
  bit=x&-x;x-=bit
  out += [a|bit for a in out[:]]
 return out

def neigh_complex(n,d=0):
 assert n>=13 and d in range(4)
 adj=[]
 for i in range(n):
  s={(i+j)%n for j in (-3,-2,-1,1,2,3)}
  if i==0 and d:s.discard(d)
  if d and i==d:s.discard(0)
  adj.append(s)
 ans={0}
 for s in adj:
  f=mask(s,n)
  ans.update(subfaces(f))
 return ans

def cofacets(f,K,n):
 return [f | (1<<i) for i in range(n)
         if not((f>>i)&1) and (f|(1<<i)) in K]

def elementary(K,f,c,n):
 assert f in K and c in K and f.bit_count()+1==c.bit_count()
 assert cofacets(f,K,n)==[c], (n,f,c,cofacets(f,K,n))
 K.remove(f);K.remove(c)

def defect_collapse(n,d):
 K=neigh_complex(n,d)
 skipped=defaultdict(list)
 for j,(L,U) in enumerate(FAMILIES,1):
  for i in range(n):
   f=mask(L,n,i);c=mask(U,n,i)
   if f not in K or c not in K:
    skipped[j].append(i)
   elif cofacets(f,K,n)==[c]:elementary(K,f,c,n)
   else:
    assert j==9 and d==3 and i in ((n-3)%n,(n-2)%n)
    skipped[j].append(i)
 for f,c in CORRECTIONS[d]: elementary(K,mask(f,n),mask(c,n),n)
 assert max(x.bit_count() for x in K)==4
 return K,dict(skipped)

def m_complex(n):
 M={0}
 for t in TEMPLATES:
  for i in range(n):M.update(subfaces(mask(t,n,i)))
 return M

def dual_condition(K,n):
 tets={f for f in K if f.bit_count()==4}
 tri=defaultdict(list)
 for t in tets:
  for v in range(n):
   if t>>v&1:tri[t^(1<<v)].append(t)
 assert all(1<=len(cs)<=2 for cs in tri.values())
 boundary=[cs[0] for cs in tri.values() if len(cs)==1]
 assert boundary
 graph={t:set() for t in tets}
 for cs in tri.values():
  if len(cs)==2:
   a,b=cs;graph[a].add(b);graph[b].add(a)
 seen=set(boundary);queue=list(boundary)
 for t in queue:
  for u in graph[t]:
   if u not in seen:seen.add(u);queue.append(u)
 assert seen==tets, (n,len(seen),len(tets))
 # A spanning forest from the exposed boundary yields unimodular triangular
 # pivots for both boundary_3 and its transpose, hence H_3=H^3=0.
 return len(tets),sum(len(cs)==1 for cs in tri.values())

def boundary_matrices(R,n):
 groups=defaultdict(list)
 for x in R: groups[x.bit_count()-1].append(x)
 for x in groups.values():x.sort()
 mat={}
 for k in groups:
  if k<1:continue
  low={x:i for i,x in enumerate(groups.get(k-1,[]))}
  a=[[0 for _ in groups[k]] for _ in low]
  for j,face in enumerate(groups[k]):
   vs=[v for v in range(n) if face>>v&1]
   for pos,v in enumerate(vs):
    f=face^(1<<v)
    if f in low:a[low[f]][j]=1 if pos%2==0 else -1
  mat[k]=a
 return groups,mat

def mat_product_zero(groups,mat):
 for k in range(2,max(groups)+1):
  if k not in mat or k-1 not in mat:continue
  a,b=mat[k-1],mat[k]
  if not a or not b:continue
  for r in range(len(a)):
   for c in range(len(b[0])):
    assert sum(a[r][t]*b[t][c] for t in range(len(b)))==0

def unit_reduction(groups,mat):
 # Exact unimodular chain cancellation at ±1 pivot, Schur complement.
 groups={k:v[:] for k,v in groups.items()}
 mat={k:[row[:] for row in a] for k,a in mat.items()}
 cancellations=[]
 for k in range(max(groups),0,-1):
  while k in mat and mat[k] and mat[k][0]:
   a=mat[k];pivot=next(((i,j) for i,row in enumerate(a)
                for j,v in enumerate(row) if abs(v)==1),None)
   if pivot is None:break
   i,j=pivot;u=a[i][j]
   mat[k]=[[a[r][c]-a[r][j]*a[i][c]//u
            for c in range(len(a[0])) if c!=j]
           for r in range(len(a)) if r!=i]
   if k-1 in mat:
    mat[k-1]=[[v for c,v in enumerate(row) if c!=i]
              for row in mat[k-1]]
   if k+1 in mat:
    mat[k+1]=[row for r,row in enumerate(mat[k+1]) if r!=j]
   cancellations.append((k,groups[k-1].pop(i),groups[k].pop(j),u))
 mat_product_zero(groups,mat)
 return groups,mat,cancellations

def relative_condition(n,d):
 R=neigh_complex(n,0)-neigh_complex(n,d)
 groups,mat=boundary_matrices(R,n)
 mat_product_zero(groups,mat)
 assert {k:len(v) for k,v in groups.items()}==MISSING_BY_DIM[d]
 final,remaining,steps=unit_reduction(groups,mat)
 assert {k:len(v) for k,v in final.items() if v}=={3:2}
 assert len(steps)=={1:18,2:16,3:20}[d]
 assert not any(v for a in remaining.values() for row in a for v in row)
 return steps

def normalize_relative(R,n):
 return frozenset(tuple(sorted(v if v<=9 else v-n
              for v in range(n) if face>>v&1)) for face in R)

def mod2_betti(K):
 by=defaultdict(list)
 for x in K:
  if x:by[x.bit_count()-1].append(x)
 for a in by.values():a.sort()
 rank={}
 for k in range(1,max(by)+1):
  low={f:i for i,f in enumerate(by[k-1])}
  basis={}
  for f in by[k]:
   z=0
   for v in range(f.bit_length()):
    if f>>v&1:z^=1<<low[f^(1<<v)]
   while z:
    b=z.bit_length()-1
    if b not in basis:basis[b]=z;break
    z^=basis[b]
  rank[k]=len(basis)
 return {k:len(v)-rank.get(k,0)-rank.get(k+1,0)-(k==0)
         for k,v in by.items()}

def verify():
 # For n>=25, the relative face systems occupy the fixed offset window
 # [-3,6], and membership is decided in the fixed neighborhood window
 # [-6,9]; this is the basis of the unbounded local reduction lemma.
 reference={d:normalize_relative(neigh_complex(25,0)-neigh_complex(25,d),25)
            for d in (1,2,3)}
 for d in (1,2,3):
  vertices={v for f in reference[d] for v in f}
  assert min(vertices)==-3 and max(vertices)==d+3
 for n in range(13,49):
  for d in (1,2,3):
   K,skip=defect_collapse(n,d)
   tets,boundary=dual_condition(K,n)
   assert tets==5*n-6
   assert boundary=={1:14,2:14,3:12}[d]
   steps=relative_condition(n,d)
   if n<=20 or n in (25,48):
    assert mod2_betti(neigh_complex(n,d))=={0:0,1:1,2:2,3:0,4:0,5:0}
   if n>=25:
    assert normalize_relative(neigh_complex(n)-neigh_complex(n,d),n)==reference[d]
   if n in (13,25,48):
    print('n=%d fault-distance=%d relative-pairs=%d tetrahedra=%d exposed-triangles=%d OK'%
          (n,d,len(steps),tets,boundary))
 print('VERIFY_OK')
if __name__=='__main__':verify()
