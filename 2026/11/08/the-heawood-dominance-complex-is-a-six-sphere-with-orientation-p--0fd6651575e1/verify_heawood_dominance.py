#!/usr/bin/env python3
"""Exact standard-library verification of the Heawood dominance-complex theorem."""
from collections import Counter, defaultdict, deque

P = tuple(range(1, 8))
LINES = tuple((a,b,a^b) for a in P for b in range(a+1, 8) if (a^b)>b)
assert len(LINES)==7 and all(len(x)==3 for x in LINES)
assert {tuple(sorted(x)) for x in LINES}=={tuple(sorted((a,b,a^b))) for a in P for b in range(a+1,8)}
N=14
NEI=[0]*N
for i,L in enumerate(LINES):
 for p in L:
  NEI[p-1]|=1<<(7+i)
  NEI[7+i]|=1<<(p-1)
assert all(x.bit_count()==3 for x in NEI)
assert sum(x.bit_count() for x in NEI)==42
CLOSED=tuple((1<<i)|NEI[i] for i in range(N))
FULL=(1<<N)-1
# Two independent descriptions of faces.
K={f for f in range(1<<N) if not any((f&c)==c for c in CLOSED)}
K2={f for f in range(1<<N) if all((FULL^f)&c for c in CLOSED)}
assert K==K2
EXPECTED_F=(1,14,91,364,987,1862,2394,1962,931,224,21)
assert tuple(sum(f.bit_count()==j for f in K) for j in range(11))==EXPECTED_F
assert len(K)==8851
assert all((f^(1<<i)) in K for f in K for i in range(N) if f>>i&1)

def verify_matching(order):
 remaining=set(K)
 pairs={}
 for v in order:
  for f in sorted(remaining):
   if f>>v&1: continue
   g=f|(1<<v)
   if g in remaining:
    pairs[f]=g
    remaining.remove(f)
    remaining.remove(g)
 assert len(pairs)==4425 and len(remaining)==1
 assert next(iter(remaining)).bit_count()==7
 assert 0 in pairs and pairs[0].bit_count()==1
 ordinary={f:g for f,g in pairs.items() if f}
 critical=remaining|{pairs[0]}
 assert len(ordinary)==4424
 assert Counter(f.bit_count()-1 for f in critical)=={0:1,6:1}
 indegree={f:0 for f in K if f}
 out=defaultdict(list);covers=0
 for h in indegree:
  for i in range(N):
   if not h>>i&1:continue
   lo=h^(1<<i)
   if not lo:continue
   s,t=(lo,h) if ordinary.get(lo)==h else (h,lo)
   out[s].append(t);indegree[t]+=1;covers+=1
 todo=deque(sorted(f for f in indegree if indegree[f]==0));seen=0
 while todo:
  f=todo.popleft();seen+=1
  for g in out[f]:
   indegree[g]-=1
   if indegree[g]==0: todo.append(g)
 assert seen==len(K)-1
 return len(ordinary),len(critical),covers,seen,tuple(sorted(remaining))

m1=verify_matching(tuple(range(N)))
m2=verify_matching(tuple(range(7,14))+tuple(range(7)))
assert m1[:4]==m2[:4]

# Full incidence automorphism group from all invertible linear maps of F_2^3,
# together with point-line interchange via the standard dot-product polarity.
def scalar(x,y):return (x&y).bit_count()%2
polar={p:next(j for j,L in enumerate(LINES) if all(scalar(p,x)==0 for x in L)) for p in P}
DUAL=tuple([7+polar[p] for p in P]+[next(p-1 for p in P if polar[p]==j) for j in range(7)])
assert sorted(DUAL)==list(range(N))

def automorphism_test(a):
 assert set(a)==set(range(N))
 assert all(bool(NEI[i]>>j&1)==bool(NEI[a[i]]>>a[j]&1)
            for i in range(N) for j in range(N))

def reduced_trace(a):
 # H_6 is the only reduced homology, and its degree has positive parity.
 t=-1
 for f in K:
  if not f:continue
  src=[i for i in range(N) if f>>i&1]
  dst=[a[i] for i in src]
  if set(src)!=set(dst): continue
  inversions=sum(dst[i]>dst[j] for i in range(len(dst)) for j in range(i+1,len(dst)))
  t+=(-1)**(len(src)-1+inversions)
 return t

GL=[]
for a in P:
 for b in P:
  if b==a:continue
  for c in P:
   if c in (a,b,a^b):continue
   def lin(x):return (a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0)
   points=[lin(p)-1 for p in P]
   lines=[next(i for i,L in enumerate(LINES) if set(L)==set(map(lin,M))) for M in LINES]
   GL.append(tuple(points+[7+i for i in lines]))
assert len(GL)==168 and len(set(GL))==168
autos=GL+[tuple(DUAL[i] for i in g) for g in GL]
assert len(set(autos))==336
assert all(a!=b for a in GL for b in autos[168:])
for g in autos:automorphism_test(g)
traces=Counter(reduced_trace(g) for g in autos)
assert traces=={1:336}
print('fano_lines=',LINES)
print('vertex_count=',N,'edge_count=',sum(x.bit_count() for x in NEI)//2)
print('faces_including_empty=',len(K),'face_counts_by_size=',EXPECTED_F)
print('first_toggle_order_ordinary_pairs_critical_cells_cover_relations_toposorted_mask=',m1)
print('second_toggle_order_ordinary_pairs_critical_cells_cover_relations_toposorted_mask=',m2)
print('automorphisms=',len(autos),'sixth_homology_traces=',dict(traces))
print('ALL_CHECKS_PASS')
