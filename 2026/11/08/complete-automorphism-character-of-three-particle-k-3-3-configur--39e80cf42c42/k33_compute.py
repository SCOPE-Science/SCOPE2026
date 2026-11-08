import itertools, math, time, collections
from functools import lru_cache
V=tuple(range(6)); E=tuple((i,3+j) for i in range(3) for j in range(3)); neigh=[[] for _ in V]
for e,(a,b) in enumerate(E):neigh[a].append(e);neigh[b].append(e)
H=[tuple((e,neigh[v][0]) for e in neigh[v][1:]) for v in V]

def mults(m,q):
    if not q:yield (0,)*m;return
    for a in itertools.combinations_with_replacement(range(m),q):
        count=[0]*m
        for x in a:count[x]+=1
        yield tuple(count)

def gen(k=3):
 out=[]
 for d in range(k+1):
  rows=[]
  for verts in itertools.combinations(V,d):
   for choices in itertools.product(range(2),repeat=d):
    for exp in mults(len(E),k-d):rows.append((tuple(zip(verts,choices)),exp))
  out.append(rows)
 return out

def boundaries(degs):
 matrices=[]
 for d in range(1,len(degs)):
  target={b:i for i,b in enumerate(degs[d-1])}
  cols=[]
  for hs,ex in degs[d]:
   col={}
   for i,(v,ch) in enumerate(hs):
    sign=(-1)**i
    nh=hs[:i]+hs[i+1:]
    e,base=H[v][ch]
    for ee,s in ((e,sign),(base,-sign)):
     nx=list(ex);nx[ee]+=1
     r=target[(nh,tuple(nx))]
     col[r]=col.get(r,0)+s
   cols.append({r:c for r,c in col.items() if c})
  matrices.append(cols)
 return matrices

def modrank(cols,p=101):
 pivot={}
 for col in cols:
  a={i:v%p for i,v in col.items() if v%p}
  while a:
   r=min(a)
   if r not in pivot:
    inv=pow(a[r],-1,p);pivot[r]={k:(v*inv)%p for k,v in a.items()};break
   v=a[r]
   for k,c in pivot[r].items():
    t=(a.get(k,0)-v*c)%p
    if t:a[k]=t
    else:a.pop(k,None)
 return len(pivot)

def integer_unit_reduce(cols,nrows):
 # elementary integer row/column operations with unit entries, using sparse active matrix
 t=time.monotonic(); cols=[dict(c) for c in cols]; active_col=set(range(len(cols)))
 row_to_col=[set() for _ in range(nrows)]
 for j,c in enumerate(cols):
  for r in c:row_to_col[r].add(j)
 piv=[]
 while True:
  # choose cheap unit pivot for row/column
  best=None;cost=10**30
  for j in active_col:
   c=cols[j]
   for r,x in c.items():
    if abs(x)!=1:continue
    cst=(len(c)-1)*(len(row_to_col[r])-1)
    if cst<cost:best=(j,r,x);cost=cst
   if cost==0:break
  if best is None:break
  j,r,v=best
  piv.append((j,r))
  # row elimination: other cols with r, remove row using pivot col
  for jj in tuple(row_to_col[r]):
   if jj==j:continue
   x=cols[jj].get(r,0)
   for rr,z in cols[j].items():
    y=cols[jj].get(rr,0)-x*v*z
    if y:cols[jj][rr]=y;row_to_col[rr].add(jj)
    else:cols[jj].pop(rr,None);row_to_col[rr].discard(jj)
  for rr in tuple(cols[j]):row_to_col[rr].discard(j)
  cols[j]={};active_col.remove(j)
  if len(piv)%100==0:print('pivot',len(piv),'cost',cost,flush=True)
 residual=[c for j,c in enumerate(cols) if j in active_col and c]
 print('unit p',len(piv),'residual_col',len(residual),'residual_entries',sum(map(len,residual)),'maxentry',max((abs(x) for c in residual for x in c.values()),default=0))
 return len(piv),residual

def assert_square_zero(A,B):
 for col in B:
  acc=collections.defaultdict(int)
  for idx,c in col.items():
   for r,w in A[idx].items():acc[r]+=c*w
  assert not any(acc.values()),'nonzero boundary composition'

if __name__=='__main__':
 degrees=gen();print('dims',[len(x) for x in degrees],flush=True)
 ds=boundaries(degrees)
 assert_square_zero(ds[0],ds[1]);assert_square_zero(ds[1],ds[2])
 print('integral boundary compositions zero',flush=True)
 for i,cols in enumerate(ds,1):
  print('boundary',i,'ncols',len(cols),'nnz',sum(len(c) for c in cols),'ranks mod',[modrank(cols,p) for p in [2,3,101]],flush=True)
  p,res=integer_unit_reduce(cols,len(degrees[i-1]));print('residue',[sorted(c.items())[:8] for c in res[:3]],flush=True)
  if i in (1,3):assert not res and p=={1:164,3:160}[i]
  if i==2:
   assert p==371 and res and max(abs(x) for c in res for x in c.values())==2
   assert all(x%2==0 for c in res for x in c.values())
   assert modrank(res,3)==1 and modrank(res,101)==1
 print('K33_INTEGRAL_SMITH_PASS: d1=1^164, d2=1^371+2, d3=1^160; H1=Z4+Z2, H2=Z8',flush=True)
