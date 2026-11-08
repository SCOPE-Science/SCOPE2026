"""Independent set-based verification from the nine-point Pappus configuration.

Points are A,B,C,a,b,c,X,Y,Z. Lines are ABC, abc, XYZ, AbX, aBX,
AcY, aCY, BcZ, bCZ. The Levi graph has 18 vertices and 27 edges.
Standalone Python 3, using no third-party packages.
"""
from collections import Counter, deque
from itertools import combinations
import json

P = 'ABCabcXYZ'
L = ('ABC', 'abc', 'XYZ', 'AbX', 'aBX', 'AcY', 'aCY', 'BcZ', 'bCZ')
V = tuple('P'+c for c in P) + tuple('L'+str(i) for i in range(9))
adj = {v:set() for v in V}
for j,line in enumerate(L):
    for p in line:
        a,b='P'+p,'L'+str(j)
        adj[a].add(b)
        adj[b].add(a)
assert len(V)==18 and sum(map(len,adj.values()))==54
assert all(len(adj[v])==3 for v in V)
# Explicit certificate identifying this incidence graph with the conventional
# Hamiltonian LCF realization of the Pappus graph.
LCF_TO_LEVI = ('PA','L0','PC','L8','Pb','L3','PX','L4','PB',
               'L7','PZ','L2','PY','L6','Pa','L1','Pc','L5')
assert set(LCF_TO_LEVI)==set(V)
shifts=(5,7,-7,7,-7,-5)*3
for i in range(18):
    assert {LCF_TO_LEVI[(i-1)%18], LCF_TO_LEVI[(i+1)%18],
            LCF_TO_LEVI[(i+shifts[i])%18]}==adj[LCF_TO_LEVI[i]]
# Strictly independently compute graph distance from every vertex.
distance = {}
for v in V:
    d={v:0};q=deque([v])
    while q:
        x=q.popleft()
        for w in adj[x]:
            if w not in d:
                d[w]=d[x]+1;q.append(w)
    assert len(d)==18
    distance[v]=d

def is_semitotal(S):
    S=set(S)
    if any(x not in S and not (adj[x]&S) for x in V):
        return False
    return all(any(t!=s and distance[s][t]<=2 for t in S) for s in S)

for k in range(1,6):
    assert not any(is_semitotal(c) for c in combinations(V,k))
sets=[frozenset(c) for c in combinations(V,6) if is_semitotal(c)]
assert len(sets)==297
full=set(sets)
EOD = {S for S in sets if all(len(adj[v]&S)==1 for v in V)}
assert len(EOD)==9

def exchange_graph(slide):
    graph={S:set() for S in sets}
    # Different transition construction: compare every unordered pair of states.
    for i,S in enumerate(sets):
        for T in sets[:i]:
            lost=S-T
            if len(lost)!=1 or len(T-S)!=1:continue
            a=next(iter(lost));b=next(iter(T-S))
            if slide and b not in adj[a]:continue
            graph[S].add(T);graph[T].add(S)
    components=[];remaining=set(sets)
    while remaining:
        x=next(iter(remaining));q=[x];c={x}
        for t in q:
            for y in graph[t]-c:
                c.add(y);q.append(y)
        components.append(c);remaining-=c
    main=max(components,key=len)
    ecc=[]
    for root in main:
        d={root:0};q=deque([root])
        while q:
            x=q.popleft()
            for y in graph[x]:
                if y not in d:
                    d[y]=d[x]+1;q.append(y)
        assert len(d)==len(main)
        ecc.append(max(d.values()))
    return {
        'edges': sum(len(x) for x in graph.values())//2,
        'components': sorted(Counter(map(len,components)).items()),
        'degrees': sorted(Counter(map(len,graph.values())).items()),
        'radius': min(ecc),'diameter': max(ecc),
        'eccentricities': sorted(Counter(ecc).items()),
        'isolates_are_efficient': {next(iter(c)) for c in components if len(c)==1}==EOD,
    }

jump=exchange_graph(False)
slide=exchange_graph(True)
assert jump['edges']==1026 and slide['edges']==432
assert jump['components']==slide['components']==[(1,9),(288,1)]
assert jump['radius']==jump['diameter']==6
assert slide['radius']==8 and slide['diameter']==10
assert jump['isolates_are_efficient'] and slide['isolates_are_efficient']
print(json.dumps({'graph':'Pappus Levi configuration, nine points and nine lines',
                  'minimum':6,'states':len(sets),'efficient':len(EOD),
                  'jump':jump,'slide':slide}, sort_keys=True, indent=2))
print('VERIFY_OK')
