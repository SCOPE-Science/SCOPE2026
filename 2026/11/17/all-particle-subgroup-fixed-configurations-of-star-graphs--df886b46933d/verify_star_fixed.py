"""Finite graph-spine checks for fixed unordered star configurations.

For a star with m arms, a combinatorial graph spine has A-nodes for
nonnegative arm occupancy vectors of total k and B-nodes for vectors
of total k-1 with one central particle; a B-node joins each A-node
formed by increasing one arm occupancy. A permutation of arms acts on
this graph, and fixed points are the fixed A/B nodes and fixed edges.
"""
from itertools import product, permutations
from math import comb


def compositions(n, m):
    if m == 0:
        if n == 0:
            yield ()
        return
    if m == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for tail in compositions(n - first, m - 1):
            yield (first,) + tail


def arm_orbits(m, generators):
    unvisited = set(range(m))
    orbits = []
    while unvisited:
        start = min(unvisited)
        orb = {start}
        pending = [start]
        while pending:
            v = pending.pop()
            for g in generators:
                nxt = g[v]
                if nxt not in orb:
                    orb.add(nxt)
                    pending.append(nxt)
        unvisited -= orb
        orbits.append(tuple(sorted(orb)))
    return orbits


def fixed_node_counts(m, k, generators):
    O = arm_orbits(m, generators)
    fixed_arms = [o[0] for o in O if len(o) == 1]
    sizes = [len(o) for o in O if len(o) > 1]

    def is_fixed(v):
        return all(all(v[o[0]] == v[j] for j in o) for o in O)

    a = [v for v in compositions(k, m) if is_fixed(v)]
    b = [v for v in compositions(k - 1, m) if is_fixed(v)] if k >= 1 else []
    nodes = [('A', v) for v in a] + [('B', v) for v in b]
    index = {v: i for i, v in enumerate(nodes)}
    edges = []
    for v in b:
        for arm in fixed_arms:
            w = list(v)
            w[arm] += 1
            w = tuple(w)
            assert ('A', w) in index
            edges.append((index[('B', v)], index[('A', w)]))
    adj = {i: set() for i in range(len(nodes))}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = set()
    cc = []
    for start in adj:
        if start in seen:
            continue
        seen.add(start)
        todo = [start]
        component = []
        while todo:
            p = todo.pop()
            component.append(p)
            for q in adj[p]:
                if q not in seen:
                    seen.add(q)
                    todo.append(q)
        cc.append(component)
    expected = {}
    for tup in product(*(range(k // sz + 1) for sz in sizes)):
        weight = sum(x * sz for x, sz in zip(tup, sizes))
        n = k - weight
        if n < 0 or (not fixed_arms and n > 1):
            continue
        if len(fixed_arms) < 3:
            rank = 0
        else:
            f = len(fixed_arms)
            rank = (f - 2) * comb(n + f - 2, f - 1) - comb(n + f - 2, f - 2) + 1
        expected[tup] = rank
    assert len(cc) == len(expected), (m,k,O,len(cc),len(expected))
    # Determine orbit profile of each component via its A/B node indices.
    found = {}
    for component in cc:
        occupancy = set()
        for j in component:
            v = nodes[j][1]
            occupancy.add(tuple(v[o[0]] for o in O if len(o)>1))
        assert len(occupancy) == 1, (m,k,O,occupancy)
        key = next(iter(occupancy))
        e_count = sum(1 for u, v in edges if u in component and v in component)
        rank = e_count - len(component) + 1
        assert key not in found and rank == expected[key], (m,k,O,key,rank,expected.get(key))
        found[key] = rank
    assert found == expected
    return len(nodes), len(edges), len(cc), sum(found.values()), sizes, len(fixed_arms)


def test():
    total = 0
    nodes = edges = components = circles = 0
    for m in range(3, 8):
        e = tuple(range(m))
        rotation = tuple((i+1)%m for i in range(m))
        reflection = tuple((-i)%m for i in range(m))
        one_swap = tuple(1 if i == 0 else 0 if i == 1 else i for i in range(m))
        disjoint_swaps = tuple((i^1) if i < 2*(m//2) else i for i in range(m))
        generators_list = [[e], [rotation], [reflection], [one_swap], [disjoint_swaps],
                           [rotation, reflection], [one_swap, reflection]]
        for gens in generators_list:
            for k in range(0, 7):
                a,b,c,d,_,_=fixed_node_counts(m,k,gens)
                nodes+=a; edges+=b; components+=c; circles+=d; total+=1
    print('STAR_FIXED_GRAPH_SPINE_PASS', 'instances='+str(total),
          'fixed_vertices='+str(nodes), 'fixed_edges='+str(edges),
          'components='+str(components), 'loops='+str(circles))
    a,b,c,d,s,f=fixed_node_counts(5,4,[tuple(1 if i==0 else 0 if i==1 else i for i in range(5))])
    assert (s,f,c,d)==([2],3,3,7)
    print('EXAMPLE_5_ARMS_SWAP_K4_PASS', 'components='+str(c), 'loops='+str(d))

if __name__ == '__main__':
    test()
