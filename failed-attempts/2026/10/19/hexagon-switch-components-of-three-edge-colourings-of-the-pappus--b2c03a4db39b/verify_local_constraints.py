#!/usr/bin/env python3
"""Independent edge-label search and fixed-hexagon switch verifier.

Each point (x,y) has exactly one incident edge of each color 0,1,2.
Line constraints are checked incrementally. Six-cycles are generated
from the uncoloured underlying graph, not from any 2-factorization.
Run: python verify_local_constraints.py pappus_hexagon_certificate.json
"""
import argparse
import hashlib
import itertools
import json
from collections import Counter,deque

P=[(x,y) for x in range(3) for y in range(3)]
L=[(m,b) for m in range(3) for b in range(3)]
E=[(x,y,m) for x in range(3) for y in range(3) for m in range(3)]
edge_id={e:i for i,e in enumerate(E)}
incident=[[] for _ in range(18)]
line_for=[]
for i,(x,y,m) in enumerate(E):
    j=9+3*m+(y-m*x)%3
    line_for.append(j)
    incident[3*x+y].append(i)
    incident[j].append(i)
assert len(E)==27 and all(len(t)==3 for t in incident)

# Enumerate each choice of color permutation at every point; prune using
# the three pairwise distinct colors required at every line.
labels=[-1]*27
used_colors=[set() for _ in L]
colours=[]
def traverse(i):
    if i==9:
        assert all(len(t)==3 for t in used_colors)
        colours.append(tuple(labels))
        return
    x,y=P[i]
    edges=[edge_id[(x,y,m)] for m in range(3)]
    for perm in itertools.permutations((0,1,2)):
        if any(perm[m] in used_colors[line_for[edges[m]]-9] for m in range(3)):
            continue
        for m in range(3):
            k=edges[m];labels[k]=perm[m];used_colors[line_for[k]-9].add(perm[m])
        traverse(i+1)
        for m in range(3):
            k=edges[m];used_colors[line_for[k]-9].remove(perm[m]);labels[k]=-1
traverse(0)
assert len(colours)==120
states=sorted(colours)
assert len(set(states))==len(states)
index={s:i for i,s in enumerate(states)}

# A static census of all geometrical six-cycles, as sets of six edges.
edge_at={}
neighbor=[set() for _ in range(18)]
for i,(x,y,m) in enumerate(E):
    a=3*x+y;b=line_for[i]
    edge_at[frozenset((a,b))]=i
    neighbor[a].add(b);neighbor[b].add(a)
hexagons=set()
def walk(path):
    v=path[-1]
    if len(path)==6:
        if path[0] in neighbor[v]:
            vertices=path+[path[0]]
            inds=frozenset(edge_at[frozenset((vertices[j],vertices[j+1]))] for j in range(6))
            assert len(inds)==6
            hexagons.add(tuple(sorted(inds)))
        return
    for nxt in sorted(neighbor[v]):
        if nxt not in path:
            walk(path+[nxt])
for v in range(18): walk([v])
assert len(hexagons)>0

# A legal six-cycle switch has two colors alternating at its six edges.
E6=set()
for i,s in enumerate(states):
    for cyc in hexagons:
        used={s[e] for e in cyc}
        if len(used)!=2: continue
        a,b=sorted(used)
        # Since the coloring is proper and the cycle is simple,
        # any two-color six-cycle is necessarily alternating.
        repl=list(s)
        for e in cyc:repl[e]=a+b-repl[e]
        target=tuple(repl)
        assert target in index
        j=index[target]
        assert j!=i
        E6.add(tuple(sorted((i,j))))
assert len(E6)==216

S=[set() for _ in states]
for i,j in E6:S[i].add(j);S[j].add(i)

def parity(s):
    sign=1
    for vertex in range(18):
        # Points have incident edges sorted by slope; lines by x.
        order=sorted(incident[vertex],key=lambda k:E[k][2] if vertex<9 else E[k][0])
        seq=[s[k] for k in order]
        inversions=sum(seq[i]>seq[j] for i in range(3) for j in range(i+1,3))
        if inversions%2:sign=-sign
    return sign
pars=[parity(s) for s in states]
assert Counter(pars)==Counter({-1:60,1:60})
assert all(pars[u]==pars[v] for u,v in E6)

components=[];rem=set(range(len(states)))
while rem:
    root=min(rem);rem.remove(root);q=[root];C={root}
    while q:
        u=q.pop()
        for v in S[u]&rem:
            rem.remove(v);C.add(v);q.append(v)
    components.append(C)
assert sorted(map(len,components))==[60,60]
assert all(len({pars[v] for v in C})==1 for C in components)
assert Counter(map(len,S))==Counter({3:108,9:12})

def distances(start):
    dist={start:0};todo=deque([start])
    while todo:
        u=todo.popleft()
        for v in S[u]:
            if v not in dist:
                dist[v]=dist[u]+1;todo.append(v)
    return dist

for C in components:
    assert all(len(distances(v))==60 and max(distances(v).values())==6 for v in C)
    hubs={v for v in C if len(S[v])==9}
    assert len(hubs)==6
    rem2=C-hubs
    hub_pairs=[]
    while rem2:
        root=min(rem2);rem2.remove(root);q=[root];cy={root}
        while q:
            u=q.pop()
            for v in S[u]&rem2:
                rem2.remove(v);cy.add(v);q.append(v)
        assert len(cy)==6
        assert all(len(S[v]&cy)==2 for v in cy)
        pair=frozenset(next(iter(S[v]&hubs)) for v in cy)
        assert len(pair)==2
        assert all(next(iter(S[v]&hubs))!=next(iter(S[w]&hubs)) for v in cy for w in S[v]&cy)
        hub_pairs.append(pair)
    assert len(hub_pairs)==9 and len(set(hub_pairs))==9
    degrees=Counter(v for pair in hub_pairs for v in pair)
    assert len(degrees)==6 and all(n==3 for n in degrees.values())
    A={min(hubs)};B={v for pair in hub_pairs if min(hubs) in pair for v in pair if v!=min(hubs)}
    A=set(hubs)-B
    assert len(A)==len(B)==3
    assert set(hub_pairs)=={frozenset((a,b)) for a in A for b in B}

state_data=[list(s) for s in states]
edge_data=[list(x) for x in sorted(E6)]
state_hash=hashlib.sha256(json.dumps(state_data,separators=(',',':')).encode()).hexdigest()
edge_hash=hashlib.sha256(json.dumps(edge_data,separators=(',',':')).encode()).hexdigest()
summary={'point_local_assignments':len(states),'static_hexagons':len(hexagons),
         'legal_hexagon_transitions':len(E6),'component_sizes':sorted(map(len,components)),
         'parities':{str(k):v for k,v in sorted(Counter(pars).items())},
         'degree_distribution':{str(k):v for k,v in sorted(Counter(map(len,S)).items())},
         'component_diameters':[6,6],'component_hub_quotients':['K3,3','K3,3'],
         'states_sha256':state_hash,'hexagon_edges_sha256':edge_hash}
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('certificate')
    args=parser.parse_args()
    with open(args.certificate,encoding='utf-8') as f:ref=json.load(f)
    assert ref['states']==state_data
    assert ref['hexagon_edges']==edge_data
    assert ref['summary']['states_sha256']==state_hash
    assert ref['summary']['hexagon_edges_sha256']==edge_hash
    print(json.dumps(summary,sort_keys=True,indent=2))
    print('VERIFY_OK')
