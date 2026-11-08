#!/usr/bin/env python3
"""Combinatorial and character checks for the icosahedral three-cut complex.
Only Python standard library is used.  Vertex labels and graph are explicit.
"""
from collections import Counter, deque
from itertools import combinations, permutations

NEIGHBORS = (
    (1, 5, 7, 8, 11), (0, 2, 5, 6, 8), (1, 3, 6, 8, 9),
    (2, 4, 6, 9, 10), (3, 5, 6, 10, 11), (0, 1, 4, 6, 11),
    (1, 2, 3, 4, 5), (0, 8, 9, 10, 11), (0, 1, 2, 7, 9),
    (2, 3, 7, 8, 10), (3, 4, 7, 9, 11), (0, 4, 5, 7, 10),
)
N = 12
A = [set(x) for x in NEIGHBORS]
def edge(a,b):return b in A[a]
def mset(s):return sum(1<<i for i in s)
def els(m):return tuple(i for i in range(N) if m>>i&1)
def subfaces(m):
 for x in range(N):
  if m>>x&1:yield m^(1<<x)

# Characterize Alexander dual as subsets whose induced nonedges form a matching.
K = {m for m in range(1,1<<N) if all(sum(y!=x and not edge(x,y) for y in els(m))<=1 for x in els(m))}
fvector = [sum(m.bit_count()==d+1 for m in K) for d in range(4)]
assert fvector == [12,66,80,30] and max(m.bit_count() for m in K)==4
tri = {mset(t) for t in combinations(range(N),3) if all(edge(a,b) for a,b in combinations(t,2))}
assert len(tri)==20
sphere_faces={m for m in K if m.bit_count()<=2 and (m.bit_count()==1 or edge(*els(m)))}|tri

# Determine graph distance exactly, and all six antipodal pairs.
dists={}
for u in range(N):
 D={u:0};q=deque([u])
 while q:
  v=q.popleft()
  for w in A[v]:
   if w not in D:D[w]=D[v]+1;q.append(w)
 assert len(D)==N
 dists[u]=D
anti = sorted((u,v) for u in range(N) for v in range(u+1,N) if dists[u][v]==3)
dist2 = sorted((u,v) for u in range(N) for v in range(u+1,N) if dists[u][v]==2)
assert len(anti)==6 and len(dist2)==30
assert sorted(x for p in anti for x in p)==list(range(N))

T=[m for m in K if m.bit_count()==4]
assert len(T)==30
for u,v in dist2:
 shared=A[u]&A[v]
 assert len(shared)==2
 assert edge(*tuple(shared))
 tetra=mset((u,v,*shared))
 assert tetra in T
for tetra in T:
 vv=els(tetra)
 nonedges=[(u,v) for u,v in combinations(vv,2) if not edge(u,v)]
 assert len(nonedges)==1 and nonedges[0] in dist2
 assert sum(mset(x) in tri for x in combinations(vv,3))==2

# Explicit independent elementary collapses, preserving all original triangles.
remaining=set(K)
collapse=[]
for u,v in dist2:
 tetra=mset((u,v,*tuple(A[u]&A[v])))
 other=[w for w in els(tetra) if w not in (u,v)]
 # P3 triangles are {u,v,other[0]} and {u,v,other[1]}.
 t=mset((u,v,other[0]));t2=mset((u,v,other[1]))
 assert t in remaining and tetra in remaining
 assert sum(1 for f in remaining if (f&t)==t and f.bit_count()==4)==1
 remaining.remove(t);remaining.remove(tetra);collapse.append((t,tetra))
 assert t2 in remaining
 e=mset((u,v))
 assert sum(1 for f in remaining if (f&e)==e and f.bit_count()==3)==1
 remaining.remove(e);remaining.remove(t2);collapse.append((e,t2))
L=sphere_faces|{mset(p) for p in anti}
assert remaining==L and len(collapse)==60

# Independently build the cut complex from its disconnected-triple facets;
# compare Alexander-dual membership on every one of the 4096 subsets.
full=(1<<N)-1
disconnected={mset(t) for t in combinations(range(N),3)
              if sum(edge(a,b) for a,b in combinations(t,2))<=1}
assert len(disconnected)==140
Delta={m for m in range(1<<N) if any((t & (full^m))==t for t in disconnected)}
assert {m for m in range(1,1<<N) if (full^m) not in Delta}==K
assert [sum(m.bit_count()==j+1 for m in Delta) for j in range(9)] == [12,66,220,495,792,924,792,465,140]

# Independent chain-complex check of dual Betti ranks, over distinct fields.
def boundary_rank(faces_by_dim,d,p):
 rows={m:i for i,m in enumerate(faces_by_dim[d-1])}
 pivots={}
 for mask in faces_by_dim[d]:
  v={}
  for pos,x in enumerate(els(mask)):
   k=rows[mask^(1<<x)]
   val=(1 if pos%2==0 else -1)%p
   if val:v[k]=val
  while v:
   pivot=max(v)
   if pivot not in pivots:pivots[pivot]=v;break
   q=pivots[pivot]
   mult=v[pivot]*pow(q[pivot],-1,p)%p
   for row,a in q.items():
    val=(v.get(row,0)-mult*a)%p
    if val:v[row]=val
    elif row in v:del v[row]
 return len(pivots)
bydim={d:sorted(m for m in K if m.bit_count()==d+1) for d in range(4)}
for p in (2,3,5):
 ranks={d:boundary_rank(bydim,d,p) for d in (1,2,3)}
 assert ranks=={1:11,2:49,3:30},(p,ranks)

# Enumerate all graph automorphisms using the image of an ordered face.
base=(0,1,5)
assert all(edge(*p) for p in combinations(base,2))
faces3=[t for t in combinations(range(N),3) if mset(t) in tri]

def extend(partial):
 used=set(partial.values())
 if len(partial)==N:
  yield tuple(partial[i] for i in range(N));return
 free=[v for v in range(N) if v not in partial]
 def possibilities(v):
  return [w for w in range(N) if w not in used and all(edge(v,x)==edge(w,y) for x,y in partial.items())]
 chosen=min(free,key=lambda v:(len(possibilities(v)),-sum(edge(v,x) for x in partial)))
 for w in possibilities(chosen):
  partial[chosen]=w
  yield from extend(partial)
  del partial[chosen]

autos=set()
for face in faces3:
 for tgt in permutations(face):
  for perm in extend(dict(zip(base,tgt))):
   autos.add(perm)
assert len(autos)==120

def perm_order(g):
 cur=tuple(range(N));t=0
 while True:
  cur=tuple(g[cur[i]] for i in range(N));t+=1
  if cur==tuple(range(N)):return t

def sgngiven(xs):
 return -1 if sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))%2 else 1

# Orient the twenty triangular faces coherently as an S^2 complex.
orient={mset(base):base};todo=deque([base]); incidences={}
for face in faces3:
 for pair in combinations(face,2):incidences.setdefault(tuple(sorted(pair)),[]).append(mset(face))
assert all(len(v)==2 for v in incidences.values())
while todo:
 tr=todo.popleft();n=len(tr)
 for i in range(3):
  a,b=tr[i],tr[(i+1)%3]
  pair=tuple(sorted((a,b)))
  other=next(x for x in incidences[pair] if x!=mset(tr))
  t=next(x for x in els(other) if x not in (a,b))
  new=(b,a,t)
  if other in orient:
   ref=orient[other]
   assert new in (ref,ref[1:]+ref[:1],ref[2:]+ref[:2])
  else: orient[other]=new;todo.append(new)
assert len(orient)==20

def orientation_character(g):
 im=tuple(g[x] for x in base);ref=orient[mset(im)]
 return 1 if im in (ref,ref[1:]+ref[:1],ref[2:]+ref[:2]) else -1

def axis_trace(g):
 res=0
 for u,v in anti:
  a,b=g[u],g[v]
  if {a,b}=={u,v}:res+= 1 if (a,b)==(u,v) else -1
 return res

def reduced_lefschetz(g):
 s=-1  # subtract the trace on H_0 to obtain reduced trace
 for m in K:
  vs=els(m)
  imgs=[g[x] for x in vs]
  if mset(imgs)==m:
   s+=((-1)**(len(vs)-1))*sgngiven(imgs)
 return s

ctr=Counter();action_rows=Counter();chk=0
for g in autos:
 assert sgngiven(g)==1  # all 120 automorphisms even on twelve vertices
 o=perm_order(g);eps=orientation_character(g);trace=axis_trace(g)
 ctr[(o,eps,trace)]+=1
 assert reduced_lefschetz(g)==eps-trace
 # Completely separate signed fixed-simplex computation on Delta itself.
 cut_lefs=-1
 for m in Delta:
  if not m:continue
  vs=els(m);imgs=[g[x] for x in vs]
  if mset(imgs)==m:
   cut_lefs+=(-1)**(len(vs)-1)*sgngiven(imgs)
 assert cut_lefs==trace-eps
 chk+=1
 if eps==1:assert {1:(6,),2:(-2,),3:(0,),5:(1,)}[o][0]==trace
# Central inversion is the unique permutation swapping all antipodes.
anti_partner={u:v for u,v in anti for u,v in [(u,v),(v,u)]}
central=tuple(anti_partner[i] for i in range(N))
assert central in autos and orientation_character(central)==-1 and axis_trace(central)==-6
assert ctr[(1,1,6)]==1
assert sum(v for (o,e,t),v in ctr.items() if e==1)==60
assert sum(v for (o,e,t),v in ctr.items() if e==-1)==60
assert {o:sum(v for (oo,e,t),v in ctr.items() if oo==o and e==1) for o in (1,2,3,5)}=={1:1,2:15,3:20,5:24}
# Verify central reversal of the 6D axis module for every group element.
for g in autos:
 comp=tuple(central[g[i]] for i in range(N))
 assert axis_trace(comp)==-axis_trace(g)
 assert orientation_character(comp)==-orientation_character(g)

print('VERIFY_OK')
print('K_f_vector:',fvector,'S_triangles:',len(tri),'tetrahedra:',len(T))
print('cut_facets:',len(disconnected),'Delta_faces:',len(Delta)-1,'dual_boundary_ranks_2_3_5:',[11,49,30])
print('distance2_pairs:',len(dist2),'antipodal_edges:',anti)
print('elementary_collapses:',len(collapse),'remaining_faces:',len(remaining))
print('automorphisms:',len(autos),'orientation_preserving:',60)
print('rotational_A5_character_by_order: 1->6, 2->-2, 3->0, 5->1')
print('degree7_character: sphere_orientation, central_inversion=-1')
print('degree8_character: signed_permutation_on_6_antipodes, central_inversion=-I')
print('all_signed_Lefschetz_tests:',chk)
print('full_character_class_counts:',sorted((list(k),v) for k,v in ctr.items()))
