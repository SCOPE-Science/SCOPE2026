#!/usr/bin/env python3
"""Exact small-case enumeration of rank-two faces from supporting objectives.
Uses vertex exposure rather than contraction/chromatic AO counting.
"""
from itertools import permutations,combinations
from math import comb
from collections import Counter

def edges(p,q):return [(i,p+j) for i in range(p) for j in range(q)]

def vertex_list(p,q):
 n=p+q; E=edges(p,q); out=set()
 for order in permutations(range(n)):
  pos={v:i for i,v in enumerate(order)}
  v=[0]*n
  for a,b in E:
   v[a if pos[a]>pos[b] else b]+=1
  out.add(tuple(v))
 return sorted(out)

def face_area_squared(V):
 assert len(V)==4,(len(V),V)
 base=V[0]; ds=[tuple(a-b for a,b in zip(v,base)) for v in V[1:]]
 for k in range(3):
  i,j=[x for x in range(3) if x!=k]
  if all(ds[i][t]+ds[j][t]==ds[k][t] for t in range(len(base))):
   u,v=ds[i],ds[j]
   dot=lambda a,b:sum(x*y for x,y in zip(a,b))
   return dot(u,u)*dot(v,v)-dot(u,v)**2
 raise AssertionError(('non-parallelogram',V))

def exhaustive_faces(p,q):
 n=p+q; E=edges(p,q); verts=vertex_list(p,q); faces=set(); cnt=Counter()
 for (u,v),(s,t) in combinations(E,2):
  parent=list(range(n))
  def find(x):
   while parent[x]!=x:x=parent[x]
   return x
  def union(a,b):parent[find(a)]=find(b)
  union(u,v);union(s,t)
  roots=sorted(set(find(x) for x in range(n)))
  # all rank-two edge-pair flats have exactly n-2 components in bipartite graph
  assert len(roots)==n-2
  root_index={x:i for i,x in enumerate(roots)}
  groups=[root_index[find(x)] for x in range(n)]
  for order in permutations(range(n-2)):
   heights=[0]*(n-2)
   for i,x in enumerate(order):heights[x]=i
   h=[heights[groups[x]] for x in range(n)]
   scores=[sum(a*b for a,b in zip(h,w)) for w in verts]
   mx=max(scores)
   face=tuple(w for w,sc in zip(verts,scores) if sc==mx)
   faces.add(face)
 for face in faces:
  cnt[face_area_squared(face)]+=1
 return cnt,len(verts)

def B(a,b,s):
 S=[[0]*(a+1) for _ in range(a+1)];S[0][0]=1
 for n in range(1,a+1):
  for k in range(1,n+1):S[n][k]=k*S[n-1][k]+S[n-1][k-1]
 return sum((-1)**(a+j)*S[a][j]*__import__('math').prod(s+t for t in range(j))*(s+j)**b for j in range(a+1))

def claimed(p,q):
 Rh=p*comb(q,2)*B(p-1,q-2,2)+q*comb(p,2)*B(p-2,q-1,2)
 Sq=4*comb(p,2)*comb(q,2)*B(p-2,q-2,3)
 return Counter({3:Rh,4:Sq})
if __name__=='__main__':
 for p,q in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3)]:
  result,nverts=exhaustive_faces(p,q)
  formula=claimed(p,q)
  print((p,q),'vertices',nverts,'areas_squared',dict(result),'formula',dict(formula),flush=True)
  assert result==formula
 print('BICLIQUE_AREA_FACE_EXACT_PASS')
