"""Exact finite discrete-Morse certificate for the perfect-matching complex of a 12-vertex quartic graph."""
from itertools import combinations
from collections import Counter, defaultdict, deque

EDGES=[(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
ORDER=[15,17,5,10,19,13,1,11,8,3,7,6,23,2,14,0,16,18,12,20,9,4,21,22]
ALL=(1<<len(EDGES))-1
V={tuple(sorted(e)) for e in EDGES}
assert len(V)==24 and sorted(sum((x==v or y==v) for x,y in V) for v in range(12))==[4]*12
P=[]
for comb in combinations(range(24),6):
 verts=[v for j in comb for v in EDGES[j]]
 if len(set(verts))==12:
  P.append(comb)
assert len(P)==52
faces={0}
for m in P:
 for d in range(1,7):
  for inds in combinations(m,d):
   faces.add(sum(1<<x for x in inds))
assert len(faces)==1880
assert Counter(f.bit_count() for f in faces)=={0:1,1:24,2:204,3:612,4:675,5:312,6:52}
nonempty=faces-{0}
remaining=nonempty.copy()
pairs=[]
for j in ORDER:
 bit=1<<j
 for face in sorted(remaining):
  upper=face|bit
  if (face&bit)==0 and upper in remaining:
   remaining.remove(face)
   remaining.remove(upper)
   pairs.append((face,upper))
assert len(pairs)==930 and len(remaining)==19
crit=Counter(f.bit_count()-1 for f in remaining)
assert crit=={0:1,2:17,3:1}
print('MORSE_PAIRS',len(pairs),'CRITICAL',dict(sorted(crit.items())))

# Full directed graph for acyclicity: down each unmatched incidence, up each matched incidence.
matched=set(pairs)
indeg={f:0 for f in nonempty}
adj={f:[] for f in nonempty}
for u in nonempty:
 for j in range(24):
  if not u&(1<<j):continue
  lo=u^(1<<j)
  if lo==0:continue # empty face is not a cell
  if (lo,u) in matched:tail,head=lo,u
  else:tail,head=u,lo
  adj[tail].append(head)
  indeg[head]+=1
queue=deque(f for f in nonempty if not indeg[f]); visited=0
while queue:
 f=queue.popleft(); visited+=1
 for g in adj[f]:
  indeg[g]-=1
  if indeg[g]==0:queue.append(g)
assert visited==len(nonempty),(visited,len(nonempty))
print('DIRECTED_HASSE_ACYCLIC',visited,'vertices',sum(map(len,adj.values())),'arrows')

low2={lo:hi for lo,hi in pairs if lo.bit_count()==3}
high2={hi for lo,hi in pairs if hi.bit_count()==3}
critical2={f for f in remaining if f.bit_count()==3}
critical3=[f for f in remaining if f.bit_count()==4]
assert len(critical3)==1

def boundary(face):
 inds=[j for j in range(24) if (face>>j)&1]
 return [(face^(1<<j), (-1)**k) for k,j in enumerate(inds)]

# Forman gradient-path summation. For a 2-face paired upward with a 3-face, eliminate
# its coefficient through that 3-face. The eliminated two-face expands into a finite
# Z-linear combination of two-faces. Acyclicity guarantees recursion termination.
from functools import lru_cache
@lru_cache(None)
def project2(f):
 if f in critical2:return {f:1}
 if f in high2:return {}
 if f not in low2:raise AssertionError('unclassified 2-simplex')
 upper=low2[f]
 inc=dict(boundary(upper))[f]
 out=defaultdict(int)
 for g,sgn in boundary(upper):
  if g==f:continue
  for critical,coeff in project2(g).items():
   out[critical]-=inc*sgn*coeff
 return {k:v for k,v in out.items() if v}
res=defaultdict(int)
for face,coeff in boundary(critical3[0]):
 for target,k in project2(face).items():res[target]+=coeff*k
res={k:v for k,v in res.items() if v}
assert not res, res
print('INTEGRAL_MORSE_BOUNDARY_3_TO_2_ZERO',len(critical2),'critical 2-cells',len(critical3),'critical 3-cell')
print('CHVATAL_PERFECT_MATCHING_MIXED_WEDGE_PASS')

# Independent simplicial boundary ranks over F_2 (not used in the integral Morse argument).
by_size={k:sorted(f for f in nonempty if f.bit_count()==k) for k in range(1,7)}
rank=[]
for k in range(2,7):
 idx={face:i for i,face in enumerate(by_size[k-1])}
 pivots={}
 for face in by_size[k]:
  col=0
  for g,_ in boundary(face):col^=(1<<idx[g])
  while col:
   p=col.bit_length()-1
   if p in pivots:col^=pivots[p]
   else:pivots[p]=col;break
 rank.append(len(pivots))
assert rank==[23,181,414,260,52],rank
print('INDEPENDENT_MOD_TWO_BOUNDARY_RANKS',rank)
print('INDEPENDENT_MOD_TWO_BETTI',17,1)
