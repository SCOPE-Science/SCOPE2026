#!/usr/bin/env python3
"""Exhaustive LCF-coordinate certificate for identifying-code reconfiguration."""
import json
from collections import Counter, deque

N = 18
OFFSETS = (5, 7, -7, 7, -7, -5) * 3
EDGES = set()
for i in range(N):
    for j in ((i + 1) % N, (i + OFFSETS[i]) % N):
        EDGES.add(tuple(sorted((i, j))))
assert len(EDGES) == 27
adj = [set() for _ in range(N)]
for i, j in EDGES:
    adj[i].add(j)
    adj[j].add(i)
assert all(len(a) == 3 for a in adj)
# Explicit bipartition-swapping automorphism, establishing mirror component isomorphisms.
SWAP = (1,0,5,6,7,8,9,16,17,12,11,10,3,4,15,14,13,2)
assert len(set(SWAP)) == N and all((SWAP[u] % 2) != (u % 2) for u in range(N))
assert {tuple(sorted((SWAP[u],SWAP[v]))) for u,v in EDGES} == EDGES
balls = [sum(1 << u for u in ({v} | adj[v])) for v in range(N)]

def identifies(mask):
    signatures = [mask & b for b in balls]
    return all(signatures) and len(set(signatures)) == N

valid = [m for m in range(1 << N) if identifies(m)]
minimum = min(m.bit_count() for m in valid)
states = [m for m in valid if m.bit_count() == minimum]
S = set(states)

# Two adjacency relations: arbitrary one-token replacement and replacement over an original edge.
slides = {m: set() for m in states}
jumps = {m: set() for m in states}
for m in states:
    ones = [v for v in range(N) if (m >> v) & 1]
    zeros = [v for v in range(N) if not ((m >> v) & 1)]
    for u in ones:
        for v in zeros:
            t = m ^ (1 << u) ^ (1 << v)
            if t not in S:
                continue
            jumps[m].add(t)
            if tuple(sorted((u, v))) in EDGES:
                slides[m].add(t)

def stats(graph):
    remaining = set(states)
    comp_sizes = Counter()
    comp_edges = Counter()
    comp_ecc = Counter()
    comp_summary = []
    while remaining:
        root = min(remaining)
        seen = {root}
        todo = [root]
        for x in todo:
            for y in graph[x]:
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        remaining.difference_update(seen)
        k = len(seen)
        e = sum(len(graph[x]) for x in seen) // 2
        comp_sizes[k] += 1
        comp_edges[e] += 1
        if k > 1:
            ecc = []
            for x in seen:
                distance = {x: 0}
                q = deque([x])
                while q:
                    u = q.popleft()
                    for v in graph[u]:
                        if v in seen and v not in distance:
                            distance[v] = distance[u] + 1
                            q.append(v)
                assert len(distance) == k
                ecc.append(max(distance.values()))
            comp_summary.append({'size': k, 'edges': e, 'radius': min(ecc),
                                 'diameter': max(ecc),
                                 'eccentricity_histogram': dict(sorted(Counter(ecc).items()))})
    return {'components_by_size': dict(sorted(comp_sizes.items())),
            'components_by_edge_count': dict(sorted(comp_edges.items())),
            'degree_histogram': dict(sorted(Counter(map(len, graph.values())).items())),
            'total_edges': sum(map(len, graph.values())) // 2,
            'nontrivial_components': comp_summary}

# LCF labels have the two incidence color classes as even/odd positions.
by_even_count = Counter(sum((m >> v) & 1 for v in range(0, N, 2)) for m in states)
assert minimum == 9 and len(states) == 1028
# A legal one-token replacement cannot change the majority bipartition of a minimum code.
assert all((sum((m >> v) & 1 for v in range(0,N,2)) >= 5) ==
           (sum((t >> v) & 1 for v in range(0,N,2)) >= 5)
           for m in states for t in jumps[m])
assert sum(1 for m in states if not slides[m] and sum((m>>v)&1 for v in range(0,N,2))==4)==54
assert sum(1 for m in states if not slides[m] and sum((m>>v)&1 for v in range(0,N,2))==5)==54
result = {
    'graph': 'Pappus F018A in LCF notation [5,7,-7,7,-7,-5]^3',
    'n': N,
    'graph_edges': len(EDGES),
    'subsets_tested': 1 << N,
    'minimum_size': minimum,
    'minimum_codes': len(states),
    'codes_by_even_side_occupancy': dict(sorted(by_even_count.items())),
    'token_slide': stats(slides),
    'token_jump': stats(jumps),
}
assert by_even_count == Counter({0:1,1:27,2:81,3:243,4:162,5:162,6:243,7:81,8:27,9:1})
assert result['token_slide']['components_by_size'] == {1:108,460:2}
assert result['token_jump']['components_by_size'] == {514:2}
# Unique 4-eccentricity centers are the monochromatic bipartition codes.
for graph in (slides, jumps):
    hubs = [sum(1 << i for i in range(0,N,2)),sum(1 << i for i in range(1,N,2))]
    for hub in hubs:
        dist = {hub:0}
        q = deque([hub])
        while q:
            x=q.popleft()
            for y in graph[x]:
                if y not in dist:
                    dist[y]=dist[x]+1
                    q.append(y)
        assert max(dist.values()) == 4
        expected = Counter({0:1,1:27,2:81,3:243,4:(108 if graph is slides else 162)})
        assert Counter(dist.values()) == expected
assert result['token_slide']['total_edges'] == 1404
assert result['token_jump']['total_edges'] == 3780
assert all(r['radius']==4 and r['diameter']==8 for r in result['token_slide']['nontrivial_components'])
assert all(r['radius']==4 and r['diameter']==8 for r in result['token_jump']['nontrivial_components'])
print(json.dumps(result, sort_keys=True, indent=2))
