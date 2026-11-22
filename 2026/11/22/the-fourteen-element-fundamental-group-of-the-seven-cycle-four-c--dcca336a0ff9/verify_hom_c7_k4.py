"""Exact integral cellular and fundamental-group verifier for the
sevenfold rotation quotient of Hom(C_7,K_4). Python standard library only.
Run: python verify_hom_c7_k4.py
"""
from collections import defaultdict
import itertools, time, pickle
from pathlib import Path
BASE=Path(__file__).resolve().parent
n=7;c=4
sets=list(range(1,1<<c))
adj={s:[t for t in sets if not s&t] for s in sets}
faces=[]
def rec(p):
 if len(p)==n:
  if not p[-1]&p[0]:faces.append(tuple(p))
  return
 for t in adj[p[-1]] if p else sets:
  rec(p+[t])
rec([])
def canon(s):
 rots=[s[k:]+s[:k] for k in range(n)]
 k=min(range(n),key=lambda k:rots[k])
 D=[x.bit_count()-1 for x in s];cross=sum(D[:k])*sum(D[k:]);
 return rots[k],(-1 if cross&1 else 1)
orbits={canon(p)[0] for p in faces}
cells=[sorted([p for p in orbits if sum(x.bit_count()-1 for x in p)==i]) for i in range(6)]
inds=[{p:j for j,p in enumerate(level)} for level in cells]
print('orbit counts',list(map(len,cells)),flush=True)
B=[]
for d in range(1,6):
 cols=[]
 for p in cells[d]:
  v=defaultdict(int); base=0
  for i,x in enumerate(p):
   bits=[b for b in range(c) if x>>b &1]
   if len(bits)>1:
    for z,b in enumerate(bits):
     y=x-(1<<b); face=p[:i]+(y,)+p[i+1:]
     rep,sg=canon(face)
     v[inds[d-1][rep]]+=(-1)**(base+z)*sg
   base+=len(bits)-1
  cols.append({k:v for k,v in v.items() if v})
 B.append(cols)
 print('B',d,'nonzeros',sum(map(len,cols)),flush=True)
for d in range(1,5):
 for j,col in enumerate(B[d]):
  sums=defaultdict(int)
  for i,x in col.items():
   for z,v in B[d-1][i].items():sums[z]+=x*v
  if any(sums.values()):raise ValueError(('boundary not 0',d,j,{k:v for k,v in sums.items() if v}))
print('B² = 0',flush=True)



import pickle,heapq,time
# cells, B remain from the enumeration
N=[len(x) for x in cells]
R=[None]+[{i:{} for i in range(N[d-1])} for d in range(1,6)]
C=[None]+[{j:dict(c) for j,c in enumerate(B[d-1])} for d in range(1,6)]
for d in range(1,6):
 for j,cc in C[d].items():
  for i,v in cc.items():R[d][i][j]=v
live=[set(range(x)) for x in N]
heap=[]
def push(d,i,j):
 if i not in R[d] or j not in C[d]:return
 v=R[d][i].get(j)
 if v in [-1,1]:
  sc=(len(R[d][i])-1)*(len(C[d][j])-1)
  heapq.heappush(heap,(sc,d,i,j))
for d in range(1,6):
 for i,row in R[d].items():
  for j in row:push(d,i,j)
start=time.time(); count=0;maxcoeff=1
while heap:
 sc,d,i,j=heapq.heappop(heap)
 if i not in R[d] or j not in C[d]:continue
 v=R[d][i].get(j,0)
 if abs(v)!=1:continue
 sc2=(len(R[d][i])-1)*(len(C[d][j])-1)
 if sc2!=sc:
  heapq.heappush(heap,(sc2,d,i,j));continue
 rdict=dict(R[d][i]);cdict=dict(C[d][j]);
 for jc,b in rdict.items():
  if jc==j:continue
  for ir,a in cdict.items():
   if ir==i:continue
   old=C[d][jc].get(ir,0);new=old-a*b*v
   if new:
    C[d][jc][ir]=new;R[d][ir][jc]=new
    maxcoeff=max(maxcoeff,abs(new))
   else:
    C[d][jc].pop(ir,None);R[d][ir].pop(jc,None)
 # remove col j, row i from degree d
 for ir in cdict: R[d][ir].pop(j,None)
 for jc in rdict: C[d][jc].pop(i,None)
 R[d].pop(i); C[d].pop(j)
 live[d].remove(j);live[d-1].remove(i)
 # remove i column of B_{d-1}
 if d>1:
  for k in C[d-1][i]:R[d-1][k].pop(i,None)
  C[d-1].pop(i)
 # remove j row of B_{d+1}
 if d<5:
  for k in R[d+1][j]:C[d+1][k].pop(j,None)
  R[d+1].pop(j)
 # candidates on affected edges in B_d
 for jc in rdict:
  if jc in C[d]:
   for ir in C[d][jc]:push(d,ir,jc)
 for ir in cdict:
  if ir in R[d]:
   for jc in R[d][ir]:push(d,ir,jc)
 # modified scores in B_{d-1}, B_{d+1}
 if d>1:
  for k in cdict: # note k indexes B_d row, not relevant
   pass
  for k in []:pass
  # column i removed from B_{d-1}, affected rows
  # need values saved before deletion? no easy; all edges still in heap and stale update on pop
 if d<5:
  pass
 count+=1
 if count%500==0:print('cancel',count,'remaining',list(map(len,live)),'heap',len(heap),'maxabs',maxcoeff,'time',round(time.time()-start,2),flush=True)
print('done',count,'remaining',list(map(len,live)), 'maxabs',maxcoeff,'time',round(time.time()-start,2),flush=True)
for d in range(1,6):
 print(d,'shape',len(R[d]),len(C[d]),'nnz',sum(map(len,C[d].values())),flush=True)
for d in range(1,5):
 for col in C[d+1].values():
  out={}
  for i,v in col.items():
   for k,w in C[d][i].items():out[k]=out.get(k,0)+v*w
  if any(out.values()):raise Exception('B²')
print('B² =0 final',flush=True)



assert count==3957 and list(map(len,live))==[1,2,2,1,0,0]
assert all(not C[d] or all(not x for x in C[d].values()) for d in (1,3,4,5))
assert len(C[2])==2 and len(R[2])==2
rr=sorted(R[2]);cc=sorted(C[2]);a,b=[C[2][cc[0]].get(i,0) for i in rr];u,v=[C[2][cc[1]].get(i,0) for i in rr]
import math
assert abs(a*v-b*u)==14 and math.gcd(a,b,u,v)==1
print('HOMOLOGY_REDUCTION_OK: H0=Z H1=Z/14 H2=0 H3=Z H4=H5=0',flush=True)


import pickle,collections,sys,time
# cells, B remain from the enumeration
inds=[{p:i for i,p in enumerate(X)} for X in cells]
n=7;c=4
def cn(p):return min(p[k:]+p[:k] for k in range(n))
# endpoint oriented edges
eps=[]
for p in cells[1]:
 i=next(i for i,s in enumerate(p) if s.bit_count()==2)
 a,b=[j for j in range(c) if p[i]>>j&1]
 lo=cn(p[:i]+(1<<a,)+p[i+1:]);hi=cn(p[:i]+(1<<b,)+p[i+1:]);eps.append((inds[0][lo],inds[0][hi]))
# spanning tree
adj=[[] for _ in cells[0]]
for j,(u,v) in enumerate(eps):adj[u].append((v,j));adj[v].append((u,j))
from collections import deque
seen={0};q=deque([0]);tree=set()
while q:
 u=q.popleft()
 for v,j in adj[u]:
  if v not in seen:seen.add(v);q.append(v);tree.add(j)
assert len(seen)==len(cells[0])
gen={j:k+1 for k,j in enumerate(j for j in range(len(eps)) if j not in tree)}
assert len(gen)==1141
# find edge for single-coordinate transition. 0cells q1,q2 as actual (not canonical) colorings; for each edge, canonical rep from union of endpoint singleton masks

def edge_step(p,q):
 diff=[i for i in range(n) if p[i]!=q[i]]
 assert len(diff)==1
 i=diff[0]; e=p[:i]+(p[i]|q[i],)+p[i+1:]
 j=inds[1][cn(e)]
 # orientation positive if increase color
 sign=1 if p[i]<q[i] else -1
 return j,sign

def words(cell):
 p=cell; ds=[i for i,x in enumerate(p) if x.bit_count()>1]
 def singleton(mask):return 1<<(mask.bit_length()-1)
 if len(ds)==1:
  i=ds[0];bit=[1<<a for a in range(c) if p[i]>>a&1];assert len(bit)==3
  colorings=[]
  for b in bit:colorings.append(tuple(b if j==i else x for j,x in enumerate(p)))
  vertices=[colorings[j] for j in [0,1,2,0]]
 else:
  assert len(ds)==2
  i,j=ds;aa=[1<<k for k in range(c) if p[i]>>k&1];bb=[1<<k for k in range(c) if p[j]>>k&1]
  def make(a,b):return tuple(a if z==i else b if z==j else s for z,s in enumerate(p))
  vertices=[make(aa[0],bb[0]),make(aa[1],bb[0]),make(aa[1],bb[1]),make(aa[0],bb[1]),make(aa[0],bb[0])]
 w=[]
 for u,v in zip(vertices,vertices[1:]):
  e,sign=edge_step(u,v)
  if e in gen:w.append(sign*gen[e])
 return freereduce(w)
def freereduce(w):
 r=[]
 for a in w:
  if r and r[-1]==-a:r.pop()
  else:r.append(a)
 # cyclic free reduction
 while len(r)>1 and r[0]==-r[-1]:r=r[1:-1]
 return r
rel=[words(p) for p in cells[2]]
for jj,w in enumerate(rel):
 exponent=collections.Counter()
 for x in w:exponent[abs(x)]+=1 if x>0 else -1
 expected={gen[e]:v for e,v in B[1][jj].items() if e in gen}
 assert all(exponent[g]==expected.get(g,0) for g in set(exponent)|set(expected))
print('RELATOR_ABELIAN_BOUNDARIES_OK',flush=True)
print('initial',len(gen),'generators',len(rel),'relators',collections.Counter(map(len,rel)),flush=True)
# Tietze using generator with one occurrence in some relation and short relator, selective minimum cost
active=set(range(1,len(gen)+1))
R={i:w for i,w in enumerate(rel) if w}
rev=collections.defaultdict(set)
for k,w in R.items():
 for g in set(abs(x) for x in w):rev[g].add(k)
start=time.time();iters=0
while True:
 options=[]
 for k,w in R.items():
  count=collections.Counter(map(abs,w))
  for g,occ in count.items():
   if occ==1 and len(w)<=8:
    cost=(len(w)-1)*len(rev[g]);options.append((cost,len(w),len(rev[g]),k,g))
 if not options:break
 cost,l,deg,k,g=min(options)
 w=R[k]
 pos=next(i for i,a in enumerate(w) if abs(a)==g)
 cyc=w[pos:]+w[:pos];a=cyc[0];rem=cyc[1:]
 sub=([ -x for x in rem[::-1] ] if a>0 else rem)
 sub=freereduce(sub)
 neighbors=rev[g].copy()
 for j in neighbors:
  v=R[j]
  for h in set(abs(x) for x in v):rev[h].discard(j)
  if j==k:
   R.pop(j,None);continue
  out=[]
  for x in v:
   if abs(x)==g:out+=sub if x>0 else [-y for y in sub[::-1]]
   else:out.append(x)
  out=freereduce(out)
  if out:R[j]=out
  else:R.pop(j,None)
  for h in set(abs(x) for x in out):rev[h].add(j)
 active.remove(g)
 iters+=1
 if iters%250==0:print('iter',iters,'active',len(active),'relators',len(R),'maxlen',max(map(len,R.values()),default=0),'elapsed',round(time.time()-start,1),flush=True)
 if time.time()-start>100:raise TimeoutError("Tietze reduction exceeded allotted verification time")
print('final','iters',iters,'gens',len(active),'rel',len(R),'time',time.time()-start,flush=True)
print('gens',sorted(active)[:100],flush=True)
print('relators sample',list(R.items())[:20],flush=True)


assert iters==1140 and len(active)==1 and len(R)==46
remaining=next(iter(active))
assert all(len(w)==14 and all(abs(x)==remaining for x in w) and abs(sum(1 if x>0 else -1 for x in w))==14 for w in R.values())
print('FUNDAMENTAL_GROUP_TIETZE_OK: pi1=C14; 1140 eliminations; 46 relators of degree +/-14',flush=True)
print('ALL_HOM_C7_K4_QUOTIENT_CHECKS_OK',flush=True)
