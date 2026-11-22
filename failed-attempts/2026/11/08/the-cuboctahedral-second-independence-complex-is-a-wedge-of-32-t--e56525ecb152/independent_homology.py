#!/usr/bin/env python3
"""Separate forbidden-triple enumerator and binary simplicial boundary reduction."""
from itertools import combinations
from collections import defaultdict
# Label cubical edges differently: coordinate then fixed remaining bits.
E=sorted(tuple(sorted((x,x^(1<<d)))) for d in range(3) for x in range(8) if not x&(1<<d))
assert len(E)==12
A=[[False]*12 for _ in range(12)]
for i in range(12):
 for j in range(i+1,12):
  A[i][j]=A[j][i]=bool(set(E[i])&set(E[j]))
assert sum(sum(a) for a in A)//2==24
# A chosen set induces an edge or singleton components only iff
# it contains no triple (i,j,k) with at least two incident edges.
forbidden=[]
for i,j,k in combinations(range(12),3):
 if int(A[i][j])+int(A[j][k])+int(A[i][k])>=2:
  forbidden.append((1<<i)|(1<<j)|(1<<k))
assert len(forbidden)==56,len(forbidden)
bydim=defaultdict(list)
for mask in range(1,1<<12):
 if not any((mask&t)==t for t in forbidden):
  bydim[mask.bit_count()-1].append(mask)
assert tuple(len(bydim[d]) for d in range(5))==(12,66,164,177,36)

# Construct each mod-two boundary directly and eliminate columns with bitsets.
def rank_boundary(d):
 smaller={f:i for i,f in enumerate(bydim[d-1])}
 reduced={}
 for f in bydim[d]:
  b=0
  for v in range(12):
   if f&(1<<v):b ^= 1<<smaller[f^(1<<v)]
  while b:
   i=b.bit_length()-1
   if i in reduced:b^=reduced[i]
   else:reduced[i]=b;break
 return len(reduced)
ranks={d:rank_boundary(d) for d in range(1,5)}
assert [ranks[d] for d in range(1,5)]==[11,55,109,36],ranks
betti=[len(bydim[0])-ranks[1]-1]
for d in range(1,5):betti.append(len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0))
assert betti==[0,0,0,32,0],betti
print('FORBIDDEN_CONNECTED_TRIPLES',len(forbidden))
print('INDEPENDENT_FACE_COUNTS',','.join(str(len(bydim[d])) for d in range(5)))
print('BINARY_BOUNDARY_RANKS',','.join(str(ranks[d]) for d in range(1,5)))
print('REDUCED_BETTI_F2',','.join(map(str,betti)))
print('INDEPENDENT_MOD2_CHECKS_PASS')
