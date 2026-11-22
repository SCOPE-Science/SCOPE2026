"""Independent Hamilton-cycle enumerator in the 2/3-subset incidence representation.
Run: python3 verify_direct_hamiltonian_cycles.py (Python 3 standard library only).
"""
from itertools import combinations, permutations
from collections import Counter, deque

subsets=[frozenset(q) for r in (2,3) for q in combinations(range(5),r)]
assert len(subsets)==20
edges={tuple(sorted((i,j))) for i in range(20) for j in range(i+1,20)
       if len(subsets[i])==2 and subsets[i]<subsets[j]}
assert len(edges)==30
adj=[set() for _ in range(20)]
for a,b in edges:
    adj[a].add(b);adj[b].add(a)
assert all(len(row)==3 for row in adj)

# Every undirected Hamiltonian cycle contains vertex 0. Branch over all spanning
# paths beginning there, accept only closed paths, and quotient by reversal.
cycles=set()
def extend(path,used):
    if len(path)==20:
        if 0 in adj[path[-1]]:
            e=frozenset(tuple(sorted((a,b))) for a,b in zip(path,path[1:]+[0]))
            assert len(e)==20
            cycles.add(e)
        return
    for v in adj[path[-1]]:
        if not (used & (1<<v)):
            extend(path+[v],used|(1<<v))
extend([0],1)
assert len(cycles)==24
cycles=sorted(cycles,key=lambda es:tuple(sorted(es)))
index={c:i for i,c in enumerate(cycles)}

def cycle_difference(A,B):
    delta=A^B
    if not delta:return 0
    nb=[set() for _ in range(20)]
    for a,b in delta:
        nb[a].add(b);nb[b].add(a)
    active={i for i in range(20) if nb[i]}
    assert all(len(nb[i])==2 for i in active)
    root=min(active);visited={root};q=[root]
    for v in q:
        for w in nb[v]:
            if w not in visited:
                visited.add(w);q.append(w)
    return len(delta) if active == visited else 0

jump=[set() for _ in cycles]; counts=Counter()
for i in range(24):
    for j in range(i):
        k=cycle_difference(cycles[i],cycles[j]);counts[k]+=1
        if k==10:jump[i].add(j);jump[j].add(i)
assert counts==Counter({10:84,18:60,0:132})
assert all(len(s)==7 for s in jump)
for root in range(24):
    distances={root:0};q=deque([root])
    while q:
        i=q.popleft()
        for j in jump[i]:
            if j not in distances:
                distances[j]=distances[i]+1;q.append(j)
    assert Counter(distances.values())==Counter({0:1,1:7,2:16})
    degrees={j:len(jump[j]&jump[root]) for j in jump[root]}
    assert Counter(degrees.values())==Counter({0:2,2:5})
assert sum(sum(len(jump[i]&jump[j]) for j in jump[i]) for i in range(24))//6==40

# Every permutation of the five symbols, with optional 2/3-complementation,
# preserves the incidence structure. Confirm transitivity and two edge types.
subindex={s:i for i,s in enumerate(subsets)}
vertex_orbit=set(); edge_orbits=Counter()
all_maps=[]
for p in permutations(range(5)):
    for swap in (False,True):
        mp=[]
        for s in subsets:
            image=frozenset(p[x] for x in s)
            if swap:image=frozenset(set(range(5))-image)
            mp.append(subindex[image])
        states=[]
        for c in cycles:
            image=frozenset(tuple(sorted((mp[a],mp[b]))) for a,b in c)
            assert image in index
            states.append(index[image])
        assert len(set(states))==24
        all_maps.append(states)
        vertex_orbit.add(states[0])
assert len(all_maps)==240 and len(vertex_orbit)==24
edge_rep=[]
for t in sorted(jump[0]):
    orb={tuple(sorted((m[0],m[t]))) for m in all_maps}
    edge_rep.append((t,len(orb)))
assert Counter(k for _,k in edge_rep)==Counter({60:5,24:2})
print('PASS direct Hamiltonian DFS: 24 undirected cycles in twenty-vertex incidence graph')
print('PASS independent symmetric-difference test: 84 decagon trades, 60 eighteen-edge trades')
print('PASS BFS and local structure: every vertex has shells (1,7,16); 40 triangles')
print('PASS geometry: transitive 240-element coordinate action, ten-trade edge orbits 60 and 24')
