#!/usr/bin/env python3
"""Subdivided cubical-model cross-check for three unordered particles on K3,3."""
import itertools,collections,sys,functools,time
from k33_research import rank_mod, group
E0=tuple((i,j) for i in range(3) for j in range(3,6))
# Original vertices 0..5, subdivision midpoints 6..14 indexed by original edge.
N=15
E=tuple(x for i,(a,b) in enumerate(E0) for x in ((a,6+i),(b,6+i)))
E=tuple(tuple(sorted(e)) for e in E)
EI={e:i for i,e in enumerate(E)}

def supports_edges(es):
 seen=set()
 for e in es:
  z=set(E[e]);
  if z&seen:return None
  seen.update(z)
 return seen

B=[]
for q in range(4):
 cur=[]
 for es in itertools.combinations(range(len(E)),q):
  used=supports_edges(es)
  if used is None:continue
  for verts in itertools.combinations((v for v in range(N) if v not in used),3-q):
   cur.append((tuple(verts),es))
 B.append(tuple(cur))
Ix=[{c:i for i,c in enumerate(cells)} for cells in B]

def boundary(q,c):
 verts,es=c
 for k,i in enumerate(es):
  a,b=E[i]
  for v,s in ((b,1),(a,-1)):
   nc=(tuple(sorted(verts+(v,))),es[:k]+es[k+1:])
   yield Ix[q-1][nc],((-1)**k)*s

def sign(perm):
 return -1 if sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))%2 else 1

def trace(g,q):
 gg=g+tuple(6+E0.index(tuple(sorted((g[a],g[b])))) for a,b in E0)
 tr=0
 for verts,es in B[q]:
  vv=tuple(sorted(gg[v] for v in verts))
  if vv!=verts:continue
  ee=[EI[tuple(sorted((gg[E[i][0]],gg[E[i][1]])))] for i in es]
  if tuple(sorted(ee))!=es:continue
  coeff=sign(ee)
  for i in es:
   u,v=E[i]
   coeff*=1 if gg[u]<gg[v] else -1
  tr+=coeff
 return tr

def main():
 t=time.time()
 print('cubical cells:',list(map(len,B)),flush=True)
 for q in range(2,4):
  for c in B[q]:
   acc=collections.Counter()
   for i,a in boundary(q,c):
    for j,b in boundary(q-1,B[q-1][i]):acc[j]+=a*b
   assert all(v==0 for v in acc.values())
 print('boundary-square-zero')
 rr=[]
 for q in (1,2,3):
  r=rank_mod((boundary(q,c) for c in B[q]),101)
  print('rank modulo 101',q,r,flush=True)
  rr.append(r)
 bs=[len(B[0])-rr[0],len(B[1])-rr[0]-rr[1],len(B[2])-rr[1]-rr[2],len(B[3])-rr[2]]
 print('Betti:',bs)
 assert bs==[1,4,8,0]
 for _,g in group():
  tr=[trace(g,q) for q in range(4)]
  alt=sum((-1)**q*tr[q] for q in range(4))
  from k33_research import graphcycletrace,symtrace
  assert alt==sum((-1)**q*symtrace(g,q) for q in range(4))
  assert alt==1-graphcycletrace(g)+(alt-1+graphcycletrace(g))
 print('All 72 Lefschetz traces agree with reduced model; elapsed seconds',round(time.time()-t,3))
if __name__=='__main__':main()
