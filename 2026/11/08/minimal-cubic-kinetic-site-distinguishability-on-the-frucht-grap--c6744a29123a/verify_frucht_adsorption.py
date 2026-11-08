"""Exact random-sequential monomer adsorption on the labeled Frucht graph.
Standard-library-only rational recursion and integer permutation aggregation.
"""
from functools import lru_cache
from fractions import Fraction
from collections import defaultdict,Counter
from itertools import combinations
# fixed edge list, no graph package needed
EDGES=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
n=12; full=(1<<n)-1
N=[1<<i for i in range(n)]; adj=[0]*n
for u,v in EDGES:N[u]|=1<<v;N[v]|=1<<u;adj[u]|=1<<v;adj[v]|=1<<u

@lru_cache(None)
def F(mask):
 if not mask:return (tuple(Fraction(0) for _ in range(n)), (Fraction(1),))
 vs=[v for v in range(n) if mask&(1<<v)]; occ=[Fraction(0)]*n; law=[Fraction(0)]*(n+1)
 for v in vs:
  sub,dist=F(mask&~N[v]);w=Fraction(1,len(vs))
  for u in range(n):occ[u]+=w*(sub[u]+int(v==u))
  for k,z in enumerate(dist):
   if z:law[k+1]+=w*z
 return tuple(occ),tuple(law)
occ,law=F(full); assert F.cache_info().currsize==97
# independent approach: count arrival permutations with DP on masks and occupied-state
states={(0,0):1}; costs=[]
for step in range(n):
 nxt=defaultdict(int)
 for (seen,occupied),ways in states.items():
  rem=full^seen
  while rem:
   b=rem & -rem; rem-=b;v=b.bit_length()-1
   new_occ=occupied | (b if occupied & adj[v]==0 else 0)
   nxt[(seen|b,new_occ)]+=ways
 states=nxt;costs.append(len(states))
assert costs==[12,84,370,1154,2583,4236,5102,4441,2715,1110,274,31]
import math
pcount=math.factorial(n); wins=[0]*n; sizes=Counter()
for (seen,occupied),num in states.items():
 assert seen==full
 sizes[occupied.bit_count()]+=num
 for v in range(n):
  if occupied>>v&1:wins[v]+=num
assert sum(sizes.values())==pcount

assert tuple(Fraction(v,pcount) for v in wins)==occ
assert all(Fraction(sizes.get(k,0),pcount)==v for k,v in enumerate(law))
assert len(set(occ))==n
assert all(adj[v].bit_count()==3 for v in range(n))
visited={0}
while True:
    nxt=visited|{i for v in visited for i in range(n) if adj[v]>>i&1}
    if nxt==visited:break
    visited=nxt
assert len(visited)==n
expected_nums=(5631,5440,6993,5877,5454,5762,5516,5319,6759,5949,5444,6506)
assert tuple(Fraction(a,17280) for a in expected_nums)==occ
assert {i:law[i] for i in range(len(law)) if law[i]}=={3:Fraction(1,64),4:Fraction(169,192),5:Fraction(5,48)}
assert len(set(expected_nums))==12
ordered=sorted(expected_nums)
assert min(b-a for a,b in zip(ordered,ordered[1:]))==4
assert Fraction(max(expected_nums)-min(expected_nums),17280)==Fraction(31,320)
assert sum(occ)==Fraction(785,192)
print('FRUCHT_ADSORPTION_CERTIFICATE_OK')
