#!/usr/bin/env python3
"""Exact finite verification for the Euclidean Rips stages of the truncated octahedron.
Run with: python3 verify.py certificate.json
Requires only the Python standard library.
"""
import collections, itertools, json, sys

THRESHOLDS = (2,4,6,8,10,12)
EXPECTED = {
 2:((24,36),{0:1,1:13}),
 4:((24,48,24,6),{0:1,1:7}),
 6:((24,96,112,30),{0:1,2:9}),
 8:((24,120,208,150,48,8),{0:1,2:1}),
 10:((24,144,328,342,168,32),{0:1,2:1}),
 12:((24,168,472,618,384,92),{0:1,2:1}),
}


def points():
 return sorted({tuple(s*x for s,x in zip(sign,p)) for p in set(itertools.permutations((0,1,2))) for sign in itertools.product((-1,1),repeat=3)})

def distance2(a,b):return sum((x-y)**2 for x,y in zip(a,b))

def clique_faces(P,threshold):
 # Every clique appears exactly once in its ascending vertex order.
 neighbors={i:{j for j in range(i+1,len(P)) if distance2(P[i],P[j])<=threshold} for i in range(len(P))}
 result=set();stack=[((i,),set(neighbors[i])) for i in range(len(P))]
 while stack:
  face,candidates=stack.pop()
  result.add(face)
  for j in sorted(candidates):stack.append((face+(j,),candidates & neighbors[j]))
 return result

def matching_certificate_check(faces,pairs_data,critical_expected):
 faces_set=set(faces);used=set();matched={};pairs=[]
 for entry in pairs_data:
  assert len(entry)==2
  lo,hi=tuple(entry[0]),tuple(entry[1])
  assert lo in faces_set and hi in faces_set
  assert len(hi)==len(lo)+1 and set(lo)<set(hi)
  assert lo not in used and hi not in used
  used.add(lo);used.add(hi);matched[(lo,hi)]=True;pairs.append((lo,hi))
 critical=faces_set-used
 got=collections.Counter(len(x)-1 for x in critical)
 assert dict(got)==critical_expected, (dict(got),critical_expected)
 # Full oriented face-poset Hasse diagram; every cover is checked.
 indeg={f:0 for f in faces_set};adj={f:[] for f in faces_set};covers=0
 for hi in faces_set:
  if len(hi)==1:continue
  for j in range(len(hi)):
   lo=hi[:j]+hi[j+1:]
   assert lo in faces_set
   if (lo,hi) in matched:src,dst=lo,hi
   else:src,dst=hi,lo
   adj[src].append(dst);indeg[dst]+=1;covers+=1
 q=collections.deque(f for f,d in indeg.items() if d==0);seen=0
 while q:
  v=q.popleft();seen+=1
  for u in adj[v]:
   indeg[u]-=1
   if indeg[u]==0:q.append(u)
 assert seen==len(faces_set), ('cyclic matching',seen,len(faces_set))
 return len(pairs),covers,got

def boundary_complex(P):
 # Six square facets x_i=+/-2; eight hexagonal facets epsilon dot x=3.
 descriptions=[]
 for a in range(3):
  for s in (-1,1):descriptions.append([i for i,v in enumerate(P) if v[a]==2*s])
 for signs in itertools.product((-1,1),repeat=3):
  descriptions.append([i for i,v in enumerate(P) if sum(a*b for a,b in zip(signs,v))==3])
 assert collections.Counter(map(len,descriptions))=={4:6,6:8}
 triang=set()
 for f in descriptions:
  # Recover cyclic boundary from shortest-distance edges in the planar polygon.
  neigh={a:sorted(b for b in f if b!=a and distance2(P[a],P[b])==2) for a in f}
  assert all(len(n)==2 for n in neigh.values())
  start=min(f);order=[start,neigh[start][0]]
  while len(order)<len(f):
   candidates=[i for i in neigh[order[-1]] if i!=order[-2]]
   assert len(candidates)==1 and candidates[0] not in order
   order.append(candidates[0])
  assert order[0] in neigh[order[-1]]
  if len(f)==4:ts=[(order[0],order[1],order[2]),(order[0],order[2],order[3])]
  else:ts=[(order[0],order[2],order[4]),(order[0],order[1],order[2]),(order[2],order[3],order[4]),(order[4],order[5],order[0])]
  triang.update(tuple(sorted(t)) for t in ts)
 assert len(triang)==44
 B=set()
 for tri in triang:
  assert max(distance2(P[a],P[b]) for a,b in itertools.combinations(tri,2))<=6
  for j in (1,2,3):B.update(itertools.combinations(tri,j))
 assert collections.Counter(map(len,B))=={1:24,2:66,3:44}
 edges_count=collections.Counter(edge for tri in triang for edge in itertools.combinations(tri,2))
 assert set(edges_count.values())=={2} # closed triangulated convex-polytope surface
 # These supporting hyperplanes describe the actual truncated octahedron.
 assert len(descriptions)==14 and all(len(f)>=4 for f in descriptions)
 return B

def verify_radial(P,facets):
 # For any clique C, the vector sum of a containing maximal clique gives
 # a supporting open hemisphere, so origin is excluded from its convex hull.
 for c in facets:
  vector=tuple(sum(P[i][j] for i in c) for j in range(3))
  assert all(sum(vector[j]*P[i][j] for j in range(3))>0 for i in c)
 return len(facets)

def main():
 assert len(sys.argv)==2
 P=points();assert len(P)==24 and len(set(P))==24
 dist_counts=collections.Counter(distance2(a,b) for a,b in itertools.combinations(P,2))
 assert dict(dist_counts)=={2:36,4:12,6:48,8:24,10:24,12:24,14:48,16:12,18:36,20:12}
 # Compare intrinsic graph and Euclidean shells, keeping the metrics distinct.
 neighbors={i:{j for j in range(len(P)) if i!=j and distance2(P[i],P[j])==2} for i in range(len(P))}
 shell=collections.defaultdict(collections.Counter)
 for src in range(len(P)):
  q=collections.deque([src]);depth={src:0}
  while q:
   i=q.popleft()
   for j in neighbors[i]:
    if j not in depth:depth[j]=depth[i]+1;q.append(j)
  assert len(depth)==len(P)
  for dst in range(src+1,len(P)):
   shell[depth[dst]][distance2(P[src],P[dst])]+=1
 assert dict(shell[1])=={2:36}
 assert dict(shell[2])=={4:12,6:48}
 assert dict(shell[3])=={8:24,10:24,12:24}
 assert dict(shell[4])=={14:48,16:12}
 assert dict(shell[5])=={18:36} and dict(shell[6])=={20:12}
 B=boundary_complex(P)
 raw=json.load(open(sys.argv[1],encoding='utf-8'))
 assert set(raw)=={str(x) for x in THRESHOLDS}
 previous=set()
 for t in THRESHOLDS:
  F=clique_faces(P,t)
  assert previous<=F
  previous=F
  counts=collections.Counter(len(f)-1 for f in F)
  fvector=tuple(counts[i] for i in range(max(counts)+1))
  assert fvector==EXPECTED[t][0],(t,fvector)
  matches=raw[str(t)]
  critical=EXPECTED[t][1]
  pairs,covers,got=matching_certificate_check(F,matches,critical)
  assert pairs*2+sum(critical.values())==len(F)
  if t>=6:assert B<=F
  if t==12:
   facets=[f for f in F if not any(f!=g and set(f).issubset(g) for g in F)]
   assert len(facets)==92
   verify_radial(P,facets)
  print('SCALE',t,'FACES',len(F),'HASSE_COVERS',covers,'MATCHES',pairs,'CRITICAL',dict(sorted(got.items())))
 print('BOUNDARY_SPHERE',len(B),'faces, included from squared radius 6 through 12')
 print('RADIAL_SEPARATION_OK')
 print('VERIFY_OK')

if __name__=='__main__':main()
