#!/usr/bin/env python3
"""Self-contained exact combinatorial verification of a five-by-five torus-grid symmetry result."""
from collections import Counter,deque
N=5
points=[(2*(x+y)%N,2*(x-y)%N) for x in range(N) for y in range(N)]
point_index={pt:i for i,pt in enumerate(points)}
def circ(a,b):
 d=(a-b)%N
 return min(d,N-d)
def distance(i,j):
 (x,y),(u,v)=points[i],points[j]
 return circ(x,u)+circ(y,v)
def is_simplex(bitset):
 vs=[i for i in range(25) if (bitset>>i)&1]
 return all(distance(i,j)<=3 for ai,i in enumerate(vs) for j in vs[ai+1:])
# Every simplex, independently from the distance criterion and 25 vertex recurrence.
faces={0}
for i in range(25):
 faces|={f|(1<<i) for f in faces if all(distance(i,j)<=3 for j in range(i) if (f>>j)&1)}
assert len(faces)==25531
assert all(is_simplex(f) for f in faces)
face_vector=tuple(Counter(f.bit_count() for f in faces)[k] for k in range(11))
assert face_vector==(1,25,250,1300,3850,6745,7100,4450,1550,250,10)
print('FACE_VECTOR',face_vector)
# Finite acyclic partial matching on all nonempty faces, left-to-right vertex pivots.
remaining=faces-{0}; matched={}; matched_pairs=0
for i in range(25):
 bit=1<<i
 lower=[f for f in remaining if not(f&bit) and (f|bit) in remaining]
 for f in lower:
  g=f|bit
  assert f not in matched and g not in matched
  matched[f]=g; matched[g]=f
 remaining.difference_update(lower)
 remaining.difference_update(f|bit for f in lower)
 matched_pairs+=len(lower)
critical=Counter(f.bit_count()-1 for f in remaining)
assert critical=={0:1,4:9},critical
assert 2*matched_pairs+sum(critical.values())==len(faces)-1
# Entire reversed Hasse diagram must be acyclic.
adj={f:[] for f in faces if f}
indeg={f:0 for f in adj}
for upper in adj:
 tmp=upper
 while tmp:
  bit=tmp&-tmp;tmp^=bit
  lower=upper^bit
  if not lower:continue
  if matched.get(lower)==upper:
   src,dst=lower,upper
  else:
   src,dst=upper,lower
  adj[src].append(dst);indeg[dst]+=1
queue=deque(f for f,d in indeg.items() if not d)
count=0
while queue:
 f=queue.popleft();count+=1
 for g in adj[f]:
  indeg[g]-=1
  if not indeg[g]:queue.append(g)
assert count==len(adj),('directed-cycle',count,len(adj))
print('MORSE_CERTIFICATE',matched_pairs,'matched pairs',dict(critical),'critical cells','DAG nodes',count)
# Cyclic order-five subgroups: choose slope infinity and slopes 0,1,2,3,4.
subgroups=[(0,1)]+[(1,s) for s in range(5)]
def translate(i,a,b):
 x,y=points[i]
 return point_index[((x+a)%5,(y+b)%5)]
def orbit_partition(a,b):
 unseen=set(range(25));orbits=[]
 while unseen:
  i=min(unseen)
  orbit=tuple(sorted({translate(i,k*a,k*b) for k in range(5)}))
  assert len(orbit)==5
  unseen.difference_update(orbit)
  orbits.append(orbit)
 assert len(orbits)==5
 return orbits

def quotient_faces(a,b):
 orbit=orbit_partition(a,b)
 full=[sum(1<<i for i in O) for O in orbit]
 simplices=[]
 for s in range(1<<5):
  union=0
  for j in range(5):
   if (s>>j)&1:union|=full[j]
  if is_simplex(union):simplices.append(s)
 assert 0 in simplices
 return simplices

def quotient_signature(simplices):
 return tuple(Counter(s.bit_count() for s in simplices)[k] for k in range(6))

# Translate each nonempty simplex under all twenty-five translations, compute signed
# chain traces. Signed reduced Lefschetz is the rational H4 trace (published rank 9).
def chain_trace(a,b):
 total=-1 # reduced empty simplex
 for f in faces:
  if not f:continue
  original=[i for i in range(25) if f>>i&1]
  mapped=[translate(i,a,b) for i in original]
  if sum(1<<j for j in mapped)!=f:continue
  inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
  total+=(-1 if len(original)%2==0 else 1)*(-1 if inversions%2 else 1)
 return total

for a,b in subgroups:
 fs=quotient_faces(a,b)
 sig=quotient_signature(fs)
 # slope ±1 has no fixed points; slope 0, infinity is 5-gon;
 # slope 2,3 consists of 5 distinct points.
 target=(1,5,5,0,0,0) if a==0 or b==0 else ((1,0,0,0,0,0) if b in (a,(-a)%5) else (1,5,0,0,0,0))
 assert sig==target,(a,b,sig,target)
 euler=sum((-1)**(k-1)*sig[k] for k in range(1,6))
 predicted=euler-1
 assert chain_trace(a,b)==predicted
 print('SUBGROUP',a,b,'fixed_quotient_fvector',sig,'trace_H4',predicted)

for a in range(5):
 for b in range(5):
  actual=chain_trace(a,b)
  predicted=9 if (a,b)==(0,0) else (4 if a and b in ((2*a)%5,(3*a)%5) else -1)
  assert actual==predicted,(a,b,actual,predicted)
print('ALL_25_GROUP_CHARACTERS_CONFIRMED')
print('INTEGRAL_MORSE_AND_FIXED_POINT_CHECKS_OK')
