"""Complete enumeration of reversal-complement closed dinucleotide circular codes.
Uses the directed-cycle characterization of circular dinucleotide codes.
Run: python3 direct_verify.py
"""
import itertools
from collections import Counter
from pathlib import Path

M=3;Q=2*M
comp=lambda x:x^1
blocks=[]
# A block is a pair of opposite orientations, each stored as a list of ordered pairs.
used=set()
for u in range(Q):
 for v in range(u+1,Q):
  pair=frozenset((u,v))
  if pair in used:continue
  counterpart=frozenset((comp(u),comp(v)))
  used.add(pair);used.add(counterpart)
  fwd=tuple(sorted({(u,v),(comp(v),comp(u))}))
  bwd=tuple(sorted({(v,u),(comp(u),comp(v))}))
  blocks.append((fwd,bwd))
assert len(blocks)==M*M

def encode(arcs):return sum(1<<(Q*u+v) for u,v in arcs)

A=[encode(b[0]) for b in blocks]
B=[encode(b[1]) for b in blocks]
assert all((a&b)==0 for a,b in zip(A,B))

def acyclic(edges):
 # Direct DFS with three colors, independent from topological-sort verifier.
 neighbors=[[] for _ in range(Q)]
 for u in range(Q):
  for v in range(Q):
   if edges>>(Q*u+v)&1:neighbors[u].append(v)
 color=[0]*Q
 def visit(u):
  color[u]=1
  for v in neighbors[u]:
   if color[v]==1:return False
   if color[v]==0 and not visit(v):return False
  color[u]=2
  return True
 return all(color[u] or visit(u) for u in range(Q))

codes={}
for choices in itertools.product((0,1,2),repeat=M*M):
 edges=0;weight=0
 for k,x in enumerate(choices):
  if x:
   edges |= A[k] if x==1 else B[k]
   weight+=len(blocks[k][0])
 if acyclic(edges):codes[edges]=weight
p=Counter(codes.values())
expected=[1,6,24,80,192,420,704,1032,1290,1334,1248,936,612,336,120,48]
assert [p[k] for k in range(16)]==expected,(p,expected)
assert len(codes)==8383

# Signed permutations form the group preserving the fixed complement matching.
group=[]
for pairs_perm in itertools.permutations(range(M)):
 for flips in itertools.product((0,1),repeat=M):
  group.append(tuple(2*pairs_perm[u//2]+((u%2)^flips[u//2]) for u in range(Q)))
assert len(group)==48

def action(e,g):
 new=0
 for u in range(Q):
  for v in range(Q):
   if e>>(Q*u+v)&1:new|=1<<(Q*g[u]+g[v])
 return new

orbits=Counter();remaining=set(codes)
while remaining:
 z=min(remaining)
 orbit={action(z,g) for g in group}
 assert orbit<=remaining
 remaining-=orbit
 orbits[codes[z]]+=1
# The canonical representative in each relabeling orbit is its least 36-bit
# adjacency mask; each serialized row lists its ordered dinucleotides.
rows=[]
for rep, orbit in sorted(((min({action(z,g) for g in group}),
                           {action(z,g) for g in group}) for z in codes), key=lambda t:t[0]):
 if rep not in {r[0] for r in rows}:
  words=' '.join(f'{u}{v}' for u in range(Q) for v in range(Q)
                 if (rep>>(Q*u+v))&1)
  rows.append((rep, codes[rep], len(orbit), words))
assert len(rows)==220
csv='size,orbit_size,codewords\n'+''.join(f'{w},{s},{t}\n' for _,w,s,t in rows)
payload=Path(__file__).with_name('representatives.csv').read_text(encoding='utf-8')
assert csv==payload
print('DIRECT_VERIFY_OK', 'blocks=',len(blocks),'codes=',len(codes),'max=',p[15], 'inequivalent=',sum(orbits.values()))
print('LABELED_COUNTS', [p[k] for k in range(16)])
print('ORBIT_COUNTS', [orbits[k] for k in range(16)])
