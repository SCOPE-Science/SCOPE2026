#!/usr/bin/env python3
"""Coordinate-based face-pattern census; independent of cube-line-graph enumeration."""
from collections import Counter
from itertools import product
from math import comb

# All permutations of (0,+/-1,+/-1), in a coordinate representation of
# the cuboctahedron. Squared-distance 2 is exactly its edge relation.
points = sorted(set(tuple(c) for axis in range(3) for signs in product((-1,1),repeat=2)
                    for c in [tuple(0 if j==axis else signs[j-(j>axis)] for j in range(3))]))
assert len(points) == 12
edges = [(u,v) for u in range(12) for v in range(u+1,12)
         if sum((points[u][j]-points[v][j])**2 for j in range(3)) == 2]
assert len(edges) == 24
assert all(sum(u in e for e in edges)==4 for u in range(12))

squares=[]
for ax in range(3):
 for sign in (-1,1):
  corners={j for j,v in enumerate(points) if v[ax]==sign}
  face=[i for i,(u,v) in enumerate(edges) if u in corners and v in corners]
  assert len(corners)==len(face)==4
  squares.append((tuple(sorted(corners)),tuple(face)))
assert sorted(i for _,face in squares for i in face) == list(range(24))

# Each square contributes one of its 16 local orientation words. Enumerate
# these words face-by-face, pruning only when an ice vertex cannot obtain
# exactly two outgoing arrows from its remaining unassigned incident edges.
choice_data=[]
for corners,face in squares:
 choices=[]
 for word in range(16):
  add={v:0 for v in corners}
  for k,idx in enumerate(face):
   u,v=edges[idx]
   tail=(v if (word>>k)&1 else u)
   add[tail]+=1
  is_cycle=all(add[v]==1 for v in corners)
  choices.append((word,add,is_cycle))
 assert sum(flag for _,_,flag in choices)==2
 choice_data.append(choices)

out=[0]*12
remaining=[4]*12
hits=[0]*6
hist=Counter()
patterns=Counter()
codes=set()

def recurse(i,wordbits,active):
 if i==6:
  assert out==[2]*12
  hist[active.bit_count()]+=1
  patterns[active]+=1
  for k in range(6):
   if (active>>k)&1: hits[k]+=1
  # Every wordbit is unique across assignments and uses all 24 directed edges.
  assert wordbits not in codes
  codes.add(wordbits)
  return
 corners,face=squares[i]
 for v in corners: remaining[v]-=2
 for word,inc,flag in choice_data[i]:
  for v in corners: out[v]+=inc[v]
  if all(out[v]<=2<=out[v]+remaining[v] for v in corners):
   recurse(i+1,wordbits | (word<<(4*i)), active | ((1<<i) if flag else 0))
  for v in corners: out[v]-=inc[v]
 for v in corners: remaining[v]+=2
recurse(0,0,0)
assert len(codes)==sum(hist.values())==600
assert hist=={0:144,1:144,2:120,3:128,6:64}, hist
assert hits==[192]*6
expected={0:144,63:64}
expected.update({1<<i:24 for i in range(6)})
expected.update({(1<<i)|(1<<j):8 for i in range(6) for j in range(i+1,6)})
expected.update({(1<<i)|(1<<j)|(1<<k):16 for i in (0,1)
                 for j in (2,3) for k in (4,5)})
assert patterns==expected,patterns
# Direct spectral consequence of a Q_d orbit: eigenvalues d-2k.
component={d:cnt//(1<<d) for d,cnt in hist.items()}
assert all(cnt%(1<<d)==0 for d,cnt in hist.items())
assert component=={0:144,1:72,2:30,3:16,6:1}
eigen=Counter()
for d,nb in component.items():
 for k in range(d+1): eigen[d-2*k]+=nb*comb(d,k)
assert eigen=={0:224,1:120,-1:120,2:45,-2:45,3:16,-3:16,4:6,-4:6,6:1,-6:1}, eigen
assert sum(eigen.values())==600
assert sum(ev*ev*mult for ev,mult in eigen.items())==1152
assert sum(ev**4*mult for ev,mult in eigen.items())==9936
print('PASS coordinates: all 600 orientations, square-activity', sorted(hist.items()))
print('PASS joint face-activity polynomial 31 nonzero face subsets')
print('PASS per-square activation 192; 263 hypercube sectors')
print('PASS exact kinetic spectrum',sorted(eigen.items()))
print('PASS spectral moments trace(A^2)=1152; trace(A^4)=9936')
