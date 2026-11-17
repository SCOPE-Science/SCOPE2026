#!/usr/bin/env python3
"""Exact acyclic discrete-Morse and integral attaching-matrix certificate for M(P3 square C6)."""
from collections import Counter,deque
from functools import lru_cache
from itertools import combinations
import hashlib,json,csv,sys
from sympy import ZZ,Matrix
from sympy.matrices.normalforms import smith_normal_form

COLS=6
edges=set()
for r in range(3):
 for c in range(COLS):
  if r<2:edges.add(tuple(sorted(((r,c),(r+1,c)))))
  edges.add(tuple(sorted(((r,c),(r,(c+1)%COLS)))))
E=tuple(sorted(edges))
assert len(E)==30
vertices={v:i for i,v in enumerate(sorted({v for e in E for v in e}))}
V=[sum(1<<vertices[v] for v in e) for e in E]
faces=[0]
occup={0:0}
for j,mask in enumerate(V):
 added=[]
 for s in faces:
  if not occup[s]&mask:
   t=s|(1<<j)
   occup[t]=occup[s]|mask
   added.append(t)
 faces+=added
assert len(faces)==57536
fvec=Counter(s.bit_count()-1 for s in faces if s)
assert [fvec[d] for d in range(9)]==[30,363,2290,8139,16446,18141,9870,2148,108]

ORDER=[25,12,24,20,6,0,28,26,27,9,5,17,19,7,4,8,2,10,3,11,15,22,21,16,23,1,29,13,18,14]
remaining=set(faces)
matched_up={}
matched_down={}
for j in ORDER:
 b=1<<j
 for s in list(remaining):
  t=s|b
  if not s&b and t in remaining:
   remaining.remove(s);remaining.remove(t)
   matched_up[s]=t;matched_down[t]=s
# Keep one vertex critical by reversing the pair containing the empty simplex.
base=matched_up.pop(0)
matched_down.pop(base)
remaining.add(base)
remaining.discard(0)
critical=sorted(remaining)
hist=Counter(s.bit_count()-1 for s in critical)
assert hist=={0:1,5:58,6:10},hist
assert len(matched_up)==28733

# Global acyclicity on the nonempty face poset. Matched incidence oriented upward;
# all other Hasse incidences oriented downward.
nonempty=[s for s in faces if s]
ids={s:i for i,s in enumerate(nonempty)}
N=len(nonempty)
indeg=[0]*N
out=[[] for _ in range(N)]
num_hasse=0
for s in nonempty:
 if s.bit_count()<2:continue
 for j in range(len(E)):
  b=1<<j
  if not s&b:continue
  t=s^b
  if not t:continue
  num_hasse+=1
  if matched_up.get(t)==s:
   src,dst=ids[t],ids[s]
  else:
   src,dst=ids[s],ids[t]
  out[src].append(dst);indeg[dst]+=1
Q=deque(i for i in range(N) if not indeg[i]);visited=0
while Q:
 i=Q.popleft();visited+=1
 for j in out[i]:
  indeg[j]-=1
  if indeg[j]==0:Q.append(j)
assert visited==N,(visited,N)

# Exact rational/integer algebraic Morse projection on dimension-five faces.
critical_5=sorted(s for s in critical if s.bit_count()==6)
critical_6=sorted(s for s in critical if s.bit_count()==7)
ci={s:i for i,s in enumerate(critical_5)}

def facets_signed(mask):
 for pos,j in enumerate(i for i in range(len(E)) if mask>>i&1):
  yield mask^(1<<j), 1 if pos%2==0 else -1

@lru_cache(None)
def project(s):
 if s in ci:return {ci[s]:1}
 if s in matched_down:return {}
 if s not in matched_up:raise AssertionError(('unclassified k-face',s))
 t=matched_up[s]
 coeff=dict(facets_signed(t))[s]
 acc={}
 for u,sign in facets_signed(t):
  if u==s:continue
  for i,c in project(u).items():
   acc[i]=acc.get(i,0)-coeff*sign*c
 return {i:c for i,c in acc.items() if c}

M=[[0]*len(critical_6) for _ in critical_5]
for col,s in enumerate(critical_6):
 for t,sign in facets_signed(s):
  for i,c in project(t).items():M[i][col]+=sign*c
D=smith_normal_form(Matrix(M),domain=ZZ)
nonzero=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
assert nonzero==[1]*10,nonzero
assert sum(fvec[d]*((-1)**d) for d in fvec)==-47  # chi=1-48=-47

# Independent homology calculation over F_2 in the original simplicial chain complex.
by_card={k:sorted(s for s in nonempty if s.bit_count()==k) for k in range(1,10)}
boundary_ranks={}
for k in range(2,10):
 low_index={s:i for i,s in enumerate(by_card[k-1])}
 pivots={}
 for face in by_card[k]:
  col=0
  for bit in range(30):
   if face>>bit&1:
    col ^= 1<<low_index[face^(1<<bit)]
  while col:
   lead=col.bit_length()-1
   prev=pivots.get(lead)
   if prev is None:
    pivots[lead]=col
    break
   col ^= prev
 boundary_ranks[k]=len(pivots)
mod2_betti={k-1:len(by_card[k])-boundary_ranks.get(k,0)-boundary_ranks.get(k+1,0) for k in range(1,10)}
assert mod2_betti=={0:1,1:0,2:0,3:0,4:0,5:48,6:0,7:0,8:0},mod2_betti

Mbytes=json.dumps(M,separators=(',',':')).encode()
if len(sys.argv)>1:
 with open(sys.argv[1],newline='',encoding='utf-8') as f:
  rows=[[int(z) for z in row] for row in csv.reader(f)]
 assert rows==M, 'provided integral Morse boundary differs from recomputed matrix'

print(json.dumps({'status':'CYLINDER_3X6_MATCHING_EXACT_PASS','vertices':len(vertices),
 'edges':len(E),'nonempty_faces':N,'face_vector':[fvec[d] for d in range(9)],
 'hasse_edges':num_hasse,'matched_pairs':len(matched_up),'critical_by_dimension':dict(sorted(hist.items())),
 'acyclic_visited':visited,'morse_boundary_shape':[len(critical_5),len(critical_6)],
 'morse_boundary_rank':len(nonzero),'smith_nonzero_factors':nonzero,
 'mod2_betti':mod2_betti,'original_mod2_boundary_ranks':boundary_ranks,
 'homotopy':'wedge of 48 spheres of dimension 5',
 'morse_matrix_sha256':hashlib.sha256(Mbytes).hexdigest()},sort_keys=True))
