from itertools import combinations,permutations
from collections import defaultdict
from time import monotonic
T=monotonic()
n=5
E=[]
for l in range(2):
 for i in range(n): E.append((l*n+i,l*n+(i+1)%n))
for i in range(n): E.append((i,n+i))
E=[tuple(sorted(e)) for e in E]
edgeidx={e:i for i,e in enumerate(E)}
P=[]
for flip in range(2):
 for sign in [1,-1]:
  for shift in range(n):
   perm=[]
   for e in E:
    def p(x):return (x//n^flip)*n+(sign*(x%n)+shift)%n
    perm.append(edgeidx[tuple(sorted(p(x) for x in e))])
   P.append(perm)
faces=[0]
for mask in range(1,1<<15):
 used=0;good=True
 for i,e in enumerate(E):
  if mask>>i&1:
   for a in e:
    if used>>a&1:good=False;break
    used|=1<<a
   if not good:break
 if good:faces.append(mask)
print('faces',len(faces),'max',max(x.bit_count() for x in faces),'t',monotonic()-T,flush=True)
# every flag is chain of distinct faces from singleton to arbitrary face with gaps (barycentric subdivision)
# start by non-empty face, and add all strict subset flags ending with given face
face_set=set(faces)
chains={0:[]} ; bydim=defaultdict(list)
for f in sorted(faces[1:],key=lambda x:x.bit_count()):
 def gen(f):
  yield (f,)
  sub=(f-1)&f
  while sub:
   if sub in face_set:
    for c in gen(sub):yield c+(f,)
   sub=(sub-1)&f
 for c in gen(f): bydim[len(c)-1].append(c)
print('chains',[(d,len(ch)) for d,ch in bydim.items()],'t',monotonic()-T,flush=True)
# orbit representatives of flags under automorphisms (stabilizer preserves ordering)
def act(mask,p):
 result=0
 for i in range(15):
  if mask>>i&1:result|=1<<p[i]
 return result
reps={};oid={};cnums={}
for d,cs in sorted(bydim.items()):
 r=[];od={}
 for c in cs:
  if c in od:continue
  k=len(r);r.append(c)
  for p in P:od[tuple(act(f,p) for f in c)]=k
 reps[d]=r;oid[d]=od;cnums[d]=len(r)
print('orbits',cnums,'t',monotonic()-T,flush=True)
# boundary by deleting a barycentric simplex vertex
bound={}
for d,rs in reps.items():
 if d==0:continue
 B=[]
 for c in rs:
  vec=defaultdict(int)
  for j in range(len(c)):
   idx=oid[d-1][c[:j]+c[j+1:]]
   vec[idx]+=(-1)**j
  B.append({i:v for i,v in vec.items() if v})
 bound[d]=B
# Fp sparse row elimination of matrices as COLUMN vectors
for p in (2,3,5,7,11,101):
 ranks={0:0}
 for d,B in bound.items():
  piv={}
  for col in B:
   v={i:a%p for i,a in col.items() if a%p}
   while v:
    i=min(v)
    if i not in piv:
     inv=pow(v[i],-1,p)
     piv[i]={j:(a*inv)%p for j,a in v.items()};break
    scale=v[i];w=piv[i]
    for j,a in w.items():
     nv=(v.get(j,0)-scale*a)%p
     if nv:v[j]=nv
     elif j in v:del v[j]
  ranks[d]=len(piv)
 bet=[cnums[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(5)]
 print('field',p,'ranks',ranks,'bettis',bet,'t',monotonic()-T,flush=True)
# Integral elementary cancellations on quotient chain complex
alive={d:set(range(cnums[d])) for d in range(5)}
V={d:[dict(c) for c in B] for d,B in bound.items()}
# d=1..4 V[d][col] sparse bottom row map
# check d*d=0 initial
for d in range(2,5):
 for c in V[d]:
  s=defaultdict(int)
  for i,a in c.items():
   for j,b in V[d-1][i].items():s[j]+=a*b
  assert not any(s.values()),(d,s)
print('boundary squared = 0',flush=True)
changes=[]
for d in range(4,0,-1):
 while True:
  pair=None
  for c in alive[d]:
   for i,a in V[d][c].items():
    if i in alive[d-1] and abs(a)==1:
     pair=(c,i,a);break
   if pair:break
  if not pair:break
  c,i,s=pair
  pivot=V[d][c]
  for other in alive[d]:
   if other==c:continue
   a=V[d][other].pop(i,0)
   if a:
    for j,b in pivot.items():
     if j==i:continue
     nv=V[d][other].get(j,0)-a*s*b
     if nv: V[d][other][j]=nv
     else: V[d][other].pop(j,None)
  alive[d].remove(c);alive[d-1].remove(i)
  if d+1 in V:
   for top in alive.get(d+1,[]): V[d+1][top].pop(c,None)
  if d-1 in V:V[d-1][i]={}
  changes.append((d,c,i))
 print('cancel at',d,'total',len(changes),'survivors', {d:len(alive[d]) for d in range(5)},'t',monotonic()-T,flush=True)
# verify residual differential d²=0
for d in range(2,5):
 for c in alive[d]:
  s=defaultdict(int)
  for i,a in V[d][c].items():
   for j,b in V[d-1][i].items():s[j]+=a*b
  assert not any(s.values()),(d,s)
print('integral residual', {d:len(alive[d]) for d in range(5)})
for d in range(1,5):
 print('nonzero in d',d,[(c,V[d][c]) for c in alive[d] if V[d][c]])
# Fundamental group of original complex: elementary triangle edge-word Tietze eliminations
vertices=[1<<i for i in range(15)]
edges=[];triangles=[]
for mask in faces[1:]:
 if mask.bit_count()==2:edges.append(mask)
 if mask.bit_count()==3:triangles.append(mask)
# spanning tree of original 1-skeleton
pa=list(range(15))
def root(x):
 while pa[x]!=x:x=pa[x]
 return x
tree=set()
for e in edges:
 ii=[i for i in range(15) if e>>i&1]; a,b=map(root,ii)
 if a!=b:pa[a]=b;tree.add(e)
assert len(tree)==14
# triangle relators vanish generators when only one non-tree edge (then recurse).
gens=set(edges)-tree
rels=[set([ (1<<i)|(1<<j) for i,j in combinations([k for k in range(15) if tri>>k&1],2)])-tree for tri in triangles]
changes=0
while True:
 kills=set()
 for rel in rels:
  remaining=rel&gens
  if len(remaining)==1:kills.update(remaining)
 if not kills:break
 gens-=kills;changes+=len(kills)
print('original π1 elementary eliminations',changes,'remaining',len(gens),'#edgefaces',len(edges),'#triangles',len(triangles),'t',monotonic()-T)
