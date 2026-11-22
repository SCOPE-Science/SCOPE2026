"""Independent edge-list, trajectory tracing and symmetry cross-check.
Run: python check_trajectory_symmetry.py
Only networkx is needed for symmetry enumeration, not for trajectories.
"""
from collections import Counter,defaultdict
from itertools import combinations
import networkx as nx

EDGES=((1,2),(1,4),(1,5),(2,3),(2,6),(2,7),(3,4),(3,8),
       (4,9),(4,10),(5,6),(5,10),(6,11),(7,8),(7,11),
       (8,9),(9,11),(10,11))
assert len(EDGES)==18
G=nx.Graph();G.add_nodes_from(range(1,12));G.add_edges_from(EDGES)
assert nx.is_connected(G) and nx.is_bipartite(G)
assert nx.check_planarity(G)[0] and nx.node_connectivity(G)==3
assert sorted(dict(G.degree()).values())==[3]*8+[4]*3
N=11

def next_state(bits):
    bits=list(bits)
    new=[]
    for v in range(1,N+1):
        nb=[bits[w-1] for w in G.neighbors(v)]
        if sum(nb)*2==len(nb):new.append(bits[v-1])
        else:new.append(int(sum(nb)*2>len(nb)))
    return tuple(new)

def number(bits):return sum(b<<i for i,b in enumerate(bits))

def tuplebits(num):return tuple((num>>i)&1 for i in range(N))

bases={};encounter=Counter();roots={};periods={}
for x in range(1<<N):
    cur=tuplebits(x);seq=[];positions={}
    while cur not in positions:
        positions[cur]=len(seq);seq.append(cur)
        cur=next_state(cur)
    t=positions[cur];period=len(seq)-t
    assert period in (1,2)
    orb=min(number(q) for q in seq[t:])
    encounter[(t,period)]+=1
    roots[x]=orb;periods[orb]=period
    bases.setdefault(orb,tuple(sorted(number(q) for q in seq[t:])))
assert sum(encounter.values())==1<<N
counts=Counter(roots.values())
assert Counter(periods.values())=={1:20,2:61}
assert max(t for t,_ in encounter)==6
assert encounter[(6,1)]==48 and encounter[(6,2)]==0
assert sorted(Counter(counts[k] for k in bases if periods[k]==1).items())==[(1,6),(7,12),(501,2)]
assert sorted(Counter(counts[k] for k in bases if periods[k]==2).items())==[(4,24),(8,12),(14,6),(25,6),(27,12),(206,1)]

permutations=[]
for iso in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():
    permutations.append(tuple(iso[i]-1 for i in range(1,N+1)))
assert len(permutations)==12

def move(x,p):return sum(((x>>i)&1)<<p[i] for i in range(N))
classes=Counter();seen=set();weighted=Counter()
for orb,states in bases.items():
    if orb in seen:continue
    keys={min(move(s,p) for s in states) for p in permutations}
    assert all(k in bases for k in keys)
    assert all(counts[k]==counts[orb] for k in keys)
    assert all(periods[k]==periods[orb] for k in keys)
    seen.update(keys);classes[periods[orb]]+=1
    weighted[(periods[orb],len(keys),counts[orb])]+=1
assert classes=={1:6,2:11}
assert len(seen)==len(bases)
assert weighted[(2,1,206)]==1
print('PASS: independent trace',1<<N,'states; automorphisms',len(permutations))
print('first entry × least period',sorted(encounter.items()))
print('spatial classes: fixed',classes[1],'two cycles',classes[2])
print('orbit-class signatures (period, multiplicity, basin):',sorted(weighted.items()))
