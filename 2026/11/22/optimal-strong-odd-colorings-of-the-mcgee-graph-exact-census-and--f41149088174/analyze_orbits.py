import networkx as nx
from collections import Counter,defaultdict
G=nx.Graph();G.add_nodes_from(range(24))
for i in range(24):G.add_edge(i,(i+1)%24);G.add_edge(i,(i+[12,7,-7][i%3])%24)
a=[tuple(int(c) for c in s.strip()) for s in open('search_colorings_5.txt')]
def signature(s):return tuple(sorted(sum(1<<i for i,c in enumerate(s) if c==j) for j in set(s)))
ids={signature(s):i for i,s in enumerate(a)}
auto=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(auto)==32
vis=set(); orbit_sizes=Counter(); profi=defaultdict(Counter); sigexamples={}
for i,s in enumerate(a):
 if i in vis:continue
 masks=signature(s); orb=set()
 for perm in auto:
  new=tuple(sorted(sum(1<<perm[i] for i in range(24) if m>>i&1) for m in masks))
  assert new in ids
  orb.add(ids[new])
 vis.update(orb)
 prof=tuple(sorted(s.count(j) for j in set(s)))
 orbit_sizes[len(orb)]+=1
 profi[prof][len(orb)]+=1
 sigexamples[(prof,len(orb))]=i
assert orbit_sizes == {8:5,16:19,32:30}
print('orbits',sum(orbit_sizes.values()),'orbit_sizes',dict(sorted(orbit_sizes.items())))
print('profiles',dict(profi))
print('examples',sigexamples)
# rainbow vertices 3 distinct neighbor colors vs monochromatic
mix=Counter()
for s in a:
 rain=sum(len({s[u] for u in G[v]})==3 for v in G.nodes())
 mix[rain]+=1
assert mix[24]==320 and sum(mix.values())==1304
print('rainbow vertex count',dict(sorted(mix.items())))

# Independent partition generation must agree with the color-assignment search.
with open("exact_cover_partitions.txt") as fh:
    exact={tuple(sorted(map(int, line.split()))) for line in fh if line.strip()}
assert len(exact)==1304 and set(ids)==exact
assert sum(orbit_sizes.values())==54
print("independent census agreement: 1304")
