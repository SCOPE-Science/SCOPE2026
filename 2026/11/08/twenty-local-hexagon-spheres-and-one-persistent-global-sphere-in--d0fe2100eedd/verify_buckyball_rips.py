#!/usr/bin/env python3
"""Exact integral certificate for two intrinsic Rips stages of the truncated-icosahedral graph. Python 3, standard library only."""
from collections import Counter, defaultdict, deque
import heapq

ROT = (
 (1,5,4,3,2),
 (0,2,6,10,5),
 (1,0,3,7,6),
 (2,0,4,8,7),
 (3,0,5,9,8),
 (4,0,1,10,9),
 (10,1,2,7,11),
 (6,2,3,8,11),
 (7,3,4,9,11),
 (8,4,5,10,11),
 (5,1,6,11,9),
 (9,10,6,7,8),
)
ORIG_EDGES = {tuple(sorted((u,v))) for u in range(12) for v in ROT[u]}
assert len(ORIG_EDGES)==30
assert all(len(x)==5 for x in ROT)
assert all(u in ROT[v] for u in range(12) for v in ROT[u])
ARCS = sorted((u,v) for u in range(12) for v in ROT[u])
assert len(ARCS)==60
VI = {a:i for i,a in enumerate(ARCS)}
ADJ = [set() for _ in ARCS]
def join(a,b):
 x,y=VI[a],VI[b];ADJ[x].add(y);ADJ[y].add(x)
for u,v in ORIG_EDGES:join((u,v),(v,u))
for u in range(12):
 row=ROT[u]
 for a,b in zip(row,row[1:]+row[:1]):join((u,a),(u,b))
assert all(len(a)==3 for a in ADJ)
assert sum(map(len,ADJ))==180
D=[]
for origin in range(60):
 d=[-1]*60;d[origin]=0;todo=deque([origin])
 while todo:
  u=todo.popleft()
  for v in ADJ[u]:
   if d[v]<0:d[v]=d[u]+1;todo.append(v)
 assert all(x>=0 for x in d);D.append(d)
assert max(max(row) for row in D)==9

def all_faces(r):
 N=[sum(1<<j for j in range(60) if j>i and D[i][j]<=r) for i in range(60)]
 faces=[]
 def extend(face,available):
  while available:
   b=available&-available;available-=b
   j=b.bit_length()-1;x=face|b
   faces.append(x)
   extend(x,available&N[j])
 for i in range(60):
  faces.append(1<<i);extend(1<<i,N[i])
 assert len(faces)==len(set(faces))
 return set(faces)

def bits(s):
 while s:
  b=s&-s;s-=b;yield b.bit_length()-1

def face_boundary(y):
 row=list(bits(y))
 return {y-(1<<v):(1 if i%2==0 else -1) for i,v in enumerate(row)}

def collapse(faces):
 F=set(faces);up={x:set() for x in F}; heap=[]
 for y in F:
  for v in bits(y):
   x=y-(1<<v)
   if x in F:up[x].add(y)
 def add(x):
  if x.bit_count()>1 and len(up[x])==1:heapq.heappush(heap,((-x.bit_count(),x),x))
 for x in F:add(x)
 pairs=[]
 while heap:
  _,x=heapq.heappop(heap)
  if x not in F or len(up[x])!=1:continue
  y=next(iter(up[x]));assert y in F and y.bit_count()==x.bit_count()+1
  assert not up[y], 'A free face must have a maximal coface'
  pairs.append((x,y));F.remove(x);F.remove(y)
  for z in (x,y):
   for v in bits(z):
    w=z-(1<<v)
    if w in F:
     up[w].discard(z)
     if len(up[w])==1:add(w)
 assert len(faces)==2*len(pairs)+len(F)
 return F,pairs

def pi1_killed(core):
 # Collapse a spanning tree in the 1-skeleton, then eliminate triangular relators.
 edges=sorted(x for x in core if x.bit_count()==2)
 tris=sorted(x for x in core if x.bit_count()==3)
 vertices=set(bits(sum(x for x in core if x.bit_count()==1))) # sum over disjoint singleton masks
 assert len(vertices)==60
 neigh=[set() for _ in range(60)]
 for e in edges:
  a,b=list(bits(e));neigh[a].add(b);neigh[b].add(a)
 seen={0};todo=deque([0]);tree=set()
 while todo:
  u=todo.popleft()
  for v in sorted(neigh[u]):
   if v not in seen:
    seen.add(v);todo.append(v);tree.add((min(u,v),max(u,v)))
 assert len(seen)==60 and len(tree)==59
 generators={};k=0
 for e in edges:
  a,b=list(bits(e))
  if (a,b) not in tree:
   k+=1;generators[(a,b)]=k
 def reduce_word(word):
  o=[]
  for a in word:
   if o and o[-1]==-a:o.pop()
   else:o.append(a)
  while len(o)>1 and o[0]==-o[-1]:o=o[1:-1]
  return o
 relations=[]
 for t in tris:
  a,b,c=list(bits(t));w=[]
  for u,v in ((a,b),(b,c),(c,a)):
   g=generators.get((min(u,v),max(u,v)))
   if g:w.append(g if u<v else -g)
  ww=reduce_word(w)
  if ww:relations.append(ww)
 killed=set()
 while True:
  singles={abs(w[0]) for w in relations if len(w)==1}
  if not singles:break
  assert not (singles&killed)
  killed.update(singles)
  relations=[reduce_word([g for g in w if abs(g) not in singles]) for w in relations]
  relations=[w for w in relations if w]
 assert len(killed)==k and relations==[]
 return k

def tri(t):
 assert len(t)==3
 mask=sum(1<<v for v in t)
 assert mask.bit_count()==3
 sign=(-1)**sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
 return mask,sign

def add_chain(out,sequence,c=1):
 x,s=tri(sequence);out[x]+=c*s

def oriented_faces():
 # The original icosahedral triangular faces and the truncated pentagonal faces.
 triangles=[]
 for a in range(12):
  for b in range(a+1,12):
   for c in range(b+1,12):
    if b not in ROT[a] or c not in ROT[a] or c not in ROT[b]:continue
    def locally(x,y,z):
     row=ROT[x];return row[(row.index(y)+1)%5]==z
    cyc=(a,b,c) if locally(a,b,c) else (a,c,b)
    a0,b0,c0=cyc
    assert locally(a0,b0,c0) and locally(b0,c0,a0) and locally(c0,a0,b0)
    triangles.append(cyc)
 assert len(triangles)==20, len(triangles)
 # A triangular face u,v,w produces a truncated hexagon:
 # (u,v),(v,u),(v,w),(w,v),(w,u),(u,w).
 hexes=[]
 for u,v,w in triangles:
  hexes.append([VI[a] for a in ((u,v),(v,u),(v,w),(w,v),(w,u),(u,w))])
 pentagons=[[VI[(u,v)] for v in ROT[u]] for u in range(12)]
 # Orient both face sets so each graph edge appears with opposite signs.
 # Pentagons have one oriented edge (u,v)->(u,w) when w follows v.
 # Hexagons have the opposite (u,w)->(u,v), hence orientations above match.
 directed=Counter()
 for f in hexes+pentagons:
  for a,b in zip(f,f[1:]+f[:1]):
   assert b in ADJ[a]
   directed[(a,b)]+=1
 assert len(directed)==180
 assert all(directed[(b,a)]==1 for a,b in directed)
 return pentagons,hexes

PENT,HEX=oriented_faces()
z=defaultdict(int)
for f in PENT:
 for i in range(1,4):add_chain(z,(f[0],f[i],f[i+1]))
for f in HEX:
 for t in ((f[0],f[1],f[2]),(f[0],f[2],f[4]),(f[2],f[3],f[4]),(f[0],f[4],f[5])):add_chain(z,t)
z={x:v for x,v in z.items() if v}
assert len(z)==116 and set(map(abs,z.values()))=={1}
hexcycles=[]
for f in HEX:
 z_h=defaultdict(int)
 for p in (0,3):
  for q in (1,4):
   for s in (2,5):
    sign=(-1)**((p//3)+(q//4)+(s//5))
    add_chain(z_h,(f[p],f[q],f[s]),sign)
 assert len(z_h)==8
 hexcycles.append(dict(z_h))

def is_cycle(z):
 boundary=defaultdict(int)
 for t,a in z.items():
  assert t.bit_count()==3
  for edge,s in face_boundary(t).items():boundary[edge]+=s*a
 return all(not a for a in boundary.values())
assert is_cycle(z)
assert all(is_cycle(c) for c in hexcycles)

def transfer(z,pairs):
 out=z.copy()
 for x,y in pairs:
  if x.bit_count()==3 and y.bit_count()==4 and out.get(x,0):
   a=out[x];db=face_boundary(y);n=a*db[x]
   for t,c in db.items():
    out[t]=out.get(t,0)-n*c
    if not out[t]:del out[t]
 return out

res={}
for r in (2,3):
 F=all_faces(r);c,pairs=collapse(F)
 assert all(x.bit_count()<=3 for x in c)
 counts=Counter(x.bit_count() for x in c)
 killed=pi1_killed(c)
 # All dimensions above two have collapsed; simply connected CW 2-complex.
 euler=sum((-1)**(i+1)*counts[i] for i in counts)
 b2=euler-1
 zz=transfer(z,pairs)
 assert set(zz)<=c and is_cycle(zz)
 assert any(abs(a)==1 for a in zz.values())
 if r==2:
  print("observed",r,len(F),len(pairs),dict(counts),killed,b2,flush=True)
  assert (len(F),len(pairs),dict(counts),killed,b2)==(802,145,{1:60,2:245,3:207},186,21)
  # 20 local octahedral hexagon cycles plus the full polyhedral sphere.
  others=[transfer(h,pairs) for h in hexcycles]
  assert all(set(h)<=c and is_cycle(h) for h in others)
  basis=others+[zz]
  rows=sorted(x for x in c if x.bit_count()==3)
  # A unit determinant submatrix: for each local hex cycle choose a coordinate
  # supported by no other cycle; the global cycle has a coefficient +/-1.
  chosen=[]
  for i in range(20):
   candidates=[t for t in rows if abs(basis[i].get(t,0))==1 and all(basis[j].get(t,0)==0 for j in range(21) if j!=i)]
   assert candidates
   chosen.append(candidates[0])
  last=next(t for t in rows if abs(zz.get(t,0))==1 and t not in chosen)
  chosen.append(last)
  assert len(set(chosen))==21
  assert all(basis[j].get(chosen[i],0)==(basis[i].get(chosen[i],0) if i==j else 0) for i in range(20) for j in range(21))
  assert abs(zz[last])==1
  # determinant of this 21x21 minor is +/-1, without numerical linear algebra.
  assert b2==21
  print('r2: faces=802 pairs=145 core=(60,245,207) pi1 generators killed=186; H2=Z^21')
  print('r2: 20 hexagonal octahedron cycles + global sphere are an integral basis (unit minor)')
 else:
  print("observed",r,len(F),len(pairs),dict(counts),killed,b2,flush=True)
  assert (len(F),len(pairs),dict(counts),killed,b2)==(6462,3120,{1:60,2:110,3:52},51,1)
  assert len(zz)==52 and set(zz.values())=={-1,1}
  # Every local 6-gon has graph diameter 3 and hence is a 5-simplex at scale 3.
  assert all(max(D[a][b] for a in face for b in face)==3 for face in HEX)
  print('r3: faces=6462 pairs=3120 core=(60,110,52) pi1 generators killed=51; H2=Z')
  print('r3: image of global cycle has all 52 coefficients +/-1; primitive generator')
 res[r]=(F,c,pairs,zz,b2)
assert res[2][0]<res[3][0]
print('inclusion: 20 local hexagonal classes die; global sphere maps to generator; kernel Z^20')
print('ALL_CHECKS_PASS')
