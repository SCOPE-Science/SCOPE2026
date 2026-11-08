#!/usr/bin/env python3
"""Exact full automorphism homology-character certificate. Standard library only."""
from collections import Counter,defaultdict,deque
from itertools import combinations
V=tuple(range(16));N=[set() for _ in V]
for i in range(8):
 for a,b in ((i,(i+1)%8),(i,i+8),(8+i,8+(i+3)%8)):
  N[a].add(b);N[b].add(a)
assert all(len(N[v])==3 for v in V)
D=[]
for s in V:
 dd=[-1]*16;dd[s]=0;q=deque([s])
 while q:
  u=q.popleft()
  for v in N[u]:
   if dd[v]<0:dd[v]=dd[u]+1;q.append(v)
 D.append(dd)
assert all(Counter(row)=={0:1,1:3,2:6,3:5,4:1} for row in D)
P=[frozenset(i for i in V if i!=v and D[v][i]<=2) for v in V]
F=[]
def visit(face,start):
 for v in range(start,16):
  if all(v in P[u] for u in face):
   new=face+(v,);F.append(new);visit(new,v+1)
visit((),0)
assert Counter(map(len,F))=={1:16,2:72,3:112,4:48}
# Independent exact mod-two simplicial boundary ranks.
bydim={k:sorted(f for f in F if len(f)==k+1) for k in range(4)}
ranks=[]
for k in (1,2,3):
 loc={f:i for i,f in enumerate(bydim[k-1])};piv={}
 for face in bydim[k]:
  vec=0
  for i in range(len(face)):vec ^= (1<<loc[face[:i]+face[i+1:]])
  while vec:
   h=vec.bit_length()-1
   if h in piv:vec ^=piv[h]
   else:piv[h]=vec;break
 ranks.append(len(piv))
assert ranks==[15,57,46]
assert len(bydim[1])-ranks[0]-ranks[1]==0 and len(bydim[2])-ranks[1]-ranks[2]==9 and len(bydim[3])-ranks[2]==2
# All graph automorphisms found via exact backtracking using distances
# to already mapped vertices as the assignment predicate.
A=[]
def backtrack(mapping,used):
 if len(mapping)==16:
  A.append(tuple(mapping[v] for v in V));return
 # Most constrained vertex first. Every candidate must have exact distances
 # to all previously mapped vertices, and map injectively.
 best_v=None;best_options=None
 for v in V:
  if v in mapping:continue
  choices=[w for w in V if w not in used and all(D[v][a]==D[w][b] for a,b in mapping.items())]
  if best_options is None or len(choices)<len(best_options):best_v,best_options=v,choices
  if len(best_options)==0:return
 for w in best_options:
  mapping[best_v]=w;used.add(w);backtrack(mapping,used);used.remove(w);del mapping[best_v]
backtrack({},set())
assert len(A)==96 and len(set(A))==96
assert all(all((u in N[v])==(g[u] in N[g[v]]) for u in V for v in V) for g in A)
# Bipartition, determined by graph adjacency, and the antipodal pairing
colors={0:0};q=deque([0])
while q:
 u=q.popleft()
 for v in N[u]:
  if v not in colors:colors[v]=1-colors[u];q.append(v)
  else:assert colors[v]!=colors[u]
parts=tuple(tuple(v for v in V if colors[v]==c) for c in (0,1))
assert set(map(len,parts))=={8}
antipode={v:next(w for w in V if D[v][w]==4) for v in V}
assert all(antipode[antipode[v]]==v for v in V)

def sign(a):
 return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1

def sphere_chain(part):
 # Fundamental 3-cycle of the join of four antipodal 0-spheres:
 # product (p_1-q_1)*...*(p_4-q_4), expressed as oriented 3-faces.
 pairlist=sorted((v,antipode[v]) for v in part if v<antipode[v])
 assert len(pairlist)==4
 out={}
 for mask in range(16):
  face=tuple(pairlist[j][bool(mask>>j&1)] for j in range(4))
  orient=sign(face);out[tuple(sorted(face))]=orient*(-1)**mask.bit_count()
 assert len(out)==16
 return out
cycles=(sphere_chain(parts[0]),sphere_chain(parts[1]))
assert not (set(cycles[0]) & set(cycles[1]))
assert all(f in bydim[3] for cyc in cycles for f in cyc)
for cyc in cycles:
    b=defaultdict(int)
    for f,coeff in cyc.items():
        for j in range(4):
            b[f[:j]+f[j+1:]]+=coeff*((-1)**j)
    assert all(x==0 for x in b.values())
# Mod-two rank 46 gives rational rank at least 46. The two
# independent integral cycles show rational nullity at least two,
# so rational rank exactly 46. Because they have disjoint supports
# with unit coefficients, they also constitute an integral basis
# of the rank-two kernel (no finite lattice index is possible).

def cycle_image(g,source):
 out=defaultdict(int)
 for f,c in source.items():
  im=tuple(g[v] for v in f)
  out[tuple(sorted(im))]+=c*sign(im)
 return dict(out)

def homology3_matrix(g):
 # No 4-simplices exist at scale two. Every 3-cycle has a canonical
 # chain representative, so this is an exact integral action on H3.
 cols=[]
 for src in cycles:
  im=cycle_image(g,src)
  if im==cycles[0]:cols.append((1,0))
  elif im==cycles[1]:cols.append((0,1))
  elif im=={k:-v for k,v in cycles[0].items()}:cols.append((-1,0))
  elif im=={k:-v for k,v in cycles[1].items()}:cols.append((0,-1))
  else:raise AssertionError('unexpected homology3 action')
 return cols

def chain_lefschetz(g):
 total=0
 for f in F:
  image=[g[v] for v in f]
  if set(image)==set(f):total+=((-1)**(len(f)-1))*sign(image)
 return total
R=[]
for g in A:
 preserve=colors[g[0]]==colors[0]
 mat=homology3_matrix(g)
 chi3=mat[0][0]+mat[1][1]
 assert chi3==(2 if preserve else 0)
 alt=chain_lefschetz(g)
 # H0 is the trivial one-dimensional module, H1=0 and H2/H3
 # are the only nonzero reduced homology in positive degrees.
 chi2=alt-1+chi3
 R.append((g,preserve,chi2,chi3,mat))

freq=Counter((x[2],x[3]) for x in R)
expected={(9,2):1, (3,0):6, (1,0):12, (-3,2):8,(-1,2):12,(1,2):27,(-1,0):30}
assert freq==expected
assert sum(x[2] for x in R)==0
assert sum(x[3] for x in R)==96
assert sum(x[2]**2 for x in R)==3*96
assert sum(x[3]**2 for x in R)==2*96
assert sum(x[2]*x[3] for x in R)==0
assert sum(x[1] for x in R)==48
assert all(x[3]==2 for x in R if x[1])
assert all(x[4]==[(1,0),(0,1)] for x in R if x[1])
assert all(x[4]==[(0,1),(1,0)] for x in R if not x[1])
# Complete character of the two rational modules; inner-product three
# shows H2 is a multiplicity-free sum of three complex irreducibles.
print('GRAPH 16 vertices, 24 edges, 96 exact graph automorphisms')
print('SCALE TWO face vector 16,72,112,48; mod-two boundary ranks 15,57,46')
print('TWO integral primitive 3-cycle generators on the bipartition halves')
print('H3: dimension 2, bipartition permutation character (2 if preserving; 0 if exchanging)')
print('H2: dimension 9, character via signed simplicial Lefschetz and H3')
for char,mul in sorted(expected.items(),reverse=True):
 print('CHARACTER',char[0],char[1],'MULTIPLICITY',mul)
print('INVARIANT_RANKS H2=0 H3=1; CHARACTER_NORMS H2=3 H3=2; INNER_PRODUCT=0')
print('ALL_CHECKS_PASS')
