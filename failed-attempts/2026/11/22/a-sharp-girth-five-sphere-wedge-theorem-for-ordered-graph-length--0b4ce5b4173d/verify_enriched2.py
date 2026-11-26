#!/usr/bin/env python3
"""Reproducible exact rational-rank checks for the inclusive ordered length nerve at scales 1 and 2."""
from itertools import combinations, permutations
from collections import deque
from sympy import Matrix

def metric(v, E):
 adj=[set() for _ in range(v)]
 for a,b in E: adj[a].add(b); adj[b].add(a)
 d=[]
 for u in range(v):
  ds={u:0};Q=deque([u])
  while Q:
   x=Q.popleft()
   for y in adj[x]:
    if y not in ds:ds[y]=ds[x]+1;Q.append(y)
  assert len(ds)==v
  d.append([ds[k] for k in range(v)])
 return d

def rank_mod(m,p):
 m=[[int(x)%p for x in row] for row in m.tolist()]
 if not m:return 0
 rows,cols=len(m),len(m[0]);i=0
 for j in range(cols):
  r=next((k for k in range(i,rows) if m[k][j]),None)
  if r is None:continue
  m[i],m[r]=m[r],m[i];z=pow(m[i][j],-1,p)
  for k in range(i+1,rows):
   if m[k][j]:
    fac=m[k][j]*z%p
    for t in range(j,cols):m[k][t]=(m[k][t]-fac*m[i][t])%p
  i+=1
  if i==rows:break
 return i

def check(name,v,E,expected=True):
 E={tuple(sorted(e)) for e in E}; d=metric(v,E)
 edges1=[(a,b) for a in range(v) for b in range(v) if a!=b and d[a][b]<=1]
 edges2=[(a,b) for a in range(v) for b in range(v) if a!=b and d[a][b]<=2]
 triangles=[(a,b,c) for a in range(v) for b in range(v) for c in range(v) if a!=b and b!=c and d[a][b]+d[b][c]<=2]
 d1=Matrix(v,len(edges2),lambda i,j: int(edges2[j][1]==i)-int(edges2[j][0]==i))
 epos={e:i for i,e in enumerate(edges2)}
 d2=Matrix(len(edges2),len(triangles),lambda i,j:0)
 for j,(a,b,c) in enumerate(triangles):
  for edge,sgn in [((b,c),1),((a,c),-1),((a,b),1)]:
   if edge[0]!=edge[1]:d2[epos[edge],j]+=sgn
 assert d1*d2==Matrix.zeros(v,len(triangles))
 ranks={p:(rank_mod(d1,p),rank_mod(d2,p)) for p in (2,3,101)}
 assert len(set(ranks.values()))==1
 r1,r2=next(iter(ranks.values()))
 b1=len(edges2)-r1-r2;b2=len(triangles)-r2
 k=len(E)-v+1
 if expected:assert (b1,b2)==(k,len(E)),(name,b1,b2,k,len(E))
 # verify 2-cycles z_e and their linear independence and signed automorphism scheme
 for u,vv in E:
  z=Matrix.zeros(len(triangles),1)
  z[triangles.index((u,vv,u)),0]=1
  z[triangles.index((vv,u,vv)),0]=-1
  assert d2*z==Matrix.zeros(len(edges2),1)
 print(name,'vertices',v,'graph_edges',len(E),'nondegenerate cells', (v,len(edges2),len(triangles)),'ranks', (r1,r2),'Betti_1_2',(b1,b2),'expected', (k,len(E)))
 return b1,b2

if __name__=='__main__':
 check('K2',2,[(0,1)])
 check('P4',4,[(0,1),(1,2),(2,3)])
 check('star_5',6,[(0,k) for k in range(1,6)])
 check('C5',5,[(i,(i+1)%5) for i in range(5)])
 check('C6',6,[(i,(i+1)%6) for i in range(6)])
 check('C5_with_leaf',6,[(i,(i+1)%5) for i in range(5)]+[(0,5)])
 check('theta_3x3',8,[(0,2),(2,3),(3,1),(0,4),(4,5),(5,1),(0,6),(6,7),(7,1)]) # girth 6
 check('triangle_exception',3,[(0,1),(1,2),(2,0)],False)
 check('square_exception',4,[(i,(i+1)%4) for i in range(4)],False)
 print('ALL_TESTS_PASS')
