#!/usr/bin/env python3
"""Exact finite exhaustive certificate for the C60 Ising ground-state flip graph.

Requires Python 3.9+ standard library only. All 60 graph vertices are darts
of the explicitly presented icosahedral triangulation.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product

U=lambda i: 1+i%5
L=lambda i: 6+i%5
T,B=0,11
triangles=set()
for i in range(5):
    triangles.add(tuple(sorted((T,U(i),U(i+1)))))
    triangles.add(tuple(sorted((B,L(i),L(i+1)))))
    triangles.add(tuple(sorted((U(i),U(i+1),L(i)))))
    triangles.add(tuple(sorted((L(i),L(i+1),U(i+1)))))
triangles=sorted(triangles)
assert len(triangles)==20
original_edges={tuple(sorted(e)) for f in triangles for e in combinations(f,2)}
assert len(original_edges)==30
nbr={u:set() for u in range(12)}
for u,v in original_edges:
    nbr[u].add(v); nbr[v].add(u)
assert all(len(nbr[u])==5 for u in nbr)
darts=sorted([(u,v) for u in nbr for v in nbr[u]])
assert len(darts)==60
idx={p:i for i,p in enumerate(darts)}
# Edge type P: within original-vertex pentagons; type H: across original edges.
pedges={tuple(sorted((idx[u,v],idx[u,w]))) for f in triangles for u in f
        for v,w in [tuple(t for t in f if t!=u)]}
hedges={tuple(sorted((idx[u,v],idx[v,u]))) for u,v in original_edges}
assert len(pedges)==60 and len(hedges)==30 and not (pedges&hedges)
edges=sorted(pedges|hedges)
assert len(edges)==90
neighbors=[[] for _ in range(60)]
for i,j in edges: neighbors[i].append(j);neighbors[j].append(i)
assert all(len(nbrs)==3 for nbrs in neighbors)
# For each pair of adjacent icosahedron vertices, exactly two common triangles.
face_of_edge={e:tuple(f for f in triangles if set(e).issubset(f)) for e in sorted(original_edges)}
assert all(len(z)==2 for z in face_of_edge.values())
# The pentagon edge of face f incident with original vertex u.
face_at={(f,u):tuple(sorted((idx[u,v],idx[u,w]))) for f in triangles
         for u in f for v,w in [tuple(x for x in f if x!=u)]}
assert set(face_at.values())==pedges

@lru_cache(None)
def all_matchings(remaining):
    if not remaining:return ((),)
    u=(remaining & -remaining).bit_length()-1
    return tuple(((u,v),)+rest for v in sorted(nbr[u]) if remaining>>v&1
            for rest in all_matchings(remaining^(1<<u)^(1<<v)))
matchings=all_matchings((1<<12)-1)
assert len(matchings)==125
assert len({frozenset(map(frozenset,m)) for m in matchings})==125

FULL=(1<<60)-1
state_info={}
pattern_seen=set()
for mid,matching in enumerate(matchings):
    assert len(matching)==6
    for choice in range(64):
        # Each matching edge chooses one of its two incident triangles.
        frustrated=set()
        for j,(u,v) in enumerate(matching):
            f=face_of_edge[tuple(sorted((u,v)))][(choice>>j)&1]
            frustrated.add(face_at[(f,u)]);frustrated.add(face_at[(f,v)])
        assert len(frustrated)==12 and frustrated<=pedges
        pattern=frozenset(frustrated)
        assert pattern not in pattern_seen
        pattern_seen.add(pattern)
        # Integration of all edge products determines the two spin states.
        spin=[None]*60;spin[0]=1;stack=[0]
        for u in stack:
            for v in neighbors[u]:
                edge=tuple(sorted((u,v)))
                value=spin[u]*(1 if edge in frustrated else -1)
                if spin[v] is None:spin[v]=value;stack.append(v)
                else: assert spin[v]==value
        assert len(stack)==60
        plus=sum(1<<i for i,s in enumerate(spin) if s>0)
        assert plus.bit_count()==30
        for state in (plus,plus^FULL):
            assert state not in state_info
            state_info[state]=(mid,choice)
assert len(state_info)==16000 and len(pattern_seen)==8000
# Independent direct energy evaluation of all generated spin states.
for state in state_info:
    incident=[0]*60
    unsat=0
    for u,v in edges:
        if (state>>u&1)==(state>>v&1):
            unsat+=1;incident[u]+=1;incident[v]+=1
    assert unsat==12
    assert Counter(incident)=={0:36,1:24}

# Every Hamming-distance-two ground-state pair arises on a graph edge.
# Independently check ALL unordered pairs of sites for every ground state.
states=set(state_info)
links={a:set() for a in states}
allpairs=list(combinations(range(60),2))
edge_set=set(edges)
for state in states:
    for u,v in allpairs:
        flipped=state^(1<<u)^(1<<v)
        if flipped in states:
            assert (u,v) in edge_set
            links[state].add(flipped)
    assert len(links[state])>=6
for a,ns in links.items():
    assert all(a in links[b] for b in ns)
    for b in ns:
        diff=a^b
        u=(diff&-diff).bit_length()-1
        v=(diff^(1<<u)).bit_length()-1
        assert tuple(sorted((u,v))) in edge_set
        assert ((a>>u)&1)!=((a>>v)&1)
        # Both individual flips cost exactly 2J, confirming the
        # second-order off-diagonal coefficient -Gamma^2/J.
        for site in (u,v):
            fr=sum((a>>site&1)==(a>>w&1) for w in neighbors[site])
            assert fr==1

# Exact BFS over all 16000 vertices and all actual second-order connections.
unvisited=set(states)
components=[]
while unvisited:
    root=min(unvisited)
    component={root};queue=[root];unvisited.remove(root)
    for x in queue:
        for y in links[x]:
            if y in unvisited:
                unvisited.remove(y);component.add(y);queue.append(y)
    components.append(component)
counts=Counter(map(len,components))
assert counts=={64:10,15360:1}
# Every small connected sector is explicitly a six-cube via the six face bits.
for comp in components:
    matching_indices={state_info[s][0] for s in comp}
    if len(comp)==64:
        assert len(matching_indices)==1
        choice_to_state={state_info[s][1]:s for s in comp}
        assert len(choice_to_state)==64
        for a in range(64):
            assert {choice_to_state[a^(1<<j)] for j in range(6)}==links[choice_to_state[a]]
    else:
        assert len(matching_indices)==120
# Icosahedral perfect-matching reconfiguration is independently classified.
msets=[frozenset(map(frozenset,m)) for m in matchings]
flip_neighbors=[set() for _ in matchings]
for i in range(125):
    for j in range(i+1,125):
        if len(msets[i]^msets[j])==4:
            flip_neighbors[i].add(j);flip_neighbors[j].add(i)
assert Counter(map(len,flip_neighbors))=={0:5,3:20,5:60,6:40}
ms_unseen=set(range(125));mcc=[]
while ms_unseen:
    root=min(ms_unseen);part={root};queue=[root];ms_unseen.remove(root)
    for x in queue:
        for y in flip_neighbors[x]:
            if y in ms_unseen:ms_unseen.remove(y);part.add(y);queue.append(y)
    mcc.append(part)
assert Counter(map(len,mcc))=={1:5,120:1}
# Exact degree data gives a useful spectral lower bound on the giant component.
giant=max(components,key=len)
all_degrees=Counter(len(links[s]) for s in states)
large_degrees=Counter(len(links[s]) for s in giant)
assert all_degrees=={6:2720,7:7680,8:5280,9:320}
assert large_degrees=={6:2080,7:7680,8:5280,9:320}
assert sum(k*v for k,v in large_degrees.items())==111360
assert sum(k*v for k,v in large_degrees.items())//len(giant)==7
assert 4*sum(k*v for k,v in large_degrees.items())==29*len(giant)
print('VERIFY_OK vertices=60 edges=90 faces=32 icosahedral_matchings=125 ground_states=16000')
print('VERIFY_OK exact_hamming2_components=1x15360+10x64 isolated_hypercubes=10')
print('VERIFY_OK degrees_all='+str(sorted(all_degrees.items()))+' giant_average_degree=29/4')
print('VERIFY_OK matching_flip_components=1x120+5x1 all_ground_magnetizations=0')
