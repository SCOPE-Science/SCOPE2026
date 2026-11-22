#!/usr/bin/env python3
"""Exact finite proof certificate for single-edge faults of the Tietze graph.
Standalone Python 3 stdlib; reads FAULT_CERTIFICATE.json in its own directory.
"""
import json
from pathlib import Path
from collections import deque
from itertools import combinations
P=Path(__file__).resolve().parent
C=json.loads((P/'FAULT_CERTIFICATE.json').read_text('utf-8'))
N=12
base=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5,7),(7,9),(9,6),(6,8),(8,5)]
E={tuple(sorted((a-1,b-1))) for a,b in base if 0 not in (a,b)}
E.update([(9,10),(9,11),(10,11),(0,9),(3,10),(4,11)])
assert sorted(map(list,E))==C['graph_edges']
assert len(E)==18
A=[set() for _ in range(N)]
for a,b in E:A[a].add(b);A[b].add(a)
assert all(len(ns)==3 for ns in A)
assert sum(all((u,v) in E for u,v in combinations(t,2)) for t in combinations(range(N),3))==1
# The unique triangle distinguishes four invariant edge categories by endpoint
# distances to its three vertices. Explicit certified graph automorphisms
# act transitively within each, proving four, and only four, edge orbits.
def distance(adj):
 d=[]
 for start in range(N):
  dist=[N+1]*N;dist[start]=0;Q=deque([start])
  while Q:
   v=Q.popleft()
   for w in adj[v]:
    if dist[w]>N:dist[w]=dist[v]+1;Q.append(w)
  assert max(dist)<N+1
  d.append(dist)
 return d
D=distance(A)
autos=C['automorphisms'];assert len(autos)==12 and len({tuple(a) for a in autos})==12
for a in autos:
 assert sorted(a)==list(range(N))
 assert {tuple(sorted((a[u],a[v]))) for u,v in E}==E
edge_groups={}
for ed in E:
 u,v=ed
 key=tuple(sorted((min(D[t][u] for t in (9,10,11)),min(D[t][v] for t in (9,10,11)))))
 edge_groups.setdefault(key,set()).add(ed)
assert len(edge_groups)==4
assert {tuple(x['representative']) for x in C['edge_orbits']}=={tuple(z['edge']) for z in C['cases']}
for orbit in C['edge_orbits']:
 e=tuple(orbit['representative']);group={tuple(x) for x in orbit['edges']}
 assert group == {tuple(sorted((a[e[0]],a[e[1]]))) for a in autos}
 assert any(group==g for g in edge_groups.values())
assert {tuple(e) for orb in C['edge_orbits'] for e in orb['edges']}==E

def rips(adj,r):
 d=distance(adj)
 bad=[(i,j) for i in range(N) for j in range(i+1,N) if d[i][j]>r]
 return {s for s in range(1,1<<N) if not any((s>>i&1) and (s>>j&1) for i,j in bad)}
def faces_of_size(F,k):return {s for s in F if s.bit_count()==k}
def check_collapse(F,pairs):
 F=set(F)
 for idx,(s,t) in enumerate(pairs):
  assert s in F and t in F,(idx,'missing face')
  assert (s&t)==s and (t^s).bit_count()==1,(idx,'codimension')
  co=[s|(1<<i) for i in range(N) if not(s>>i&1) and (s|(1<<i)) in F]
  assert co==[t],(idx,'not free')
  F.remove(s);F.remove(t)
 return F
def mod2_betti(F):
 gr={d:sorted(faces_of_size(F,d+1)) for d in range(N)}
 ranks={}
 for d in range(1,N):
  m={s:i for i,s in enumerate(gr[d-1])}; piv={}
  for s in gr[d]:
   col=0
   for i in range(N):
    if s>>i&1:col^=1<<m[s^(1<<i)]
   while col:
    j=col.bit_length()-1
    if j not in piv:piv[j]=col;break
    col^=piv[j]
  ranks[d]=len(piv)
 return {d:len(gr[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(N) if len(gr[d])-ranks.get(d,0)-ranks.get(d+1,0)}

def verify_core(F,c):
 R=check_collapse(F,c['radius_two_collapses'])
 assert sorted(R)==c['radius_two_residual_faces']
 assert max(s.bit_count() for s in R)==3
 V={i for s in R if s.bit_count()==1 for i in range(N) if s>>i&1}
 Ed={tuple(i for i in range(N) if s>>i&1) for s in R if s.bit_count()==2}
 Tri={tuple(i for i in range(N) if s>>i&1) for s in R if s.bit_count()==3}
 tree={tuple(e) for e in c['spanning_tree']}
 assert len(tree)==len(V)-1 and tree<=Ed
 par={i:i for i in V}
 def root(i):
  while par[i]!=i:i=par[i]
  return i
 for u,v in tree:
  assert root(u)!=root(v)
  par[root(u)]=root(v)
 assert len({root(i) for i in V})==1
 active=Ed-tree; used=set()
 for e,t in c['relator_eliminations']:
  e,t=tuple(e),tuple(t)
  assert t in Tri and t not in used
  sides={(t[0],t[1]),(t[0],t[2]),(t[1],t[2])}
  assert sides & active=={e}
  used.add(t);active.remove(e)
 assert not active and len(used)==len(Ed)-len(V)+1
 # Each relator has exactly one live generator: a nonabelian Tietze
 # elimination and a unit-pivot integral boundary elimination.
 # Thus pi_1=0, H_1=0, and integral H_2 is free of rank below.
 b2=len(Tri)-len(Ed)+len(V)-1
 assert b2>=1 and mod2_betti(F)=={0:1,2:b2}
 return len(R),b2,len(c['radius_two_collapses']),len(c['relator_eliminations'])
expected={(0,1):(5,4,4),(0,9):(5,1,5),(1,2):(5,4,4),(9,10):(6,2,3)}
for c in C['cases']:
 e=tuple(c['edge'])
 adj=[set(ns) for ns in A];u,v=e;adj[u].remove(v);adj[v].remove(u)
 diam=max(max(x) for x in distance(adj))
 assert diam==c['diameter'] and diam==expected[e][2]
 F1=rips(adj,1)
 assert len(F1)-len(faces_of_size(F1,1))==17 + (1 if e!=(9,10) else 0)
 b1=expected[e][0]
 assert mod2_betti(F1)=={0:1,1:b1}
 F2=rips(adj,2)
 fvec=[len(faces_of_size(F2,k)) for k in range(1,13)]
 assert fvec[:len(c['face_vector_radius_two'])]==c['face_vector_radius_two']
 assert all(x==0 for x in fvec[len(c['face_vector_radius_two']):])
 length,b2,steps,rels=verify_core(F2,c)
 assert b2==expected[e][1]
 for r in range(3,diam):
  F=rips(adj,r)
  R=check_collapse(F,c[f'radius_{r}_collapses'])
  assert sorted(R)==c[f'radius_{r}_residual_faces']
  assert len(R)==1
 assert len(rips(adj,diam))==2**12-1
 print(f'edge class {e}: orbit {next(len(g) for g in edge_groups.values() if e in g)}; diameter {diam}; H1 rank {b1}; radius-2 wedge of {b2} spheres; {steps} free-face pairs, {rels} primitive group relators; later stages contractible')
print('Four edge-orbit classes cover all 18 edges; 12 explicit automorphisms checked.')
print('All higher-scale elementary-collapse certificates checked; exact mod-two cross-checks PASS.')
print('ALL CHECKS PASSED')
