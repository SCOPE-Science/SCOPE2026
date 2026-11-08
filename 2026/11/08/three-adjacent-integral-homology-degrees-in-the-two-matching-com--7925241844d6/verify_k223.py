import sys
from itertools import combinations
from collections import defaultdict, Counter,deque
from functools import lru_cache
def unit_reduce(A):
    A=[row[:] for row in A]
    units=0
    while A and A[0]:
        found=next(((i,j) for i,row in enumerate(A) for j,v in enumerate(row) if abs(v)==1),None)
        if found is None:
            assert not any(any(row) for row in A), 'nonunit residual matrix'
            return units
        i,j=found
        A[0],A[i]=A[i],A[0]
        for row in A:row[0],row[j]=row[j],row[0]
        p=A[0][0]
        A=[[A[r][c]-A[r][0]*A[0][c]*p for c in range(1,len(A[0]))] for r in range(1,len(A))]
        units+=1
    return units
parts=[(0,1),(2,3),(4,5,6)]
edges=[(u,v) for a in range(3) for b in range(a+1,3) for u in parts[a] for v in parts[b]]
assert len(edges)==16
REVERSE = len(sys.argv) > 1 and sys.argv[1] == 'reverse'
assert len(sys.argv) == 1 or (len(sys.argv) == 2 and REVERSE)
if REVERSE: edges.reverse()
f=set()
for m in range(1<<16):
 deg=[0]*7
 for i,(a,b) in enumerate(edges):
  if m>>i&1:deg[a]+=1;deg[b]+=1
 if max(deg)<3:f.add(m)
assert Counter(m.bit_count() for m in f) == {0:1,1:16,2:120,3:508,4:1213,5:1476,6:714,7:60}
# Independently enumerate forbidden three-edge stars; this is logically equivalent
# to degree <=2 but uses a different face predicate.
forbidden=[]
for v in range(7):
    incident=[i for i,(a,b) in enumerate(edges) if v in (a,b)]
    for t in combinations(incident,3): forbidden.append(sum(1<<i for i in t))
for m in range(1<<16):
    assert (m in f)==all(m&t != t for t in forbidden)
print('F',len(f),sorted(Counter(m.bit_count() for m in f).items()),flush=True)
unmatched=set(f);lowup={};up=set()
for i in range(16):
 bit=1<<i
 p=[(m,m|bit) for m in sorted(unmatched) if not m&bit and (m|bit) in unmatched]
 for a,b in p:unmatched.remove(a);unmatched.remove(b);lowup[a]=b;up.add(b)
print('M',len(lowup),'crit',Counter(m.bit_count()-1 for m in unmatched),flush=True)
assert len(lowup)==(2026 if REVERSE else 2018)
assert Counter(m.bit_count()-1 for m in unmatched)==({3:2,4:34,5:20} if REVERSE else {3:9,4:42,5:21})
# orientation boundary coefficient of an element with bit i in ordered simplex
@lru_cache(None)
def boundary(m):
 return [(m^(1<<i),(-1)**((m&((1<<i)-1)).bit_count())) for i in range(16) if m>>i&1]
# Verify reversed matched Hasse DAG, use all nonempty faces to match standard unaugmented complex
nodes=sorted(f-{0});deg={m:0 for m in nodes};out=defaultdict(list);incs=0
for x in nodes:
 for a,sign in boundary(x):
  if a==0:continue
  incs+=1
  # usual incidence down: x->a. Matched incidence upwards a->x
  if lowup.get(a)==x:u,v=a,x
  else:u,v=x,a
  out[u].append(v);deg[v]+=1
Q=deque([x for x in nodes if deg[x]==0]);vis=0
while Q:
 x=Q.popleft();vis+=1
 for y in out[x]:
  deg[y]-=1
  if deg[y]==0:Q.append(y)
print('DAG',vis,len(nodes),'incs',incs,flush=True)
assert vis==len(nodes)==4107 and incs==18700
critical={d:sorted(m for m in unmatched if m.bit_count()-1==d) for d in range(7)}
# To compute Morse boundary from k crit to k-1 crit, recursive projection of (k-1)-simplices.
# The pair where a is LOWER (a,b) gives relationship p(a)=-sum_{c != a}[b:c]p(c)/[b:a]
# where b a k simplex. The pair where x is an UPPER of pair of dimensions(k-2,k-1) gives zero.
for k in [4,5,6]:
 dest=critical[k-1];src=critical[k]
 ix={m:i for i,m in enumerate(dest)}
 @lru_cache(None)
 def proj(x):
  if x in unmatched: return {ix[x]:1} if x in ix else {}
  if x in up: return {}
  b=lowup[x]
  q=dict(boundary(b)); pivot=q.pop(x)
  acc=defaultdict(int)
  for c,v in q.items():
   for z,w in proj(c).items():acc[z]-=v*w*pivot
  return {z:w for z,w in acc.items() if w}
 vals=[]
 for s in src:
  v=defaultdict(int)
  for c,z in boundary(s):
   for a,w in proj(c).items():v[a]+=z*w
  vals.append([v[i] for i in range(len(dest))])
 mat=[[vals[b][a] for b in range(len(src))] for a in range(len(dest))];rank=unit_reduce(mat)
 print('MORSE',k,'shape',(len(dest),len(src)),'rank',rank,'nz',sum(int(v!=0) for row in mat for v in row),'maxabs',max([abs(v) for row in mat for v in row] or [0]),flush=True)
 print('SNF',k,Counter({1:rank}),flush=True)
 if k==4: assert rank==(1 if REVERSE else 8)
 if k==5: assert rank==(14 if REVERSE else 15)
 if k==6: assert rank==0
 if k==4: M4=mat
 elif k==5: M5=mat
assert all(sum(M4[i][j]*M5[j][k] for j in range(len(M5)))==0 for i in range(len(M4)) for k in range(len(M5[0])))
# Independently build all simplicial boundaries over F_2 and row-reduce.
bydim={d:sorted(m for m in f if m.bit_count()==d+1) for d in range(7)}
expected=[15,105,403,809,648,60]
for d in range(1,7):
    ix={m:i for i,m in enumerate(bydim[d-1])}
    pivots={}
    for m in bydim[d]:
        bits=0
        for a,z in boundary(m):bits^=1<<ix[a]
        while bits:
            j=bits.bit_length()-1
            if j in pivots:bits^=pivots[j]
            else:pivots[j]=bits;break
    assert len(pivots)==expected[d-1]
print('INDEPENDENT_MOD2_RANKS',expected,flush=True)
print('CHECKED_MORSE',flush=True)
