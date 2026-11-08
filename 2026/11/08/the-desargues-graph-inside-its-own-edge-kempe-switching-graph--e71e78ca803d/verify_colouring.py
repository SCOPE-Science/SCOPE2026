#!/usr/bin/env python3
"""Self-contained exhaustive edge-colouring and Kempe-switch certificate checker."""
import itertools
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
C = json.loads((HERE / 'certificate.json').read_text(encoding='utf-8'))
n = 10
E = sorted({tuple(sorted(e)) for i in range(n) for e in
            ((i, (i+1) % n), (i, n+i), (n+i, n+(i+3) % n))})
assert len(E) == 30
pairs = list(itertools.permutations((0, 1, 2)))
def canonical(x):
    return min(''.join(str(p[int(k)]) for k in x) for p in pairs)
# First independent route: label each edge with a colour, using local incidence constraints.
col = [-1] * len(E)
used = [0] * 20
solutions = []
def backtrack(assigned):
    if assigned == 30:
        solutions.append(canonical(col))
        return
    viable = []
    for j, (u, v) in enumerate(E):
        if col[j] != -1:
            continue
        a = [x for x in range(3) if not (used[u] | used[v]) & (1 << x)]
        if not a:
            return
        viable.append((len(a), j, a))
    _, j, options = min(viable)
    u, v = E[j]
    for x in options:
        col[j] = x
        used[u] |= 1 << x
        used[v] |= 1 << x
        backtrack(assigned+1)
        used[u] ^= 1 << x
        used[v] ^= 1 << x
        col[j] = -1
backtrack(0)
assert len(solutions) == 192, len(solutions)
states = sorted(set(solutions))
assert states == C['colourings'] and len(states) == 32
index = {s: i for i, s in enumerate(states)}

def cycles_for_pair(s, a, b):
    adj = [[] for _ in range(20)]
    for k,(u,v) in enumerate(E):
        if int(s[k]) in (a,b):
            adj[u].append((v,k))
            adj[v].append((u,k))
    assert all(len(x)==2 for x in adj)
    unseen = set(range(20))
    cyc = []
    while unseen:
        source = min(unseen)
        unseen.remove(source)
        stack=[source]; edges=set()
        while stack:
            v=stack.pop()
            for w,k in adj[v]:
                edges.add(k)
                if w in unseen:
                    unseen.remove(w);stack.append(w)
        assert len(edges) in (10,20)
        cyc.append(edges)
    return cyc

switches=set()
type_count={((10,10),(10,10),(10,10)):0, ((10,10),(20,),(20,)):0}
for i,s in enumerate(states):
    profiles=[]
    for a,b in ((0,1),(0,2),(1,2)):
        cyc=cycles_for_pair(s,a,b)
        profiles.append(tuple(sorted(map(len,cyc))))
        for ce in cyc:
            out=list(s)
            for k in ce: out[k]=str(a+b-int(out[k]))
            j=index[canonical(out)]
            if i != j: switches.add(tuple(sorted((i,j))))
    key=tuple(sorted(profiles))
    assert key in type_count,key
    type_count[key]+=1
assert sorted(type_count.values())==[12,20], type_count
assert [list(e) for e in sorted(switches)] == C['switch_edges']

adj=[set() for _ in states]
for i,j in switches: adj[i].add(j);adj[j].add(i)
components=[]; unseen=set(range(len(states)))
while unseen:
    seed=min(unseen);todo=[seed];unseen.remove(seed);comp=set()
    for v in todo:
        comp.add(v)
        for w in adj[v]:
            if w in unseen: unseen.remove(w);todo.append(w)
    components.append(comp)
assert sorted(map(len,components)) == [2]*6+[20]
assert sorted([sorted(c) for c in components if len(c)==2]) == C['other_components']
core=next(c for c in components if len(c)==20)
iso=dict(C['large_component_to_GP'])
assert set(iso)==core and set(iso.values())==set(range(20))
expected={tuple(sorted(e)) for e in E}
translated={tuple(sorted((iso[i],iso[j]))) for i,j in switches if i in core}
assert translated==expected and len(translated)==30
assert sorted(len(adj[i]) for i in core)==[3]*20
assert sorted(len(adj[i]) for i in set(range(32))-core)==[1]*12
# Verify the complete distance and shortest-cycle geometry of the large component.
def bfs(start):
    distances = {start: 0}
    parent = {start: None}
    todo = [start]
    girth = 100
    for v in todo:
        for w in adj[v]:
            if w not in core:
                raise AssertionError('component leak')
            if w not in distances:
                distances[w] = distances[v] + 1
                parent[w] = v
                todo.append(w)
            elif parent[v] != w:
                girth = min(girth, distances[v]+distances[w]+1)
    return distances,girth
metric=[bfs(v) for v in sorted(core)]
assert all(len(ds)==20 for ds,g in metric)
assert max(max(ds.values()) for ds,g in metric)==5
assert min(g for ds,g in metric)==6
# The explicitly constructed GP graph's bipartition is also checked directly.
assert all((ds[v]%2)!=(ds[w]%2) for ds,g in metric for v,w in switches if v in core and w in core)
print('COLOURING_ENUMERATION_PASS named=192 unlabelled=32 edges=36 graph=GP(10,3)+6K2')
