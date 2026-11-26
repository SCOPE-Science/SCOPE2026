"""Exact finite-field and integral Frobenius certificate for a 27-line divisor."""
import itertools, collections
# GF4=F2[t]/(t^2+t+1), 0,1,t,t+1

def mm(a,b):
 c=0
 for i in range(2):
  for j in range(2):
   if a&(1<<i) and b&(1<<j):c^=1<<(i+j)
 if c&4:c^=7
 return c
assert all(mm(a,b)==mm(b,a) for a in range(4) for b in range(4))
frob=lambda a:mm(a,a)
nonzero=[1,2,3]
def norm(x):
 j=next(i for i,a in enumerate(x) if a)
 inv=next(b for b in nonzero if mm(x[j],b)==1)
 return tuple(mm(v,inv) for v in x)
P=sorted({norm(t) for t in itertools.product(range(4),repeat=4) if any(t)})
lines=[]
for pi in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]:
 a,b,c,d=pi
 for r in nonzero:
  for s in nonzero:
   pts={norm(tuple((mm(r,x) if i==b else x if i==a else mm(s,y) if i==d else y) for i in range(4))) for x,y in itertools.product(range(4),repeat=2) if x or y}
   assert len(pts)==5
   lines.append((pi,r,s,pts))
assert len(lines)==27
p2l=collections.defaultdict(list)
for i,(_,_,_,pts) in enumerate(lines):
 for p in pts:p2l[p].append(i)
assert collections.Counter(map(len,p2l.values()))=={3:45}
assert len(P)==85
assert all(sum(1 for v in p if v)!=1 for p in p2l)
assert len(p2l)==45 and set(map(len,p2l.values()))=={3}
keys=sorted(p2l)
Pindex={p:i for i,p in enumerate(keys)}
assert all(frob(0)==0 for _ in [1])
def fpoint(p):return norm(tuple(frob(x) for x in p))
def fline(i):
 pi,r,s,_=lines[i]; return next(j for j,(p,t,u,_) in enumerate(lines) if p==pi and t==frob(r) and u==frob(s))
vp=[fline(i) for i in range(27)]+[27+Pindex[fpoint(p)] for p in keys]
edges=sorted((i,27+Pindex[p]) for i,(_,_,_,pts) in enumerate(lines) for p in pts)
ei={e:i for i,e in enumerate(edges)}
ef=[ei[(vp[u],vp[v])] for u,v in edges]
assert len(edges)==135 and len(set(ef))==135
assert all(vp[vp[i]]==i for i in range(len(vp)))
assert sum(vp[i]==i for i in range(72))==10 and sum(ef[i]==i for i in range(135))==9
assert len(edges)-72+1==64
# construct fundamental cycles using BFS tree (also simple different order)
def fcycles(reverse=False):
 adj=[[] for _ in range(72)]
 for i,(u,v) in enumerate(edges):adj[u].append((v,i));adj[v].append((u,i))
 par={0:(-1,-1)};que=[0]
 for u in que:
  for v,i in sorted(adj[u],reverse=reverse):
   if v not in par:par[v]=(u,i);que.append(v)
 assert len(par)==72
 tree={i for u,(v,i) in par.items() if i>=0};chords=[i for i in range(135) if i not in tree]
 assert len(chords)==64
 def treepath(u,v):
  au=[]; av=[];x=u;y=v
  while x!=-1:au.append(x);x=par[x][0]
  while y!=-1:av.append(y);y=par[y][0]
  j=next(w for w in au if w in set(av))
  chain=[];x=u
  while x!=j:
   z,e=par[x];chain.append((e,1 if edges[e][0]==x else -1));x=z
  tail=[];y=v
  while y!=j:
   z,e=par[y];tail.append((e,1 if edges[e][0]==z else -1));y=z
  return chain+tail[::-1]
 cycles=[]
 for i in chords:
  u,v=edges[i];d={i:1}
  for e,s in treepath(v,u):d[e]=s
  cycles.append(d)
 # obtain F matrix on chord coeffs, source columns
 rankrows=[0]*64; tr=0
 for k,cy in enumerate(cycles):
  moved={ef[e]:v for e,v in cy.items()}
  for j,c in enumerate(chords):
   f=moved.get(c,0)
   if j==k:tr+=f
   if (f-(j==k))&1: rankrows[j]^=1<<k
 piv={};rank=0
 for row in rankrows:
  while row:
   b=row.bit_length()-1
   if b not in piv:piv[b]=row;rank+=1;break
   row^=piv[b]
 return rank,tr
assert fcycles()==(32,0) and fcycles(True)==(32,0)
print('CHAR2_FERMAT_CUBIC_INTEGRAL_PICARD_TORUS_OK')
print('lines=27, triple_points=45, branches=135, genus=109, torus_rank=64, unipotent_dimension=45')
print('fixed_vertices=10 fixed_branches=9, trace=0, rank_F2(F-I)=32 for two integral cycle bases')
