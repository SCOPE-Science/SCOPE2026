from itertools import product
from collections import defaultdict
N=12; weights=(1,3,5)
# 0 denotes no simplex in a circle; 1..N denotes vertex, N+1..2N denotes oriented edge i -> i+1
def localdim(x):return -1 if x==0 else (0 if x<=N else 1)
def dim(cell):return sum(localdim(x)+1 for x in cell)-1
def act(cell,j):
 return tuple(0 if x==0 else (1+((x-1+j*w)%N) if x<=N else N+1+((x-N-1+j*w)%N)) for w,x in zip(weights,cell))
def rep(cell):return min(act(cell,j) for j in range(N))
allcells = defaultdict(set)
for cell in product(range(2*N+1),repeat=len(weights)):
 if cell==(0,)*len(weights):continue
 allcells[dim(cell)].add(rep(cell))
for d in sorted(allcells):print('cells',d,len(allcells[d]),flush=True)
bases={d:sorted(v) for d,v in allcells.items()}
index={d:{x:i for i,x in enumerate(bases[d])} for d in bases}
def boundary(cell):
 pref=0
 for j,x in enumerate(cell):
  if x==0:continue
  if x<=N:
   new=cell[:j]+(0,)+cell[j+1:]
   if new !=(0,)*len(weights):yield new,(-1)**pref
  else:
   tail=(x-N-1)%N
   head=(tail+1)%N
   for v,sgn in ((head,1),(tail,-1)):
    new=cell[:j]+(v+1,)+cell[j+1:]
    yield new,(-1)**pref*sgn
  pref+=localdim(x)+1
mats={}
for d in range(1,6):
 cols=[]
 for cell in bases[d]:
  accum=defaultdict(int)
  for face,sgn in boundary(cell):accum[index[d-1][rep(face)]]+=sgn
  cols.append({i:v for i,v in accum.items() if v})
 mats[d]=cols
 print('boundary',d,'shape',(len(bases[d-1]),len(cols)),'nonzeros',sum(len(c) for c in cols),flush=True)
 # d^2 verification
 if d>=2:
  for col in cols:
   twice=defaultdict(int)
   for i,v in col.items():
    for j,w in mats[d-1][i].items():twice[j]+=v*w
   assert all(x==0 for x in twice.values()),(d,twice)

def modrank(cols,p):
 pivots={}
 for col in cols:
  v={i:(x%p) for i,x in col.items() if x%p}
  while v:
   pivot=min(v)
   if pivot not in pivots:
    a=v[pivot];inv=pow(a,-1,p)
    pivots[pivot]={i:(x*inv)%p for i,x in v.items()};break
   a=v[pivot];basis=pivots[pivot]
   for i,w in basis.items():
    value=(v.get(i,0)-a*w)%p
    if value: v[i]=value
    elif i in v: del v[i]
 return len(pivots)
for prime in (2,3,5,7):
 ranks={d:modrank(cols,prime) for d,cols in mats.items()}
 betti={d:len(bases[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
 print('prime',prime,'ranks',ranks,'betti',betti,flush=True)
assert sum(((-1)**d)*len(bases[d]) for d in bases)==0
print('COXETER_B6_ORBIT_MODULAR_CHECK_OK')
