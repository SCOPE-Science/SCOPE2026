#!/usr/bin/env python3
"""Exact signed-chain verification for the Fano rank-three matroid complex."""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from fractions import Fraction

POINTS=tuple(range(1,8))
LINES={frozenset((a,b,a^b)) for a,b in combinations(POINTS,2)}
F={-1:[()], 0:[(a,) for a in POINTS], 1:list(combinations(POINTS,2)),
   2:[t for t in combinations(POINTS,3) if frozenset(t) not in LINES]}
assert tuple(len(F[d]) for d in (-1,0,1,2))==(1,7,21,28)
S={d:set(F[d]) for d in F}

def sg(seq):
 return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def bd(s):
 return {s[:i]+s[i+1:]:(-1)**i for i in range(len(s))}

for d in (1,2):
 for s in F[d]:
  out=Counter()
  for t,a in bd(s).items():
   for u,b in bd(t).items():out[u]+=a*b
  assert not any(out.values()),(d,s,out)

# Prove integrally, not just by field ranks: every omitted triangular
# boundary equals a sum of three retained triangular boundaries, obtained
# by coning to an off-line vertex. Therefore im(boundary_2) is the full
# cycle lattice of the complete graph K_7. Hence H_1=0 integrally.
for l in LINES:
 a,b,c=sorted(l)
 for x in POINTS:
  if x in l:continue
  combo=Counter()
  for tri in ((a,b,x),(a,x,c),(x,b,c)):
   canon=tuple(sorted(tri)); coeff=sg(tri)
   assert canon in S[2],(l,x,tri)
   for t,z in bd(canon).items():combo[t]+=coeff*z
  target=bd((a,b,c))
  assert all(combo[t]==v for t,v in target.items()) and not any(combo[t] for t in combo if t not in target)

G=[]
for x,y,z in permutations(POINTS,3):
 if x^y==z:continue
 g={a:((x if a&1 else 0)^(y if a&2 else 0)^(z if a&4 else 0)) for a in POINTS}
 G.append(g)
assert len(G)==168

def order(g):
 v={a:a for a in POINTS}
 for i in range(1,9):
  v={a:g[v[a]] for a in POINTS}
  if all(v[a]==a for a in POINTS):return i
 raise ValueError('order too large')

def tr(g,d):
 return sum(sg(tuple(g[x] for x in s)) for s in F[d] if tuple(sorted(g[x] for x in s))==s)

# All face maps commute with the signed boundary, for the full 168-element
# automorphism group; check individual coefficients on each face.
checks=0
for g in G:
 for d in (1,2):
  for s in F[d]:
   lhs=Counter()
   for t,a in bd(s).items():
    im=tuple(g[x] for x in t);lhs[tuple(sorted(im))]+=a*sg(im)
   im=tuple(g[x] for x in s)
   rhs=Counter({t:a*sg(im) for t,a in bd(tuple(sorted(im))).items()})
   assert all(lhs[k]==rhs[k] for k in set(lhs)|set(rhs)),(d,s,g)
   checks+=1

hist=Counter();trace_set=defaultdict(set)
for g in G:
 o=order(g)
 trc=tuple(tr(g,d) for d in (-1,0,1,2))
 ch=trc[3]-trc[2]+trc[1]-trc[0]
 hist[o]+=1;trace_set[o].add((ch,trc))
expected={1:(1,13,(1,7,21,28)),2:(21,-3,(1,3,1,-4)),3:(56,1,(1,1,0,1)),4:(42,1,(1,1,-1,0)),7:(48,-1,(1,0,0,0))}
assert set(hist)==set(expected)
for o,(size,ch,t) in expected.items():
 assert hist[o]==size and trace_set[o]=={(ch,t)},(o,hist[o],trace_set[o])

# Decomposition into the degree-seven irrep plus the rational sum of the
# conjugate degree-three representations, by the classical PSL(2,7) table.
char7={1:7,2:-1,3:1,4:-1,7:0}
char6={1:6,2:-2,3:0,4:2,7:-1}
for o,(size,ch,t) in expected.items(): assert char7[o]+char6[o]==ch
assert sum(size*ch for size,ch,t in expected.values())==0
# For a generator of order 2,3,4,7 evaluate all its subgroup powers.
fixdims={}
for o in (2,3,4,7):
 g=next(g for g in G if order(g)==o)
 p={a:a for a in POINTS};v=0
 for k in range(o):
  trc=tuple(tr(p,d) for d in (-1,0,1,2))
  v+=trc[3]-trc[2]+trc[1]-trc[0]
  p={a:g[p[a]] for a in POINTS}
 assert v%o==0
 fixdims[o]=v//o
assert fixdims=={2:5,3:5,4:3,7:1}

print('FANO_MATROID_EQUIVARIANT_HOMOLOGY_PASS')
print('number_of_lines=7 noncollinear_triangles=28 graph_edges=21')
print('integer_coning_identites=',7*4)
print('chain_equivariance_checks=',checks)
print('group_size=',len(G))
print('order_classes=',dict(sorted(hist.items())))
print('signed_euler_trace_by_order=',{o:next(iter(trace_set[o]))[0] for o in sorted(trace_set)})
print('complex_irreducible_dimensions=7+3+3')
print('cyclic_fixed_ranks=',fixdims)
print('FULL_GROUP_FIXED_RANK=0')
