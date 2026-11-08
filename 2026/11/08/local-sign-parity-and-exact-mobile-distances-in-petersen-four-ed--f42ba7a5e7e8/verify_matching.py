"""Independent exact-cover certificate for proper four-edge-colouring reconfiguration of the Petersen graph."""
from itertools import combinations,permutations
from collections import Counter, deque
P=list(combinations(range(5),2))
E=[(i,j) for i,j in combinations(range(10),2) if set(P[i]).isdisjoint(P[j])]
assert len(E)==15
vertex_edge=[sum(1<<k for k,(u,v) in enumerate(E) if i in (u,v)) for i in range(10)]
ALL=(1<<15)-1
matching_masks=[]
for m in range(1,ALL+1):
 if all((m&vm).bit_count()<2 for vm in vertex_edge):matching_masks.append(m)
by_edge=[[m for m in matching_masks if m&(1<<e)] for e in range(15)]
canonical=[]
def parts(remaining,parts_so_far):
 if len(parts_so_far)==4:
  if not remaining:canonical.append(tuple(parts_so_far))
  return
 if not remaining:return
 e=(remaining&-remaining).bit_length()-1
 for mask in by_edge[e]:
  if (mask & remaining)==mask:parts(remaining^mask,parts_so_far+[mask])
parts(ALL,[])
assert len(canonical)==2080,len(canonical)
config=[tuple(row[i] for i in p) for row in canonical for p in permutations(range(4))]
assert len(config)==49920
lookup={c:i for i,c in enumerate(config)}
assert len(lookup)==len(config)
G=[[] for _ in config]
for i,c in enumerate(config):
 for a in range(4):
  for b in range(4):
   if a==b:continue
   for e in range(15):
    bit=1<<e
    if not (c[a]&bit):continue
    u,v=E[e]
    if (c[b]&(vertex_edge[u]|vertex_edge[v])):continue
    nc=list(c);nc[a]^=bit;nc[b]^=bit
    G[i].append(lookup[tuple(nc)])
assert all(len(set(ng))==len(ng) for ng in G)
assert sum(map(len,G))//2==109440
component=[-1]*len(config);sizes=[]
for start in range(len(config)):
 if component[start]>=0:continue
 k=len(sizes);Q=[start];component[start]=k
 for u in Q:
  for v in G[u]:
   if component[v]<0:component[v]=k;Q.append(v)
 sizes.append(len(Q))
assert Counter(sizes)=={1:960,24480:2},Counter(sizes)
assert Counter(map(len,G))=={0:960,1:1440,2:2880,3:10560,4:8640,5:12960,6:6720,7:5760}
# parity sign of local permutation in edge-index order followed by absent color.
def sign_of(arr):
 return -1 if sum(arr[i]>arr[j] for i in range(4) for j in range(i+1,4))%2 else 1
PSign=[]
for c in config:
 color_by_edge=[next(a for a,m in enumerate(c) if m&(1<<e)) for e in range(15)]
 s=1
 for vertex in range(10):
  colors=[color_by_edge[e] for e in range(15) if vertex_edge[vertex]&(1<<e)]
  colors.append(next(a for a in range(4) if a not in colors))
  s*=sign_of(colors)
 PSign.append(s)
assert all(PSign[i]==PSign[j] for i,row in enumerate(G) for j in row)
large=[k for k,z in enumerate(sizes) if z>1]
assert {PSign[i] for i in range(len(G)) if component[i]==large[0]}=={-1} or {PSign[i] for i in range(len(G)) if component[i]==large[0]}=={1}
assert set(PSign[i] for i in range(len(G)) if component[i]==large[0])!=set(PSign[i] for i in range(len(G)) if component[i]==large[1])
assert Counter(PSign[i] for i in range(len(G)) if len(G[i])==0)=={-1:480,1:480}
assert all(sum(bool(c[a]&(1<<e)) for a in range(4))==1 for c in config for e in range(15))
print('EXACT_COVER_2080_PARTITIONS_49920_NAMED_PASS')
print('109440_EDGES_960_ISOLATED_TWO_24480_COMPONENTS_PASS')
print('SIGN_PARITY_TWO_MOBILE_COMPONENTS_PASS')
print('DEGREE_ENUMERATOR_PASS')
