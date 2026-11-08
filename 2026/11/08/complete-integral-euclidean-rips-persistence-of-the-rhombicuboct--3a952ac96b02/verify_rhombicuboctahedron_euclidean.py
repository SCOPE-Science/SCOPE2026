#!/usr/bin/env python3
"""Exact finite certificates for Euclidean rhombicuboctahedron Rips complexes.
Run in the directory containing the three JSON certificates. Python standard library only.
"""
import collections, itertools, json, pathlib
P=pathlib.Path(__file__).resolve().parent
read=lambda name:json.loads((P/name).read_text('utf-8'))
COL=read('collapse_certificate.json')
RANK=read('rank_certificate.json')
FILL=read('filling.json')

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return(x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sg(x):
 a,b=x
 if a==b==0:return 0
 if a>=0 and b>=0:return 1
 if a<=0 and b<=0:return -1
 if a>0 and b<0:return 1 if a*a>2*b*b else -1
 return -1 if a*a>2*b*b else 1

A=(1,1);O=(1,0)
verts=[]
for pos in range(3):
 for signs in itertools.product((-1,1),repeat=3):
  verts.append(tuple(tuple(signs[i]*v for v in (A if i==pos else O)) for i in range(3)))
verts=sorted(set(verts))
assert len(verts)==24

def dist2(v,w):
 out=(0,0)
 for x,y in zip(v,w):
  z=sub(x,y);out=add(out,mul(z,z))
 return out
D={(i,j):dist2(verts[i],verts[j]) for i in range(24) for j in range(i+1,24)}
SHELLS=[(4,0),(8,0),(8,4),(12,4),(12,8),(16,8),(20,8)]
assert list(sorted(set(D.values()),key=lambda x:SHELLS.index(x)))==SHELLS
assert [sum(d==s for d in D.values()) for s in SHELLS]==[48,36,48,48,36,48,12]

def cliques(stage):
 edges={e for e,d in D.items() if d in SHELLS[:stage]}
 neighbors=[set() for _ in range(24)]
 for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
 faces=set()
 def build(pre,allow):
  for i,v in enumerate(allow):
   z=pre+(v,);faces.add(z)
   build(z,[w for w in allow[i+1:] if w in neighbors[v]])
 build((),list(range(24)))
 return faces

# Validate the fixed triangulation of the actual convex-polyhedron boundary.
tris={tuple(t) for t in COL['surface_triangles']}
assert len(tris)==44 and all(len(t)==3 and t==tuple(sorted(t)) for t in tris)
surface=set()
for t in tris:
 for k in (1,2,3):surface.update(itertools.combinations(t,k))
assert collections.Counter(map(len,surface))=={1:24,2:66,3:44}
counts=collections.Counter(e for t in tris for e in itertools.combinations(t,2))
assert len(counts)==66 and set(counts.values())=={2}
for v in range(24):
 lk=[tuple(x for x in t if x!=v) for t in tris if v in t]
 assert len(lk)>=3
 deg=collections.Counter(w for e in lk for w in e)
 assert all(x==2 for x in deg.values())
 seen={next(iter(deg))}
 while True:
  old=len(seen)
  for u,w in lk:
   if u in seen:seen.add(w)
   if w in seen:seen.add(u)
  if len(seen)==old:break
 assert len(seen)==len(deg)
assert 24-66+44==2
# Check surface triangles are exactly 8 graph triangles + 2 per one of 18 induced square faces.
e1={e for e,d in D.items() if d==SHELLS[0]}
surf_gtri={t for t in itertools.combinations(range(24),3) if all(e in e1 for e in itertools.combinations(t,2))}
assert len(surf_gtri)==8
squares=[]
for q in itertools.combinations(range(24),4):
 es=[e for e in itertools.combinations(q,2) if e in e1]
 if len(es)==4 and all(sum(v in e for e in es)==2 for v in q):squares.append(q)
assert len(squares)==18
want=set(surf_gtri)
for q in squares:
 missing=[e for e in itertools.combinations(q,2) if e not in e1]
 assert len(missing)==2
 a,b=min(missing)
 for c in q:
  if c not in (a,b):want.add(tuple(sorted((a,b,c))))
assert want==tris
print('SURFACE_OK f=(24,66,44) 8 triangles + 18 triangulated squares')

def normal_sign(t):
 pts=[verts[i] for i in t]
 p,q,r=pts
 u=[sub(q[i],p[i]) for i in range(3)];v=[sub(r[i],p[i]) for i in range(3)]
 cross=[sub(mul(u[1],v[2]),mul(u[2],v[1])),sub(mul(u[2],v[0]),mul(u[0],v[2])),sub(mul(u[0],v[1]),mul(u[1],v[0]))]
 dot=(0,0)
 for i in range(3):
  s=(0,0)
  for pt in pts:s=add(s,pt[i])
  dot=add(dot,mul(s,cross[i]))
 return sg(dot)

orient={t:normal_sign(t) for t in tris}
assert all(s in (-1,1) for s in orient.values())
boundary=collections.Counter()
for t,s in orient.items():
 for i,e in enumerate(itertools.combinations(t,2)):
  # deleted position i gives t with that index removed
  e=t[:i]+t[i+1:]
  boundary[e]+=s*(-1)**i
assert all(x==0 for x in boundary.values())
print('INTEGRAL_SURFACE_CYCLE_OK 44 signed triangles')

# Replay every elementary collapse with current cofaces (no historical or external evidence).
def replay(stage):
 faces=cliques(stage)
 cofaces={f:set() for f in faces}
 for t in faces:
  if len(t)>1:
   for s in itertools.combinations(t,len(t)-1):cofaces[s].add(t)
 obj=COL['stages'][str(stage)]
 assert obj['initial_faces']==len(faces)
 for a,b in obj['pairs']:
  s=tuple(a);t=tuple(b)
  assert s in faces and t in faces and len(t)==len(s)+1
  assert cofaces[s]=={t} and len(cofaces[t])==0
  if stage<=4:assert s not in surface and t not in surface
  for f in (s,t):
   if len(f)>1:
    for u in itertools.combinations(f,len(f)-1):
     if u!=s:cofaces[u].remove(f)
   faces.remove(f)
 if stage<=4:assert faces==surface
 else:
  assert len(faces)==obj['remaining_faces']
  assert max(map(len,faces))==4
 print('COLLAPSE_OK stage',stage,'pairs',len(obj['pairs']),'remaining',len(faces))
 return faces

# Stage 1: 8 disjoint 2-simplices can be collapsed to a graph with rank 17.
f1=cliques(1)
assert collections.Counter(map(len,f1))=={1:24,2:48,3:8}
tri1=[f for f in f1 if len(f)==3]
assert len(set(itertools.chain.from_iterable(tri1)))==24
# The edge graph is connected, hence each of the eight disjoint 2-faces
# has a free edge and leaves a connected graph with 40 edges.
edge_adjacency={i:set() for i in range(24)}
for e in f1:
 if len(e)==2:
  a,b=e;edge_adjacency[a].add(b);edge_adjacency[b].add(a)
visited={0};stack=[0]
while stack:
 for v in edge_adjacency[stack.pop()]:
  if v not in visited:visited.add(v);stack.append(v)
assert len(visited)==24
assert 48-8-24+1==17
print('SCALE_ONE_OK 8 disjoint triangles, wedge of 17 circles')
for stage in (2,3,4):replay(stage)
reduced5=replay(5)
f5=cliques(5)

# Every new edge from stage 4 to 5 forms a triangle with two older edges;
# hence these attachments cannot create pi_1 after stage 4 retracts to S^2.
f4=cliques(4)
E4={t for t in f4 if len(t)==2};E5={t for t in f5 if len(t)==2}
assert len(E5-E4)==36
for a,b in E5-E4:
 assert any(tuple(sorted((a,v))) in E4 and tuple(sorted((v,b))) in E4 for v in range(24) if v not in (a,b))
print('SIMPLY_CONNECTED_STAGE5_OK 36 new edges triangularly killed')

# Unit-pivot integer elimination: verifies rank 751 and unimodular minor
# of d_3, therefore im(d_3) is a direct summand of the free group C_2.
tri=sorted(f for f in f5 if len(f)==3)
ix={f:i for i,f in enumerate(tri)}
tetra=sorted(f for f in f5 if len(f)==4)
assert len(tri)==944 and len(tetra)==2202
basis={};pivots=[]
for t in tetra:
 col={ix[t[:k]+t[k+1:]]:(-1)**k for k in range(4)}
 while col:
  p=max(col)
  if p not in basis:
   assert abs(col[p])==1
   basis[p]=dict(col)
   pivots.append([list(t),list(tri[p]),col[p]])
   break
  x=basis[p]
  assert abs(x[p])==1
  q=col[p]//x[p]
  for row,val in x.items():
   w=col.get(row,0)-q*val
   if w:col[row]=w
   else:col.pop(row,None)
assert len(basis)==751 and pivots==RANK['unimodular_pivots']
assert RANK['triangle_count']==944 and RANK['tetrahedron_count']==2202
# d_2 has maximal possible rank 193 over F2, hence rank 193 over Q.
edges=sorted(f for f in f5 if len(f)==2)
edge_ix={f:i for i,f in enumerate(edges)}
B={}
for t in tri:
 c=0
 for k in range(3):c ^=1<<edge_ix[t[:k]+t[k+1:]]
 while c:
  p=c.bit_length()-1
  if p not in B:B[p]=c;break
  c^=B[p]
assert len(B)==193 and len(edges)==216
assert len(basis)+len(B)==len(tri)
print('INTEGRAL_H2_STAGE5_ZERO_OK d2_rank=193 d3_unit_minor_rank=751')

# Explicit integral 3-chain whose signed boundary equals the orientation cycle.
tetra_set=set(tetra)
check=collections.Counter()
for vv,coef in FILL:
 t=tuple(vv)
 assert t in tetra_set and coef in (-1,1)
 for k in range(4):check[t[:k]+t[k+1:]]+=coef*(-1)**k
check={t:c for t,c in check.items() if c}
assert check==orient
print('FILLING_OK',len(FILL),'oriented tetrahedra')

# Final next stage is boundary of 12-dimensional cross-polytope.
# Precisely 12 missing pairs at shell 6, a perfect matching, all filled at shell 7.
missing={e for e,d in D.items() if d==SHELLS[6]}
assert len(missing)==12
assert set(itertools.chain.from_iterable(missing))==set(range(24))
print('LATE_STAGES_OK 12 antipodal pairs -> S11, then full simplex')
print('VERIFY_OK')
