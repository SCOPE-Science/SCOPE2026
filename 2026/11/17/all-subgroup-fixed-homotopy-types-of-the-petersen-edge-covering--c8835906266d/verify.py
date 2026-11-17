"""Exact finite certificate for the geometric subgroup-fixed homotopy of M_2(KG(5,2)).
Run with Python 3 (standard library only): python verify.py
The face convention includes the empty face for reduced discrete Morse theory.
"""
import itertools
from collections import Counter

V=list(itertools.combinations(range(5),2))
E=[(i,j) for i in range(10) for j in range(i+1,10) if set(V[i]).isdisjoint(V[j])]
assert len(E)==15
stars=[sum(1<<i for i,e in enumerate(E) if v in e) for v in range(10)]
assert sorted(s.bit_count() for s in stars)==[3]*10
ps=list(itertools.permutations(range(5)))
pos={p:i for i,p in enumerate(ps)}
identity=pos[tuple(range(5))]
mult=[[pos[tuple(a[b[i]] for i in range(5))] for b in ps] for a in ps]
inv=[pos[tuple(p.index(i) for i in range(5))] for p in ps]
vertexindex={v:i for i,v in enumerate(V)}
edgeindex={e:i for i,e in enumerate(E)}
perms=[]
for p in ps:
 q=[vertexindex[tuple(sorted((p[a],p[b])))] for a,b in V]
 perms.append([edgeindex[tuple(sorted((q[a],q[b])))] for a,b in E])

def closure(gens):
 steps=list(set(gens+[inv[x] for x in gens]))
 seen={identity};queue=[identity]
 for a in queue:
  for b in steps:
   c=mult[a][b]
   if c not in seen:
    seen.add(c);queue.append(c)
 return frozenset(seen)

subgroups={frozenset([identity]):()}
queue=list(subgroups)
for H in queue:
 for g in range(120):
  if g not in H:
   J=closure(list(subgroups[H])+[g])
   if J not in subgroups:
    subgroups[J]=tuple(list(subgroups[H])+[g]);queue.append(J)
assert len(subgroups)==156

def conjugate(H,g):
 return frozenset(mult[mult[g][h]][inv[g]] for h in H)

remaining=set(subgroups)
reps=[]
while remaining:
 H=min(remaining,key=lambda h:(len(h),tuple(sorted(h))))
 orbit={conjugate(H,g) for g in range(120)}
 assert orbit<=remaining
 reps.append((H,len(orbit)))
 remaining-=orbit
assert len(reps)==19 and sum(m for _,m in reps)==156

# Fixed orbit-complex vertices are the edge orbits, with an orbit vertex
# present iff its union is an allowed degree-at-most-two edge set.
def fixedfaces(H):
 seen=set();orbs=[]
 for e in range(15):
  if e not in seen:
   o={perms[g][e] for g in H}
   assert all(perms[g][x] in o for x in o for g in H)
   seen.update(o);orbs.append(sum(1<<x for x in o))
 assert len(seen)==15
 faces=[]
 for m in range(1<<len(orbs)):
  union=0
  for j,o in enumerate(orbs):
   if m>>j&1:union|=o
  if all((union&st)!=st for st in stars):faces.append(m)
 assert 0 in faces and all(m^(1<<j) in faces for m in faces for j in range(len(orbs)) if m>>j&1)
 return orbs,faces

# Lexicographically chosen representatives are deterministic; these are
# explicit (0-based) orbit-toggle orders, not stochastic searches.
orders={2:[1,5,7,6,3,4,8,2,0],4:[5,3,0,2,1,4],5:[1,5,3,0,4,2],6:[0,4,1,2,3],11:[2,3,0,1]}
expected={0:(8,4),1:(4,2),2:None,3:(2,1),4:None,5:None,6:None,7:(1,1),8:(1,1),9:(1,1),10:(2,1),11:None,12:(1,1),13:(1,1),14:None,15:(1,1),16:None,17:(0,1),18:(0,1)}
categories=Counter()

for i,(H,conjugate_count) in enumerate(reps):
 orbs,faces=fixedfaces(H)
 n=len(orbs)
 order=orders.get(i,list(range(n)))
 assert sorted(order)==list(range(n))
 remaining_faces=set(faces);pairs=[]
 for j in order:
  bit=1<<j
  for a in sorted(remaining_faces):
   b=a|bit
   if b!=a and b in remaining_faces:
    remaining_faces.remove(a);remaining_faces.remove(b);pairs.append((a,b))
 critical=Counter(s.bit_count() for s in remaining_faces)
 exp=expected[i]
 assert critical==(Counter({exp[0]:exp[1]}) if exp else Counter()),(i,critical)
 assert len(faces)==2*len(pairs)+len(remaining_faces)
 # Reverse every matched cover relation, and orient every other codimension-one
 # Hasse edge downward. Topologically sort the FULL directed Hasse diagram.
 matching=set(pairs)
 outgoing={f:[] for f in faces}
 indegree={f:0 for f in faces}
 for f in faces:
  for j in range(n):
   if f>>j&1:
    sub=f^(1<<j)
    source,dest=(sub,f) if (sub,f) in matching else (f,sub)
    outgoing[source].append(dest);indegree[dest]+=1
 zeros=[f for f,d in indegree.items() if d==0]
 visited=0
 for f in zeros:
  visited+=1
  for dest in outgoing[f]:
   indegree[dest]-=1
   if indegree[dest]==0:zeros.append(dest)
 assert visited==len(faces),(i,visited,len(faces))
 label='empty' if exp==(0,1) else 'point' if exp is None else 'S^0' if exp==(1,1) else 'S^1' if exp==(2,1) else 'S^3 wedge S^3' if exp==(4,2) else 'four S^7'
 categories[label]+=conjugate_count
 print('CLASS',i,'subgroup_order',len(H),'members',conjugate_count,'orbit_vertices',len(orbs),'faces',len(faces),'critical_face_cardinalities',dict(critical),'type',label)
assert categories==Counter({'point':75,'S^0':48,'S^1':20,'S^3 wedge S^3':10,'empty':2,'four S^7':1}),categories
print('TOTAL_SUBGROUPS',len(subgroups),'CONJUGACY_CLASSES',len(reps))
print('TOTAL_TYPES',dict(sorted(categories.items())))
print('PETERSEN_M2_FIXED_LOCI_ALL_SUBGROUPS_PASS')
