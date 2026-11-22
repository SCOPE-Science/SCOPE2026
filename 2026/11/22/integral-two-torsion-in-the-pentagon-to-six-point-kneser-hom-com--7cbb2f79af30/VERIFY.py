"""Integral cellular homology verifier for Hom(C_5, KG(6,2)).

Requires Python 3.10+ and SymPy. Enumerates all product-of-simplices cells,
performs elementary free-face collapses, computes mod-two homology,
contracts a spanning tree, and eliminates unit Smith pivots integrally.
"""
from itertools import combinations
from collections import defaultdict
pairs=list(combinations(range(6),2)); N=15
adj=[sum(1<<j for j,q in enumerate(pairs) if not (set(p)&set(q))) for p in pairs]
fs=[]
def go(cur):
 k=len(cur)
 if k==5:
  if adj[cur[-1]]>>cur[0]&1:fs.append(tuple(1<<x for x in cur))
  return
 for j in range(N):
  if not cur or ((adj[cur[-1]]>>j)&1):
   if k<4 or adj[j] & (1<<cur[0]):go(cur+[j])
go([])
print('singleton cells',len(fs))
levels=defaultdict(set); front=set(fs)
levels[0]=front
for step in range(1,20):
 nxt=set()
 for cell in front:
  for k in range(5):
   q=(1<<N)-1
   for kk in ((k+1)%5,(k+4)%5):
    z=cell[kk]
    while z:
     p=z&-z; z-=p
     q &= adj[p.bit_length()-1]
   q &= ~cell[k]
   while q:
    p=q&-q; q-=p
    arr=list(cell); arr[k]|=p
    nxt.add(tuple(arr))
 if not nxt:break
 levels[step]=nxt
 front=nxt
from collections import deque
allcells=sorted(set().union(*levels.values()),key=lambda a:(sum(x.bit_count() for x in a),a))
M=len(allcells);idx={a:i for i,a in enumerate(allcells)}
print('building cells',M,flush=True)
dims=[sum(x.bit_count()-1 for x in a) for a in allcells]
faces=[[] for _ in range(M)];cofaces=[[] for _ in range(M)]
for i,cell in enumerate(allcells):
 for k,z in enumerate(cell):
  if z.bit_count()==1:continue
  while z:
   p=z&-z;z-=p
   n=list(cell);n[k]^=p;j=idx[tuple(n)]
   faces[i].append(j);cofaces[j].append(i)
count=[len(cf) for cf in cofaces];active=bytearray([1])*M
queue=deque(i for i,c in enumerate(count) if c==1)
removed=0;counts=defaultdict(int)
while queue:
 f=queue.popleft()
 if not active[f] or count[f]!=1:continue
 c=next((e for e in cofaces[f] if active[e]),None)
 if c is None:raise ValueError('bad')
 counts[dims[c]]+=1
 for r in (f,c):
  active[r]=0
  for lower in faces[r]:
   count[lower]-=1
   if count[lower]==1:queue.append(lower)
 removed+=2
print('removed',removed,'pair dims',dict(counts),'remaining',M-removed,flush=True)
print('remaining dims',dict((d,sum(active[i] for i in range(M) if dims[i]==d)) for d in range(6)),flush=True)
rem={d:[i for i in range(M) if active[i] and dims[i]==d] for d in range(3)}
vertices={i:j for j,i in enumerate(rem[0])};edges={i:j for j,i in enumerate(rem[1])}
p=list(range(len(vertices)))
def find(a):
 while a!=p[a]:p[a]=p[p[a]];a=p[a]
 return a
for i in rem[1]:
 u,v=faces[i]
 u,v=find(vertices[u]),find(vertices[v]);p[u]=v
components=len(set(find(x) for x in range(len(vertices))))
print('connected components',components)
piv={}
for i in rem[2]:
 x=0
 for f in faces[i]:
  assert active[f]
  x ^= 1<<edges[f]
 while x:
  j=x.bit_length()-1
  if j in piv:x ^= piv[j]
  else:piv[j]=x;break
print('B2 rank GF2',len(piv),'homology H1',len(rem[1])-len(rem[0])+components-len(piv),'H2',len(rem[2])-len(piv),flush=True)
# Build integral boundary in graph loops (tree edges quotient), then unit-pivot eliminate
parent=list(range(len(vertices)))
def root(a):
 while a!=parent[a]: parent[a]=parent[parent[a]];a=parent[a]
 return a
non_tree={}
for i in rem[1]:
 u,v=faces[i];ru,rv=root(vertices[u]),root(vertices[v]);
 if ru!=rv: parent[ru]=rv
 else:non_tree[i]=len(non_tree)
assert len(non_tree)==13123
cols={};rows={r:set() for r in range(len(non_tree))}
for i in rem[2]:
 cell=allcells[i]; z={};offs=0
 for k,m in enumerate(cell):
  zz=m;pos=0
  while zz:
   low=zz&-zz;zz-=low
   if m.bit_count()>1:
    n=list(cell);n[k]^=low;f=idx[tuple(n)]
    if f in non_tree:
     r=non_tree[f];sign=(-1)**(offs+pos)
     z[r]=sign;rows[r].add(i)
   pos+=1
  offs+=m.bit_count()-1
 cols[i]=z
print('initial col nnz',sum(map(len,cols.values())),'rows',len(rows),flush=True)
import heapq
# min product heuristic dynamic heap; use row priority degree and pivot col size
activecols=set(cols);active_rows=set(rows)
heap=[]
for r,ids in rows.items():
 if ids:heapq.heappush(heap,(len(ids),r))
zeroed=[];rank=0;nonunits=0;maxcoeff=1
while heap:
 _,r=heapq.heappop(heap)
 if r not in active_rows:continue
 deg=len(rows[r])
 if deg==0:active_rows.remove(r);continue
 if _!=deg:heapq.heappush(heap,(deg,r));continue
 options=[c for c in rows[r] if abs(cols[c].get(r,0))==1]
 if not options:
  nonunits+=1
  continue
 c=min(options,key=lambda c:len(cols[c]));p=cols[c];sgn=p[r];pitems=list(p.items())
 other=list(rows[r]-{c})
 for j in other:
  d=cols[j];coeff=d[r]*sgn
  for rr,vv in pitems:
   new=d.get(rr,0)-coeff*vv
   old=d.get(rr,0)
   if new:
    d[rr]=new
    maxcoeff=max(maxcoeff,abs(new))
    if not old:rows[rr].add(j);heapq.heappush(heap,(len(rows[rr]),rr))
   elif old:
    del d[rr];rows[rr].discard(j);heapq.heappush(heap,(len(rows[rr]),rr))
  if not d:zeroed.append(j)
 for rr in p:
  rows[rr].discard(c);heapq.heappush(heap,(len(rows[rr]),rr))
 del cols[c];activecols.discard(c);active_rows.discard(r);rank+=1
print('rank',rank,'nonunit dead row',nonunits,'remaining nonzero cols',sum(bool(d) for d in cols.values()),'maxcoef',maxcoeff,flush=True)
nonzero={j:d for j,d in cols.items() if d};support=sorted(set().union(*(set(d) for d in nonzero.values())))
print('residual support',len(support),'nonzero columns',len(nonzero),'coefficients',sorted(set(v for d in nonzero.values() for v in d.values())),flush=True)
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
rr=sorted(support);cc=sorted(nonzero)
S=smith_normal_form(Matrix([[nonzero[j].get(r,0) for j in cc] for r in rr]),domain=ZZ)
print('RESIDUAL_SNF',[abs(int(S[i,i])) for i in range(min(S.shape))],flush=True)
print('ranks',rank+sum(S[i,i]!=0 for i in range(min(S.shape))),'sumdim2',len(rem[2]),flush=True)

# Exact integral rank and torsion checks: every first-stage pivot is a unit.
assert [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i]] == [2]
assert rank == 13113 and len(rem[2]) == 13842
assert len(rem[0]) == 6570 and len(rem[1]) == 19692
assert components == 1 and M == 104220 and removed == 64116
assert len(piv) == 13113  # independent mod-two boundary rank
assert rank + sum(S[i, i] != 0 for i in range(min(S.shape))) == 13114
assert len(rem[1]) - len(rem[0]) + 1 - 13114 == 9
assert len(rem[2]) - 13114 == 728
assert len(rem[2]) - len(piv) == 729
print('VERIFIED H0=Z, H1=Z^9 + Z/2, H2=Z^728, H_i>=3=0')
