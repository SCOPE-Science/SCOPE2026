#!/usr/bin/env python3
"""Independent exact invariant-cochain computation for a nine-generator graph Lie algebra."""
from itertools import combinations
from collections import defaultdict
from sympy import Matrix
edges=((0,1),(0,2),(0,3),(1,2),(1,3))
basis=[[tuple(v) for v in combinations(range(9),k)] for k in range(10)]
perms={'e':(0,1,2,3),'h':(1,0,2,3),'t':(0,1,3,2),'ht':(1,0,3,2)}
def wedge(t):
 if len(set(t))<len(t):return None,0
 s=(-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
 return tuple(sorted(t)),s
def act(t,g):
 u=[];sign=1
 for a in t:
  if a<4:u.append(perms[g][a])
  else:
   b,c=edges[a-4];b,c=perms[g][b],perms[g][c]
   if b>c:b,c=c,b;sign=-sign
   u.append(4+edges.index((b,c)))
 x,s=wedge(u)
 return x,sign*s
def d(t):
 out=defaultdict(int)
 for j,a in enumerate(t):
  if a<4:continue
  b,c=edges[a-4]
  nxt,s=wedge(t[:j]+(b,c)+t[j+1:])
  if s:out[nxt]+=(-1)**j*s
 return {u:z for u,z in out.items() if z}
def invariant_vectors(k,group):
 seen=set();vecs=[]
 for x in basis[k]:
  if x in seen:continue
  closure={act(x,g)[0] for g in group}
  seen.update(closure)
  signs={};good=True
  for g in group:
   y,s=act(x,g)
   if y in signs and signs[y]!=s:good=False
   signs[y]=s
  if good:
   assert len(signs)==len(closure)
   vecs.append(signs)
 return vecs
def rank_of_d(vecs):
 if not vecs:return 0
 images=[];keys=set()
 for v in vecs:
  col=defaultdict(int)
  for x,c in v.items():
   for y,a in d(x).items():col[y]+=c*a
  col={u:v for u,v in col.items() if v}
  keys.update(col);images.append(col)
 keys=sorted(keys)
 if not keys:return 0
 M=Matrix([[v.get(key,0) for v in images] for key in keys]);return M.rank()
for group in [('e',),('e','h'),('e','t'),('e','h','t','ht')]:
 vs=[invariant_vectors(k,group) for k in range(10)]
 ranks=[rank_of_d(vs[k]) for k in range(9)]
 dim=list(map(len,vs))
 bt=[dim[k]-(ranks[k-1] if k else 0)-(ranks[k] if k<9 else 0) for k in range(10)]
 print(','.join(group),'dims',dim,'ranks',ranks,'betti',bt,'total',sum(bt))
