"""Independent GF(4) orbit classification: u^2+u+1=0, elements 0..3."""
from itertools import product
from collections import Counter
MUL=[[0]*4 for _ in range(4)]
for a in range(4):
 for b in range(4):
  z=0
  for i in range(2):
   for j in range(2):
    if (a>>i)&1 and (b>>j)&1:
     k=i+j;z^=(1<<k if k<2 else 3)
  MUL[a][b]=z
assert MUL[2][2]==3 and MUL[3][2]==1

def rnk(n,edges,S):
 par=list(range(n))
 def root(v):
  while v!=par[v]:v=par[v]
  return v
 for e in S:
  a,b=edges[e];par[root(a)]=root(b)
 return n-len(set(root(v) for v in range(n)))

def exp(n,edges):
 res=Counter()
 for bits in product((0,1),repeat=len(edges)):
  S=[i for i,b in enumerate(bits) if b]
  r=rnk(n,edges,S)
  res[12**r]+=4**(n-r)*3**(len(S)-r)
 return res

def bfs(n,edges):
 m=len(edges);rem=set(product(range(4),repeat=n+m));hist=Counter();gen=[]
 for j,(u,v) in enumerate(edges):
  if u==v:continue
  for scalar in (1,2):
   def sh(x,j=j,u=u,v=v,scalar=scalar):
    y=list(x);w=MUL[scalar][x[n+j]];y[u]^=w;y[v]^=w;return tuple(y)
   gen.append(sh)
 for v in range(n):
  def sc(x,v=v):
   y=list(x)
   for j,(u,w) in enumerate(edges):
    if u==v and w!=v:y[n+j]=MUL[2][y[n+j]]
    if w==v and u!=v:y[n+j]=MUL[3][y[n+j]]
   return tuple(y)
  gen.append(sc)
 while rem:
  x=next(iter(rem));vis={x};queue=[x]
  while queue:
   a=queue.pop()
   for fn in gen:
    b=fn(a)
    if b not in vis:vis.add(b);queue.append(b)
  rem.difference_update(vis);hist[len(vis)]+=1
 return hist

for name,n,ed in [('edge',2,[(0,1)]),('parallel',2,[(0,1),(0,1)]),('loop',2,[(0,0)]),('triangle',3,[(0,1),(1,2),(2,0)])]:
 a,b=bfs(n,ed),exp(n,ed)
 assert a==b,(name,a,b)
 print('PASS GF4',name,'orbit histogram',dict(sorted(a.items())))
print('ALL_GF4_COADJOINT_ORBIT_CHECKS_PASS')
