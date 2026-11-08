#!/usr/bin/env python3
"""Exhaustive simplicial collapse checks for cube three-cut Alexander duals.
The mathematical theorem covers all dimensions d >= 3; this checks small d only.
"""
from itertools import combinations
from math import comb

def pop(x):return x.bit_count()

def run(d):
 n=1<<d
 edges={frozenset(e) for e in combinations(range(n),2)}
 paths={frozenset(t) for t in combinations(range(n),3) if sum(pop(a^b)==1 for a,b in combinations(t,2))==2}
 squares=[]
 for a in range(n):
  for i,j in combinations(range(d),2):
   if ((a>>i)&1)==((a>>j)&1)==0:
    b=a^(1<<i); c=b^(1<<j); e=a^(1<<j)
    squares.append((a,b,c,e))
 assert len(squares)==2**(d-2)*comb(d,2)
 faces={1:{frozenset([v]) for v in range(n)},2:edges.copy(),3:paths.copy(),4:{frozenset(s) for s in squares}}
 for a,b,c,e in squares:
  tetra=frozenset((a,b,c,e)); triangle=frozenset((a,b,e));diag=frozenset((b,e));tri2=frozenset((b,c,e))
  assert tetra in faces[4] and triangle in faces[3]
  assert sum(triangle<=t for t in faces[4])==1
  faces[4].remove(tetra);faces[3].remove(triangle)
  assert sum(diag<=t for t in faces[3])==1
  assert sum(diag<=t for t in faces[4])==0
  assert tri2 in faces[3] and diag in faces[2]
  faces[3].remove(tri2);faces[2].remove(diag)
 assert not faces[4]
 expected_tri={frozenset((a,b,c)) for a,b,c,e in squares}|{frozenset((a,c,e)) for a,b,c,e in squares}
 expected_diagonals={frozenset((a,c)) for a,b,c,e in squares}
 assert faces[3]==expected_tri
 assert faces[2]=={frozenset((a,b)) for a,b in combinations(range(n),2) if pop(a^b) in (1,) or pop(a^b)>=3}|expected_diagonals
 assert all(not all(sum(pop(x^y)==1 for x,y in combinations(t,2))==2 for t in combinations(w,3)) for w in combinations(range(n),5)) if d<=4 else True
 longedges=sum(pop(a^b)>=3 for a,b in combinations(range(n),2))
 alpha=2**(d-2)*comb(d,2)-d*2**(d-1)+2**d-1
 assert alpha>0
 return d, (n,len(edges),len(paths),len(squares)),(len(faces[1]),len(faces[2]),len(faces[3]),len(faces[4])),alpha,longedges

if __name__=='__main__':
 for d in range(3,7):print('d,dual_f_vector,collapsed_f_vector,beta2,beta1',run(d))
 print('ALL COLLAPSE CHECKS PASS')
